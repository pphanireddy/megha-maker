# ./topology.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2014-12-26 19:37:30.158140 by PyXB version 1.2.4 using Python 2.7.8.final.0
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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:af6534a6-8d79-11e4-804a-0023ae5e9502')

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


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 3, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element service uses Python identifier service
    __service = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'service'), 'service', '__AbsentNamespace0_CTD_ANON_service', False, pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 5, 8), )

    
    service = property(__service.value, __service.set, None, None)

    
    # Element storage uses Python identifier storage
    __storage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'storage'), 'storage', '__AbsentNamespace0_CTD_ANON_storage', False, pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 15, 8), )

    
    storage = property(__storage.value, __storage.set, None, None)

    
    # Element compute uses Python identifier compute
    __compute = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'compute'), 'compute', '__AbsentNamespace0_CTD_ANON_compute', False, pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 24, 8), )

    
    compute = property(__compute.value, __compute.set, None, None)

    
    # Element network uses Python identifier network
    __network = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'network'), 'network', '__AbsentNamespace0_CTD_ANON_network', False, pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 102, 8), )

    
    network = property(__network.value, __network.set, None, None)

    _ElementMap.update({
        __service.name() : __service,
        __storage.name() : __storage,
        __compute.name() : __compute,
        __network.name() : __network
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 6, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON__name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 9, 16)
    __name._UseLocation = pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 9, 16)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute region uses Python identifier region
    __region = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'region'), 'region', '__AbsentNamespace0_CTD_ANON__region', pyxb.binding.datatypes.string)
    __region._DeclarationLocation = pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 10, 16)
    __region._UseLocation = pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 10, 16)
    
    region = property(__region.value, __region.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name,
        __region.name() : __region
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 16, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON_2_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 19, 16)
    __name._UseLocation = pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 19, 16)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 25, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element role uses Python identifier role
    __role = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'role'), 'role', '__AbsentNamespace0_CTD_ANON_3_role', True, pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 27, 14), )

    
    role = property(__role.value, __role.set, None, None)

    _ElementMap.update({
        __role.name() : __role
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
    _XSDLocation = pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 28, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element osvhd uses Python identifier osvhd
    __osvhd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'osvhd'), 'osvhd', '__AbsentNamespace0_CTD_ANON_4_osvhd', False, pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 30, 20), )

    
    osvhd = property(__osvhd.value, __osvhd.set, None, None)

    
    # Element vmconf uses Python identifier vmconf
    __vmconf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'vmconf'), 'vmconf', '__AbsentNamespace0_CTD_ANON_4_vmconf', False, pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 56, 20), )

    
    vmconf = property(__vmconf.value, __vmconf.set, None, None)

    
    # Element netconf uses Python identifier netconf
    __netconf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'netconf'), 'netconf', '__AbsentNamespace0_CTD_ANON_4_netconf', False, pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 73, 20), )

    
    netconf = property(__netconf.value, __netconf.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__AbsentNamespace0_CTD_ANON_4_id', pyxb.binding.datatypes.string)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 94, 18)
    __id._UseLocation = pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 94, 18)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute count uses Python identifier count
    __count = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'count'), 'count', '__AbsentNamespace0_CTD_ANON_4_count', pyxb.binding.datatypes.byte)
    __count._DeclarationLocation = pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 95, 18)
    __count._UseLocation = pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 95, 18)
    
    count = property(__count.value, __count.set, None, None)

    
    # Attribute size uses Python identifier size
    __size = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'size'), 'size', '__AbsentNamespace0_CTD_ANON_4_size', pyxb.binding.datatypes.string)
    __size._DeclarationLocation = pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 96, 18)
    __size._UseLocation = pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 96, 18)
    
    size = property(__size.value, __size.set, None, None)

    _ElementMap.update({
        __osvhd.name() : __osvhd,
        __vmconf.name() : __vmconf,
        __netconf.name() : __netconf
    })
    _AttributeMap.update({
        __id.name() : __id,
        __count.name() : __count,
        __size.name() : __size
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 31, 22)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element image uses Python identifier image
    __image = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'image'), 'image', '__AbsentNamespace0_CTD_ANON_5_image', False, pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 33, 26), )

    
    image = property(__image.value, __image.set, None, None)

    
    # Element media uses Python identifier media
    __media = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'media'), 'media', '__AbsentNamespace0_CTD_ANON_5_media', False, pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 42, 26), )

    
    media = property(__media.value, __media.set, None, None)

    _ElementMap.update({
        __image.name() : __image,
        __media.name() : __media
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 34, 28)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__AbsentNamespace0_CTD_ANON_6_id', pyxb.binding.datatypes.string)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 37, 34)
    __id._UseLocation = pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 37, 34)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 43, 28)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute storageid uses Python identifier storageid
    __storageid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'storageid'), 'storageid', '__AbsentNamespace0_CTD_ANON_7_storageid', pyxb.binding.datatypes.string)
    __storageid._DeclarationLocation = pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 46, 34)
    __storageid._UseLocation = pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 46, 34)
    
    storageid = property(__storageid.value, __storageid.set, None, None)

    
    # Attribute container uses Python identifier container
    __container = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'container'), 'container', '__AbsentNamespace0_CTD_ANON_7_container', pyxb.binding.datatypes.string)
    __container._DeclarationLocation = pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 47, 34)
    __container._UseLocation = pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 47, 34)
    
    container = property(__container.value, __container.set, None, None)

    
    # Attribute blob uses Python identifier blob
    __blob = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'blob'), 'blob', '__AbsentNamespace0_CTD_ANON_7_blob', pyxb.binding.datatypes.string)
    __blob._DeclarationLocation = pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 48, 34)
    __blob._UseLocation = pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 48, 34)
    
    blob = property(__blob.value, __blob.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __storageid.name() : __storageid,
        __container.name() : __container,
        __blob.name() : __blob
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_8 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 57, 22)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element ssh uses Python identifier ssh
    __ssh = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ssh'), 'ssh', '__AbsentNamespace0_CTD_ANON_8_ssh', False, pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 59, 26), )

    
    ssh = property(__ssh.value, __ssh.set, None, None)

    _ElementMap.update({
        __ssh.name() : __ssh
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_9 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 60, 28)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute disablepasswordauth uses Python identifier disablepasswordauth
    __disablepasswordauth = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'disablepasswordauth'), 'disablepasswordauth', '__AbsentNamespace0_CTD_ANON_9_disablepasswordauth', pyxb.binding.datatypes.string)
    __disablepasswordauth._DeclarationLocation = pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 63, 34)
    __disablepasswordauth._UseLocation = pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 63, 34)
    
    disablepasswordauth = property(__disablepasswordauth.value, __disablepasswordauth.set, None, None)

    
    # Attribute username uses Python identifier username
    __username = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'username'), 'username', '__AbsentNamespace0_CTD_ANON_9_username', pyxb.binding.datatypes.string)
    __username._DeclarationLocation = pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 64, 34)
    __username._UseLocation = pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 64, 34)
    
    username = property(__username.value, __username.set, None, None)

    
    # Attribute password uses Python identifier password
    __password = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'password'), 'password', '__AbsentNamespace0_CTD_ANON_9_password', pyxb.binding.datatypes.string)
    __password._DeclarationLocation = pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 65, 34)
    __password._UseLocation = pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 65, 34)
    
    password = property(__password.value, __password.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __disablepasswordauth.name() : __disablepasswordauth,
        __username.name() : __username,
        __password.name() : __password
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_10 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 74, 22)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element endpoint uses Python identifier endpoint
    __endpoint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'endpoint'), 'endpoint', '__AbsentNamespace0_CTD_ANON_10_endpoint', True, pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 76, 26), )

    
    endpoint = property(__endpoint.value, __endpoint.set, None, None)

    _ElementMap.update({
        __endpoint.name() : __endpoint
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_11 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 77, 28)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON_11_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 80, 34)
    __name._UseLocation = pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 80, 34)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute isloadbalanced uses Python identifier isloadbalanced
    __isloadbalanced = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'isloadbalanced'), 'isloadbalanced', '__AbsentNamespace0_CTD_ANON_11_isloadbalanced', pyxb.binding.datatypes.string)
    __isloadbalanced._DeclarationLocation = pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 81, 34)
    __isloadbalanced._UseLocation = pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 81, 34)
    
    isloadbalanced = property(__isloadbalanced.value, __isloadbalanced.set, None, None)

    
    # Attribute protocol uses Python identifier protocol
    __protocol = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'protocol'), 'protocol', '__AbsentNamespace0_CTD_ANON_11_protocol', pyxb.binding.datatypes.string)
    __protocol._DeclarationLocation = pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 82, 34)
    __protocol._UseLocation = pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 82, 34)
    
    protocol = property(__protocol.value, __protocol.set, None, None)

    
    # Attribute start uses Python identifier start
    __start = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'start'), 'start', '__AbsentNamespace0_CTD_ANON_11_start', pyxb.binding.datatypes.byte)
    __start._DeclarationLocation = pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 83, 34)
    __start._UseLocation = pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 83, 34)
    
    start = property(__start.value, __start.set, None, None)

    
    # Attribute local uses Python identifier local
    __local = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'local'), 'local', '__AbsentNamespace0_CTD_ANON_11_local', pyxb.binding.datatypes.byte)
    __local._DeclarationLocation = pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 84, 34)
    __local._UseLocation = pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 84, 34)
    
    local = property(__local.value, __local.set, None, None)

    
    # Attribute cloud uses Python identifier cloud
    __cloud = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'cloud'), 'cloud', '__AbsentNamespace0_CTD_ANON_11_cloud', pyxb.binding.datatypes.byte)
    __cloud._DeclarationLocation = pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 85, 34)
    __cloud._UseLocation = pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 85, 34)
    
    cloud = property(__cloud.value, __cloud.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name,
        __isloadbalanced.name() : __isloadbalanced,
        __protocol.name() : __protocol,
        __start.name() : __start,
        __local.name() : __local,
        __cloud.name() : __cloud
    })



