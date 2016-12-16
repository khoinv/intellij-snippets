####js-proto
```javascript
    ${1:class_name}.prototype.${2:method_name} = function(${3}) {

        ${0}

    };
```
####js-fun
```javascript
    function ${1:function_name}(${2}) {

        ${0}

    }
```
####js-f
```javascript
    function(${1}) {

        ${0}

    }
```
####js-vaf
```javascript
    var ${1:function_name} = function(${2}) {

        ${0}

    };
```
####js-vf
```javascript
    var ${1:function_name} = function $1(${2}) {

        ${0}

    };
```
####js-(f
```javascript
    (function(${1}) {

        ${0}

    }(${2}));
```
####js-;fe
```javascript
    ;(function(${1}) {

        ${0}

    }(${2}))
```
####js-sdf
```javascript
    var ${1:function_name} = function (${2:argument}) {

        ${3}



        $1 = function ($2) {

            ${0}

        };

    };
```
####js-if
```javascript
    if (${1:true}) {

        ${0}

    }
```
####js-ife
```javascript
    if (${1:true}) {

        ${2}

    } else {

        ${0}

    }
```
####js-ter
```javascript
    ${1:/* condition */} ? ${2:/* if true */} : ${0:/* if false */}
```
####js-switch
```javascript
    switch (${1:expression}) {

        case '${3:case}':

            ${4}

            break;

        ${0}

        default:

            ${2}

    }
```
####js-case
```javascript
    case '${1:case}':

        ${2}

        break;

    ${0}
```
####js-try
```javascript
    try {

        ${1}

    } catch (${2:e}) {

        ${0:/* handle error */}

    }
```
####js-tryf
```javascript
    try {

        ${1}

    } catch (${2:e}) {

        ${0:/* handle error */}

    } finally {

        ${3:/* be executed regardless of the try / catch result*/}

    }
```
####js-terr
```javascript
    throw new Error('${1:error message}')
```
####js-ret
```javascript
    return ${0:result};
```
####js-for
```javascript
    for (var ${2:i} = 0, l = ${1:arr}.length; $2 < l; $2++) {

        var ${3:v} = $1[$2];${0:}

    }
```
####js-forr
```javascript
    for (var ${2:i} = ${1:arr}.length - 1; $2 >= 0; $2--) {

        var ${3:v} = $1[$2];${0:}

    }
```
####js-wh
```javascript
    while (${1:/* condition */}) {

        ${0}

    }
```
####js-do
```javascript
    do {

        ${0}

    } while (${1:/* condition */});
```
####js-fori
```javascript
    for (var ${1:prop} in ${2:object}) {

        ${0:$2[$1]}

    }
```
####js-:f
```javascript
    ${1:method_name}: function (${2:attribute}) {

        ${3}

    },
```
####js-has
```javascript
    hasOwnProperty(${0})
```
####js-sing
```javascript
    function ${1:Singleton} (${2:argument}) {

        // the cached instance

        var instance;



        // rewrite the constructor

        $1 = function $1($2) {

            return instance;

        };



        // carry over the prototype properties

        $1.prototype = this;



        // the instance

        instance = new $1();



        // reset the constructor pointer

        instance.constructor = $1;



        ${0}



        return instance;

    }
```
####js-obj
```javascript
    function object(o) {

        function F() {}

        F.prototype = o;

        return new F();

    }
```
####js-props
```javascript
    var ${1:my_object} = Object.defineProperties(

        ${2:new Object()},

        {

            ${3:property} : {

                get : function $1_$3_getter() {

                    // getter code

                },

                set : function $1_$3_setter(value) {

                    // setter code

                },

                value        : ${4:value},

                writeable    : ${5:boolean},

                enumerable   : ${6:boolean},

                configurable : ${0:boolean}

            }

        }

    );
```
####js-prop
```javascript
    Object.defineProperty(

        ${1:object},

        '${2:property}',

        {

            get : function $1_$2_getter() {

                // getter code

            },

            set : function $1_$2_setter(value) {

                // setter code

            },

            value        : ${3:value},

            writeable    : ${4:boolean},

            enumerable   : ${5:boolean},

            configurable : ${0:boolean}

        }

    );
```
####js-/**
```javascript
    /**

     * ${0:description}

     *

     */
```
####js-@par
```javascript
    @param {${1:type}} ${2:name} ${0:description}
```
####js-@ret
```javascript
    @return {${1:type}} ${0:description}
```
####js-jsonp
```javascript
    JSON.parse(${0:jstr});
```
####js-jsons
```javascript
    JSON.stringify(${0:object});
```
####js-get
```javascript
    getElementsBy${1:TagName}('${0}')
```
####js-gett
```javascript
    getElementBy${1:Id}('${0}')
```
####js-by.
```javascript
    ${1:document}.getElementsByClassName('${0:class}')
```
####js-by#
```javascript
    ${1:document}.getElementById('${0:element ID}')
```
####js-qs
```javascript
    ${1:document}.querySelector('${0:CSS selector}')
```
####js-qsa
```javascript
    ${1:document}.querySelectorAll('${0:CSS selector}')
```
####js-de
```javascript
    debugger;
```
####js-cl
```javascript
    console.log(${0});
```
####js-cd
```javascript
    console.debug(${0});
```
####js-ce
```javascript
    console.error(${0});
```
####js-cw
```javascript
    console.warn(${0});
```
####js-ci
```javascript
    console.info(${0});
```
####js-ct
```javascript
    console.trace(${0:label});
```
####js-ctime
```javascript
    console.time(${0:label});
```
####js-ca
```javascript
    console.assert(${1:expression}, ${0:obj});
```
####js-cdir
```javascript
    console.dir(${0:obj});
```
####js-us
```javascript
    'use strict';
```
