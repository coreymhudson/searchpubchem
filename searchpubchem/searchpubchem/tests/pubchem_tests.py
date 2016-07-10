from NCBI import pubchem
import unittest


class PubchemException(Exception):

    """Exception type for the Pubchem Class"""

    pass


class PubchemTests(unittest.TestCase):
    """Test the Pubchem class."""

    def setUp(self):
        """Initialize before every test."""
        self._convert = pubchem.Convert()

    def tearDown(self):
        """Clean up after each test."""
        del self._convert

    def test_pubchem(self):
        """Ensure that features were extracted."""
        self._convert.pubchem(5090)
        self.assertEqual('314.06128', self._convert.values['Exact Mass'])

    def test_pubchem_xrefs(self):
        """Ensure that links were extracted"""
        self._convert.pubchem_xrefs(5090)
        _found = 0
        _test_url = 'http://www.chemspider.com/Chemical-Structure.4911.html'
        if _test_url in set(self._convert.urls):
            _found = 1
        self.assertEqual(_found, 1)

    def test_pubchem_inchi(self):
        """Ensure that you can get cid from InChi"""
        inchi = 'InChI=1S/C3H8/c1-3-2/h3H2,1-2H3'
        cid = self._convert.pubchem_inchi(inchi)
        self.assertEqual(cid, '6334')

    def test_pubchem_synonym(self):
        """Ensure that cas number conversion works"""
        self._convert.synonym('162011-90-7')
        self.assertEqual(self._convert.cid, '5090')


    def test_pubchem_cactvs(self):
        _test_cactvs = 'AAADccB4OABAAAAAAAAAAAAAAAAAAQAAAAAwYAAAAAAAAAABQAAAG'\
                       'gQAAAAADACg2AKyCYAABAqIAiDSCHBCAAAgCBAIiBkAAMgIJDKgNR'\
                       'CCMAAkwAEIqQeIyKCOEAAAAAAAAAAgAAAAAAAAAAAAAAAAAA=='
        _test_binstring = "11000000011110000011100000000000010000000000000000"\
                          "00000000000000000000000000000000000000000000000000"\
                          "00000000000000000000000000000000000000000001000000"\
                          "00000000000000000000000000001100000110000000000000"\
                          "00000000000000000000000000000000000000000000000000"\
                          "00000101000000000000000000000000011010000001000000"\
                          "00000000000000000000000000000000110000000000101000"\
                          "00110110000000001010110010000010011000000000000000"\
                          "00000100000010101000100000000010001000001101001000"\
                          "00100001110000010000100000000000000000001000000000"\
                          "10000001000000001000100010000001100100000000000000"\
                          "00110010000000100000100100001100101010000000110101"\
                          "00010000100000100011000000000000001001001100000000"\
                          "00000100001000101010010000011110001000110010001010"\
                          "00001000111000010000000000000000000000000000000000"\
                          "00000000000000000000000000001000000000000000000000"\
                          "00000000000000000000000000000000000000000000000000"\
                          "0000000000000000000000000000000"
        _test_binstring = ''.join(_test_binstring)
        self._convert.pubchem_cactvs(5090)
        self.assertEqual(self._convert.binstring, _test_binstring)
        self.assertEqual(self._convert.cactvs, _test_cactvs)

if __name__ == '__main__':
    unittest.main()