topology = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'topology'), CTD_ANON, location=pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 2, 2))
Namespace.addCategoryObject('elementBinding', topology.name().localName(), topology)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'service'), CTD_ANON_, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 5, 8)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'storage'), CTD_ANON_2, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 15, 8)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'compute'), CTD_ANON_3, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 24, 8)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'network'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 102, 8)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'service')), pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 5, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'storage')), pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 15, 8))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'compute')), pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 24, 8))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'network')), pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 102, 8))
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
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'role'), CTD_ANON_4, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 27, 14)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 27, 14))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, 'role')), pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 27, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'osvhd'), CTD_ANON_5, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 30, 20)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'vmconf'), CTD_ANON_8, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 56, 20)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'netconf'), CTD_ANON_10, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 73, 20)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(None, 'osvhd')), pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 30, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(None, 'vmconf')), pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 56, 20))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(None, 'netconf')), pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 73, 20))
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
CTD_ANON_4._Automaton = _BuildAutomaton_2()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'image'), CTD_ANON_6, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 33, 26)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'media'), CTD_ANON_7, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 42, 26)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(None, 'image')), pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 33, 26))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(None, 'media')), pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 42, 26))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_3()




CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ssh'), CTD_ANON_9, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 59, 26)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(None, 'ssh')), pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 59, 26))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_8._Automaton = _BuildAutomaton_4()




CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'endpoint'), CTD_ANON_11, scope=CTD_ANON_10, location=pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 76, 26)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 76, 26))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(None, 'endpoint')), pyxb.utils.utility.Location('/home/blr/cloudinfra/cloud-barista/cloudbarista/topology.xsd', 76, 26))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_10._Automaton = _BuildAutomaton_5()

