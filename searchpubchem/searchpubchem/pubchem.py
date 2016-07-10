'''
Retrieve PubChem data
BioPython also allows retrieval of pubchem records
the purpose of this package it to allow rich retreival
of PubChem data. This includes, for instance, query
by CAS, ChemSpider, SMILES, etc. It also handles a variety
of data outputs: computed/experimental data, SDFs and
fingerprints. Computed/experimental data is processed using
bs4 principally.
'''

from xsd_schema import pug_rest, pug_view
from pyxb.utils.six.moves.urllib.request import urlopen
import urllib2
from urllib import urlencode
from pyxb.utils import domutils
from bs4 import BeautifulSoup
import os
from time import sleep
from collections import defaultdict

_base = 'pubchem.ncbi.nlm.nih.gov'
_pug_rest = '"http://pubchem.ncbi.nlm.nih.gov/pug_rest"'
_path = os.path.abspath(__file__)
_directory = os.path.dirname(_path)
_fp_file = _directory + '/fingerprints.txt'


'''
    Per NCBI:
        "All PubChem web pages (or requests to NCBI in general) have
        a policy that users should throttle their web page requests,
        which includes web-based programmatic services. Users should
        limit their web-requests to no more than three per second.
        Violators of usage policies may result in the user being
        temporarily blocked from accessing PubChem (or NCBI) resources."
    As such the API has been designed to limit programmatic requests
    to 3 per second.
    We also designed the API to stick with NCBI's policy of requiring
    an email associated with the request.
'''


def _url_factory(uri, proxy=False):
    '''
    This function handles the url processing using the urllib2
    module. In particular it handles the passing of proxy
    paramters.
    '''
    if proxy:
        proxy = urllib2.ProxyHandler({"https": proxy, "http": proxy})
        opener = urllib2.build_opener(proxy)
        urllib2.install_opener(opener)
        uri = 'http://' + _base + uri
        response = urllib2.urlopen(uri)
        value = response.read().strip()
    else:
        uri = 'http://' + _base + uri
        response = urllib2.urlopen(uri)
        value = response.read().strip()
    return value


class Collect(object):
    def __init__(self, pubchem_ids, predictors=False, fingerprint=False,
                 xml=False, sdf=False, proxy=False, user=False,
                 id_name='PubChem', chunks=False, try_count=3):
        self.id_name = id_name
        self.pubchem_ids = ["".join(x[id_name].split()) for x in pubchem_ids]
        self._convert = Convert()
        self.uri = dict()
        self.compound = defaultdict(dict)
        length = len(pubchem_ids)
        concatenated_ids = ",".join(self.pubchem_ids)
        if user is True:
            print "Adding user provided features"
            for count, id in enumerate(self.pubchem_ids):
                self.compound[id]['userhash'] = pubchem_ids[count]['userhash']
        if fingerprint is True:
            print "Getting fingerprints from NCBI"
            fps = []
            percent = 0.
            if chunks is not False:
                print '{:2.1%} out of {}'.format(percent, length)
                concatenated_ids = concatenated_ids.split(',')
                for concatenated_id in\
                    [concatenated_ids[i:i + chunks] for i in
                     xrange(0, len(concatenated_ids), chunks)]:
                    percent = percent + chunks
                    val = float(percent) / float(length)
                    concatenated_id = ','.join(concatenated_id)
                    uri = self._convert.cactvs_uri(concatenated_id)
                    fps.extend(_url_factory(uri, proxy).split('\n'))
                print
            else:
                uri = self._convert.cactvs_uri(concatenated_ids)
                fps = _url_factory(uri, proxy)
                fps = fps.split('\n')
            for i, line in enumerate(fps):
                binhash = self._convert.get_binhash(line)
                self.compound[self.pubchem_ids[i]]['binhash'] = binhash
            if fps:
                print "Fingerprints collected"
        if sdf is True:
            print "Getting sdfs from NCBI"
            uri = self._convert.sdf_uri(concatenated_ids)
            sdf_stream = _url_factory(uri, proxy)
            sdfs = [data.lstrip() + '$$$$' for data in
                    sdf_stream.split('$$$$') if data is not ""]
            for i, sdf_each in enumerate(sdfs):
                self.compound[self.pubchem_ids[i]]['sdf'] = sdf_each
            if sdf_stream:
                print "sdfs collected"
        if xml is True:
            print "Collecting XMLs from NCBI"
            for count, id in enumerate(self.pubchem_ids):
                percent = float(count) / float(length)
                print '{} {} {:2.1%} out of {}\r'.\
                    format(id, count, percent, length)
                uri = self._convert.pubchem_uri(id)
        val = False
        count = 0
        while (val is False) and (count < try_count):
            try:
                xml_value = _url_factory(uri, proxy)
                self.compound[id]['pubchem'] = self._convert.pubchem(xml_value)
                val = True
            except:
                sleep(5)
            count = count + 1
            print
        for count, id in enumerate(self.pubchem_ids):
            if predictors is not False:
                self.compound[id]['predictor'] = predictors[count]


