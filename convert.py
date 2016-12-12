#!/usr/bin/python
import re
import os
from lxml import etree
import xml.etree.cElementTree as ET
import glob
import fnmatch

VIM_DFAULT_VALUE = re.compile(r'(?P<var_name>(?<=\$\{)[0-9]{1,}):(?P<var_default>.+?)\}')
VIM_REPLACE = re.compile(r'\$\{([0-9]+):?.*?\}')
SNIPPET_TEXT_LENGTH = len('snippet')
VIM_SNIPPET_PATH = 'vim-snippets/snippets/'
BOOTSTRAP_VIM_SNIPPET_PATH = 'bootstrap-snippets/snippets/'
INTELLIJ_SNIPPET_PATH = 'intellij-snippets/resources/templates/'


def convert(fn):
    basename = os.path.basename(fn)
    name = os.path.splitext(basename)[0]
    if name is '_':
        return
    outputPath = INTELLIJ_SNIPPET_PATH + name + '.xml'
    language = name
    if name.startswith('javascript'):
        language = 'javascript'
    elif name.startswith('perl'):
        language = 'perl'
    elif name.startswith('php'):
        language = 'php'
    elif name.startswith('bootstrap'):
        language = 'html'

    templateSetNode = etree.Element('templateSet', group = name)
    with open(fn) as f:
        vimTemplate = {}
        for line in f:
            if line.startswith('#') or line.startswith('snippet'):
                # Store previous vimTemplate to new file
                if 'value' in vimTemplate and 'name' in vimTemplate:
                    templateSetNode.append(vimToIntellijTemplate(vimTemplate, language))

                # Reset vimTemplate to store new snippet structs
                vimTemplate = {}
                if line.startswith('#'):
                    vimTemplate['comment'] = line[1:].strip()
                else:
                    vimTemplate['name'] = line[SNIPPET_TEXT_LENGTH:].strip().split(' ')[0]
            else:
                if 'value' not in vimTemplate:
                    vimTemplate['value'] = []
                vimTemplate['value'].append(line.strip())

    s = etree.tostring(templateSetNode, pretty_print=True)
    output = open(outputPath, 'w')
    output.write(s)


def vimToIntellijTemplate(vimTemplate, language):
    intellijTemplate = {}
    name = vimTemplate['name']
    description = vimTemplate['comment'] if 'comment' in vimTemplate else ''
    value = ''.join([re.sub(VIM_REPLACE, r'$\1$', v).replace('$0$', '$END$') for v in vimTemplate['value']])
    templateNode = etree.Element('template', name=name, value=value, description=description, toReformat="true", toShortenFQNames="true")

    defaultValues = [re.findall(VIM_DFAULT_VALUE, v) for v in vimTemplate['value']]
    # flatten
    defaultValues = [item for sublist in defaultValues for item in sublist]
    for defaultValue in defaultValues:
        if defaultValue:
            defaultValueNode = etree.Element('variable', name=defaultValue[0], expression="", defaultValue='"{}"'.format(defaultValue[1]), alwaysStopAt="true")
            templateNode.append(defaultValueNode)
    contextNode = etree.Element('context')
    optionNode = etree.Element('option', name=language.upper(), value="true")
    contextNode.append(optionNode)
    templateNode.append(contextNode)
    return templateNode


if __name__ == '__main__':
    fns = []
    for root, dirnames, filenames in os.walk(VIM_SNIPPET_PATH):
        for filename in fnmatch.filter(filenames, '*.snippets'):
            fns.append(os.path.join(root, filename))
    for fn in fns:
        convert(fn)
