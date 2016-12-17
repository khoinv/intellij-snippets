#!/usr/bin/python
import re
import os
from lxml import etree
import xml.etree.cElementTree as ET
import glob
import fnmatch

VIM_DFAULT_VALUE = re.compile(r'(?P<var_name>(?<=\$\{)[0-9]{1,}):(?P<var_default>.+?)\}')
VIM_REPLACE1 = re.compile(r'\$\{([0-9]+):?.*?\}')
VIM_REPLACE2 = re.compile(r'\$([0-9]+)')
SNIPPET_TEXT_LENGTH = len('snippet')
INTELLIJ_SNIPPET_PATH = 'intellij-snippets/resources/templates/'

def convert(inFile, outFile, prefix, group, language, supportLanguages):

    templateSetNode = etree.Element('templateSet', group = group)
    md = open('intellij-snippets/resources/documents/{}.md'.format(group), 'w')
    with open(inFile) as f:
        vimTemplate = {}
        for line in f:
            if line.startswith('#') or line.startswith('snippet'):
                # Store previous vimTemplate to new file
                if 'value' in vimTemplate and 'name' in vimTemplate:
                    templateSetNode.append(vimToIntellijTemplate(vimTemplate, supportLanguages, prefix))
                    md.write('####{}{}\n'.format(prefix, vimTemplate['name']))
                    md.write('```{}\n'.format(language))

                    for content in vimTemplate['value'][:-1]:
                        md.write('{}\n'.format(content))
                    md.write('{}```'.format(vimTemplate['value'][-1]))
                    md.write('\n')

                # Reset vimTemplate to store new snippet structs
                vimTemplate = {}
                if line.startswith('#'):
                    vimTemplate['comment'] = line[1:].strip()
                else:
                    vimTemplate['name'] = line[SNIPPET_TEXT_LENGTH:].strip().split(' ')[0]
            else:
                if 'value' not in vimTemplate:
                    vimTemplate['value'] = []
                vimTemplate['value'].append(line.replace('\t', '    '))

    s = etree.tostring(templateSetNode, pretty_print=True)
    output = open(outFile, 'w')
    output.write(s)


def vimToIntellijTemplate(vimTemplate, supportLanguages, prefix):
    # Convert(inFile, outFile, prefix, language, [supportLanguages])
    # If you want create a snippet support all language please set languages is 'OTHER'
    # Prefix can be empty

    intellijTemplate = {}
    name = prefix + vimTemplate['name']
    description = vimTemplate['comment'] if 'comment' in vimTemplate else ''
    # value = ''.join([re.sub(VIM_REPLACE1, r'$var\1$', re.sub(VIM_REPLACE2, r'$var\1$', v) ).replace('$var0$', '$END$') for v in vimTemplate['value']])
    value = ''.join([re.sub(VIM_REPLACE1, r'$var\1$', re.sub(VIM_REPLACE2, r'$var\1$', v) ) for v in vimTemplate['value']])
    templateNode = etree.Element('template', name=name, value=value, description=description, toReformat="true", toShortenFQNames="true")

    defaultValues = [re.findall(VIM_DFAULT_VALUE, v) for v in vimTemplate['value']]
    # flatten
    defaultValues = [item for sublist in defaultValues for item in sublist]
    for defaultValue in defaultValues:
        if defaultValue:
            # if(defaultValue[0]) == '0':
            #     defaultValueNode = etree.Element('variable', name="END", expression="", defaultValue='"{}"'.format(defaultValue[1]), alwaysStopAt="true")
            # else:
            defaultValueNode = etree.Element('variable', name="var{}".format(defaultValue[0]), expression="", defaultValue='"{}"'.format(defaultValue[1].replace('"', '\\"')), alwaysStopAt="true")
            templateNode.append(defaultValueNode)
    contextNode = etree.Element('context')
    for lg in supportLanguages:
        optionNode = etree.Element('option', name=lg, value="true")
        contextNode.append(optionNode)

    templateNode.append(contextNode)
    return templateNode

