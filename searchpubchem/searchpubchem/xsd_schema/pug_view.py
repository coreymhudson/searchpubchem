# ./pug_view.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:ab0c9708514235065268b3a38971dc1c51967c4a
# Generated 2016-02-27 01:23:31.783845 by PyXB version 1.2.4 using Python 2.7.5.final.0
# Namespace http://pubchem.ncbi.nlm.nih.gov/pug_view

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:c4a6d4de-dd33-11e5-991d-542696d54607')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://pubchem.ncbi.nlm.nih.gov/pug_view', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 47, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}Code uses Python identifier Code
    __Code = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Code'), 'Code', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_httppubchem_ncbi_nlm_nih_govpug_viewCode', False, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 49, 6), )

    
    Code = property(__Code.value, __Code.set, None, None)

    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}Message uses Python identifier Message
    __Message = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Message'), 'Message', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_httppubchem_ncbi_nlm_nih_govpug_viewMessage', False, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 50, 6), )

    
    Message = property(__Message.value, __Message.set, None, None)

    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}Details uses Python identifier Details
    __Details = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Details'), 'Details', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_httppubchem_ncbi_nlm_nih_govpug_viewDetails', True, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 51, 6), )

    
    Details = property(__Details.value, __Details.set, None, None)

    _ElementMap.update({
        __Code.name() : __Code,
        __Message.name() : __Message,
        __Details.name() : __Details
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 57, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}Record uses Python identifier Record
    __Record = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Record'), 'Record', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON__httppubchem_ncbi_nlm_nih_govpug_viewRecord', True, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 64, 0), )

    
    Record = property(__Record.value, __Record.set, None, None)

    _ElementMap.update({
        __Record.name() : __Record
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 65, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}RecordType uses Python identifier RecordType
    __RecordType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RecordType'), 'RecordType', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_2_httppubchem_ncbi_nlm_nih_govpug_viewRecordType', False, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 67, 6), )

    
    RecordType = property(__RecordType.value, __RecordType.set, None, None)

    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}RecordNumber uses Python identifier RecordNumber
    __RecordNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RecordNumber'), 'RecordNumber', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_2_httppubchem_ncbi_nlm_nih_govpug_viewRecordNumber', False, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 68, 6), )

    
    RecordNumber = property(__RecordNumber.value, __RecordNumber.set, None, None)

    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}AvailableViews uses Python identifier AvailableViews
    __AvailableViews = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AvailableViews'), 'AvailableViews', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_2_httppubchem_ncbi_nlm_nih_govpug_viewAvailableViews', True, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 69, 6), )

    
    AvailableViews = property(__AvailableViews.value, __AvailableViews.set, None, None)

    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}Section uses Python identifier Section
    __Section = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Section'), 'Section', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_2_httppubchem_ncbi_nlm_nih_govpug_viewSection', True, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 77, 0), )

    
    Section = property(__Section.value, __Section.set, None, None)

    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}Information uses Python identifier Information
    __Information = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Information'), 'Information', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_2_httppubchem_ncbi_nlm_nih_govpug_viewInformation', True, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 94, 0), )

    
    Information = property(__Information.value, __Information.set, None, None)

    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}Reference uses Python identifier Reference
    __Reference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Reference'), 'Reference', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_2_httppubchem_ncbi_nlm_nih_govpug_viewReference', True, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 122, 0), )

    
    Reference = property(__Reference.value, __Reference.set, None, None)

    _ElementMap.update({
        __RecordType.name() : __RecordType,
        __RecordNumber.name() : __RecordNumber,
        __AvailableViews.name() : __AvailableViews,
        __Section.name() : __Section,
        __Information.name() : __Information,
        __Reference.name() : __Reference
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 78, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}Section uses Python identifier Section
    __Section = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Section'), 'Section', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_3_httppubchem_ncbi_nlm_nih_govpug_viewSection', True, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 77, 0), )

    
    Section = property(__Section.value, __Section.set, None, None)

    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}TOCHeading uses Python identifier TOCHeading
    __TOCHeading = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TOCHeading'), 'TOCHeading', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_3_httppubchem_ncbi_nlm_nih_govpug_viewTOCHeading', False, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 81, 8), )

    
    TOCHeading = property(__TOCHeading.value, __TOCHeading.set, None, None)

    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}TOCID uses Python identifier TOCID
    __TOCID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TOCID'), 'TOCID', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_3_httppubchem_ncbi_nlm_nih_govpug_viewTOCID', False, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 82, 8), )

    
    TOCID = property(__TOCID.value, __TOCID.set, None, None)

    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Description'), 'Description', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_3_httppubchem_ncbi_nlm_nih_govpug_viewDescription', False, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 84, 6), )

    
    Description = property(__Description.value, __Description.set, None, None)

    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}Views uses Python identifier Views
    __Views = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Views'), 'Views', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_3_httppubchem_ncbi_nlm_nih_govpug_viewViews', True, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 85, 6), )

    
    Views = property(__Views.value, __Views.set, None, None)

    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}HintGroupSubsectionsByReference uses Python identifier HintGroupSubsectionsByReference
    __HintGroupSubsectionsByReference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'HintGroupSubsectionsByReference'), 'HintGroupSubsectionsByReference', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_3_httppubchem_ncbi_nlm_nih_govpug_viewHintGroupSubsectionsByReference', False, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 86, 6), )

    
    HintGroupSubsectionsByReference = property(__HintGroupSubsectionsByReference.value, __HintGroupSubsectionsByReference.set, None, None)

    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}HintEmbeddedHTML uses Python identifier HintEmbeddedHTML
    __HintEmbeddedHTML = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'HintEmbeddedHTML'), 'HintEmbeddedHTML', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_3_httppubchem_ncbi_nlm_nih_govpug_viewHintEmbeddedHTML', False, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 87, 6), )

    
    HintEmbeddedHTML = property(__HintEmbeddedHTML.value, __HintEmbeddedHTML.set, None, None)

    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}Information uses Python identifier Information
    __Information = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Information'), 'Information', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_3_httppubchem_ncbi_nlm_nih_govpug_viewInformation', True, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 94, 0), )

    
    Information = property(__Information.value, __Information.set, None, None)

    _ElementMap.update({
        __Section.name() : __Section,
        __TOCHeading.name() : __TOCHeading,
        __TOCID.name() : __TOCID,
        __Description.name() : __Description,
        __Views.name() : __Views,
        __HintGroupSubsectionsByReference.name() : __HintGroupSubsectionsByReference,
        __HintEmbeddedHTML.name() : __HintEmbeddedHTML,
        __Information.name() : __Information
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 95, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}ReferenceNumber uses Python identifier ReferenceNumber
    __ReferenceNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ReferenceNumber'), 'ReferenceNumber', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_4_httppubchem_ncbi_nlm_nih_govpug_viewReferenceNumber', False, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 97, 6), )

    
    ReferenceNumber = property(__ReferenceNumber.value, __ReferenceNumber.set, None, None)

    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Name'), 'Name', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_4_httppubchem_ncbi_nlm_nih_govpug_viewName', False, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 98, 6), )

    
    Name = property(__Name.value, __Name.set, None, None)

    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Description'), 'Description', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_4_httppubchem_ncbi_nlm_nih_govpug_viewDescription', False, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 99, 6), )

    
    Description = property(__Description.value, __Description.set, None, None)

    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}Reference uses Python identifier Reference
    __Reference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Reference'), 'Reference', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_4_httppubchem_ncbi_nlm_nih_govpug_viewReference', True, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 100, 6), )

    
    Reference = property(__Reference.value, __Reference.set, None, None)

    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}URL uses Python identifier URL
    __URL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'URL'), 'URL', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_4_httppubchem_ncbi_nlm_nih_govpug_viewURL', False, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 101, 6), )

    
    URL = property(__URL.value, __URL.set, None, None)

    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}NumValue uses Python identifier NumValue
    __NumValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NumValue'), 'NumValue', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_4_httppubchem_ncbi_nlm_nih_govpug_viewNumValue', False, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 103, 8), )

    
    NumValue = property(__NumValue.value, __NumValue.set, None, None)

    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}NumValueList uses Python identifier NumValueList
    __NumValueList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NumValueList'), 'NumValueList', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_4_httppubchem_ncbi_nlm_nih_govpug_viewNumValueList', True, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 104, 8), )

    
    NumValueList = property(__NumValueList.value, __NumValueList.set, None, None)

    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}DateValue uses Python identifier DateValue
    __DateValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DateValue'), 'DateValue', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_4_httppubchem_ncbi_nlm_nih_govpug_viewDateValue', False, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 105, 8), )

    
    DateValue = property(__DateValue.value, __DateValue.set, None, None)

    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}DateValueList uses Python identifier DateValueList
    __DateValueList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DateValueList'), 'DateValueList', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_4_httppubchem_ncbi_nlm_nih_govpug_viewDateValueList', True, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 106, 8), )

    
    DateValueList = property(__DateValueList.value, __DateValueList.set, None, None)

    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}BoolValue uses Python identifier BoolValue
    __BoolValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BoolValue'), 'BoolValue', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_4_httppubchem_ncbi_nlm_nih_govpug_viewBoolValue', False, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 107, 8), )

    
    BoolValue = property(__BoolValue.value, __BoolValue.set, None, None)

    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}BoolValueList uses Python identifier BoolValueList
    __BoolValueList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BoolValueList'), 'BoolValueList', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_4_httppubchem_ncbi_nlm_nih_govpug_viewBoolValueList', True, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 108, 8), )

    
    BoolValueList = property(__BoolValueList.value, __BoolValueList.set, None, None)

    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}StringValue uses Python identifier StringValue
    __StringValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'StringValue'), 'StringValue', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_4_httppubchem_ncbi_nlm_nih_govpug_viewStringValue', False, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 109, 8), )

    
    StringValue = property(__StringValue.value, __StringValue.set, None, None)

    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}StringValueList uses Python identifier StringValueList
    __StringValueList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'StringValueList'), 'StringValueList', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_4_httppubchem_ncbi_nlm_nih_govpug_viewStringValueList', True, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 110, 8), )

    
    StringValueList = property(__StringValueList.value, __StringValueList.set, None, None)

    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}BinaryValue uses Python identifier BinaryValue
    __BinaryValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BinaryValue'), 'BinaryValue', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_4_httppubchem_ncbi_nlm_nih_govpug_viewBinaryValue', False, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 111, 8), )

    
    BinaryValue = property(__BinaryValue.value, __BinaryValue.set, None, None)

    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}BinaryValueList uses Python identifier BinaryValueList
    __BinaryValueList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BinaryValueList'), 'BinaryValueList', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_4_httppubchem_ncbi_nlm_nih_govpug_viewBinaryValueList', True, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 112, 8), )

    
    BinaryValueList = property(__BinaryValueList.value, __BinaryValueList.set, None, None)

    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}ExternalDataURL uses Python identifier ExternalDataURL
    __ExternalDataURL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ExternalDataURL'), 'ExternalDataURL', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_4_httppubchem_ncbi_nlm_nih_govpug_viewExternalDataURL', False, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 113, 8), )

    
    ExternalDataURL = property(__ExternalDataURL.value, __ExternalDataURL.set, None, None)

    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}ExternalDataURLList uses Python identifier ExternalDataURLList
    __ExternalDataURLList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ExternalDataURLList'), 'ExternalDataURLList', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_4_httppubchem_ncbi_nlm_nih_govpug_viewExternalDataURLList', True, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 114, 8), )

    
    ExternalDataURLList = property(__ExternalDataURLList.value, __ExternalDataURLList.set, None, None)

    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}ValueUnit uses Python identifier ValueUnit
    __ValueUnit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ValueUnit'), 'ValueUnit', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_4_httppubchem_ncbi_nlm_nih_govpug_viewValueUnit', False, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 116, 6), )

    
    ValueUnit = property(__ValueUnit.value, __ValueUnit.set, None, None)

    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}ExternalDataMimeType uses Python identifier ExternalDataMimeType
    __ExternalDataMimeType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ExternalDataMimeType'), 'ExternalDataMimeType', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_4_httppubchem_ncbi_nlm_nih_govpug_viewExternalDataMimeType', False, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 117, 6), )

    
    ExternalDataMimeType = property(__ExternalDataMimeType.value, __ExternalDataMimeType.set, None, None)

    _ElementMap.update({
        __ReferenceNumber.name() : __ReferenceNumber,
        __Name.name() : __Name,
        __Description.name() : __Description,
        __Reference.name() : __Reference,
        __URL.name() : __URL,
        __NumValue.name() : __NumValue,
        __NumValueList.name() : __NumValueList,
        __DateValue.name() : __DateValue,
        __DateValueList.name() : __DateValueList,
        __BoolValue.name() : __BoolValue,
        __BoolValueList.name() : __BoolValueList,
        __StringValue.name() : __StringValue,
        __StringValueList.name() : __StringValueList,
        __BinaryValue.name() : __BinaryValue,
        __BinaryValueList.name() : __BinaryValueList,
        __ExternalDataURL.name() : __ExternalDataURL,
        __ExternalDataURLList.name() : __ExternalDataURLList,
        __ValueUnit.name() : __ValueUnit,
        __ExternalDataMimeType.name() : __ExternalDataMimeType
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 123, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}ReferenceNumber uses Python identifier ReferenceNumber
    __ReferenceNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ReferenceNumber'), 'ReferenceNumber', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_5_httppubchem_ncbi_nlm_nih_govpug_viewReferenceNumber', False, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 125, 6), )

    
    ReferenceNumber = property(__ReferenceNumber.value, __ReferenceNumber.set, None, None)

    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}SourceName uses Python identifier SourceName
    __SourceName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SourceName'), 'SourceName', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_5_httppubchem_ncbi_nlm_nih_govpug_viewSourceName', False, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 126, 6), )

    
    SourceName = property(__SourceName.value, __SourceName.set, None, None)

    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}SourceID uses Python identifier SourceID
    __SourceID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SourceID'), 'SourceID', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_5_httppubchem_ncbi_nlm_nih_govpug_viewSourceID', False, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 127, 6), )

    
    SourceID = property(__SourceID.value, __SourceID.set, None, None)

    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Name'), 'Name', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_5_httppubchem_ncbi_nlm_nih_govpug_viewName', False, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 128, 6), )

    
    Name = property(__Name.value, __Name.set, None, None)

    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Description'), 'Description', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_5_httppubchem_ncbi_nlm_nih_govpug_viewDescription', False, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 129, 6), )

    
    Description = property(__Description.value, __Description.set, None, None)

    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}URL uses Python identifier URL
    __URL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'URL'), 'URL', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_5_httppubchem_ncbi_nlm_nih_govpug_viewURL', False, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 130, 6), )

    
    URL = property(__URL.value, __URL.set, None, None)

    _ElementMap.update({
        __ReferenceNumber.name() : __ReferenceNumber,
        __SourceName.name() : __SourceName,
        __SourceID.name() : __SourceID,
        __Name.name() : __Name,
        __Description.name() : __Description,
        __URL.name() : __URL
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 138, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}RecordType uses Python identifier RecordType
    __RecordType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RecordType'), 'RecordType', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_6_httppubchem_ncbi_nlm_nih_govpug_viewRecordType', False, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 140, 6), )

    
    RecordType = property(__RecordType.value, __RecordType.set, None, None)

    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}RecordNumber uses Python identifier RecordNumber
    __RecordNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RecordNumber'), 'RecordNumber', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_6_httppubchem_ncbi_nlm_nih_govpug_viewRecordNumber', False, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 141, 6), )

    
    RecordNumber = property(__RecordNumber.value, __RecordNumber.set, None, None)

    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}NeighborsOfType uses Python identifier NeighborsOfType
    __NeighborsOfType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NeighborsOfType'), 'NeighborsOfType', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_6_httppubchem_ncbi_nlm_nih_govpug_viewNeighborsOfType', True, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 142, 6), )

    
    NeighborsOfType = property(__NeighborsOfType.value, __NeighborsOfType.set, None, None)

    _ElementMap.update({
        __RecordType.name() : __RecordType,
        __RecordNumber.name() : __RecordNumber,
        __NeighborsOfType.name() : __NeighborsOfType
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 143, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}Type uses Python identifier Type
    __Type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Type'), 'Type', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_7_httppubchem_ncbi_nlm_nih_govpug_viewType', False, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 145, 12), )

    
    Type = property(__Type.value, __Type.set, None, None)

    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}IDList uses Python identifier IDList
    __IDList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'IDList'), 'IDList', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_7_httppubchem_ncbi_nlm_nih_govpug_viewIDList', True, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 146, 12), )

    
    IDList = property(__IDList.value, __IDList.set, None, None)

    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}NameList uses Python identifier NameList
    __NameList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NameList'), 'NameList', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_7_httppubchem_ncbi_nlm_nih_govpug_viewNameList', True, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 147, 12), )

    
    NameList = property(__NameList.value, __NameList.set, None, None)

    _ElementMap.update({
        __Type.name() : __Type,
        __IDList.name() : __IDList,
        __NameList.name() : __NameList
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_8 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 156, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}RecordType uses Python identifier RecordType
    __RecordType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RecordType'), 'RecordType', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_8_httppubchem_ncbi_nlm_nih_govpug_viewRecordType', False, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 158, 6), )

    
    RecordType = property(__RecordType.value, __RecordType.set, None, None)

    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}RecordNumber uses Python identifier RecordNumber
    __RecordNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RecordNumber'), 'RecordNumber', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_8_httppubchem_ncbi_nlm_nih_govpug_viewRecordNumber', False, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 159, 6), )

    
    RecordNumber = property(__RecordNumber.value, __RecordNumber.set, None, None)

    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}URL uses Python identifier URL
    __URL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'URL'), 'URL', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_8_httppubchem_ncbi_nlm_nih_govpug_viewURL', False, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 160, 3), )

    
    URL = property(__URL.value, __URL.set, None, None)

    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}NumberOfStructures uses Python identifier NumberOfStructures
    __NumberOfStructures = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NumberOfStructures'), 'NumberOfStructures', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_8_httppubchem_ncbi_nlm_nih_govpug_viewNumberOfStructures', False, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 161, 3), )

    
    NumberOfStructures = property(__NumberOfStructures.value, __NumberOfStructures.set, None, None)

    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}Structures uses Python identifier Structures
    __Structures = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Structures'), 'Structures', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_8_httppubchem_ncbi_nlm_nih_govpug_viewStructures', True, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 162, 6), )

    
    Structures = property(__Structures.value, __Structures.set, None, None)

    _ElementMap.update({
        __RecordType.name() : __RecordType,
        __RecordNumber.name() : __RecordNumber,
        __URL.name() : __URL,
        __NumberOfStructures.name() : __NumberOfStructures,
        __Structures.name() : __Structures
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_9 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 163, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}MMDB_ID uses Python identifier MMDB_ID
    __MMDB_ID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MMDB_ID'), 'MMDB_ID', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_9_httppubchem_ncbi_nlm_nih_govpug_viewMMDB_ID', False, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 165, 12), )

    
    MMDB_ID = property(__MMDB_ID.value, __MMDB_ID.set, None, None)

    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}PDB_ID uses Python identifier PDB_ID
    __PDB_ID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PDB_ID'), 'PDB_ID', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_9_httppubchem_ncbi_nlm_nih_govpug_viewPDB_ID', False, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 166, 12), )

    
    PDB_ID = property(__PDB_ID.value, __PDB_ID.set, None, None)

    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}URL uses Python identifier URL
    __URL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'URL'), 'URL', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_9_httppubchem_ncbi_nlm_nih_govpug_viewURL', False, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 167, 12), )

    
    URL = property(__URL.value, __URL.set, None, None)

    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}ImageURL uses Python identifier ImageURL
    __ImageURL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ImageURL'), 'ImageURL', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_9_httppubchem_ncbi_nlm_nih_govpug_viewImageURL', False, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 168, 12), )

    
    ImageURL = property(__ImageURL.value, __ImageURL.set, None, None)

    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Description'), 'Description', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_9_httppubchem_ncbi_nlm_nih_govpug_viewDescription', False, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 169, 12), )

    
    Description = property(__Description.value, __Description.set, None, None)

    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}Taxonomy uses Python identifier Taxonomy
    __Taxonomy = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Taxonomy'), 'Taxonomy', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_9_httppubchem_ncbi_nlm_nih_govpug_viewTaxonomy', False, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 170, 12), )

    
    Taxonomy = property(__Taxonomy.value, __Taxonomy.set, None, None)

    _ElementMap.update({
        __MMDB_ID.name() : __MMDB_ID,
        __PDB_ID.name() : __PDB_ID,
        __URL.name() : __URL,
        __ImageURL.name() : __ImageURL,
        __Description.name() : __Description,
        __Taxonomy.name() : __Taxonomy
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_10 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 171, 14)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}ID uses Python identifier ID
    __ID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ID'), 'ID', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_10_httppubchem_ncbi_nlm_nih_govpug_viewID', False, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 173, 18), )

    
    ID = property(__ID.value, __ID.set, None, None)

    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Name'), 'Name', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_10_httppubchem_ncbi_nlm_nih_govpug_viewName', False, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 174, 18), )

    
    Name = property(__Name.value, __Name.set, None, None)

    _ElementMap.update({
        __ID.name() : __ID,
        __Name.name() : __Name
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_11 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 186, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}RecordType uses Python identifier RecordType
    __RecordType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RecordType'), 'RecordType', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_11_httppubchem_ncbi_nlm_nih_govpug_viewRecordType', False, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 188, 6), )

    
    RecordType = property(__RecordType.value, __RecordType.set, None, None)

    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}RecordNumber uses Python identifier RecordNumber
    __RecordNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RecordNumber'), 'RecordNumber', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_11_httppubchem_ncbi_nlm_nih_govpug_viewRecordNumber', False, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 189, 6), )

    
    RecordNumber = property(__RecordNumber.value, __RecordNumber.set, None, None)

    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}Categories uses Python identifier Categories
    __Categories = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Categories'), 'Categories', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_11_httppubchem_ncbi_nlm_nih_govpug_viewCategories', True, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 190, 6), )

    
    Categories = property(__Categories.value, __Categories.set, None, None)

    _ElementMap.update({
        __RecordType.name() : __RecordType,
        __RecordNumber.name() : __RecordNumber,
        __Categories.name() : __Categories
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_12 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 191, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}Category uses Python identifier Category
    __Category = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Category'), 'Category', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_12_httppubchem_ncbi_nlm_nih_govpug_viewCategory', False, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 193, 12), )

    
    Category = property(__Category.value, __Category.set, None, None)

    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}URL uses Python identifier URL
    __URL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'URL'), 'URL', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_12_httppubchem_ncbi_nlm_nih_govpug_viewURL', False, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 194, 12), )

    
    URL = property(__URL.value, __URL.set, None, None)

    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}Sources uses Python identifier Sources
    __Sources = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Sources'), 'Sources', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_12_httppubchem_ncbi_nlm_nih_govpug_viewSources', True, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 195, 12), )

    
    Sources = property(__Sources.value, __Sources.set, None, None)

    _ElementMap.update({
        __Category.name() : __Category,
        __URL.name() : __URL,
        __Sources.name() : __Sources
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_13 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 196, 14)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}SID uses Python identifier SID
    __SID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SID'), 'SID', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_13_httppubchem_ncbi_nlm_nih_govpug_viewSID', False, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 198, 18), )

    
    SID = property(__SID.value, __SID.set, None, None)

    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}SourceName uses Python identifier SourceName
    __SourceName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SourceName'), 'SourceName', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_13_httppubchem_ncbi_nlm_nih_govpug_viewSourceName', False, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 199, 18), )

    
    SourceName = property(__SourceName.value, __SourceName.set, None, None)

    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}SourceURL uses Python identifier SourceURL
    __SourceURL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SourceURL'), 'SourceURL', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_13_httppubchem_ncbi_nlm_nih_govpug_viewSourceURL', False, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 200, 18), )

    
    SourceURL = property(__SourceURL.value, __SourceURL.set, None, None)

    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}RegistryID uses Python identifier RegistryID
    __RegistryID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RegistryID'), 'RegistryID', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_13_httppubchem_ncbi_nlm_nih_govpug_viewRegistryID', False, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 201, 18), )

    
    RegistryID = property(__RegistryID.value, __RegistryID.set, None, None)

    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}SourceRecordURL uses Python identifier SourceRecordURL
    __SourceRecordURL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SourceRecordURL'), 'SourceRecordURL', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_13_httppubchem_ncbi_nlm_nih_govpug_viewSourceRecordURL', False, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 202, 18), )

    
    SourceRecordURL = property(__SourceRecordURL.value, __SourceRecordURL.set, None, None)

    _ElementMap.update({
        __SID.name() : __SID,
        __SourceName.name() : __SourceName,
        __SourceURL.name() : __SourceURL,
        __RegistryID.name() : __RegistryID,
        __SourceRecordURL.name() : __SourceRecordURL
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_14 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 214, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}RecordType uses Python identifier RecordType
    __RecordType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RecordType'), 'RecordType', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_14_httppubchem_ncbi_nlm_nih_govpug_viewRecordType', False, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 216, 6), )

    
    RecordType = property(__RecordType.value, __RecordType.set, None, None)

    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}RecordNumber uses Python identifier RecordNumber
    __RecordNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RecordNumber'), 'RecordNumber', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_14_httppubchem_ncbi_nlm_nih_govpug_viewRecordNumber', False, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 217, 6), )

    
    RecordNumber = property(__RecordNumber.value, __RecordNumber.set, None, None)

    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}AllURL uses Python identifier AllURL
    __AllURL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AllURL'), 'AllURL', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_14_httppubchem_ncbi_nlm_nih_govpug_viewAllURL', False, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 218, 6), )

    
    AllURL = property(__AllURL.value, __AllURL.set, None, None)

    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}Subheadings uses Python identifier Subheadings
    __Subheadings = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Subheadings'), 'Subheadings', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_14_httppubchem_ncbi_nlm_nih_govpug_viewSubheadings', True, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 219, 6), )

    
    Subheadings = property(__Subheadings.value, __Subheadings.set, None, None)

    _ElementMap.update({
        __RecordType.name() : __RecordType,
        __RecordNumber.name() : __RecordNumber,
        __AllURL.name() : __AllURL,
        __Subheadings.name() : __Subheadings
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_15 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 220, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}Subheading uses Python identifier Subheading
    __Subheading = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Subheading'), 'Subheading', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_15_httppubchem_ncbi_nlm_nih_govpug_viewSubheading', False, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 222, 12), )

    
    Subheading = property(__Subheading.value, __Subheading.set, None, None)

    
    # Element {http://pubchem.ncbi.nlm.nih.gov/pug_view}SubheadingURL uses Python identifier SubheadingURL
    __SubheadingURL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SubheadingURL'), 'SubheadingURL', '__httppubchem_ncbi_nlm_nih_govpug_view_CTD_ANON_15_httppubchem_ncbi_nlm_nih_govpug_viewSubheadingURL', False, pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 223, 12), )

    
    SubheadingURL = property(__SubheadingURL.value, __SubheadingURL.set, None, None)

    _ElementMap.update({
        __Subheading.name() : __Subheading,
        __SubheadingURL.name() : __SubheadingURL
    })
    _AttributeMap.update({
        
    })



