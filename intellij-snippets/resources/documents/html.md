####nbs
```html
    &nbsp;
```
####left
```html
    &#x2190;
```
####right
```html
    &#x2192;
```
####up
```html
    &#x2191;
```
####down
```html
    &#x2193;
```
####return
```html
    &#x21A9;
```
####backtab
```html
    &#x21E4;
```
####tab
```html
    &#x21E5;
```
####shift
```html
    &#x21E7;
```
####ctrl
```html
    &#x2303;
```
####enter
```html
    &#x2305;
```
####cmd
```html
    &#x2318;
```
####option
```html
    &#x2325;
```
####delete
```html
    &#x2326;
```
####backspace
```html
    &#x232B;
```
####esc
```html
    &#x238B;
```
####//
```html
    <!-- ${1} -->${0}
```
####doctype
```html
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"

    "http://www.w3.org/TR/html4/strict.dtd">
```
####doctype
```html
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"

    "http://www.w3.org/TR/html4/loose.dtd">
```
####doctype
```html
    <!DOCTYPE HTML>
```
####doctype
```html
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"

    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
```
####doctype
```html
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"

    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
```
####doctype
```html
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"

    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
```
####doctype
```html
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"

    "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
```
####docts
```html
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"

    "http://www.w3.org/TR/html4/strict.dtd">
```
####doct
```html
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"

    "http://www.w3.org/TR/html4/loose.dtd">
```
####doct5
```html
    <!DOCTYPE HTML>
```
####docxf
```html
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Frameset//EN"

    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-frameset.dtd">
```
####docxs
```html
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"

    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
```
####docxt
```html
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"

    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
```
####docx
```html
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"

    "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
```
####attr
```html
    ${1:attribute}="${0:property}"
```
####attr+
```html
    ${1:attribute}="${2:property}" attr+
```
####.
```html
    class="${1}"
```
#####
```html
    id="${1}"
```
####alt
```html
    alt="${1}"
```
####charset
```html
    charset="${1:utf-8}"
```
####data
```html
    data-${1}="${2:$1}"
```
####for
```html
    for="${1}"
```
####height
```html
    height="${1}"
```
####href
```html
    href="${1:#}"
```
####lang
```html
    lang="${1:en}"
```
####media
```html
    media="${1}"
```
####name
```html
    name="${1}"
```
####rel
```html
    rel="${1}"
```
####scope
```html
    scope="${1:row}"
```
####src
```html
    src="${1}"
```
####title=
```html
    title="${1}"
```
####type
```html
    type="${1}"
```
####value
```html
    value="${1}"
```
####width
```html
    width="${1}"
```
####a
```html
    <a href="${1:#}">${0:$1}</a>
```
####a.
```html
    <a class="${1}" href="${2:#}">${0:$1}</a>
```
####a#
```html
    <a id="${1}" href="${2:#}">${0:$1}</a>
```
####a:ext
```html
    <a href="http://${1:example.com}">${0:$1}</a>
```
####a:mail
```html
    <a href="mailto:${1:joe@example.com}?subject=${2:feedback}">${0:email me}</a>
```
####ac
```html
    <a href="`@+`">${0:`@+`}</a>
```
####abbr
```html
    <abbr title="${1}">${0}</abbr>
```
####address
```html
    <address>

        ${0}

    </address>
```
####area
```html
    <area shape="${1:rect}" coords="${2}" href="${3}" alt="${0}" />
```
####area+
```html
    <area shape="${1:rect}" coords="${2}" href="${3}" alt="${4}" />

    area+
```
####area:c
```html
    <area shape="circle" coords="${1}" href="${2}" alt="${0}" />
```
####area:d
```html
    <area shape="default" coords="${1}" href="${2}" alt="${0}" />
```
####area:p
```html
    <area shape="poly" coords="${1}" href="${2}" alt="${0}" />
```
####area:r
```html
    <area shape="rect" coords="${1}" href="${2}" alt="${0}" />
```
####article
```html
    <article>

        ${0}

    </article>
```
####article.
```html
    <article class="${1}">

        ${0}

    </article>
```
####article#
```html
    <article id="${1}">

        ${0}

    </article>
```
####aside
```html
    <aside>

        ${0}

    </aside>
```
####aside.
```html
    <aside class="${1}">

        ${0}

    </aside>
```
####aside#
```html
    <aside id="${1}">

        ${0}

    </aside>
```
####audio
```html
    <audio src="${1}>${0}</audio>
```
####b
```html
    <b>${0}</b>
```
####base
```html
    <base href="${1}" target="${0}" />
```
####bdi
```html
    <bdi>${0}</bdo>
```
####bdo
```html
    <bdo dir="${1}">${0}</bdo>
```
####bdo:l
```html
    <bdo dir="ltr">${0}</bdo>
```
####bdo:r
```html
    <bdo dir="rtl">${0}</bdo>
```
####blockquote
```html
    <blockquote>

        ${0}

    </blockquote>
```
####body
```html
    <body>

        ${0}

    </body>
```
####br
```html
    <br />
```
####button
```html
    <button type="${1:submit}">${0}</button>
```
####button.
```html
    <button class="${1:button}" type="${2:submit}">${0}</button>
```
####button#
```html
    <button id="${1}" type="${2:submit}">${0}</button>
```
####button:s
```html
    <button type="submit">${0}</button>
```
####button:r
```html
    <button type="reset">${0}</button>
```
####canvas
```html
    <canvas>

        ${0}

    </canvas>
```
####caption
```html
    <caption>${0}</caption>
```
####cite
```html
    <cite>${0}</cite>
```
####code
```html
    <code>${0}</code>
```
####col
```html
    <col />
```
####col+
```html
    <col />

    col+
```
####colgroup
```html
    <colgroup>

        ${0}

    </colgroup>
```
####colgroup+
```html
    <colgroup>

        <col />

        col+${0}

    </colgroup>
```
####command
```html
    <command type="command" label="${1}" icon="${0}">
```
####command:c
```html
    <command type="checkbox" label="${1}" icon="${0}">
```
####command:r
```html
    <command type="radio" radiogroup="${1}" label="${2}" icon="${0}">
```
####datagrid
```html
    <datagrid>

        ${0}

    </datagrid>
```
####datalist
```html
    <datalist>

        ${0}

    </datalist>
```
####datatemplate
```html
    <datatemplate>

        ${0}

    </datatemplate>
```
####dd
```html
    <dd>${0}</dd>
```
####dd.
```html
    <dd class="${1}">${0}</dd>
```
####dd#
```html
    <dd id="${1}">${0}</dd>
```
####del
```html
    <del>${0}</del>
```
####details
```html
    <details>${0}</details>
```
####dfn
```html
    <dfn>${0}</dfn>
```
####dialog
```html
    <dialog>

        ${0}

    </dialog>
```
####div
```html
    <div>

        ${0}

    </div>
```
####div.
```html
    <div class="${1}">

        ${0}

    </div>
```
####div#
```html
    <div id="${1}">

        ${0}

    </div>
```
####dl
```html
    <dl>

        ${0}

    </dl>
```
####dl.
```html
    <dl class="${1}">

        ${0}

    </dl>
```
####dl#
```html
    <dl id="${1}">

        ${0}

    </dl>
```
####dl+
```html
    <dl>

        <dt>${1}</dt>

        <dd>${2}</dd>

        dt+${0}

    </dl>
```
####dt
```html
    <dt>${0}</dt>
```
####dt.
```html
    <dt class="${1}">${0}</dt>
```
####dt#
```html
    <dt id="${1}">${0}</dt>
```
####dt+
```html
    <dt>${1}</dt>

    <dd>${2}</dd>

    dt+${0}
```
####em
```html
    <em>${0}</em>
```
####embed
```html
    <embed src="${1}" type="${0}" />
```
####fieldset
```html
    <fieldset>

        ${0}

    </fieldset>
```
####fieldset.
```html
    <fieldset class="${1}">

        ${0}

    </fieldset>
```
####fieldset#
```html
    <fieldset id="${1}">

        ${0}

    </fieldset>
```
####fieldset+
```html
    <fieldset>

        <legend><span>${1}</span></legend>

        ${2}

    </fieldset>

    fieldset+${0}
```
####figcaption
```html
    <figcaption>${0}</figcaption>
```
####figure
```html
    <figure>${0}</figure>
```
####figure#
```html
    <figure id="${1}">

        ${0}

    </figure>
```
####figure.
```html
    <figure class="${1}">

        ${0}

    </figure>
```
####footer
```html
    <footer>

        ${0}

    </footer>
```
####footer.
```html
    <footer class="${1}">

        ${0}

    </footer>
```
####footer#
```html
    <footer id="${1}">

        ${0}

    </footer>
```
####form
```html
    <form action="${1}" method="${2:post}">

        ${0}

    </form>
```
####form.
```html
    <form class="${1}" action="${2}" method="${3:post}">

        ${0}

    </form>
```
####form#
```html
    <form id="${1}" action="${2}" method="${3:post}">

        ${0}

    </form>
```
####h1
```html
    <h1>${0}</h1>
```
####h1.
```html
    <h1 class="${1}">${0}</h1>
```
####h1#
```html
    <h1 id="${1}">${0}</h1>
```
####h2
```html
    <h2>${0}</h2>
```
####h2.
```html
    <h2 class="${1}">${0}</h2>
```
####h2#
```html
    <h2 id="${1}">${0}</h2>
```
####h3
```html
    <h3>${0}</h3>
```
####h3.
```html
    <h3 class="${1}">${0}</h3>
```
####h3#
```html
    <h3 id="${1}">${0}</h3>
```
####h4
```html
    <h4>${0}</h4>
```
####h4.
```html
    <h4 class="${1}">${0}</h4>
```
####h4#
```html
    <h4 id="${1}">${0}</h4>
```
####h5
```html
    <h5>${0}</h5>
```
####h5.
```html
    <h5 class="${1}">${0}</h5>
```
####h5#
```html
    <h5 id="${1}">${0}</h5>
```
####h6
```html
    <h6>${0}</h6>
```
####h6.
```html
    <h6 class="${1}">${0}</h6>
```
####h6#
```html
    <h6 id="${1}">${0}</h6>
```
####head
```html
    <head>

        <meta http-equiv="content-type" content="text/html; charset=utf-8" />



        <title>${1:`substitute(vim_snippets#Filename('', 'Page Title'), '^.', '\u&', '')`}</title>

        ${0}

    </head>
```
####header
```html
    <header>

        ${0}

    </header>
```
####header.
```html
    <header class="${1}">

        ${0}

    </header>
```
####header#
```html
    <header id="${1}">

        ${0}

    </header>
```
####hgroup
```html
    <hgroup>

        ${0}

    </hgroup>
```
####hgroup.
```html
    <hgroup class="${1}>

        ${0}

    </hgroup>
```
####hr
```html
    <hr />
```
####html
```html
    <html>

    ${0}

    </html>
```
####xhtml
```html
    <html xmlns="http://www.w3.org/1999/xhtml">

    ${0}

    </html>
```
####html5
```html
    <!DOCTYPE html>

    <html>

        <head>

            <meta charset="utf-8" />

            <meta name="viewport" content="width=device-width" />

            <title>${1:`substitute(vim_snippets#Filename('', 'Page Title'), '^.', '\u&', '')`}</title>

            ${2:link}

        </head>

        <body>

            ${0:body}

        </body>

    </html>
```
####html5l
```html
    <!DOCTYPE html>

    <html lang="${1:es}">

        <head>

            <meta charset="utf-8" />

            <meta name="viewport" content="width=device-width" />

            <title>${2:`substitute(vim_snippets#Filename('', 'Page Title'), '^.', '\u&', '')`}</title>

            ${3:link}

        </head>

        <body>

            ${0:body}

        </body>

    </html>
```
####i
```html
    <i>${0}</i>
```
####iframe
```html
    <iframe src="${1}" frameborder="0"></iframe>
```
####iframe.
```html
    <iframe class="${1}" src="${2}" frameborder="0"></iframe>
```
####iframe#
```html
    <iframe id="${1}" src="${2}" frameborder="0"></iframe>
```
####img
```html
    <img src="${1}" alt="${2}" />
```
####img.
```html
    <img class="${1}" src="${2}" alt="${3}" />
```
####img#
```html
    <img id="${1}" src="${2}" alt="${3}" />
```
####input
```html
    <input type="${1:text/submit/hidden/button/image}" name="${2}" id="${3:$2}" value="${4}" />
```
####input.
```html
    <input class="${1}" type="${2:text/submit/hidden/button/image}" name="${3}" id="${4:$3}" value="${5}" />
```
####input:text
```html
    <input type="text" name="${1}" id="${2:$1}" value="${3}" />
```
####input:submit
```html
    <input type="submit" name="${1}" id="${2:$1}" value="${3}" />
```
####input:hidden
```html
    <input type="hidden" name="${1}" id="${2:$1}" value="${3}" />
```
####input:button
```html
    <input type="button" name="${1}" id="${2:$1}" value="${3}" />
```
####input:image
```html
    <input type="image" name="${1}" id="${2:$1}" src="${3}" alt="${4}" />
```
####input:checkbox
```html
    <input type="checkbox" name="${1}" id="${2:$1}" />
```
####input:radio
```html
    <input type="radio" name="${1}" id="${2:$1}" />
```
####input:color
```html
    <input type="color" name="${1}" id="${2:$1}" value="${3}" />
```
####input:date
```html
    <input type="date" name="${1}" id="${2:$1}" value="${3}" />
```
####input:datetime
```html
    <input type="datetime" name="${1}" id="${2:$1}" value="${3}" />
```
####input:datetime-local
```html
    <input type="datetime-local" name="${1}" id="${2:$1}" value="${3}" />
```
####input:email
```html
    <input type="email" name="${1}" id="${2:$1}" value="${3}" />
```
####input:file
```html
    <input type="file" name="${1}" id="${2:$1}" value="${3}" />
```
####input:month
```html
    <input type="month" name="${1}" id="${2:$1}" value="${3}" />
```
####input:number
```html
    <input type="number" name="${1}" id="${2:$1}" value="${3}" />
```
####input:password
```html
    <input type="password" name="${1}" id="${2:$1}" value="${3}" />
```
####input:range
```html
    <input type="range" name="${1}" id="${2:$1}" value="${3}" />
```
####input:reset
```html
    <input type="reset" name="${1}" id="${2:$1}" value="${3}" />
```
####input:search
```html
    <input type="search" name="${1}" id="${2:$1}" value="${3}" />
```
####input:time
```html
    <input type="time" name="${1}" id="${2:$1}" value="${3}" />
```
####input:url
```html
    <input type="url" name="${1}" id="${2:$1}" value="${3}" />
```
####input:week
```html
    <input type="week" name="${1}" id="${2:$1}" value="${3}" />
```
####ins
```html
    <ins>${0}</ins>
```
####kbd
```html
    <kbd>${0}</kbd>
```
####label
```html
    <label for="${0:$1}">${1}</label>
```
####label:i
```html
    <label for="${2:$1}">${1}</label>

    <input type="${3:text/submit/hidden/button}" name="${4:$2}" id="${5:$2}" value="${6}" />
```
####label:s
```html
    <label for="${2:$1}">${1}</label>

    <select name="${3:$2}" id="${4:$2}">

        <option value="${5}">${0:$5}</option>

    </select>
```
####legend
```html
    <legend>${0}</legend>
```
####legend+
```html
    <legend><span>${0}</span></legend>
```
####li
```html
    <li>${0}</li>
```
####li.
```html
    <li class="${1}">${0}</li>
```
####li+
```html
    <li>${1}</li>

    li+
```
####lia
```html
    <li><a href="${0:#}">${1}</a></li>
```
####lia+
```html
    <li><a href="${2:#}">${1}</a></li>

    lia+
```
####link
```html
    <link rel="${1}" href="${2}" title="${3}" type="${4}" />
```
####link:atom
```html
    <link rel="alternate" href="${1:atom.xml}" title="Atom" type="application/atom+xml" />
```
####link:s
```html
    <link rel="stylesheet" href="${1:style.css}" />
```
####link:css
```html
    <link rel="stylesheet" href="${1:style.css}" type="text/css" media="${2:all}" />
```
####link:favicon
```html
    <link rel="shortcut icon" href="${1:favicon.ico}" type="image/x-icon" />
```
####link:rss
```html
    <link rel="alternate" href="${1:rss.xml}" title="RSS" type="application/atom+xml" />
```
####link:touch
```html
    <link rel="apple-touch-icon" href="${1:favicon.png}" />
```
####main
```html
    <main role="main">

        ${0}

    </main>
```
####map
```html
    <map name="${1}">

        ${0}

    </map>
```
####map.
```html
    <map class="${1}" name="${2}">

        ${0}

    </map>
```
####map#
```html
    <map name="${1}" id="${2:$1}>

        ${0}

    </map>
```
####map+
```html
    <map name="${1}">

        <area shape="${2}" coords="${3}" href="${4}" alt="${5}" />${6}

    </map>
```
####mark
```html
    <mark>${0}</mark>
```
####menu
```html
    <menu>

        ${0}

    </menu>
```
####menu:c
```html
    <menu type="context">

        ${0}

    </menu>
```
####menu:t
```html
    <menu type="toolbar">

        ${0}

    </menu>
```
####meta
```html
    <meta http-equiv="${1}" content="${2}" />
```
####meta:s
```html
    <meta ${0} />
```
####meta:d
```html
    <meta name="description" content="${0}" />
```
####meta:compat
```html
    <meta http-equiv="X-UA-Compatible" content="IE=${1:7,8,edge}" />
```
####meta:refresh
```html
    <meta http-equiv="refresh" content="text/html;charset=UTF-8" />
```
####meta:utf
```html
    <meta http-equiv="content-type" content="text/html;charset=UTF-8" />
```
####meter
```html
    <meter>${0}</meter>
```
####nav
```html
    <nav>

        ${0}

    </nav>
```
####nav.
```html
    <nav class="${1}">

        ${0}

    </nav>
```
####nav#
```html
    <nav id="${1}">

        ${0}

    </nav>
```
####noscript
```html
    <noscript>

        ${0}

    </noscript>
```
####object
```html
    <object data="${1}" type="${2}">

        ${3}

    </object>
```
####movie
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
####ol
```html
    <ol>

        ${0}

    </ol>
```
####ol.
```html
    <ol class="${1}">

        ${0}

    </ol>
```
####ol#
```html
    <ol id="${1}">

        ${0}

    </ol>
```
####ol+
```html
    <ol>

        <li>${1}</li>

        li+${0}

    </ol>
```
####opt
```html
    <option value="${1}">${0:$1}</option>
```
####opt+
```html
    <option value="${1}">${2:$1}</option>

    opt+${0}
```
####optt
```html
    <option>${0}</option>
```
####optgroup
```html
    <optgroup>

        <option value="${1}">${2:$1}</option>

        opt+${0}

    </optgroup>
```
####output
```html
    <output>${0}</output>
```
####p
```html
    <p>${0}</p>
```
####p.
```html
    <p class="${1}">${0}</p>
```
####p#
```html
    <p id="${1}">${0}</p>
```
####param
```html
    <param name="${1}" value="${2}" />
```
####pre
```html
    <pre>

        ${0}

    </pre>
```
####progress
```html
    <progress>${0}</progress>
```
####q
```html
    <q>${0}</q>
```
####rp
```html
    <rp>${0}</rp>
```
####rt
```html
    <rt>${0}</rt>
```
####ruby
```html
    <ruby>

        <rp><rt>${0}</rt></rp>

    </ruby>
```
####s
```html
    <s>${0}</s>
```
####samp
```html
    <samp>

        ${0}

    </samp>
```
####script
```html
    <script type="text/javascript" charset="utf-8">

        ${0}

    </script>
```
####scripts
```html
    <script src="${0}.js"></script>
```
####scriptt
```html
    <script type="${1}" id="${2}">

        ${0}

    </script>
```
####scriptsrc
```html
    <script src="${0}.js" type="text/javascript" charset="utf-8"></script>
```
####section
```html
    <section>

        ${0}

    </section>
```
####section.
```html
    <section class="${1}">

        ${0}

    </section>
```
####section#
```html
    <section id="${1}">

        ${0}

    </section>
```
####select
```html
    <select name="${1}" id="${2:$1}">

        ${0}

    </select>
```
####select.
```html
    <select name="${1}" id="${2:$1}" class="${3}>

        ${0}

    </select>
```
####select+
```html
    <select name="${1}" id="${2:$1}">

        <option value="${3}">${4:$3}</option>

        opt+${0}

    </select>
```
####small
```html
    <small>${0}</small>
```
####source
```html
    <source src="${1}" type="${2}" media="${0}" />
```
####span
```html
    <span>${0}</span>
```
####span.
```html
    <span class="${1}">${0}</span>
```
####span#
```html
    <span id="${1}">${0}</span>
```
####strong
```html
    <strong>${0}</strong>
```
####style
```html
    <style type="text/css" media="${1:all}">

        ${0}

    </style>
```
####sub
```html
    <sub>${0}</sub>
```
####summary
```html
    <summary>

        ${0}

    </summary>
```
####sup
```html
    <sup>${0}</sup>
```
####table
```html
    <table>

        ${0}

    </table>
```
####table.
```html
    <table class="${1}">

        ${0}

    </table>
```
####table#
```html
    <table id="${1}">

        ${0}

    </table>
```
####tbody
```html
    <tbody>

        ${0}

    </tbody>
```
####td
```html
    <td>${0}</td>
```
####td.
```html
    <td class="${1}">${0}</td>
```
####td#
```html
    <td id="${1}">${0}</td>
```
####td+
```html
    <td>${1}</td>

    td+${0}
```
####textarea
```html
    <textarea name="${1}" id="${2:$1}" rows="${3:8}" cols="${4:40}">${5}</textarea>
```
####tfoot
```html
    <tfoot>

        ${0}

    </tfoot>
```
####th
```html
    <th>${0}</th>
```
####th.
```html
    <th class="${1}">${0}</th>
```
####th#
```html
    <th id="${1}">${0}</th>
```
####th+
```html
    <th>${1}</th>

    th+${0}
```
####thead
```html
    <thead>

        ${0}

    </thead>
```
####time
```html
    <time datetime="${1}" pubdate="${2:$1}">${0:$1}</time>
```
####title
```html
    <title>${0:`substitute(vim_snippets#Filename('', 'Page Title'), '^.', '\u&', '')`}</title>
```
####tr
```html
    <tr>

        ${0}

    </tr>
```
####tr+
```html
    <tr>

        <td>${1}</td>

        td+${0}

    </tr>
```
####track
```html
    <track src="${1}" srclang="${2}" label="${3}" default="${4:default} />${5}
```
####ul
```html
    <ul>

        ${0}

    </ul>
```
####ul.
```html
    <ul class="${1}">

        ${0}

    </ul>
```
####ul#
```html
    <ul id="${1}">

        ${0}

    </ul>
```
####ul+
```html
    <ul>

        <li>${1}</li>

        li+${0}

    </ul>
```
####var
```html
    <var>${0}</var>
```
####video
```html
    <video src="${1} height="${2}" width="${3}" preload="${5:none}" autoplay="${6:autoplay}>${7}</video>
```
####wbr
```html
    <wbr />
```
