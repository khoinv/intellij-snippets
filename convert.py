#!/usr/bin/python
import re
import os
from lxml import etree
import xml.etree.cElementTree as ET
import glob
import fnmatch

VIM_DFAULT_VALUE = re.compile(r'(?P<var_name>(?<=\$\{)[0-9]{1,}):(?P<var_default>.+?)\}')
VIM_ALL_VARS = re.compile(r'(?P<var_name>(?<=\$\{)[0-9]{1,}):?.*?\}')
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
            if line.startswith('#') or line.startswith('snippet') or line.startswith('endsnippet'):
                if 'value' in vimTemplate and 'name' in vimTemplate:
                    # TODO: remove ignoring bash shell
                    valueStr = ''.join(vimTemplate['value'])
                    if valueStr != '\n' and '`' not in valueStr:
                        templateSetNode.append(vimToIntelliJTemplate(vimTemplate, supportLanguages, prefix))

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

def getIntelliJDefaultValue(express):
    hasDefaultValues = [re.findall(VIM_DFAULT_VALUE, v) for v in express]
    allVars = [re.findall(VIM_ALL_VARS, v) for v in express]

    # flatten
    hasDefaultValues = [item for sublist in hasDefaultValues for item in sublist]
    allVars= [item for sublist in allVars for item in sublist]

    hasDefaultValuesDict = {}
    defaultValues = {}

    for item in hasDefaultValues:
        hasDefaultValuesDict[item[0]] = item[1]

    for item in allVars:
        if item[0] in hasDefaultValuesDict:
            defaultValues[item[0]] = hasDefaultValuesDict[item[0]].replace('"', '\\"')
        else:
            defaultValues[item[0]] = None

    return defaultValues

def getInelliJExpression(expression, defaultValues):
    value = None
    if '0' in defaultValues:
        if not defaultValues['0']:
            # var0 is $END$
            value = ''.join([re.sub(VIM_REPLACE1, r'$var\1$', re.sub(VIM_REPLACE2, r'$var\1$', v) ).replace('$var0$', '$END$') for v in expression])
            del defaultValues['0']
        else:
         value = ''.join([re.sub(VIM_REPLACE1, r'$var\1$', re.sub(VIM_REPLACE2, r'$var\1$', v) ) for v in expression])
         value +='$END$'
    else:
         value = ''.join([re.sub(VIM_REPLACE1, r'$var\1$', re.sub(VIM_REPLACE2, r'$var\1$', v) ) for v in expression])

    return value