Fault = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Fault'), CTD_ANON, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 46, 0))
Namespace.addCategoryObject('elementBinding', Fault.name().localName(), Fault)

Records = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Records'), CTD_ANON_, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 56, 0))
Namespace.addCategoryObject('elementBinding', Records.name().localName(), Records)

Record = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Record'), CTD_ANON_2, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 64, 0))
Namespace.addCategoryObject('elementBinding', Record.name().localName(), Record)

Section = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Section'), CTD_ANON_3, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 77, 0))
Namespace.addCategoryObject('elementBinding', Section.name().localName(), Section)

Information = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Information'), CTD_ANON_4, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 94, 0))
Namespace.addCategoryObject('elementBinding', Information.name().localName(), Information)

Reference = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Reference'), CTD_ANON_5, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 122, 0))
Namespace.addCategoryObject('elementBinding', Reference.name().localName(), Reference)

Neighbors = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Neighbors'), CTD_ANON_6, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 137, 0))
Namespace.addCategoryObject('elementBinding', Neighbors.name().localName(), Neighbors)

Structure = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Structure'), CTD_ANON_8, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 155, 0))
Namespace.addCategoryObject('elementBinding', Structure.name().localName(), Structure)

SourceCategories = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SourceCategories'), CTD_ANON_11, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 185, 0))
Namespace.addCategoryObject('elementBinding', SourceCategories.name().localName(), SourceCategories)

