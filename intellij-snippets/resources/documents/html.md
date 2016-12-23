####h-nbs
```html
    &nbsp;
```
####h-left
```html
    &#x2190;
```
####h-right
```html
    &#x2192;
```
####h-up
```html
    &#x2191;
```
####h-down
```html
    &#x2193;
```
####h-return
```html
    &#x21A9;
```
####h-backtab
```html
    &#x21E4;
```
####h-tab
```html
    &#x21E5;
```
####h-shift
```html
    &#x21E7;
```
####h-ctrl
```html
    &#x2303;
```
####h-enter
```html
    &#x2305;
```
####h-cmd
```html
    &#x2318;
```
####h-option
```html
    &#x2325;
```
####h-delete
```html
    &#x2326;
```
####h-backspace
```html
    &#x232B;
```
####h-esc
```html
    &#x238B;
```
####h-//
```html
    <!-- ${1} -->${0}
```
####h-doctype
```html
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"

    "http://www.w3.org/TR/html4/strict.dtd">
```
####h-doctype
```html
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"

    "http://www.w3.org/TR/html4/loose.dtd">
```
####h-doctype
```html
    <!DOCTYPE HTML>
```
####h-doctype
```html
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"

    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
```
####h-doctype
```html
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"

    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
```
####h-doctype
```html
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"

    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
```
####h-doctype
```html
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"

    "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
```
####h-docts
```html
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"

    "http://www.w3.org/TR/html4/strict.dtd">
```
####h-doct
```html
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"

    "http://www.w3.org/TR/html4/loose.dtd">
```
####h-doct5
```html
    <!DOCTYPE HTML>
```
####h-docxf
```html
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Frameset//EN"

    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-frameset.dtd">
```
####h-docxs
```html
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"

    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
```
####h-docxt
```html
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"

    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
```
####h-docx
```html
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"

    "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
```
####h-attr
```html
    ${1:attribute}="${0:property}"
```
####h-attr+
```html
    ${1:attribute}="${2:property}" attr+
```
####h-.
```html
    class="${1}"
```
####h-#
```html
    id="${1}"
```
####h-alt
```html
    alt="${1}"
```
####h-charset
```html
    charset="${1:utf-8}"
```
####h-data
```html
    data-${1}="${2:$1}"
```
####h-for
```html
    for="${1}"
```
####h-height
```html
    height="${1}"
```
####h-href
```html
    href="${1:#}"
```
####h-lang
```html
    lang="${1:en}"
```
####h-media
```html
    media="${1}"
```
####h-name
```html
    name="${1}"
```
####h-rel
```html
    rel="${1}"
```
####h-scope
```html
    scope="${1:row}"
```
####h-src
```html
    src="${1}"
```
####h-title=
```html
    title="${1}"
```
####h-type
```html
    type="${1}"
```
####h-value
```html
    value="${1}"
```
####h-width
```html
    width="${1}"
```
####h-a
```html
    <a href="${1:#}">${0:$1}</a>
```
####h-a.
```html
    <a class="${1}" href="${2:#}">${0:$1}</a>
```
####h-a#
```html
    <a id="${1}" href="${2:#}">${0:$1}</a>
```
####h-a:ext
```html
    <a href="http://${1:example.com}">${0:$1}</a>
```
####h-a:mail
```html
    <a href="mailto:${1:joe@example.com}?subject=${2:feedback}">${0:email me}</a>
```
####h-abbr
```html
    <abbr title="${1}">${0}</abbr>
```
####h-address
```html
    <address>

        ${0}

    </address>
```
####h-area
```html
    <area shape="${1:rect}" coords="${2}" href="${3}" alt="${0}" />
```
####h-area+
```html
    <area shape="${1:rect}" coords="${2}" href="${3}" alt="${4}" />

    area+
```
####h-area:c
```html
    <area shape="circle" coords="${1}" href="${2}" alt="${0}" />
```
####h-area:d
```html
    <area shape="default" coords="${1}" href="${2}" alt="${0}" />
```
####h-area:p
```html
    <area shape="poly" coords="${1}" href="${2}" alt="${0}" />
```
####h-area:r
```html
    <area shape="rect" coords="${1}" href="${2}" alt="${0}" />
```
####h-article
```html
    <article>

        ${0}

    </article>
```
####h-article.
```html
    <article class="${1}">

        ${0}

    </article>
```
####h-article#
```html
    <article id="${1}">

        ${0}

    </article>
```
####h-aside
```html
    <aside>

        ${0}

    </aside>
```
####h-aside.
```html
    <aside class="${1}">

        ${0}

    </aside>
```
####h-aside#
```html
    <aside id="${1}">

        ${0}

    </aside>
```
####h-audio
```html
    <audio src="${1}>${0}</audio>
```
####h-b
```html
    <b>${0}</b>
```
####h-base
```html
    <base href="${1}" target="${0}" />
```
####h-bdi
```html
    <bdi>${0}</bdo>
```
####h-bdo
```html
    <bdo dir="${1}">${0}</bdo>
```
####h-bdo:l
```html
    <bdo dir="ltr">${0}</bdo>
```
####h-bdo:r
```html
    <bdo dir="rtl">${0}</bdo>
```
####h-blockquote
```html
    <blockquote>

        ${0}

    </blockquote>
```
####h-body
```html
    <body>

        ${0}

    </body>
```
####h-br
```html
    <br />
```
####h-button
```html
    <button type="${1:submit}">${0}</button>
```
####h-button.
```html
    <button class="${1:button}" type="${2:submit}">${0}</button>
```
####h-button#
```html
    <button id="${1}" type="${2:submit}">${0}</button>
```
####h-button:s
```html
    <button type="submit">${0}</button>
```
####h-button:r
```html
    <button type="reset">${0}</button>
```
####h-canvas
```html
    <canvas>

        ${0}

    </canvas>
```
####h-caption
```html
    <caption>${0}</caption>
```
####h-cite
```html
    <cite>${0}</cite>
```
####h-code
```html
    <code>${0}</code>
```
####h-col
```html
    <col />
```
####h-col+
```html
    <col />

    col+
```
####h-colgroup
```html
    <colgroup>

        ${0}

    </colgroup>
```
####h-colgroup+
```html
    <colgroup>

        <col />

        col+${0}

    </colgroup>
```
####h-command
```html
    <command type="command" label="${1}" icon="${0}">
```
####h-command:c
```html
    <command type="checkbox" label="${1}" icon="${0}">
```
####h-command:r
```html
    <command type="radio" radiogroup="${1}" label="${2}" icon="${0}">
```
####h-datagrid
```html
    <datagrid>

        ${0}

    </datagrid>
```
####h-datalist
```html
    <datalist>

        ${0}

    </datalist>
```
####h-datatemplate
```html
    <datatemplate>

        ${0}

    </datatemplate>
```
####h-dd
```html
    <dd>${0}</dd>
```
####h-dd.
```html
    <dd class="${1}">${0}</dd>
```
####h-dd#
```html
    <dd id="${1}">${0}</dd>
```
####h-del
```html
    <del>${0}</del>
```
####h-details
```html
    <details>${0}</details>
```
####h-dfn
```html
    <dfn>${0}</dfn>
```
####h-dialog
```html
    <dialog>

        ${0}

    </dialog>
```
####h-div
```html
    <div>

        ${0}

    </div>
```
####h-div.
```html
    <div class="${1}">

        ${0}

    </div>
```
####h-div#
```html
    <div id="${1}">

        ${0}

    </div>
```
####h-dl
```html
    <dl>

        ${0}

    </dl>
```
####h-dl.
```html
    <dl class="${1}">

        ${0}

    </dl>
```
####h-dl#
```html
    <dl id="${1}">

        ${0}

    </dl>
```
####h-dl+
```html
    <dl>

        <dt>${1}</dt>

        <dd>${2}</dd>

        dt+${0}

    </dl>
```
####h-dt
```html
    <dt>${0}</dt>
```
####h-dt.
```html
    <dt class="${1}">${0}</dt>
```
####h-dt#
```html
    <dt id="${1}">${0}</dt>
```
####h-dt+
```html
    <dt>${1}</dt>

    <dd>${2}</dd>

    dt+${0}
```
####h-em
```html
    <em>${0}</em>
```
####h-embed
```html
    <embed src="${1}" type="${0}" />
```
####h-fieldset
```html
    <fieldset>

        ${0}

    </fieldset>
```
####h-fieldset.
```html
    <fieldset class="${1}">

        ${0}

    </fieldset>
```
####h-fieldset#
```html
    <fieldset id="${1}">

        ${0}

    </fieldset>
```
####h-fieldset+
```html
    <fieldset>

        <legend><span>${1}</span></legend>

        ${2}

    </fieldset>

    fieldset+${0}
```
####h-figcaption
```html
    <figcaption>${0}</figcaption>
```
####h-figure
```html
    <figure>${0}</figure>
```
####h-figure#
```html
    <figure id="${1}">

        ${0}

    </figure>
```
####h-figure.
```html
    <figure class="${1}">

        ${0}

    </figure>
```
####h-footer
```html
    <footer>

        ${0}

    </footer>
```
####h-footer.
```html
    <footer class="${1}">

        ${0}

    </footer>
```
####h-footer#
```html
    <footer id="${1}">

        ${0}

    </footer>
```
####h-form
```html
    <form action="${1}" method="${2:post}">

        ${0}

    </form>
```
####h-form.
```html
    <form class="${1}" action="${2}" method="${3:post}">

        ${0}

    </form>
```
####h-form#
```html
    <form id="${1}" action="${2}" method="${3:post}">

        ${0}

    </form>
```
####h-h1
```html
    <h1>${0}</h1>
```
####h-h1.
```html
    <h1 class="${1}">${0}</h1>
```
####h-h1#
```html
    <h1 id="${1}">${0}</h1>
```
####h-h2
```html
    <h2>${0}</h2>
```
####h-h2.
```html
    <h2 class="${1}">${0}</h2>
```
####h-h2#
```html
    <h2 id="${1}">${0}</h2>
```
####h-h3
```html
    <h3>${0}</h3>
```
####h-h3.
```html
    <h3 class="${1}">${0}</h3>
```
####h-h3#
```html
    <h3 id="${1}">${0}</h3>
```
####h-h4
```html
    <h4>${0}</h4>
```
####h-h4.
```html
    <h4 class="${1}">${0}</h4>
```
####h-h4#
```html
    <h4 id="${1}">${0}</h4>
```
####h-h5
```html
    <h5>${0}</h5>
```
####h-h5.
```html
    <h5 class="${1}">${0}</h5>
```
####h-h5#
```html
    <h5 id="${1}">${0}</h5>
```
####h-h6
```html
    <h6>${0}</h6>
```
####h-h6.
```html
    <h6 class="${1}">${0}</h6>
```
####h-h6#
```html
    <h6 id="${1}">${0}</h6>
```
####h-header
```html
    <header>

        ${0}

    </header>
```
####h-header.
```html
    <header class="${1}">

        ${0}

    </header>
```
####h-header#
```html
    <header id="${1}">

        ${0}

    </header>
```
####h-hgroup
```html
    <hgroup>

        ${0}

    </hgroup>
```
####h-hgroup.
```html
    <hgroup class="${1}>

        ${0}

    </hgroup>
```
####h-hr
```html
    <hr />
```
####h-html
```html
    <html>

    ${0}

    </html>
```
####h-xhtml
```html
    <html xmlns="http://www.w3.org/1999/xhtml">

    ${0}

    </html>
```
####h-i
```html
    <i>${0}</i>
```
####h-iframe
```html
    <iframe src="${1}" frameborder="0"></iframe>
```
####h-iframe.
```html
    <iframe class="${1}" src="${2}" frameborder="0"></iframe>
```
####h-iframe#
```html
    <iframe id="${1}" src="${2}" frameborder="0"></iframe>
```
####h-img
```html
    <img src="${1}" alt="${2}" />
```
####h-img.
```html
    <img class="${1}" src="${2}" alt="${3}" />
```
####h-img#
```html
    <img id="${1}" src="${2}" alt="${3}" />
```
####h-input
```html
    <input type="${1:text/submit/hidden/button/image}" name="${2}" id="${3:$2}" value="${4}" />
```
####h-input.
```html
    <input class="${1}" type="${2:text/submit/hidden/button/image}" name="${3}" id="${4:$3}" value="${5}" />
```
####h-input:text
```html
    <input type="text" name="${1}" id="${2:$1}" value="${3}" />
```
####h-input:submit
```html
    <input type="submit" name="${1}" id="${2:$1}" value="${3}" />
```
####h-input:hidden
```html
    <input type="hidden" name="${1}" id="${2:$1}" value="${3}" />
```
####h-input:button
```html
    <input type="button" name="${1}" id="${2:$1}" value="${3}" />
```
####h-input:image
```html
    <input type="image" name="${1}" id="${2:$1}" src="${3}" alt="${4}" />
```
####h-input:checkbox
```html
    <input type="checkbox" name="${1}" id="${2:$1}" />
```
####h-input:radio
```html
    <input type="radio" name="${1}" id="${2:$1}" />
```
####h-input:color
```html
    <input type="color" name="${1}" id="${2:$1}" value="${3}" />
```
####h-input:date
```html
    <input type="date" name="${1}" id="${2:$1}" value="${3}" />
```
####h-input:datetime
```html
    <input type="datetime" name="${1}" id="${2:$1}" value="${3}" />
```
####h-input:datetime-local
```html
    <input type="datetime-local" name="${1}" id="${2:$1}" value="${3}" />
```
####h-input:email
```html
    <input type="email" name="${1}" id="${2:$1}" value="${3}" />
```
####h-input:file
```html
    <input type="file" name="${1}" id="${2:$1}" value="${3}" />
```
####h-input:month
```html
    <input type="month" name="${1}" id="${2:$1}" value="${3}" />
```
####h-input:number
```html
    <input type="number" name="${1}" id="${2:$1}" value="${3}" />
```
####h-input:password
```html
    <input type="password" name="${1}" id="${2:$1}" value="${3}" />
```
####h-input:range
```html
    <input type="range" name="${1}" id="${2:$1}" value="${3}" />
```
####h-input:reset
```html
    <input type="reset" name="${1}" id="${2:$1}" value="${3}" />
```
####h-input:search
```html
    <input type="search" name="${1}" id="${2:$1}" value="${3}" />
```
####h-input:time
```html
    <input type="time" name="${1}" id="${2:$1}" value="${3}" />
```
####h-input:url
```html
    <input type="url" name="${1}" id="${2:$1}" value="${3}" />
```
####h-input:week
```html
    <input type="week" name="${1}" id="${2:$1}" value="${3}" />
```
####h-ins
```html
    <ins>${0}</ins>
```
####h-kbd
```html
    <kbd>${0}</kbd>
```
####h-label
```html
    <label for="${0:$1}">${1}</label>
```
####h-label:i
```html
    <label for="${2:$1}">${1}</label>

    <input type="${3:text/submit/hidden/button}" name="${4:$2}" id="${5:$2}" value="${6}" />
```
####h-label:s
```html
    <label for="${2:$1}">${1}</label>

    <select name="${3:$2}" id="${4:$2}">

        <option value="${5}">${0:$5}</option>

    </select>
```
####h-legend
```html
    <legend>${0}</legend>
```
####h-legend+
```html
    <legend><span>${0}</span></legend>
```
####h-li
```html
    <li>${0}</li>
```
####h-li.
```html
    <li class="${1}">${0}</li>
```
####h-li+
```html
    <li>${1}</li>

    li+
```
####h-lia
```html
    <li><a href="${0:#}">${1}</a></li>
```
####h-lia+
```html
    <li><a href="${2:#}">${1}</a></li>

    lia+
```
####h-link
```html
    <link rel="${1}" href="${2}" title="${3}" type="${4}" />
```
####h-link:atom
```html
    <link rel="alternate" href="${1:atom.xml}" title="Atom" type="application/atom+xml" />
```
####h-link:s
```html
    <link rel="stylesheet" href="${1:style.css}" />
```
####h-link:css
```html
    <link rel="stylesheet" href="${1:style.css}" type="text/css" media="${2:all}" />
```
####h-link:favicon
```html
    <link rel="shortcut icon" href="${1:favicon.ico}" type="image/x-icon" />
```
####h-link:rss
```html
    <link rel="alternate" href="${1:rss.xml}" title="RSS" type="application/atom+xml" />
```
####h-link:touch
```html
    <link rel="apple-touch-icon" href="${1:favicon.png}" />
```
####h-main
```html
    <main role="main">

        ${0}

    </main>
```
####h-map
```html
    <map name="${1}">

        ${0}

    </map>
```
####h-map.
```html
    <map class="${1}" name="${2}">

        ${0}

    </map>
```
####h-map#
```html
    <map name="${1}" id="${2:$1}>

        ${0}

    </map>
```
####h-map+
```html
    <map name="${1}">

        <area shape="${2}" coords="${3}" href="${4}" alt="${5}" />${6}

    </map>
```
####h-mark
```html
    <mark>${0}</mark>
```
####h-menu
```html
    <menu>

        ${0}

    </menu>
```
####h-menu:c
```html
    <menu type="context">

        ${0}

    </menu>
```
####h-menu:t
```html
    <menu type="toolbar">

        ${0}

    </menu>
```
####h-meta
```html
    <meta http-equiv="${1}" content="${2}" />
```
####h-meta:s
```html
    <meta ${0} />
```
####h-meta:d
```html
    <meta name="description" content="${0}" />
```
####h-meta:compat
```html
    <meta http-equiv="X-UA-Compatible" content="IE=${1:7,8,edge}" />
```
####h-meta:refresh
```html
    <meta http-equiv="refresh" content="text/html;charset=UTF-8" />
```
####h-meta:utf
```html
    <meta http-equiv="content-type" content="text/html;charset=UTF-8" />
```
####h-meter
```html
    <meter>${0}</meter>
```
####h-nav
```html
    <nav>

        ${0}

    </nav>
```
####h-nav.
```html
    <nav class="${1}">

        ${0}

    </nav>
```
####h-nav#
```html
    <nav id="${1}">

        ${0}

    </nav>
```
####h-noscript
```html
    <noscript>

        ${0}

    </noscript>
```
####h-object
```html
    <object data="${1}" type="${2}">

        ${3}

    </object>
```
####h-movie
```html
    <object width="$2" height="$3" classid="clsid:02BF25D5-8C17-4B23-BC80-D3488ABDDC6B"

    codebase="http://www.apple.com/qtactivex/qtplugin.cab">

        <param name="src" value="$1" />

        <param name="controller" value="$4" />

        <param name="autoplay" value="$5" />

        <embed src="${1:movie.mov}"

            width="${2:320}" height="${3:240}"

            controller="${4:true}" autoplay="${5:true}"

            scale="tofit" cache="true"

            pluginspage="http://www.apple.com/quicktime/download/" />

    </object>
```
####h-ol
```html
    <ol>

        ${0}

    </ol>
```
####h-ol.
```html
    <ol class="${1}">

        ${0}

    </ol>
```
####h-ol#
```html
    <ol id="${1}">

        ${0}

    </ol>
```
####h-ol+
```html
    <ol>

        <li>${1}</li>

        li+${0}

    </ol>
```
####h-opt
```html
    <option value="${1}">${0:$1}</option>
```
####h-opt+
```html
    <option value="${1}">${2:$1}</option>

    opt+${0}
```
####h-optt
```html
    <option>${0}</option>
```
####h-optgroup
```html
    <optgroup>

        <option value="${1}">${2:$1}</option>

        opt+${0}

    </optgroup>
```
####h-output
```html
    <output>${0}</output>
```
####h-p
```html
    <p>${0}</p>
```
####h-p.
```html
    <p class="${1}">${0}</p>
```
####h-p#
```html
    <p id="${1}">${0}</p>
```
####h-param
```html
    <param name="${1}" value="${2}" />
```
####h-pre
```html
    <pre>

        ${0}

    </pre>
```
####h-progress
```html
    <progress>${0}</progress>
```
####h-q
```html
    <q>${0}</q>
```
####h-rp
```html
    <rp>${0}</rp>
```
####h-rt
```html
    <rt>${0}</rt>
```
####h-ruby
```html
    <ruby>

        <rp><rt>${0}</rt></rp>

    </ruby>
```
####h-s
```html
    <s>${0}</s>
```
####h-samp
```html
    <samp>

        ${0}

    </samp>
```
####h-script
```html
    <script type="text/javascript" charset="utf-8">

        ${0}

    </script>
```
####h-scripts
```html
    <script src="${0}.js"></script>
```
####h-scriptt
```html
    <script type="${1}" id="${2}">

        ${0}

    </script>
```
####h-scriptsrc
```html
    <script src="${0}.js" type="text/javascript" charset="utf-8"></script>
```
####h-section
```html
    <section>

        ${0}

    </section>
```
####h-section.
```html
    <section class="${1}">

        ${0}

    </section>
```
####h-section#
```html
    <section id="${1}">

        ${0}

    </section>
```
####h-select
```html
    <select name="${1}" id="${2:$1}">

        ${0}

    </select>
```
####h-select.
```html
    <select name="${1}" id="${2:$1}" class="${3}>

        ${0}

    </select>
```
####h-select+
```html
    <select name="${1}" id="${2:$1}">

        <option value="${3}">${4:$3}</option>

        opt+${0}

    </select>
```
####h-small
```html
    <small>${0}</small>
```
####h-source
```html
    <source src="${1}" type="${2}" media="${0}" />
```
####h-span
```html
    <span>${0}</span>
```
####h-span.
```html
    <span class="${1}">${0}</span>
```
####h-span#
```html
    <span id="${1}">${0}</span>
```
####h-strong
```html
    <strong>${0}</strong>
```
####h-style
```html
    <style type="text/css" media="${1:all}">

        ${0}

    </style>
```
####h-sub
```html
    <sub>${0}</sub>
```
####h-summary
```html
    <summary>

        ${0}

    </summary>
```
####h-sup
```html
    <sup>${0}</sup>
```
####h-table
```html
    <table>

        ${0}

    </table>
```
####h-table.
```html
    <table class="${1}">

        ${0}

    </table>
```
####h-table#
```html
    <table id="${1}">

        ${0}

    </table>
```
####h-tbody
```html
    <tbody>

        ${0}

    </tbody>
```
####h-td
```html
    <td>${0}</td>
```
####h-td.
```html
    <td class="${1}">${0}</td>
```
####h-td#
```html
    <td id="${1}">${0}</td>
```
####h-td+
```html
    <td>${1}</td>

    td+${0}
```
####h-textarea
```html
    <textarea name="${1}" id="${2:$1}" rows="${3:8}" cols="${4:40}">${5}</textarea>
```
####h-tfoot
```html
    <tfoot>

        ${0}

    </tfoot>
```
####h-th
```html
    <th>${0}</th>
```
####h-th.
```html
    <th class="${1}">${0}</th>
```
####h-th#
```html
    <th id="${1}">${0}</th>
```
####h-th+
```html
    <th>${1}</th>

    th+${0}
```
####h-thead
```html
    <thead>

        ${0}

    </thead>
```
####h-time
```html
    <time datetime="${1}" pubdate="${2:$1}">${0:$1}</time>
```
####h-tr
```html
    <tr>

        ${0}

    </tr>
```
####h-tr+
```html
    <tr>

        <td>${1}</td>

        td+${0}

    </tr>
```
####h-track
```html
    <track src="${1}" srclang="${2}" label="${3}" default="${4:default} />${5}
```
####h-ul
```html
    <ul>

        ${0}

    </ul>
```
####h-ul.
```html
    <ul class="${1}">

        ${0}

    </ul>
```
####h-ul#
```html
    <ul id="${1}">

        ${0}

    </ul>
```
####h-ul+
```html
    <ul>

        <li>${1}</li>

        li+${0}

    </ul>
```
####h-var
```html
    <var>${0}</var>
```
####h-video
```html
    <video src="${1} height="${2}" width="${3}" preload="${5:none}" autoplay="${6:autoplay}>${7}</video>
```
####h-wbr
```html
    <wbr />
```
