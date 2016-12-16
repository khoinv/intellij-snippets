####php-<?
```php
    <?php



    ${0}
```
####php-dst
```php
    declare(strict_types=${1:1});
```
####php-ec
```php
    echo ${0};
```
####php-<?e
```php
    <?php echo ${0} ?>
```
####php-<?=
```php
    <?=${0}?>
```
####php-?=
```php
    <?= ${0} ?>
```
####php-?
```php
    <?php ${0} ?>
```
####php-?f
```php
    <?php foreach ($${1:vars} as $${2:$var}): ?>

        ${0}

    <?php endforeach ?>
```
####php-?i
```php
    <?php if ($${1:var}): ?>

        ${0}

    <?php endif ?>
```
####php-ns
```php
    namespace ${1:Foo\Bar\Baz};

    ${0}
```
####php-c
```php
    class ${1:`vim_snippets#Filename()`}

    {

        ${0}

    }
```
####php-i
```php
    interface ${1:`vim_snippets#Filename()`}

    {

        ${0}

    }
```
####php-t.
```php
    $this->
```
####php-f
```php
    function ${1}(${3})

    {

        ${0}

    }
```
####php-m
```php
    ${1:protected} function ${2:foo}()

    {

        ${0}

    }
```
####php-sm
```php
    /**

     * Sets the value of ${1:foo}

     *

     * @param ${2:string} $$1 ${3:description}

     *

     * @return ${4:`vim_snippets#Filename()`}

     */

    ${5:public} function set${6:$1}(${7:$2 }$$1)

    {

        $this->${8:$1} = $$1;



        return $this;

    }
```
####php-gm
```php
    /**

     * Gets the value of ${1:foo}

     *

     * @return ${2:string}

     */

    ${3:public} function get${4:$1}()

    {

        return $this->${5:$1};

    }
```
####php-$s
```php
    ${1:$foo}->set${2:Bar}(${0});
```
####php-$g
```php
    ${1:$foo}->get${0:Bar}();
```
####php-=?:
```php
    $${1:foo} = ${2:true} ? ${3:a} : ${0};
```
####php-?:
```php
    ${1:true} ? ${2:a} : ${0}
```
####php-t
```php
    $${1:retVal} = (${2:condition}) ? ${3:a} : ${4:b};
```
####php-C
```php
    $_COOKIE['${1:variable}']
```
####php-E
```php
    $_ENV['${1:variable}']
```
####php-F
```php
    $_FILES['${1:variable}']
```
####php-G
```php
    $_GET['${1:variable}']
```
####php-P
```php
    $_POST['${1:variable}']
```
####php-R
```php
    $_REQUEST['${1:variable}']
```
####php-S
```php
    $_SERVER['${1:variable}']
```
####php-SS
```php
    $_SESSION['${1:variable}']
```
####php-get
```php
    $_GET['${1}']
```
####php-post
```php
    $_POST['${1}']
```
####php-session
```php
    $_SESSION['${1}']
```
####php-inc
```php
    include '${1:file}';
```
####php-inc1
```php
    include_once '${1:file}';
```
####php-req
```php
    require '${1:file}';
```
####php-req1
```php
    require_once '${1:file}';
```
####php-/*
```php
    /**

     * ${0}

     */
```
####php-doc_cp
```php
    /**

     * ${1:undocumented class}

     *

     * @package ${2:default}

     * @subpackage ${3:default}

     * @author ${4:`g:snips_author`}

     */
```
####php-doc_vp
```php
    /**

     * ${1:undocumented class variable}

     *

     * @var ${2:string}

     */
```
####php-doc_v
```php
    /**

     * ${3:undocumented class variable}

     *

     * @var ${4:string}

     */

    ${1:var} $${2};
```
####php-doc_c
```php
    /**

     * ${3:undocumented class}

     *

     * @package ${4:default}

     * @subpackage ${5:default}

     * @author ${6:`g:snips_author`}

     */

    ${1:}class ${2:}

    {

        ${0}

    } // END $1class $2
```
####php-doc_dp
```php
    /**

     * ${1:undocumented constant}

     */
```
####php-doc_d
```php
    /**

     * ${3:undocumented constant}

     */

    define(${1}, ${2});
