# ./service.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2014-11-02 12:59:22.204253 by PyXB version 1.2.4 using Python 2.7.6.final.0
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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:1ec4c9b4-62d3-11e4-956d-001cc06aed61')

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


# Complex type machineType with content type ELEMENT_ONLY
class machineType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type machineType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'machineType')
    _XSDLocation = pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 4, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element size uses Python identifier size
    __size = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'size'), 'size', '__AbsentNamespace0_machineType_size', False, pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 6, 6), )

    
    size = property(__size.value, __size.set, None, None)

    
    # Element count uses Python identifier count
    __count = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'count'), 'count', '__AbsentNamespace0_machineType_count', False, pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 7, 6), )

    
    count = property(__count.value, __count.set, None, None)

    
    # Element location uses Python identifier location
    __location = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'location'), 'location', '__AbsentNamespace0_machineType_location', False, pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 8, 6), )

    
    location = property(__location.value, __location.set, None, None)

    
    # Element image uses Python identifier image
    __image = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'image'), 'image', '__AbsentNamespace0_machineType_image', False, pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 9, 6), )

    
    image = property(__image.value, __image.set, None, None)

    _ElementMap.update({
        __size.name() : __size,
        __count.name() : __count,
        __location.name() : __location,
        __image.name() : __image
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'machineType', machineType)


# Complex type securityType with content type ELEMENT_ONLY
class securityType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type securityType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'securityType')
    _XSDLocation = pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 12, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element sshpempath uses Python identifier sshpempath
    __sshpempath = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'sshpempath'), 'sshpempath', '__AbsentNamespace0_securityType_sshpempath', False, pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 14, 6), )

    
    sshpempath = property(__sshpempath.value, __sshpempath.set, None, None)

    _ElementMap.update({
        __sshpempath.name() : __sshpempath
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'securityType', securityType)


# Complex type repositoriesType with content type ELEMENT_ONLY
class repositoriesType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type repositoriesType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'repositoriesType')
    _XSDLocation = pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 17, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element repository uses Python identifier repository
    __repository = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'repository'), 'repository', '__AbsentNamespace0_repositoriesType_repository', False, pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 19, 6), )

    
    repository = property(__repository.value, __repository.set, None, None)

    _ElementMap.update({
        __repository.name() : __repository
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'repositoriesType', repositoriesType)


# Complex type installationsType with content type ELEMENT_ONLY
class installationsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type installationsType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'installationsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 22, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element install uses Python identifier install
    __install = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'install'), 'install', '__AbsentNamespace0_installationsType_install', True, pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 24, 6), )

    
    install = property(__install.value, __install.set, None, None)

    _ElementMap.update({
        __install.name() : __install
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'installationsType', installationsType)


# Complex type packagesType with content type ELEMENT_ONLY
class packagesType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type packagesType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'packagesType')
    _XSDLocation = pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 27, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element repositories uses Python identifier repositories
    __repositories = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'repositories'), 'repositories', '__AbsentNamespace0_packagesType_repositories', False, pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 29, 6), )

    
    repositories = property(__repositories.value, __repositories.set, None, None)

    
    # Element installations uses Python identifier installations
    __installations = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'installations'), 'installations', '__AbsentNamespace0_packagesType_installations', False, pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 30, 6), )

    
    installations = property(__installations.value, __installations.set, None, None)

    _ElementMap.update({
        __repositories.name() : __repositories,
        __installations.name() : __installations
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'packagesType', packagesType)


# Complex type roleType with content type ELEMENT_ONLY
class roleType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type roleType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'roleType')
    _XSDLocation = pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 33, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element machine uses Python identifier machine
    __machine = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'machine'), 'machine', '__AbsentNamespace0_roleType_machine', False, pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 35, 6), )

    
    machine = property(__machine.value, __machine.set, None, None)

    
    # Element security uses Python identifier security
    __security = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'security'), 'security', '__AbsentNamespace0_roleType_security', False, pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 36, 6), )

    
    security = property(__security.value, __security.set, None, None)

    
    # Element packages uses Python identifier packages
    __packages = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'packages'), 'packages', '__AbsentNamespace0_roleType_packages', False, pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 37, 6), )

    
    packages = property(__packages.value, __packages.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_roleType_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 39, 4)
    __name._UseLocation = pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 39, 4)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        __machine.name() : __machine,
        __security.name() : __security,
        __packages.name() : __packages
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
    _XSDLocation = pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 41, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element location uses Python identifier location
    __location = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'location'), 'location', '__AbsentNamespace0_serviceType_location', False, pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 43, 6), )

    
    location = property(__location.value, __location.set, None, None)

    
    # Element role uses Python identifier role
    __role = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'role'), 'role', '__AbsentNamespace0_serviceType_role', True, pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 44, 6), )

    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_serviceType_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 46, 4)
    __name._UseLocation = pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 46, 4)
    
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