class Convert(object):
    '''Conversion class for interacting with NCBI data'''
    def _parse_fingerprint(self):
        fp_features = {}
        with open(_fp_file) as fp:
            for line in fp:
                (pos, feature) = line.strip().split('\t')
                fp_features[int(pos)] = feature
        return fp_features

    def __init__(self):
        self.fingerprint = self._parse_fingerprint()

    def synonym(self, label):
        '''
        Retreives the best PubChem id using a registered synonym
        CAS # is an example of a synonym that works well.
        '''
        uri = _base + 'pug/compound/name/%s/xrefs/RegistryID/XML' % (label,)
        xml = urlopen(uri).read()
        xml = xml.replace('xmlns=' + _pug_rest, '')
        order = pug_rest.CreateFromDOM(domutils.StringToDOM(xml))
        o = order.Information[0].CID[0]
        self.cid = str(o)

    def pubchem_inchi(self, inchi, proxy=''):
        '''
        InChi is a bit special, it requires the a post http, rather
        than a get, this is its particular format
        '''
        u = 'http://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchi/cids/TXT'
        data = urlencode({'inchi': inchi})
        cid = urllib2.urlopen(u, data).read().strip()
        return cid

    def pubchem_xrefs(self, id):
        '''
        Retrieves the external references, given a PubChem
        identifier
        '''
        uri = _base + 'pug/compound/cid/%s/xrefs/SBURL/xml' % (id,)
        xml = urlopen(uri).read()
        xml = xml.replace('xmlns=' + _pug_rest, '')
        order = pug_rest.CreateFromDOM(domutils.StringToDOM(xml))
        o = order.Information[0]
        urls = o.SBURL
        self.urls = urls

    def getSMILES(self, id):
        '''
        Retreive cid given a smiles input
        '''
        uri = 'http://' + _base +\
              '/rest/pug/compound/smiles/%s/cids/TXT' % (id,)
        txt = urlopen(uri).read().rstrip()
        self.cid = txt

    def getCAS(self, id):
        '''
        Retrieves the CAS from PubChem Identifier.
        '''
        uri = _base + 'pug_view/data/compound/%s/XML' % (id,)
        xml = urlopen(uri).read()
        xml_soup = BeautifulSoup(xml, "lxml")
        self.xml = xml_soup
        value = None
        iupac = None
        for x in xml_soup.find_all('name'):
            name = x.get_text()
            if name == "CAS" and value is None:
                value = x.find_next_sibling('stringvalue').get_text()
            if name == 'IUPAC Name' and iupac is None:
                iupac = x.find_next_sibling('stringvalue').get_text()
        self.cas = value
        self.iupac = iupac

    def pubchem_uri(self, id):
        uri = '/rest/pug_view/data/compound/%s/XML' % (id,)
        return uri

    def pubchem(self, xml):
        '''
        Retrieves the primary PubChem data, using a
        PubChem Identifier. If multiple values are reported
        for a given descriptor, the first is given, since, by
        convention, these are the highest quality.
        '''
        xml_soup = BeautifulSoup(xml, "lxml")
        self.cid = id
        values = {}

        def _return_value_list(text, key):
            '''Special function for returning list of values'''
            return [y.get_text() for y in text.find_next_siblings(key)]

        xml_soups = xml_soup.find_all('section')
        properties = ''
        match_text = 'Chemical and Physical Properties'
        for xml_soup in xml_soups:
            try:
                if xml_soup.find('tocheading').get_text() == match_text:
                    properties = xml_soup
            except:
                pass
        try:
            for x in properties.find_all('name'):
                value = None
                name = x.get_text()
                if name not in values:
                    if x.find_next_sibling('numvalue'):
                        value = x.find_next_sibling('numvalue').get_text()
                    if x.find_next_sibling('stringvalue'):
                        value = x.find_next_sibling('stringvalue').get_text()
                    if x.find_next_siblings('stringvaluelist'):
                        value = _return_value_list(x, 'stringvaluelist')
                    if x.find_next_siblings('numvaluelist'):
                        value = _return_value_list(x, 'stringvaluelist')
                    if value:
                        values[name] = value
        except:
            pass
        return values

    def _convert_cactvs(self, cactvs):
        '''
        This internal function converts 2D fingerprints to a string of 0/1s
        The fingerprint is defined here:
        ftp.ncbi.nlm.nih.gov/pubchem/specifications/pubchem_fingerprints.txt
        The way that this function works is:
        1) Pass cactvs
        2) Strip the 2 trailing bytes
        3) Strip the 2 leading bytes
        4) Convert the letters to base64 binary (6-bits)
        5) Report bits 32 through (881+32-11), which are the 881 informative
            bits.
        '''
        b64 = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6,
               "H": 7, "I": 8, "J": 9, "K": 10, "L": 11, "M": 12, "N": 13,
               "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18, "T": 19,
               "U": 20, "V": 21, "W": 22, "X": 23, "Y": 24, "Z": 25,
               "a": 26, "b": 27, "c": 28, "d": 29, "e": 30, "f": 31,
               "g": 32, "h": 33, "i": 34, "j": 35, "k": 36, "l": 37,
               "m": 38, "n": 39, "o": 40, "p": 41, "q": 42, "r": 43,
               "s": 44, "t": 45, "u": 46, "v": 47, "w": 48, "x": 49,
               "y": 50, "z": 51, "0": 52, "1": 53, "2": 54, "3": 55,
               "4": 56, "5": 57, "6": 58, "7": 59, "8": 60, "9": 61,
               "+": 62, "/": 63}
        c = cactvs[:-2]
        binstring = (''.join([str(bin(b64[x]))[2:].zfill(6) for x in c]))
        return binstring[32:-11]

    def get_binhash(self, cactvs):
        '''
        This function turns the CACTVS into a hash
        '''
        binstring = self._convert_cactvs(cactvs)
        binhash = {}
        for count, val in enumerate(binstring):
            binhash[self.fingerprint[count]] = val
        return binhash

    def cactvs_uri(self, id):
        '''
        This function retreives the CACTVS uri from PubChem, which is a base64
        encoded string, specifying the 881 bits, corresponding to the
        fingerprint
        '''
        _id = str(id)
        uri = '/rest/pug/compound/cid/' + _id + '/property/Fingerprint2D/TXT'
        return uri

    def sdf_uri(self, id):
        '''
        This function retreives sdfs from PubChem
        '''
        _id = str(id)
        uri = "/rest/pug/compound/cid/" + _id + '/record/SDF'
        return uri