```
####php-doc_fp
```php
    /**

     * ${1:undocumented function}

     *

     * @return ${2:void}

     * @author ${3:`g:snips_author`}

     */
```
####php-doc_s
```php
    /**

     * ${4:undocumented function}

     *

     * @return ${5:void}

     * @author ${6:`g:snips_author`}

     */

    ${1}function ${2}(${3});
```
####php-doc_f
```php
    /**

     * ${4:undocumented function}

     *

     * @return ${5:void}

     * @author ${6:`g:snips_author`}

     */

    ${1}function ${2}(${3})

    {${0}

    }
```
####php-doc_h
```php
    /**

     * ${1}

     *

     * @author ${2:`g:snips_author`}

     * @version ${3:$Id$}

     * @copyright ${4:$2}, `strftime('%d %B, %Y')`

     * @package ${0:default}

     */
```
####php-doc_i
```php
    /**

     * $1

     * @package ${2:default}

     * @author ${3:`!v g:snips_author`}

     **/

    interface ${1:someClass}

    {${4}

    }
```
####php-inheritdoc
```php
    /**

     * {@inheritdoc}

     */
```
####php-interface
```php
    /**

     * ${2:undocumented class}

     *

     * @package ${3:default}

     * @author ${4:`g:snips_author`}

     */

    interface ${1:`vim_snippets#Filename()`}

    {

        ${0}

    }
```
####php-trait
```php
    /**

     * ${2:undocumented class}

     *

     * @package ${3:default}

     * @author ${4:`g:snips_author`}

     */

    trait ${1:`vim_snippets#Filename()`}

    {

        ${0}

    }
```
####php-class
```php
    /**

     * ${1}

     */

    class ${2:`vim_snippets#Filename()`}

    {

        ${3}

        /**

         * ${4}

         */

        ${5:public} function ${6:__construct}(${7:argument})

        {

            ${0}

        }

    }
```
####php-nc
```php
    namespace ${1:`substitute(substitute(expand("%:h"), '\v^\w+\/(\u)', '\1', ''), '\/', '\\\', 'g')`};



    ${2:abstract }class ${3:`vim_snippets#Filename()`}

    {

        ${0}

    }
```
####php-def
```php
    define('${1:VARIABLE_NAME}', ${2:'definition'});
```
####php-def?
```php
    ${1}defined('${2}')
```
####php-wh
```php
    while (${1:/* condition */}) {

        ${0}

    }
```
####php-do
```php
    do {

        ${0}

    } while (${1});
```
####php-if
```php
    if (${1}) {

        ${0}

    }
```
####php-ifn
```php
    if (!${1}) {

        ${2}

    }
```
####php-ifil
```php
    <?php if (${1}): ?>

        ${0}

    <?php endif; ?>
```
####php-ife
```php
    if (${1}) {

        ${2}

    } else {

        ${3}

    }

    ${0}
```
####php-ifeil
```php
    <?php if (${1}): ?>

        ${2}

    <?php else: ?>

        ${3}

    <?php endif; ?>

    ${0}
```
####php-el
```php
    else {

        ${0}

    }
```
####php-eif
```php
    elseif (${1}) {

        ${0}

    }
```
####php-switch
```php
    switch ($${1:variable}) {

        case '${2:value}':

            ${3}

            break;

        ${0}

        default:

            ${4}

            break;

    }
```
####php-case
```php
    case '${1:value}':

        ${2}

        break;
```
####php-for
```php
    for ($${2:i} = 0; $$2 < ${1:count}; $$2${3:++}) {

        ${0}

    }
```
####php-foreach
```php
    foreach ($${1:variable} as $${2:value}) {

        ${0}

    }
```
####php-foreachil
```php
    <?php foreach ($${1:variable} as $${2:value}): ?>

        ${0}

    <?php endforeach; ?>
```
####php-foreachk
```php
    foreach ($${1:variable} as $${2:key} => $${3:value}) {

        ${0}

    }
```
####php-foreachkil
```php
    <?php foreach ($${1:variable} as $${2:key} => $${3:value}): ?>

        ${0:<!-- html... -->}

    <?php endforeach; ?>
