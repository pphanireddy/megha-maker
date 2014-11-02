# ./service.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2014-11-02 11:12:34.546325 by PyXB version 1.2.4 using Python 2.7.6.final.0
# Namespace AbsentNamespace0

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:3382d7ba-62c4-11e4-a8ab-001cc06aed61')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.CreateAbsentNamespace()
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


# Complex type vminfoType with content type ELEMENT_ONLY
class vminfoType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type vminfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'vminfoType')
    _XSDLocation = pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 4, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element size uses Python identifier size
    __size = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'size'), 'size', '__AbsentNamespace0_vminfoType_size', False, pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 6, 6), )

    
    size = property(__size.value, __size.set, None, None)

    
    # Element count uses Python identifier count
    __count = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'count'), 'count', '__AbsentNamespace0_vminfoType_count', False, pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 7, 6), )

    
    count = property(__count.value, __count.set, None, None)

    
    # Element location uses Python identifier location
    __location = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'location'), 'location', '__AbsentNamespace0_vminfoType_location', False, pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 8, 6), )

    
    location = property(__location.value, __location.set, None, None)

    
    # Element image uses Python identifier image
    __image = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'image'), 'image', '__AbsentNamespace0_vminfoType_image', False, pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 9, 6), )

    
    image = property(__image.value, __image.set, None, None)

    _ElementMap.update({
        __size.name() : __size,
        __count.name() : __count,
        __location.name() : __location,
        __image.name() : __image
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'vminfoType', vminfoType)


# Complex type roleType with content type ELEMENT_ONLY
class roleType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type roleType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'roleType')
    _XSDLocation = pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 12, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element vminfo uses Python identifier vminfo
    __vminfo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'vminfo'), 'vminfo', '__AbsentNamespace0_roleType_vminfo', False, pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 14, 6), )

    
    vminfo = property(__vminfo.value, __vminfo.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_roleType_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 16, 4)
    __name._UseLocation = pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 16, 4)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        __vminfo.name() : __vminfo
    })
    _AttributeMap.update({
        __name.name() : __name
    })
Namespace.addCategoryObject('typeBinding', 'roleType', roleType)


# Complex type serviceType with content type ELEMENT_ONLY
class serviceType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type serviceType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'serviceType')
    _XSDLocation = pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 18, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element location uses Python identifier location
    __location = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'location'), 'location', '__AbsentNamespace0_serviceType_location', False, pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 20, 6), )

    
    location = property(__location.value, __location.set, None, None)

    
    # Element role uses Python identifier role
    __role = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'role'), 'role', '__AbsentNamespace0_serviceType_role', True, pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 21, 6), )

    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_serviceType_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 23, 4)
    __name._UseLocation = pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 23, 4)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        __location.name() : __location,
        __role.name() : __role
    })
    _AttributeMap.update({
        __name.name() : __name
    })
Namespace.addCategoryObject('typeBinding', 'serviceType', serviceType)


service = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'service'), serviceType, location=pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 3, 2))
Namespace.addCategoryObject('elementBinding', service.name().localName(), service)



vminfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'size'), pyxb.binding.datatypes.string, scope=vminfoType, location=pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 6, 6)))

vminfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'count'), pyxb.binding.datatypes.byte, scope=vminfoType, location=pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 7, 6)))

vminfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'location'), pyxb.binding.datatypes.string, scope=vminfoType, location=pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 8, 6)))

vminfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'image'), pyxb.binding.datatypes.string, scope=vminfoType, location=pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 9, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(vminfoType._UseForTag(pyxb.namespace.ExpandedName(None, 'size')), pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 6, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(vminfoType._UseForTag(pyxb.namespace.ExpandedName(None, 'count')), pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 7, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(vminfoType._UseForTag(pyxb.namespace.ExpandedName(None, 'location')), pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 8, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(vminfoType._UseForTag(pyxb.namespace.ExpandedName(None, 'image')), pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 9, 6))
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
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
vminfoType._Automaton = _BuildAutomaton()




roleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'vminfo'), vminfoType, scope=roleType, location=pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 14, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(roleType._UseForTag(pyxb.namespace.ExpandedName(None, 'vminfo')), pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 14, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
roleType._Automaton = _BuildAutomaton_()




serviceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'location'), pyxb.binding.datatypes.string, scope=serviceType, location=pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 20, 6)))

serviceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'role'), roleType, scope=serviceType, location=pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 21, 6)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 21, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(serviceType._UseForTag(pyxb.namespace.ExpandedName(None, 'location')), pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 20, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(serviceType._UseForTag(pyxb.namespace.ExpandedName(None, 'role')), pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 21, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
serviceType._Automaton = _BuildAutomaton_2()

