#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#
# Generated Fri Nov 30 13:17:29 2012 by generateDS.py version 2.7c.
#

import sys
import getopt
import re as re_

import common_types_1_0

etree_ = None
Verbose_import_ = False
(   XMLParser_import_none, XMLParser_import_lxml,
    XMLParser_import_elementtree
    ) = range(3)
XMLParser_import_library = None
try:
    # lxml
    from lxml import etree as etree_
    XMLParser_import_library = XMLParser_import_lxml
    if Verbose_import_:
        print("running with lxml.etree")
except ImportError:
    try:
        # cElementTree from Python 2.5+
        import xml.etree.cElementTree as etree_
        XMLParser_import_library = XMLParser_import_elementtree
        if Verbose_import_:
            print("running with cElementTree on Python 2.5+")
    except ImportError:
        try:
            # ElementTree from Python 2.5+
            import xml.etree.ElementTree as etree_
            XMLParser_import_library = XMLParser_import_elementtree
            if Verbose_import_:
                print("running with ElementTree on Python 2.5+")
        except ImportError:
            try:
                # normal cElementTree install
                import cElementTree as etree_
                XMLParser_import_library = XMLParser_import_elementtree
                if Verbose_import_:
                    print("running with cElementTree")
            except ImportError:
                try:
                    # normal ElementTree install
                    import elementtree.ElementTree as etree_
                    XMLParser_import_library = XMLParser_import_elementtree
                    if Verbose_import_:
                        print("running with ElementTree")
                except ImportError:
                    raise ImportError("Failed to import ElementTree from any known place")

def parsexml_(*args, **kwargs):
    if (XMLParser_import_library == XMLParser_import_lxml and
        'parser' not in kwargs):
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        kwargs['parser'] = etree_.ETCompatXMLParser()
    doc = etree_.parse(*args, **kwargs)
    return doc

#
# User methods
#
# Calls to the methods in these classes are generated by generateDS.py.
# You can replace these methods by re-implementing the following class
#   in a module named generatedssuper.py.

try:
    from generatedssuper import GeneratedsSuper