```
####php-array
```php
    $${1:arrayName} = ['${2}' => ${3}];
```
####php-try
```php
    try {

        ${0}

    } catch (${1:Exception} $e) {

    }
```
####php-lambda
```php
    ${1:static }function (${2:args}) use (${3:&$x, $y /*put vars in scope (closure) */}) {

        ${0}

    };
```
####php-pd
```php
    echo '<pre>'; var_dump(${0}); echo '</pre>';
```
####php-pdd
```php
    echo '<pre>'; var_dump(${1}); echo '</pre>'; die(${0:});
```
####php-vd
```php
    var_dump(${0});
```
####php-vdd
```php
    var_dump(${1}); die(${0:});
```
####php-pr
```php
    print_r(${0});
```
####php-prs
```php
    print_r(${0}, 1);
```
####php-vdf
```php
    error_log(print_r($${1:foo}, true), 3, '${2:/tmp/debug.log}');
```
####php-http_redirect
```php
    header ("HTTP/1.1 301 Moved Permanently");

    header ("Location: ".URL);

    exit();
```
####php-log
```php
    error_log(var_export(${1}, true));
```
####php-var
```php
    var_export(${1});
```
####php-ve
```php
    echo '<pre>' . var_export(${1}, 1) . '</pre>';
```
####php-pc
```php
    var_export($1);$0
```
####php-gs
```php
    /**

     * Gets the value of ${1:foo}

     *

     * @return ${2:string}

     */

    public function get${3:$1}()

    {

        return $this->${4:$1};

    }



    /**

     * Sets the value of $1

     *

     * @param $2 $$1 ${5:description}

     *

     * @return ${6:`vim_snippets#Filename()`}

     */

    public function set$3(${7:$2 }$$1)

    {

        $this->$4 = $$1;

        return $this;

    }
```
####php-ags
```php
    /**

     * ${1:description}

     *

     * @${0}

     */

    ${2:protected} $${3:foo};



    public function get${4:$3}()

    {

        return $this->$3;

    }



    public function set$4(${5:$4 }$${6:$3})

    {

        $this->$3 = $$6;

        return $this;

    }
```
####php-rett
```php
    return true;
```
####php-retf
```php
    return false;
```
####php-am
```php
    $${1:foo} = array_map(function($${2:v}) {

        ${0}

        return $$2;

    }, $$1);
```
####php-aw
```php
    array_walk($${1:foo}, function(&$${2:v}, $${3:k}) {

        $$2 = ${0};

    });
```
####php-static_var
```php
    static $${1} = null;

    if (is_null($$1)){

        $$1 = ${2};

    }
```
####php-CSVWriter
```php
    <?php

    

    class CSVWriter {

        public function __construct($file_or_handle, $sep = "\t", $quot = '"'){

            $args = func_get_args();

            $mode = isset($opts['mode']) ? $opts['mode'] : 'w';

    

            $this->f =

                is_string($file_or_handle)

                ? fopen($file_or_handle, $mode)

                : $file_or_handle;

    

            $this->fputcsv_args = [$this->f, null, $sep, $quot];

    

            if (!$this->f) throw new Exception('bad file descriptor');

        }

    

        public function write($row){

            $this->fputcsv_args[1] =& $row;

            call_user_func_array('fputcsv', $this->fputcsv_args);

        }

    

        public function close(){

            if (!is_null($this->f))

                fclose($this->f);

            $this->f = null;

        }

    

        public function __destruct(){

            $this->close();

        }

    

    }