Literature = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Literature'), CTD_ANON_14, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 213, 0))
Namespace.addCategoryObject('elementBinding', Literature.name().localName(), Literature)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Code'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 49, 6)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Message'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 50, 6)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Details'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 51, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 51, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Code')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 49, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Message')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 50, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Details')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 51, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Record'), CTD_ANON_2, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 64, 0)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Record')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 59, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RecordType'), pyxb.binding.datatypes.string, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 67, 6)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RecordNumber'), pyxb.binding.datatypes.int, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 68, 6)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AvailableViews'), pyxb.binding.datatypes.string, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 69, 6)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Section'), CTD_ANON_3, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 77, 0)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Information'), CTD_ANON_4, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 94, 0)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Reference'), CTD_ANON_5, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 122, 0)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 69, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 70, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 71, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 72, 6))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RecordType')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 67, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RecordNumber')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 68, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AvailableViews')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 69, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Information')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 70, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Section')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 71, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Reference')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 72, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_2()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Section'), CTD_ANON_3, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 77, 0)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TOCHeading'), pyxb.binding.datatypes.string, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 81, 8)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TOCID'), pyxb.binding.datatypes.int, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 82, 8)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Description'), pyxb.binding.datatypes.string, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 84, 6)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Views'), pyxb.binding.datatypes.string, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 85, 6)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'HintGroupSubsectionsByReference'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 86, 6)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'HintEmbeddedHTML'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 87, 6)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Information'), CTD_ANON_4, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 94, 0)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 84, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 85, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 86, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 87, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 88, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 89, 6))
    counters.add(cc_5)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TOCHeading')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 81, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TOCID')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 82, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Description')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 84, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Views')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 85, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'HintGroupSubsectionsByReference')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 86, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'HintEmbeddedHTML')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 87, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Information')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 88, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Section')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 89, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_3()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ReferenceNumber'), pyxb.binding.datatypes.int, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 97, 6)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Name'), pyxb.binding.datatypes.string, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 98, 6)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Description'), pyxb.binding.datatypes.string, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 99, 6)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Reference'), pyxb.binding.datatypes.string, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 100, 6)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'URL'), pyxb.binding.datatypes.string, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 101, 6)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NumValue'), pyxb.binding.datatypes.double, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 103, 8)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NumValueList'), pyxb.binding.datatypes.double, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 104, 8)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DateValue'), pyxb.binding.datatypes.string, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 105, 8)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DateValueList'), pyxb.binding.datatypes.string, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 106, 8)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BoolValue'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 107, 8)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BoolValueList'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 108, 8)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StringValue'), pyxb.binding.datatypes.string, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 109, 8)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StringValueList'), pyxb.binding.datatypes.string, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 110, 8)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BinaryValue'), pyxb.binding.datatypes.base64Binary, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 111, 8)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BinaryValueList'), pyxb.binding.datatypes.base64Binary, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 112, 8)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ExternalDataURL'), pyxb.binding.datatypes.string, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 113, 8)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ExternalDataURLList'), pyxb.binding.datatypes.string, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 114, 8)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ValueUnit'), pyxb.binding.datatypes.string, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 116, 6)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ExternalDataMimeType'), pyxb.binding.datatypes.string, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 117, 6)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 98, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 99, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 100, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 101, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 102, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 116, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 117, 6))
    counters.add(cc_6)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ReferenceNumber')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 97, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Name')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 98, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Description')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 99, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Reference')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 100, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'URL')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 101, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NumValue')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 103, 8))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NumValueList')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 104, 8))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DateValue')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 105, 8))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DateValueList')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 106, 8))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BoolValue')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 107, 8))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BoolValueList')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 108, 8))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'StringValue')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 109, 8))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'StringValueList')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 110, 8))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BinaryValue')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 111, 8))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BinaryValueList')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 112, 8))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ExternalDataURL')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 113, 8))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ExternalDataURLList')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 114, 8))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ValueUnit')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 116, 6))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ExternalDataMimeType')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 117, 6))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_18._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_4()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ReferenceNumber'), pyxb.binding.datatypes.int, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 125, 6)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SourceName'), pyxb.binding.datatypes.string, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 126, 6)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SourceID'), pyxb.binding.datatypes.string, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 127, 6)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Name'), pyxb.binding.datatypes.string, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 128, 6)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Description'), pyxb.binding.datatypes.string, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 129, 6)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'URL'), pyxb.binding.datatypes.string, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 130, 6)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 127, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 128, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 129, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 130, 6))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ReferenceNumber')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 125, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SourceName')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 126, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SourceID')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 127, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Name')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 128, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Description')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 129, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'URL')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 130, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_5()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RecordType'), pyxb.binding.datatypes.string, scope=CTD_ANON_6, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 140, 6)))

CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RecordNumber'), pyxb.binding.datatypes.int, scope=CTD_ANON_6, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 141, 6)))

CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NeighborsOfType'), CTD_ANON_7, scope=CTD_ANON_6, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 142, 6)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RecordType')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 140, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RecordNumber')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 141, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NeighborsOfType')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 142, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_6._Automaton = _BuildAutomaton_6()




CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Type'), pyxb.binding.datatypes.string, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 145, 12)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IDList'), pyxb.binding.datatypes.int, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 146, 12)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NameList'), pyxb.binding.datatypes.string, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 147, 12)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Type')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 145, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IDList')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 146, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NameList')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 147, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_7._Automaton = _BuildAutomaton_7()




CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RecordType'), pyxb.binding.datatypes.string, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 158, 6)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RecordNumber'), pyxb.binding.datatypes.int, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 159, 6)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'URL'), pyxb.binding.datatypes.string, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 160, 3)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NumberOfStructures'), pyxb.binding.datatypes.int, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 161, 3)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Structures'), CTD_ANON_9, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 162, 6)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RecordType')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 158, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RecordNumber')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 159, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'URL')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 160, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NumberOfStructures')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 161, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Structures')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 162, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_8._Automaton = _BuildAutomaton_8()




CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MMDB_ID'), pyxb.binding.datatypes.int, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 165, 12)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PDB_ID'), pyxb.binding.datatypes.string, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 166, 12)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'URL'), pyxb.binding.datatypes.string, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 167, 12)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ImageURL'), pyxb.binding.datatypes.string, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 168, 12)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Description'), pyxb.binding.datatypes.string, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 169, 12)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Taxonomy'), CTD_ANON_10, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 170, 12)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 166, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 169, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 170, 12))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MMDB_ID')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 165, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PDB_ID')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 166, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'URL')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 167, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ImageURL')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 168, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Description')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 169, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Taxonomy')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 170, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_9._Automaton = _BuildAutomaton_9()




CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ID'), pyxb.binding.datatypes.int, scope=CTD_ANON_10, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 173, 18)))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Name'), pyxb.binding.datatypes.string, scope=CTD_ANON_10, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 174, 18)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ID')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 173, 18))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Name')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 174, 18))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_10._Automaton = _BuildAutomaton_10()




CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RecordType'), pyxb.binding.datatypes.string, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 188, 6)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RecordNumber'), pyxb.binding.datatypes.int, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 189, 6)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Categories'), CTD_ANON_12, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 190, 6)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RecordType')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 188, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RecordNumber')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 189, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Categories')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 190, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_11._Automaton = _BuildAutomaton_11()




CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Category'), pyxb.binding.datatypes.string, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 193, 12)))

CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'URL'), pyxb.binding.datatypes.string, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 194, 12)))

CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Sources'), CTD_ANON_13, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 195, 12)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Category')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 193, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'URL')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 194, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Sources')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 195, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_12._Automaton = _BuildAutomaton_12()




CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SID'), pyxb.binding.datatypes.int, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 198, 18)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SourceName'), pyxb.binding.datatypes.string, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 199, 18)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SourceURL'), pyxb.binding.datatypes.string, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 200, 18)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RegistryID'), pyxb.binding.datatypes.string, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 201, 18)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SourceRecordURL'), pyxb.binding.datatypes.string, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 202, 18)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 200, 18))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 202, 18))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SID')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 198, 18))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SourceName')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 199, 18))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SourceURL')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 200, 18))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RegistryID')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 201, 18))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SourceRecordURL')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 202, 18))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_13._Automaton = _BuildAutomaton_13()




CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RecordType'), pyxb.binding.datatypes.string, scope=CTD_ANON_14, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 216, 6)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RecordNumber'), pyxb.binding.datatypes.int, scope=CTD_ANON_14, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 217, 6)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AllURL'), pyxb.binding.datatypes.string, scope=CTD_ANON_14, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 218, 6)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Subheadings'), CTD_ANON_15, scope=CTD_ANON_14, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 219, 6)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 219, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RecordType')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 216, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RecordNumber')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 217, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AllURL')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 218, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Subheadings')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 219, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_14._Automaton = _BuildAutomaton_14()




CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Subheading'), pyxb.binding.datatypes.string, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 222, 12)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SubheadingURL'), pyxb.binding.datatypes.string, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 223, 12)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Subheading')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 222, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SubheadingURL')), pyxb.utils.utility.Location('/Users/cmhudso/Desktop/SRAnt/NCBI/pug_view.xsd', 223, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_15._Automaton = _BuildAutomaton_15()