def vimToIntelliJTemplate(vimTemplate, supportLanguages, prefix):
    # Convert(inFile, outFile, prefix, language, [supportLanguages])
    # If you want create a snippet support all language please set languages is 'OTHER'
    # Prefix can be empty

    intellijTemplate = {}
    name = prefix + vimTemplate['name']
    description = vimTemplate['comment'] if 'comment' in vimTemplate else ''

    defaultValues = getIntelliJDefaultValue(vimTemplate['value'])
    expression = getInelliJExpression(vimTemplate['value'], defaultValues)
    templateNode = etree.Element('template', name=name, value=expression, description=description, toReformat="true", toShortenFQNames="true")

    defaultValueKeys = defaultValues.keys();
    for key in sorted(defaultValueKeys):
        if(key != '0'):
            value = defaultValues[key]
            if value:
                defaultValueNode = etree.Element('variable', name="var{}".format(key), expression="", defaultValue='"{}"'.format(value), alwaysStopAt="true")
            else:
                defaultValueNode = etree.Element('variable', name="var{}".format(key), expression="", defaultValue="", alwaysStopAt="true")
            templateNode.append(defaultValueNode)

    if '0' in defaultValues:
        key = '0'
        value = defaultValues[key]
        if value:
            defaultValueNode = etree.Element('variable', name="var{}".format(key), expression="", defaultValue='"{}"'.format(value), alwaysStopAt="true")
        else:
            defaultValueNode = etree.Element('variable', name="var{}".format(key), expression="", defaultValue="", alwaysStopAt="true")
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
    convert('vim-snippets/snippets/javascript/javascript.es6.snippets', 'intellij-snippets/resources/templates/javascript.es6.xml', 'js6-', 'javascript.es6', 'javascript', ['TypeScript','JAVA_SCRIPT', 'HTML'])
    convert('vim-snippets/snippets/javascript/javascript.node.snippets', 'intellij-snippets/resources/templates/javascript.node.xml', 'nd-', 'node', 'javascript', ['TypeScript','JAVA_SCRIPT', 'HTML'])
    convert('vim-snippets/snippets/javascript-d3.snippets', 'intellij-snippets/resources/templates/javascript-d3.xml', 'd3-', 'javascript-d3', 'javascript', ['TypeScript','JAVA_SCRIPT', 'HTML'])
    convert('vim-snippets/UltiSnips/javascript-angular.snippets', 'intellij-snippets/resources/templates/angular.xml', 'ng-', 'angular', 'javascript', ['TypeScript','JAVA_SCRIPT', 'HTML'])
    convert('vim-snippets/snippets/html.snippets', 'intellij-snippets/resources/templates/html.xml', 'h-', 'html','html', ['TypeScript', 'JAVA_SCRIPT', 'HTML'])
    convert('vim-snippets/snippets/django.snippets', 'intellij-snippets/resources/templates/django.xml', 'dj', 'django', 'python',  ['Django'])
    convert('vim-snippets/snippets/php.snippets', 'intellij-snippets/resources/templates/php.xml', 'p-', 'php','php', ['PHP', 'HTML'])
    convert('vim-snippets/snippets/go.snippets', 'intellij-snippets/resources/templates/go.xml', '', 'go', 'go', ['GO'])
    convert('vim-snippets/snippets/scala.snippets', 'intellij-snippets/resources/templates/scala.xml', 's-', 'scala','scala', ['SCALA'])
    convert('vim-snippets/snippets/ruby.snippets', 'intellij-snippets/resources/templates/ruby.xml', 'rb-', 'ruby','ruby', ['RUBY'])
    convert('vim-snippets/snippets/rails.snippets', 'intellij-snippets/resources/templates/rails.xml', 'rl-', 'rails', 'ruby', ['RUBY', 'RHTML'])
    convert('vim-snippets/snippets/eruby.snippets', 'intellij-snippets/resources/templates/eruby.xml', 'er-', 'eruby', 'ruby', ['RHTML', 'RUBY', 'HTML'])
    convert('vim-snippets/snippets/laravel.snippets', 'intellij-snippets/resources/templates/laravel.xml', '', 'laravel', 'php', ['PHP', 'HTML'])
    convert('vim-snippets/snippets/codeigniter.snippets', 'intellij-snippets/resources/templates/codeigniter.xml', '', 'codeigniter','php', ['PHP', 'HTML'])
    convert('vim-snippets/snippets/cs.snippets', 'intellij-snippets/resources/templates/cs.xml', 'js-', 'javascript2', 'cs', ['JAVA_SCRIPT', 'HTML'])
    convert('vim-snippets/snippets/css.snippets', 'intellij-snippets/resources/templates/css.xml', 'c-', 'css', 'css', ['CSS', 'HTML'])
    convert('vim-snippets/snippets/sass.snippets', 'intellij-snippets/resources/templates/sass.xml', 's-', 'sass', 'css', ['CSS', 'HTML'])
    convert('vim-snippets/snippets/markdown.snippets', 'intellij-snippets/resources/templates/markdown.xml', 'md-', 'markdown', 'markdown', ['OTHER'])
    convert('vim-snippets/snippets/java.snippets', 'intellij-snippets/resources/templates/java.xml', 'j-', 'java', 'java', ['JAVA_CODE', 'JSP', 'HTML'])
    convert('vim-snippets/snippets/sql.snippets', 'intellij-snippets/resources/templates/sql.xml', 'sql-', 'sql', 'sql', ['SQL'])
    convert('bootstrap-snippets/snippets/html.snippets', 'intellij-snippets/resources/templates/bootstrap.xml', 'bs-', 'bootstrap', 'html', ['HTML'])
