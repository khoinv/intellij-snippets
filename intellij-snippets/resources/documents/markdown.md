####md-[
```markdown
    [${1:text}](http://${2:address})
```
####md-[*
```markdown
    [${1:link}](${2:`@*`})
```
####md-[c
```markdown
    [${1:link}](${2:`@+`})
```
####md-["
```markdown
    [${1:text}](http://${2:address} "${3:title}")
```
####md-["*
```markdown
    [${1:link}](${2:`@*`} "${3:title}")
```
####md-["c
```markdown
    [${1:link}](${2:`@+`} "${3:title}")
```
####md-[:
```markdown
    [${1:id}]: http://${2:url}


```
####md-[:*
```markdown
    [${1:id}]: ${2:`@*`}


```
####md-[:c
```markdown
    [${1:id}]: ${2:`@+`}


```
####md-[:"
```markdown
    [${1:id}]: http://${2:url} "${3:title}"


```
####md-[:"*
```markdown
    [${1:id}]: ${2:`@*`} "${3:title}"


```
####md-[:"c
```markdown
    [${1:id}]: ${2:`@+`} "${3:title}"


```
####md-![
```markdown
    ![${1:alttext}](${2:/images/image.jpg})
```
####md-![*
```markdown
    ![${1:alt}](${2:`@*`})
```
####md-![c
```markdown
    ![${1:alt}](${2:`@+`})
```
####md-!["
```markdown
    ![${1:alttext}](${2:/images/image.jpg} "${3:title}")
```
####md-!["*
```markdown
    ![${1:alt}](${2:`@*`} "${3:title}")
```
####md-!["c
```markdown
    ![${1:alt}](${2:`@+`} "${3:title}")
```
####md-![:
```markdown
    ![${1:id}]: ${2:url}


```
####md-![:*
```markdown
    ![${1:id}]: ${2:`@*`}


```
####md-![:"
```markdown
    ![${1:id}]: ${2:url} "${3:title}"


```
####md-![:"*
```markdown
    ![${1:id}]: ${2:`@*`} "${3:title}"


```
####md-![:"c
```markdown
    ![${1:id}]: ${2:`@+`} "${3:title}"


```
####md-<
```markdown
    <http://${1:url}>
```
####md-<*
```markdown
    <`@*`>
```
####md-<c
```markdown
    <`@+`>
```
####md-**
```markdown
    **${1:bold}**
```
####md-__
```markdown
    __${1:bold}__
```
####md-===
```markdown
    `repeat('=', strlen(getline(line(".") - 1)) - strlen(getline('.')))`



    ${0}
```
####md--
```markdown
    -   ${0}
```
####md----
```markdown
    `repeat('-', strlen(getline(line(".") - 1)) - strlen(getline('.')))`



    ${0}


```
####md-blockquote
```markdown
    {% blockquote %}

    ${0:quote}

    {% endblockquote %}


```
####md-blockquote-author
```markdown
    {% blockquote ${1:author}, ${2:title} %}

    ${0:quote}

    {% endblockquote %}


```
####md-blockquote-link
```markdown
    {% blockquote ${1:author} ${2:URL} ${3:link_text} %}

    ${0:quote}

    {% endblockquote %}


```
####md-```
```markdown
    \`\`\`

    ${1:code}

    \`\`\`


```
####md-```l
```markdown
    \`\`\`${1:language}

    ${2:code}

    \`\`\`


```
####md-codeblock-short
```markdown
    {% codeblock %}

    ${0:code_snippet}

    {% endcodeblock %}


```
####md-codeblock-full
```markdown
    {% codeblock ${1:title} lang:${2:language} ${3:URL} ${4:link_text} %}

    ${0:code_snippet}

    {% endcodeblock %}


```
####md-gist-full
```markdown
    {% gist ${1:gist_id} ${0:filename} %}


```
####md-gist-short
```markdown
    {% gist ${0:gist_id} %}


```
####md-img
```markdown
    {% img ${1:class} ${2:URL} ${3:width} ${4:height} ${5:title_text} ${0:alt_text} %}


```
####md-youtube
```markdown
    {% youtube ${0:video_id} %}


```