```
####php-CSVIterator
```php
    

    // http://snipplr.com/view.php?codeview&id=1986 // modified

    class CSVIterator implements Iterator

    {    

        private $f;

        private $curr;

        private $rowCounter;

    

         /* opts keys:

            * row_size

            * escape

            * enclosure

            * delimiter

            */

        public function __construct( $file_or_handle, $opts = [4096, ','] )

        {

            $d = function($n) use(&$opts){ return isset($opts[$n]) ? $opts[$n] : false; };

    

            $this->combine = $d('combine');

            $this->headers = $d('headers');

            $this->headerCheckFunction = $d('header_check_function');

    

            $this->f =

                is_string($file_or_handle)

                ? fopen( $file_or_handle, 'r' )

                : $file_or_handle;

            if (!$this->f) throw new Exception('bad file descriptor');

            $this->fgetcsv_args = [

                    $this->f,

                    isset($opts['row_size']) ? $opts['row_size'] : 4096,

                    isset($opts['delimiter']) ? $opts['delimiter'] : ',',

                    isset($opts['enclosure']) ? $opts['enclosure'] : '"',

                    isset($opts['escape']) ? $opts['escape'] : '\\',

            ];

            $this->start();

        }

    

        protected function readRow(){

            $this->curr = call_user_func_array('fgetcsv', $this->fgetcsv_args );

            $this->rowCounter++;

            if ($this->rowCounter == 1){

                $this->processHeader();

            } elseif ($this->curr) {

                $this->processRow();

            }

        }

    

        public function processHeader(){

            if ($this->headers || $this->combine){

                $this->header = $this->curr;

                if ($this->headerCheckFunction){

                    $f = $this->headerCheckFunction;

                    $f($this->header);

                }

                $this->readRow();

            }

        }

    

        public function processRow(){

            if ($this->combine)

                $this->curr = array_combine($this->header, $this->curr);

        }

    

        public function start(){

            $this->rowCounter = 0;

            rewind( $this->f );

            $this->readRow();

        }

    

        public function rewind()

        {

            $this->start();

        }

    

        public function current()

        {

            $curr = $this->curr;

            $this->readRow();

            return $curr;

        }

    

        public function key()

        {

            return $this->rowCounter;

        }

    

        public function next()

        {

            return $this->curr;

        }

    

        public function valid(){

            if( !$this->next() )

            {

                fclose( $this->f );

                return FALSE;

            }

            return TRUE;

        }

    

    } // end class
```
####php-ase
```php
    $this->assertEquals(${1:expected}, ${2:actual});
```
####php-asne
```php
    $this->assertNotEquals(${1:expected}, ${2:actual});
```
####php-asf
```php
    $this->assertFalse(${1});
```
####php-ast
```php
    $this->assertTrue(${1});
```
####php-asfex
```php
    $this->assertFileExists(${1:'path/to/file'});
```
####php-asfnex
```php
    $this->assertFileNotExists(${1:'path/to/file'});
```
####php-ascon
```php
    $this->assertContains(${1:$needle}, ${2:$haystack});
```
####php-ashk
```php
    $this->assertArrayHasKey(${1:$key}, ${2:$array});
```
####php-asnhk
```php
    this->assertArrayNotHasKey(${1:$key}, ${2:$array});
```
####php-ascha
```php
    $this->assertClassHasAttribute(${1:$attributeName}, '${2:$className}');
```
####php-asi
```php
    $this->assertInstanceOf(${1:expected}, ${2:actual});
```
####php-test
```php
    public function test${1}()

    {

        ${0}

    }
```
####php-setup
```php
    protected function setUp()

    {

        ${0}

    }
```
####php-teardown
```php
    protected function tearDown()

    {

        ${0}

    }
```
####php-exp
```php
    expects($this->${1:once}())

        ->method('${2}')

        ->with($this->equalTo(${3})${4})

        ->will($this->returnValue(${5}));
```
####php-testcmt
```php
    /**

    * @group ${1}

    */
```
####php-fail
```php
    $this->fail(${1});
```
####php-marki
```php
    $this->markTestIncomplete(${1});
```
####php-marks
```php
    $this->markTestSkipped(${1});
```
####php-te
```php
    throw new ${1:Exception}("${2:Error Processing Request}");
```
####php-fpc
```php
    file_put_contents(${1:file}, ${2:content}${3:, FILE_APPEND});$0
```
####php-sr
```php
    str_replace(${1:search}, ${2:replace}, ${3:subject})$0
```
####php-ia
```php
    in_array(${1:needle}, ${2:haystack})$0
```
####php-is
```php
    isset(${1:var})$0
```
####php-isa
```php
    isset($${1:array}[${2:key}])$0
```
####php-in
```php
    is_null($${1:var})$0
```
####php-fe
```php
    file_exists(${1:file})$0
```
