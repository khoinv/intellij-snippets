####jq-add
```javascript
    ${1:obj}.add('${2:selector expression}')
```
####jq-addClass
```javascript
    ${1:obj}.addClass('${2:class name}')
```
####jq-after
```javascript
    ${1:obj}.after('${2:Some text <b>and bold!</b>}')
```
####jq-ajax
```javascript
    $.ajax({

        url: '${1:mydomain.com/url}',

        type: '${2:POST}',

        dataType: '${3:xml/html/script/json}',

        data: $.param( $('${4:Element or Expression}') ),

        complete: function (jqXHR, textStatus) {

            ${5:// callback}

        },

        success: function (data, textStatus, jqXHR) {

            ${6:// success callback}

        },

        error: function (jqXHR, textStatus, errorThrown) {

            ${0:// error callback}

        }

    });
```
####jq-ajaxcomplete
```javascript
    ${1:obj}.ajaxComplete(function (${1:e}, xhr, settings) {

        ${0:// callback}

    });
```
####jq-ajaxerror
```javascript
    ${1:obj}.ajaxError(function (${1:e}, xhr, settings, thrownError) {

        ${2:// error callback}

    });

    ${0}
```
####jq-ajaxget
```javascript
    $.get('${1:mydomain.com/url}',

        ${2:{ param1: value1 },}

        function (data, textStatus, jqXHR) {

            ${0:// success callback}

        }

    );
```
####jq-ajaxpost
```javascript
    $.post('${1:mydomain.com/url}',

        ${2:{ param1: value1 },}

        function (data, textStatus, jqXHR) {

            ${0:// success callback}

        }

    );
```
####jq-ajaxprefilter
```javascript
    $.ajaxPrefilter(function (${1:options}, ${2:originalOptions}, jqXHR) {

        ${0: // Modify options, control originalOptions, store jqXHR, etc}

    });
```
####jq-ajaxsend
```javascript
    ${1:obj}.ajaxSend(function (${1:request, settings}) {

        ${2:// error callback}

    });

    ${0}
```
####jq-ajaxsetup
```javascript
    $.ajaxSetup({

        url: "${1:mydomain.com/url}",

        type: "${2:POST}",

        dataType: "${3:xml/html/script/json}",

        data: $.param( $("${4:Element or Expression}") ),

        complete: function (jqXHR, textStatus) {

            ${5:// callback}

        },

        success: function (data, textStatus, jqXHR) {

            ${6:// success callback}

        },

        error: function (jqXHR, textStatus, errorThrown) {

            ${0:// error callback}

        }

    });
```
####jq-ajaxstart
```javascript
    $.ajaxStart(function () {

        ${1:// handler for when an AJAX call is started and no other AJAX calls are in progress};

    });

    ${0}
```
####jq-ajaxstop
```javascript
    $.ajaxStop(function () {

        ${1:// handler for when all AJAX calls have been completed};

    });

    ${0}
```
####jq-ajaxsuccess
```javascript
    $.ajaxSuccess(function (${1:e}, xhr, settings) {

        ${2:// handler for when any AJAX call is successfully completed};

    });

    ${0}
```
####jq-andself
```javascript
    ${1:obj}.andSelf()
```
####jq-animate
```javascript
    ${1:obj}.animate({${2:param1: value1, param2: value2}}, ${3:speed})
```
####jq-append
```javascript
    ${1:obj}.append('${2:Some text <b>and bold!</b>}')
```
####jq-appendTo
```javascript
    ${1:obj}.appendTo('${2:selector expression}')
```
####jq-attr
```javascript
    ${1:obj}.attr('${2:attribute}', '${3:value}')
```
####jq-attrm
```javascript
    ${1:obj}.attr({'${2:attr1}': '${3:value1}', '${4:attr2}': '${5:value2}'})
```
####jq-before
```javascript
    ${1:obj}.before('${2:Some text <b>and bold!</b>}')
```
####jq-bind
```javascript
    ${1:obj}.bind('${2:event name}', function (${3:e}) {

        ${0:// event handler}

    });
```
####jq-blur
```javascript
    ${1:obj}.blur(function (${2:e}) {

        ${0:// event handler}

    });
```
####jq-C
```javascript
    $.Callbacks()
```
####jq-Cadd
```javascript
    ${1:callbacks}.add(${2:callbacks})
```
####jq-Cdis
```javascript
    ${1:callbacks}.disable()
```
####jq-Cempty
```javascript
    ${1:callbacks}.empty()
```
####jq-Cfire
```javascript
    ${1:callbacks}.fire(${2:args})
```
####jq-Cfired
```javascript
    ${1:callbacks}.fired()
```
####jq-Cfirew
```javascript
    ${1:callbacks}.fireWith(${2:this}, ${3:args})
```
####jq-Chas
```javascript
    ${1:callbacks}.has(${2:callback})
```
####jq-Clock
```javascript
    ${1:callbacks}.lock()
```
####jq-Clocked
```javascript
    ${1:callbacks}.locked()
```
####jq-Crem
```javascript
    ${1:callbacks}.remove(${2:callbacks})
```
####jq-change
```javascript
    ${1:obj}.change(function (${2:e}) {

        ${0:// event handler}

    });
```
####jq-children
```javascript
    ${1:obj}.children('${2:selector expression}')
```
####jq-clearq
```javascript
    ${1:obj}.clearQueue(${2:'queue name'})
```
####jq-click
```javascript
    ${1:obj}.click(function (${2:e}) {

        ${0:// event handler}

    });
```
####jq-clone
```javascript
    ${1:obj}.clone()
```
####jq-contains
```javascript
    $.contains(${1:container}, ${0:contents});
```
####jq-css
```javascript
    ${1:obj}.css('${2:attribute}', '${3:value}')
```
####jq-csshooks
```javascript
    $.cssHooks['${1:CSS prop}'] = {

        get: function (elem, computed, extra) {

            ${2: // handle getting the CSS property}

        },

        set: function (elem, value) {

            ${0: // handle setting the CSS value}

        }

    };
```
####jq-cssm
```javascript
    ${1:obj}.css({${2:attribute1}: '${3:value1}', ${4:attribute2}: '${5:value2}'})
```
####jq-D
```javascript
    $.Deferred()
```
####jq-Dalways
```javascript
    ${1:deferred}.always(${2:callbacks})
```
####jq-Ddone
```javascript
    ${1:deferred}.done(${2:callbacks})
```
####jq-Dfail
```javascript
    ${1:deferred}.fail(${2:callbacks})
```
####jq-Disrej
```javascript
    ${1:deferred}.isRejected()
```
####jq-Disres
```javascript
    ${1:deferred}.isResolved()
```
####jq-Dnotify
```javascript
    ${1:deferred}.notify(${2:args})
```
####jq-Dnotifyw
```javascript
    ${1:deferred}.notifyWith(${2:this}, ${3:args})
```
####jq-Dpipe
```javascript
    ${1:deferred}.then(${2:doneFilter}, ${3:failFilter}, ${4:progressFilter})
```
####jq-Dprog
```javascript
    ${1:deferred}.progress(${2:callbacks})
```
####jq-Dprom
```javascript
    ${1:deferred}.promise(${2:target})
```
####jq-Drej
```javascript
    ${1:deferred}.reject(${2:args})
```
####jq-Drejw
```javascript
    ${1:deferred}.rejectWith(${2:this}, ${3:args})
```
####jq-Dres
```javascript
    ${1:deferred}.resolve(${2:args})
```
####jq-Dresw
```javascript
    ${1:deferred}.resolveWith(${2:this}, ${3:args})
```
####jq-Dstate
```javascript
    ${1:deferred}.state()
```
####jq-Dthen
```javascript
    ${1:deferred}.then(${2:doneCallbacks}, ${3:failCallbacks}, ${4:progressCallbacks})
```
####jq-Dwhen
```javascript
    $.when(${1:deferreds})
```
####jq-data
```javascript
    ${1:obj}.data(${2:obj})
```
####jq-dataa
```javascript
    $.data('${1:selector expression}', '${2:key}'${3:, 'value'})
```
####jq-dblclick
```javascript
    ${1:obj}.dblclick(function (${2:e}) {

        ${0:// event handler}

    });
```
####jq-delay
```javascript
    ${1:obj}.delay('${2:slow/400/fast}'${3:, 'queue name'})
```
####jq-dele
```javascript
    ${1:obj}.delegate('${2:selector expression}', '${3:event name}', function (${4:e}) {

        ${0:// event handler}

    });
```
####jq-deq
```javascript
    ${1:obj}.dequeue(${2:'queue name'})
```
####jq-deqq
```javascript
    $.dequeue('${1:selector expression}'${2:, 'queue name'})
```
####jq-detach
```javascript
    ${1:obj}.detach('${2:selector expression}')
```
####jq-die
```javascript
    ${1:obj}.die(${2:event}, ${3:handler})
```
####jq-each
```javascript
    ${1:obj}.each(function (index) {

        ${0:this.innerHTML = this + " is the element, " + index + " is the position";}

    });
```
####jq-el
```javascript
    $('<${1}/>'${2:, {}})
```
####jq-eltrim
```javascript
    $.trim('${1:string}')
```
####jq-empty
```javascript
    ${1:obj}.empty()
```
####jq-end
```javascript
    ${1:obj}.end()
```
####jq-eq
```javascript
    ${1:obj}.eq(${2:element index})
```
####jq-error
```javascript
    ${1:obj}.error(function (${2:e}) {

        ${0:// event handler}

    });
```
####jq-eventsmap
```javascript
    {

        :f${0}

    }
```
####jq-extend
```javascript
    $.extend(${1:true, }${2:target}, ${3:obj})
```
####jq-fadein
```javascript
    ${1:obj}.fadeIn('${2:slow/400/fast}')
```
####jq-fadeinc
```javascript
    ${1:obj}.fadeIn('slow/400/fast', function () {

        ${0:// callback};

    });
```
####jq-fadeout
```javascript
    ${1:obj}.fadeOut('${2:slow/400/fast}')
```
####jq-fadeoutc
```javascript
    ${1:obj}.fadeOut('slow/400/fast', function () {

        ${0:// callback};

    });
```
####jq-fadeto
```javascript
    ${1:obj}.fadeTo('${2:slow/400/fast}', ${3:0.5})
```
####jq-fadetoc
```javascript
    ${1:obj}.fadeTo('slow/400/fast', ${2:0.5}, function () {

        ${0:// callback};

    });
```
####jq-filter
```javascript
    ${1:obj}.filter('${2:selector expression}')
```
####jq-filtert
```javascript
    ${1:obj}.filter(function (${2:index}) {

        ${3}

    })
```
####jq-find
```javascript
    ${1:obj}.find('${2:selector expression}')
```
####jq-focus
```javascript
    ${1:obj}.focus(function (${2:e}) {

        ${0:// event handler}

    });
```
####jq-focusin
```javascript
    ${1:obj}.focusIn(function (${2:e}) {

        ${0:// event handler}

    });
```
####jq-focusout
```javascript
    ${1:obj}.focusOut(function (${2:e}) {

        ${0:// event handler}

    });
```
####jq-get
```javascript
    ${1:obj}.get(${2:element index})
```
####jq-getjson
```javascript
    $.getJSON('${1:mydomain.com/url}',

        ${2:{ param1: value1 },}

        function (data, textStatus, jqXHR) {

            ${0:// success callback}

        }

    );
```
####jq-getscript
```javascript
    $.getScript('${1:mydomain.com/url}', function (script, textStatus, jqXHR) {

        ${0:// callback}

    });
```
####jq-grep
```javascript
    $.grep(${1:array}, function (item, index) {

        ${2}

    }${0:, true});
```
####jq-hasc
```javascript
    ${1:obj}.hasClass('${2:className}')
```
####jq-hasd
```javascript
    $.hasData('${0:selector expression}');
```
####jq-height
```javascript
    ${1:obj}.height(${2:integer})
```
####jq-hide
```javascript
    ${1:obj}.hide('${2:slow/400/fast}')
```
####jq-hidec
```javascript
    ${1:obj}.hide('${2:slow/400/fast}', function () {

        ${0:// callback}

    });
```
####jq-hover
```javascript
    ${1:obj}.hover(function (${2:e}) {

        ${3:// event handler}

    }, function ($2) {

        ${4:// event handler}

    });
```
####jq-html
```javascript
    ${1:obj}.html('${2:Some text <b>and bold!</b>}')
```
####jq-inarr
```javascript
    $.inArray(${1:value}, ${0:array});
```
####jq-insa
```javascript
    ${1:obj}.insertAfter('${2:selector expression}')
```
####jq-insb
```javascript
    ${1:obj}.insertBefore('${2:selector expression}')
```
####jq-is
```javascript
    ${1:obj}.is('${2:selector expression}')
```
####jq-isarr
```javascript
    $.isArray(${1:obj})
```
####jq-isempty
```javascript
    $.isEmptyObject(${1:obj})
```
####jq-isfunc
```javascript
    $.isFunction(${1:obj})
```
####jq-isnum
```javascript
    $.isNumeric(${1:value})
```
####jq-isobj
```javascript
    $.isPlainObject(${1:obj})
```
####jq-iswin
```javascript
    $.isWindow(${1:obj})
```
####jq-isxml
```javascript
    $.isXMLDoc(${1:node})
```
####jq-jj
```javascript
    $('${1:selector}')
```
####jq-kdown
```javascript
    ${1:obj}.keydown(function (${2:e}) {

        ${0:// event handler}

    });
```
####jq-kpress
```javascript
    ${1:obj}.keypress(function (${2:e}) {

        ${0:// event handler}

    });
```
####jq-kup
```javascript
    ${1:obj}.keyup(function (${2:e}) {

        ${0:// event handler}

    });
```
####jq-last
```javascript
    ${1:obj}.last('${1:selector expression}')
```
####jq-live
```javascript
    ${1:obj}.live('${2:events}', function (${3:e}) {

        ${0:// event handler}

    });
```
####jq-load
```javascript
    ${1:obj}.load(function (${2:e}) {

        ${0:// event handler}

    });
```
####jq-loadf
```javascript
    ${1:obj}.load('${2:mydomain.com/url}',

        ${2:{ param1: value1 },}

        function (responseText, textStatus, xhr) {

            ${0:// success callback}

        }

    });
```
####jq-makearray
```javascript
    $.makeArray(${0:obj});
```
####jq-map
```javascript
    ${1:obj}.map(function (${2:index}, ${3:element}) {

        ${0:// callback}

    });
```
####jq-mapp
```javascript
    $.map(${1:arrayOrObject}, function (${2:value}, ${3:indexOrKey}) {

        ${0:// callback}

    });
```
####jq-merge
```javascript
    $.merge(${1:target}, ${0:original});
```
####jq-mdown
```javascript
    ${1:obj}.mousedown(function (${2:e}) {

        ${0:// event handler}

    });
```
####jq-menter
```javascript
    ${1:obj}.mouseenter(function (${2:e}) {

        ${0:// event handler}

    });
```
####jq-mleave
```javascript
    ${1:obj}.mouseleave(function (${2:e}) {

        ${0:// event handler}

    });
```
####jq-mmove
```javascript
    ${1:obj}.mousemove(function (${2:e}) {

        ${0:// event handler}

    });
```
####jq-mout
```javascript
    ${1:obj}.mouseout(function (${2:e}) {

        ${0:// event handler}

    });
```
####jq-mover
```javascript
    ${1:obj}.mouseover(function (${2:e}) {

        ${0:// event handler}

    });
```
####jq-mup
```javascript
    ${1:obj}.mouseup(function (${2:e}) {

        ${0:// event handler}

    });
```
####jq-next
```javascript
    ${1:obj}.next('${2:selector expression}')
```
####jq-nexta
```javascript
    ${1:obj}.nextAll('${2:selector expression}')
```
####jq-nextu
```javascript
    ${1:obj}.nextUntil('${2:selector expression}'${3:, 'filter expression'})
```
####jq-not
```javascript
    ${1:obj}.not('${2:selector expression}')
```
####jq-off
```javascript
    ${1:obj}.off('${2:events}', '${3:selector expression}'${4:, handler})
```
####jq-offset
```javascript
    ${1:obj}.offset()
```
####jq-offsetp
```javascript
    ${1:obj}.offsetParent()
```
####jq-on
```javascript
    ${1:obj}.on('${2:events}', '${3:selector expression}', function (${4:e}) {

        ${0:// event handler}

    });
```
####jq-one
```javascript
    ${1:obj}.one('${2:event name}', function (${3:e}) {

        ${0:// event handler}

    });
```
####jq-outerh
```javascript
    ${1:obj}.outerHeight()
```
####jq-outerw
```javascript
    ${1:obj}.outerWidth()
```
####jq-param
```javascript
    $.param(${1:obj})
```
####jq-parent
```javascript
    ${1:obj}.parent('${2:selector expression}')
```
####jq-parents
```javascript
    ${1:obj}.parents('${2:selector expression}')
```
####jq-parentsu
```javascript
    ${1:obj}.parentsUntil('${2:selector expression}'${3:, 'filter expression'})
```
####jq-parsejson
```javascript
    $.parseJSON(${1:data})
```
####jq-parsexml
```javascript
    $.parseXML(${1:data})
```
####jq-pos
```javascript
    ${1:obj}.position()
```
####jq-prepend
```javascript
    ${1:obj}.prepend('${2:Some text <b>and bold!</b>}')
```
####jq-prependto
```javascript
    ${1:obj}.prependTo('${2:selector expression}')
```
####jq-prev
```javascript
    ${1:obj}.prev('${2:selector expression}')
```
####jq-preva
```javascript
    ${1:obj}.prevAll('${2:selector expression}')
```
####jq-prevu
```javascript
    ${1:obj}.prevUntil('${2:selector expression}'${3:, 'filter expression'})
```
####jq-promise
```javascript
    ${1:obj}.promise(${2:'fx'}, ${3:target})
```
####jq-prop
```javascript
    ${1:obj}.prop('${2:property name}')
```
####jq-proxy
```javascript
    $.proxy(${1:function}, ${2:this})
```
####jq-pushstack
```javascript
    ${1:obj}.pushStack(${2:elements})
```
####jq-queue
```javascript
    ${1:obj}.queue(${2:name}${3:, newQueue})
```
####jq-queuee
```javascript
    $.queue(${1:element}${2:, name}${3:, newQueue})
```
####jq-ready
```javascript
    $(function () {

        ${0}

    });
```
####jq-rem
```javascript
    ${1:obj}.remove()
```
####jq-rema
```javascript
    ${1:obj}.removeAttr('${2:attribute name}')
```
####jq-remc
```javascript
    ${1:obj}.removeClass('${2:class name}')
```
####jq-remd
```javascript
    ${1:obj}.removeData('${2:key name}')
```
####jq-remdd
```javascript
    $.removeData(${1:element}${2:, 'key name}')
```
####jq-remp
```javascript
    ${1:obj}.removeProp('${2:property name}')
```
####jq-repa
```javascript
    ${1:obj}.replaceAll(${2:target})
```
####jq-repw
```javascript
    ${1:obj}.replaceWith(${2:content})
```
####jq-reset
```javascript
    ${1:obj}.reset(function (${2:e}) {

        ${0:// event handler}

    });
```
####jq-resize
```javascript
    ${1:obj}.resize(function (${2:e}) {

        ${0:// event handler}

    });
```
####jq-scroll
```javascript
    ${1:obj}.scroll(function (${2:e}) {

        ${0:// event handler}

    });
```
####jq-scrolll
```javascript
    ${1:obj}.scrollLeft(${2:value})
```
####jq-scrollt
```javascript
    ${1:obj}.scrollTop(${2:value})
```
####jq-sdown
```javascript
    ${1:obj}.slideDown('${2:slow/400/fast}')
```
####jq-sdownc
```javascript
    ${1:obj}.slideDown('${2:slow/400/fast}', function () {

        ${0:// callback};

    });
```
####jq-select
```javascript
    ${1:obj}.select(function (${2:e}) {

        ${0:// event handler}

    });
```
####jq-serialize
```javascript
    ${1:obj}.serialize()
```
####jq-serializea
```javascript
    ${1:obj}.serializeArray()
```
####jq-show
```javascript
    ${1:obj}.show('${2:slow/400/fast}')
```
####jq-showc
```javascript
    ${1:obj}.show('${2:slow/400/fast}', function () {

        ${0:// callback}

    });
```
####jq-sib
```javascript
    ${1:obj}.siblings('${2:selector expression}')
```
####jq-size
```javascript
    ${1:obj}.size()
```
####jq-slice
```javascript
    ${1:obj}.slice(${2:start}${3:, end})
```
####jq-stoggle
```javascript
    ${1:obj}.slideToggle('${2:slow/400/fast}')
```
####jq-stop
```javascript
    ${1:obj}.stop('${2:queue}', ${3:false}, ${4:false})
```
####jq-submit
```javascript
    ${1:obj}.submit(function (${2:e}) {

        ${0:// event handler}

    });
```
####jq-sup
```javascript
    ${1:obj}.slideUp('${2:slow/400/fast}')
```
####jq-supc
```javascript
    ${1:obj}.slideUp('${2:slow/400/fast}', function () {

        ${0:// callback};

    });
```
####jq-text
```javascript
    ${1:obj}.text(${2:'some text'})
```
####jq-this
```javascript
    $(this)
```
####jq-toarr
```javascript
    ${0:obj}.toArray()
```
####jq-tog
```javascript
    ${1:obj}.toggle(function (${2:e}) {

        ${3:// event handler}

    }, function ($2) {

        ${4:// event handler}

    });

    ${0}
```
####jq-togclass
```javascript
    ${1:obj}.toggleClass('${2:class name}')
```
####jq-togsh
```javascript
    ${1:obj}.toggle('${2:slow/400/fast}')
```
####jq-trig
```javascript
    ${1:obj}.trigger('${2:event name}')
```
####jq-trigh
```javascript
    ${1:obj}.triggerHandler('${2:event name}')
```
####jq-$trim
```javascript
    $.trim(${1:str})
```
####jq-$type
```javascript
    $.type(${1:obj})
```
####jq-unbind
```javascript
    ${1:obj}.unbind('${2:event name}')
```
####jq-undele
```javascript
    ${1:obj}.undelegate(${2:selector expression}, ${3:event}, ${4:handler})
```
####jq-uniq
```javascript
    $.unique(${1:array})
```
####jq-unload
```javascript
    ${1:obj}.unload(function (${2:e}) {

        ${0:// event handler}

    });
```
####jq-unwrap
```javascript
    ${1:obj}.unwrap()
```
####jq-val
```javascript
    ${1:obj}.val('${2:text}')
```
####jq-width
```javascript
    ${1:obj}.width(${2:integer})
```