machineType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'size'), pyxb.binding.datatypes.string, scope=machineType, location=pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 6, 6)))

machineType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'count'), pyxb.binding.datatypes.byte, scope=machineType, location=pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 7, 6)))

machineType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'location'), pyxb.binding.datatypes.string, scope=machineType, location=pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 8, 6)))

machineType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'image'), pyxb.binding.datatypes.string, scope=machineType, location=pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 9, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(machineType._UseForTag(pyxb.namespace.ExpandedName(None, 'size')), pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 6, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(machineType._UseForTag(pyxb.namespace.ExpandedName(None, 'count')), pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 7, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(machineType._UseForTag(pyxb.namespace.ExpandedName(None, 'location')), pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 8, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(machineType._UseForTag(pyxb.namespace.ExpandedName(None, 'image')), pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 9, 6))
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
machineType._Automaton = _BuildAutomaton()




securityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'sshpempath'), pyxb.binding.datatypes.string, scope=securityType, location=pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 14, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(securityType._UseForTag(pyxb.namespace.ExpandedName(None, 'sshpempath')), pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 14, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
securityType._Automaton = _BuildAutomaton_()




repositoriesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'repository'), pyxb.binding.datatypes.string, scope=repositoriesType, location=pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 19, 6)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(repositoriesType._UseForTag(pyxb.namespace.ExpandedName(None, 'repository')), pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 19, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
repositoriesType._Automaton = _BuildAutomaton_2()




installationsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'install'), pyxb.binding.datatypes.string, scope=installationsType, location=pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 24, 6)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 24, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(installationsType._UseForTag(pyxb.namespace.ExpandedName(None, 'install')), pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 24, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
installationsType._Automaton = _BuildAutomaton_3()




packagesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'repositories'), repositoriesType, scope=packagesType, location=pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 29, 6)))

packagesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'installations'), installationsType, scope=packagesType, location=pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 30, 6)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(packagesType._UseForTag(pyxb.namespace.ExpandedName(None, 'repositories')), pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 29, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(packagesType._UseForTag(pyxb.namespace.ExpandedName(None, 'installations')), pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 30, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
packagesType._Automaton = _BuildAutomaton_4()




roleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'machine'), machineType, scope=roleType, location=pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 35, 6)))

roleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'security'), securityType, scope=roleType, location=pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 36, 6)))

roleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'packages'), packagesType, scope=roleType, location=pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 37, 6)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(roleType._UseForTag(pyxb.namespace.ExpandedName(None, 'machine')), pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 35, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(roleType._UseForTag(pyxb.namespace.ExpandedName(None, 'security')), pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 36, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(roleType._UseForTag(pyxb.namespace.ExpandedName(None, 'packages')), pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 37, 6))
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
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
roleType._Automaton = _BuildAutomaton_5()




serviceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'location'), pyxb.binding.datatypes.string, scope=serviceType, location=pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 43, 6)))

serviceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'role'), roleType, scope=serviceType, location=pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 44, 6)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 44, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(serviceType._UseForTag(pyxb.namespace.ExpandedName(None, 'location')), pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 43, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(serviceType._UseForTag(pyxb.namespace.ExpandedName(None, 'role')), pyxb.utils.utility.Location('/home/blr/azure-programming/cloud-barista/service.xsd', 44, 6))
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
serviceType._Automaton = _BuildAutomaton_6()