if __name__ == '__main__':
    convert('vim-snippets/snippets/javascript/javascript.snippets', 'intellij-snippets/resources/templates/javascript.xml', 'js-','javascript', 'javascript', ['TypeScript','JAVA_SCRIPT', 'HTML'])
    convert('vim-snippets/snippets/javascript/javascript-jquery.snippets', 'intellij-snippets/resources/templates/javascript-jquery.xml', 'jq-', 'jquery', 'javascript', ['TypeScript','JAVA_SCRIPT', 'HTML'])
    convert('vim-snippets/snippets/javascript/javascript-react.snippets', 'intellij-snippets/resources/templates/javascript-react.xml', 're-', 'react', 'javascript', ['TypeScript','JAVA_SCRIPT', 'HTML'])
    convert('vim-snippets/snippets/javascript/javascript.es6.snippets', 'intellij-snippets/resources/templates/javascript.es6.xml', 'js6-', 'javascritp.es6', 'javascript', ['TypeScript','JAVA_SCRIPT', 'HTML'])
    convert('vim-snippets/snippets/javascript/javascript.node.snippets', 'intellij-snippets/resources/templates/javascript.node.xml', 'nd-', 'node', 'javascript', ['TypeScript','JAVA_SCRIPT', 'HTML'])
    convert('vim-snippets/snippets/javascript-d3.snippets', 'intellij-snippets/resources/templates/javascript-d3.xml', 'd3-', 'javascript-d3', 'javascript', ['TypeScript','JAVA_SCRIPT', 'HTML'])
    convert('vim-snippets/UltiSnips/javascript-angular.snippets', 'intellij-snippets/resources/templates/angular.xml', 'd3-', 'angular', 'javascript', ['TypeScript','JAVA_SCRIPT', 'HTML'])
    convert('vim-snippets/snippets/html.snippets', 'intellij-snippets/resources/templates/html.xml', '', 'html','html', ['TypeScript', 'JAVA_SCRIPT', 'HTML'])
    convert('vim-snippets/snippets/django.snippets', 'intellij-snippets/resources/templates/django.xml', '', 'django', 'python',  ['Django'])
    convert('vim-snippets/snippets/php.snippets', 'intellij-snippets/resources/templates/php.xml', 'php-', 'php','php', ['PHP', 'HTML'])
    convert('vim-snippets/snippets/go.snippets', 'intellij-snippets/resources/templates/go.xml', '', 'go', 'go', ['GO'])
    convert('vim-snippets/snippets/scala.snippets', 'intellij-snippets/resources/templates/scala.xml', 'sl-', 'scala','scala', ['SCALA'])
    convert('vim-snippets/snippets/ruby.snippets', 'intellij-snippets/resources/templates/ruby.xml', 'rb-', 'ruby','ruby', ['RUBY'])
    convert('vim-snippets/snippets/rails.snippets', 'intellij-snippets/resources/templates/rails.xml', 'rail-', 'rails', 'ruby', ['RUBY', 'RHTML'])
    convert('vim-snippets/snippets/eruby.snippets', 'intellij-snippets/resources/templates/eruby.xml', 'er-', 'eruby', 'ruby', ['RHTML', 'RUBY', 'HTML'])
    convert('vim-snippets/snippets/laravel.snippets', 'intellij-snippets/resources/templates/laravel.xml', '', 'laravel', 'php', ['PHP', 'HTML'])
    convert('vim-snippets/snippets/codeigniter.snippets', 'intellij-snippets/resources/templates/codeigniter.xml', '', 'codeigniter','php', ['PHP', 'HTML'])
    convert('vim-snippets/snippets/cs.snippets', 'intellij-snippets/resources/templates/cs.xml', 'js-', 'javascript2', 'cs', ['OTHER'])
    convert('vim-snippets/snippets/css.snippets', 'intellij-snippets/resources/templates/css.xml', '', 'css', 'css', ['CSS', 'HTML'])
    convert('vim-snippets/snippets/sass.snippets', 'intellij-snippets/resources/templates/sass.xml', '', 'sass', 'css', ['CSS', 'HTML'])
    convert('vim-snippets/snippets/markdown.snippets', 'intellij-snippets/resources/templates/markdown.xml', 'md-', 'markdown', 'markdown', ['OTHER'])
    convert('vim-snippets/snippets/java.snippets', 'intellij-snippets/resources/templates/java.xml', 'jv-', 'java', 'java', ['JAVA_CODE', 'JSP', 'HTML'])
    convert('vim-snippets/snippets/sql.snippets', 'intellij-snippets/resources/templates/sql.xml', 'sql-', 'sql', 'sql', ['SQL'])
    convert('bootstrap-snippets/snippets/html.snippets', 'intellij-snippets/resources/templates/bootstrap.xml', 'bs-', 'bootstrap', 'html', ['JAVA_SCRIPT', 'HTML'])