except ImportError, exp:

    class GeneratedsSuper(object):
        def gds_format_string(self, input_data, input_name=''):
            return input_data
        def gds_validate_string(self, input_data, node, input_name=''):
            return input_data
        def gds_format_integer(self, input_data, input_name=''):
            return '%d' % input_data
        def gds_validate_integer(self, input_data, node, input_name=''):
            return input_data
        def gds_format_integer_list(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_integer_list(self, input_data, node, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    fvalue = float(value)
                except (TypeError, ValueError), exp:
                    raise_parse_error(node, 'Requires sequence of integers')
            return input_data
        def gds_format_float(self, input_data, input_name=''):
            return '%f' % input_data
        def gds_validate_float(self, input_data, node, input_name=''):
            return input_data
        def gds_format_float_list(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_float_list(self, input_data, node, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    fvalue = float(value)
                except (TypeError, ValueError), exp:
                    raise_parse_error(node, 'Requires sequence of floats')
            return input_data
        def gds_format_double(self, input_data, input_name=''):
            return '%e' % input_data
        def gds_validate_double(self, input_data, node, input_name=''):
            return input_data
        def gds_format_double_list(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_double_list(self, input_data, node, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    fvalue = float(value)
                except (TypeError, ValueError), exp:
                    raise_parse_error(node, 'Requires sequence of doubles')
            return input_data
        def gds_format_boolean(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_boolean(self, input_data, node, input_name=''):
            return input_data
        def gds_format_boolean_list(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_boolean_list(self, input_data, node, input_name=''):
            values = input_data.split()
            for value in values:
                if value not in ('true', '1', 'false', '0', ):
                    raise_parse_error(node, 'Requires sequence of booleans ("true", "1", "false", "0")')
            return input_data
        def gds_str_lower(self, instring):
            return instring.lower()
        def get_path_(self, node):
            path_list = []
            self.get_path_list_(node, path_list)
            path_list.reverse()
            path = '/'.join(path_list)
            return path
        Tag_strip_pattern_ = re_.compile(r'\{.*\}')
        def get_path_list_(self, node, path_list):
            if node is None:
                return
            tag = GeneratedsSuper.Tag_strip_pattern_.sub('', node.tag)
            if tag:
                path_list.append(tag)
            self.get_path_list_(node.getparent(), path_list)
        def get_class_obj_(self, node, default_class=None):
            class_obj1 = default_class
            if 'xsi' in node.nsmap:
                classname = node.get('{%s}type' % node.nsmap['xsi'])
                if classname is not None:
                    names = classname.split(':')
                    if len(names) == 2:
                        classname = names[1]
                    class_obj2 = globals().get(classname)
                    if class_obj2 is not None:
                        class_obj1 = class_obj2
            return class_obj1
        def gds_build_any(self, node, type_name=None):
            return None


#
# If you have installed IPython you can uncomment and use the following.
# IPython is available from http://ipython.scipy.org/.
#

## from IPython.Shell import IPShellEmbed
## args = ''
## ipshell = IPShellEmbed(args,
##     banner = 'Dropping into IPython',
##     exit_msg = 'Leaving Interpreter, back to program.')

# Then use the following line where and when you want to drop into the
# IPython shell:
#    ipshell('<some message> -- Entering ipshell.\nHit Ctrl-D to exit')

#
# Globals
#

ExternalEncoding = 'ascii'
Tag_pattern_ = re_.compile(r'({.*})?(.*)')
String_cleanup_pat_ = re_.compile(r"[\n\r\s]+")
Namespace_extract_pat_ = re_.compile(r'{(.*)}(.*)')

#
# Support/utility functions.
#

def showIndent(outfile, level, pretty_print=True):
    if pretty_print:
        for idx in range(level):
            outfile.write('    ')

def quote_xml(inStr):
    if not inStr:
        return ''
    s1 = (isinstance(inStr, basestring) and inStr or
          '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    return s1

def quote_attrib(inStr):
    s1 = (isinstance(inStr, basestring) and inStr or
          '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    if '"' in s1:
        if "'" in s1:
            s1 = '"%s"' % s1.replace('"', "&quot;")
        else:
            s1 = "'%s'" % s1
    else:
        s1 = '"%s"' % s1
    return s1

def quote_python(inStr):
    s1 = inStr
    if s1.find("'") == -1:
        if s1.find('\n') == -1:
            return "'%s'" % s1
        else:
            return "'''%s'''" % s1
    else:
        if s1.find('"') != -1:
            s1 = s1.replace('"', '\\"')
        if s1.find('\n') == -1:
            return '"%s"' % s1
        else:
            return '"""%s"""' % s1

def get_all_text_(node):
    if node.text is not None:
        text = node.text
    else:
        text = ''
    for child in node:
        if child.tail is not None:
            text += child.tail
    return text

def find_attr_value_(attr_name, node):
    attrs = node.attrib
    attr_parts = attr_name.split(':')
    value = None
    if len(attr_parts) == 1:
        value = attrs.get(attr_name)
    elif len(attr_parts) == 2:
        prefix, name = attr_parts
        namespace = node.nsmap.get(prefix)
        if namespace is not None:
            value = attrs.get('{%s}%s' % (namespace, name, ))
    return value


class GDSParseError(Exception):
    pass

def raise_parse_error(node, msg):
    if XMLParser_import_library == XMLParser_import_lxml:
        msg = '%s (element %s/line %d)' % (msg, node.tag, node.sourceline, )
    else:
        msg = '%s (element %s)' % (msg, node.tag, )
    raise GDSParseError(msg)


class MixedContainer:
    # Constants for category:
    CategoryNone = 0
    CategoryText = 1
    CategorySimple = 2
    CategoryComplex = 3
    # Constants for content_type:
    TypeNone = 0
    TypeText = 1
    TypeString = 2
    TypeInteger = 3
    TypeFloat = 4
    TypeDecimal = 5
    TypeDouble = 6
    TypeBoolean = 7
    def __init__(self, category, content_type, name, value):
        self.category = category
        self.content_type = content_type
        self.name = name
        self.value = value
    def getCategory(self):
        return self.category
    def getContenttype(self, content_type):
        return self.content_type
    def getValue(self):
        return self.value
    def getName(self):
        return self.name
    def export(self, outfile, level, name, namespace, pretty_print=True):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip(): 
                outfile.write(self.value)
        elif self.category == MixedContainer.CategorySimple:
            self.exportSimple(outfile, level, name)
        else:    # category == MixedContainer.CategoryComplex
            self.value.export(outfile, level, namespace, name, pretty_print)
    def exportSimple(self, outfile, level, name):
        if self.content_type == MixedContainer.TypeString:
            outfile.write('<%s>%s</%s>' % (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeInteger or \
                self.content_type == MixedContainer.TypeBoolean:
            outfile.write('<%s>%d</%s>' % (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeFloat or \
                self.content_type == MixedContainer.TypeDecimal:
            outfile.write('<%s>%f</%s>' % (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeDouble:
            outfile.write('<%s>%g</%s>' % (self.name, self.value, self.name))
    def exportLiteral(self, outfile, level, name):
        if self.category == MixedContainer.CategoryText:
            showIndent(outfile, level)
            outfile.write('model_.MixedContainer(%d, %d, "%s", "%s"),\n' % \
                (self.category, self.content_type, self.name, self.value))
        elif self.category == MixedContainer.CategorySimple:
            showIndent(outfile, level)
            outfile.write('model_.MixedContainer(%d, %d, "%s", "%s"),\n' % \
                (self.category, self.content_type, self.name, self.value))
        else:    # category == MixedContainer.CategoryComplex
            showIndent(outfile, level)
            outfile.write('model_.MixedContainer(%d, %d, "%s",\n' % \
                (self.category, self.content_type, self.name,))
            self.value.exportLiteral(outfile, level + 1)
            showIndent(outfile, level)
            outfile.write(')\n')


class MemberSpec_(object):
    def __init__(self, name='', data_type='', container=0):
        self.name = name
        self.data_type = data_type
        self.container = container
    def set_name(self, name): self.name = name
    def get_name(self): return self.name
    def set_data_type(self, data_type): self.data_type = data_type
    def get_data_type_chain(self): return self.data_type
    def get_data_type(self):
        if isinstance(self.data_type, list):
            if len(self.data_type) > 0:
                return self.data_type[-1]
            else:
                return 'xs:string'
        else:
            return self.data_type
    def set_container(self, container): self.container = container
    def get_container(self): return self.container

def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)

#
# Data representation classes.
#

class LibraryType(GeneratedsSuper):
    """The LibraryType identifies a single library incorporated into the
    build of the tool.This field identifies the name of the
    library.This field identifies the version of the library."""
    subclass = None
    superclass = None
    def __init__(self, version=None, name=None, valueOf_=None):
        self.version = _cast(None, version)
        self.name = _cast(None, name)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if common_types_1_0.LibraryType.subclass:
            return LibraryType.subclass(*args_, **kwargs_)
        else:
            return LibraryType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_version(self): return self.version
    def set_version(self, version): self.version = version
    def get_name(self): return self.name
    def set_name(self, name): self.name = name
    def export(self, outfile, level, namespace_='LibraryObj:', name_='LibraryType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='LibraryType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='LibraryObj:', name_='LibraryType'):
        if self.version is not None and 'version' not in already_processed:
            already_processed.append('version')
            outfile.write(' version=%s' % (self.gds_format_string(quote_attrib(self.version).encode(ExternalEncoding), input_name='version'), ))
        if self.name is not None and 'name' not in already_processed:
            already_processed.append('name')
            outfile.write(' name=%s' % (self.gds_format_string(quote_attrib(self.name).encode(ExternalEncoding), input_name='name'), ))
    def exportChildren(self, outfile, level, namespace_='LibraryObj:', name_='LibraryType', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='LibraryType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.version is not None and 'version' not in already_processed:
            already_processed.append('version')
            showIndent(outfile, level)
            outfile.write('version = "%s",\n' % (self.version,))
        if self.name is not None and 'name' not in already_processed:
            already_processed.append('name')
            showIndent(outfile, level)
            outfile.write('name = "%s",\n' % (self.name,))
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('version', node)
        if value is not None and 'version' not in already_processed:
            already_processed.append('version')
            self.version = value
        value = find_attr_value_('name', node)
        if value is not None and 'name' not in already_processed:
            already_processed.append('name')
            self.name = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class LibraryType

class LibraryObjectType(common_types_1_0.DefinedObjectType):
    """The LibraryObjectType type is intended to characterize software
    libraries."""
    subclass = None
    superclass = common_types_1_0.DefinedObjectType
    def __init__(self, object_reference=None, Name=None, Path=None, Size=None, Type=None, Version=None, Base_Address=None):
        super(LibraryObjectType, self).__init__(object_reference, )
        self.Name = Name
        self.Path = Path
        self.Size = Size
        self.Type = Type
        self.Version = Version
        self.Base_Address = Base_Address
    def factory(*args_, **kwargs_):
        if LibraryObjectType.subclass:
            return LibraryObjectType.subclass(*args_, **kwargs_)
        else:
            return LibraryObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Name(self): return self.Name
    def set_Name(self, Name): self.Name = Name
    def validate_StringObjectAttributeType(self, value):
        # Validate type common_types_1_0.StringObjectAttributeType, a restriction on xs:string.
        pass
    def get_Path(self): return self.Path
    def set_Path(self, Path): self.Path = Path
    def get_Size(self): return self.Size
    def set_Size(self, Size): self.Size = Size
    def validate_UnsignedLongObjectAttributeType(self, value):
        # Validate type common_types_1_0.UnsignedLongObjectAttributeType, a restriction on None.
        pass
    def get_Type(self): return self.Type
    def set_Type(self, Type): self.Type = Type
    def validate_LibraryType(self, value):
        # Validate type LibraryType, a restriction on None.
        pass
    def get_Version(self): return self.Version
    def set_Version(self, Version): self.Version = Version
    def get_Base_Address(self): return self.Base_Address
    def set_Base_Address(self, Base_Address): self.Base_Address = Base_Address
    def validate_HexBinaryObjectAttributeType(self, value):
        # Validate type common_types_1_0.HexBinaryObjectAttributeType, a restriction on xs:hexBinary.
        pass
    def export(self, outfile, level, namespace_='LibraryObj:', name_='LibraryObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='LibraryObjectType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='LibraryObj:', name_='LibraryObjectType'):
        super(LibraryObjectType, self).exportAttributes(outfile, level, already_processed, namespace_, name_='LibraryObjectType')
    def exportChildren(self, outfile, level, namespace_='LibraryObj:', name_='LibraryObjectType', fromsubclass_=False, pretty_print=True):
        super(LibraryObjectType, self).exportChildren(outfile, level, 'LibraryObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Name is not None:
            self.Name.export(outfile, level, 'LibraryObj:', name_='Name', pretty_print=pretty_print)
        if self.Path is not None:
            self.Path.export(outfile, level, 'LibraryObj:', name_='Path', pretty_print=pretty_print)
        if self.Size is not None:
            self.Size.export(outfile, level, 'LibraryObj:', name_='Size', pretty_print=pretty_print)
        if self.Type is not None:
            self.Type.export(outfile, level, 'LibraryObj:', name_='Type', pretty_print=pretty_print)
        if self.Version is not None:
            self.Version.export(outfile, level, 'LibraryObj:', name_='Version', pretty_print=pretty_print)
        if self.Base_Address is not None:
            self.Base_Address.export(outfile, level, 'LibraryObj:', name_='Base_Address', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.Name is not None or
            self.Path is not None or
            self.Size is not None or
            self.Type is not None or
            self.Version is not None or
            self.Base_Address is not None or
            super(LibraryObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='LibraryObjectType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        super(LibraryObjectType, self).exportLiteralAttributes(outfile, level, already_processed, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        super(LibraryObjectType, self).exportLiteralChildren(outfile, level, name_)
        if self.Name is not None:
            showIndent(outfile, level)
            outfile.write('Name=%s,\n' % quote_python(self.Name).encode(ExternalEncoding))
        if self.Path is not None:
            showIndent(outfile, level)
            outfile.write('Path=%s,\n' % quote_python(self.Path).encode(ExternalEncoding))
        if self.Size is not None:
            showIndent(outfile, level)
            outfile.write('Size=model_.common_types_1_0.UnsignedLongObjectAttributeType(\n')
            self.Size.exportLiteral(outfile, level, name_='Size')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Type is not None:
            showIndent(outfile, level)
            outfile.write('Type=model_.LibraryType(\n')
            self.Type.exportLiteral(outfile, level, name_='Type')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Version is not None:
            showIndent(outfile, level)
            outfile.write('Version=%s,\n' % quote_python(self.Version).encode(ExternalEncoding))
        if self.Base_Address is not None:
            showIndent(outfile, level)
            outfile.write('Base_Address=%s,\n' % quote_python(self.Base_Address).encode(ExternalEncoding))
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(LibraryObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Name':
            obj_ = common_types_1_0.StringObjectAttributeType.factory()
            obj_.build(child_)
            self.set_Name(obj_)
        elif nodeName_ == 'Path':
            obj_ = common_types_1_0.StringObjectAttributeType.factory()
            obj_.build(child_)
            self.set_Path(obj_)
        elif nodeName_ == 'Size':
            obj_ = common_types_1_0.UnsignedLongObjectAttributeType.factory()
            obj_.build(child_)
            self.set_Size(obj_)
        elif nodeName_ == 'Type':
            obj_ = LibraryType.factory()
            obj_.build(child_)
            self.set_Type(obj_)
        elif nodeName_ == 'Version':
            obj_ = common_types_1_0.StringObjectAttributeType.factory()
            obj_.build(child_)
            self.set_Version(obj_)
        elif nodeName_ == 'Base_Address':
            obj_ = common_types_1_0.HexBinaryObjectAttributeType.factory()
            obj_.build(child_)
            self.set_Base_Address(obj_)
        super(LibraryObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class LibraryObjectType

USAGE_TEXT = """
Usage: python <Parser>.py [ -s ] <in_xml_file>
"""

def usage():
    print USAGE_TEXT
    sys.exit(1)

def get_root_tag(node):
    tag = Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = globals().get(tag)
    return tag, rootClass

def parse(inFileName):
    doc = parsexml_(inFileName)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Library'
        rootClass = LibraryObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0, name_=rootTag,
        namespacedef_='',
        pretty_print=True)
    return rootObj

def parseString(inString):
    from StringIO import StringIO
    doc = parsexml_(StringIO(inString))
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Library'
        rootClass = LibraryObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0, name_="Library",
        namespacedef_='')
    return rootObj

def parseLiteral(inFileName):
    doc = parsexml_(inFileName)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Library'
        rootClass = LibraryObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('#from temp import *\n\n')
    sys.stdout.write('import temp as model_\n\n')
    sys.stdout.write('rootObj = model_.rootTag(\n')
    rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
    sys.stdout.write(')\n')
    return rootObj

def main():
    args = sys.argv[1:]
    if len(args) == 1:
        parse(args[0])
    else:
        usage()

if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()

__all__ = [
    "LibraryObjectType",
    "LibraryType"
    ]