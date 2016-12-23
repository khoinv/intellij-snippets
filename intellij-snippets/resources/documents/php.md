####p-<?
```php
    <?php



    ${0}
```
####p-dst
```php
    declare(strict_types=${1:1});
```
####p-ec
```php
    echo ${0};
```
####p-<?e
```php
    <?php echo ${0} ?>
```
####p-<?=
```php
    <?=${0}?>
```
####p-?=
```php
    <?= ${0} ?>
```
####p-?
```php
    <?php ${0} ?>
```
####p-?f
```php
    <?php foreach ($${1:vars} as $${2:$var}): ?>

        ${0}

    <?php endforeach ?>
```
####p-?i
```php
    <?php if ($${1:var}): ?>

        ${0}

    <?php endif ?>
```
####p-ns
```php
    namespace ${1:Foo\Bar\Baz};

    ${0}
```
####p-t.
```php
    $this->
```
####p-f
```php
    function ${1}(${3})

    {

        ${0}

    }
```
####p-m
```php
    ${1:protected} function ${2:foo}()

    {

        ${0}

    }
```
####p-gm
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
####p-$s
```php
    ${1:$foo}->set${2:Bar}(${0});
```
####p-$g
```php
    ${1:$foo}->get${0:Bar}();
```
####p-=?:
```php
    $${1:foo} = ${2:true} ? ${3:a} : ${0};
```
####p-?:
```php
    ${1:true} ? ${2:a} : ${0}
```
####p-t
```php
    $${1:retVal} = (${2:condition}) ? ${3:a} : ${4:b};
```
####p-C
```php
    $_COOKIE['${1:variable}']
```
####p-E
```php
    $_ENV['${1:variable}']
```
####p-F
```php
    $_FILES['${1:variable}']
```
####p-G
```php
    $_GET['${1:variable}']
```
####p-P
```php
    $_POST['${1:variable}']
```
####p-R
```php
    $_REQUEST['${1:variable}']
```
####p-S
```php
    $_SERVER['${1:variable}']
```
####p-SS
```php
    $_SESSION['${1:variable}']
```
####p-get
```php
    $_GET['${1}']
```
####p-post
```php
    $_POST['${1}']
```
####p-session
```php
    $_SESSION['${1}']
```
####p-inc
```php
    include '${1:file}';
```
####p-inc1
```php
    include_once '${1:file}';
```
####p-req
```php
    require '${1:file}';
```
####p-req1
```php
    require_once '${1:file}';
```
####p-/*
```php
    /**

     * ${0}

     */
```
####p-doc_vp
```php
    /**

     * ${1:undocumented class variable}

     *

     * @var ${2:string}

     */
```
####p-doc_v
```php
    /**

     * ${3:undocumented class variable}

     *

     * @var ${4:string}

     */

    ${1:var} $${2};
```
####p-doc_dp
```php
    /**

     * ${1:undocumented constant}

     */
```
####p-doc_d
```php
    /**

     * ${3:undocumented constant}

     */

    define(${1}, ${2});
```
####p-inheritdoc
```php
    /**

     * {@inheritdoc}

     */
```
####p-def
```php
    define('${1:VARIABLE_NAME}', ${2:'definition'});
```
####p-def?
```php
    ${1}defined('${2}')
```
####p-wh
```php
    while (${1:/* condition */}) {

        ${0}

    }
```
####p-do
```php
    do {

        ${0}

    } while (${1});
```
####p-if
```php
    if (${1}) {

        ${0}

    }
```
####p-ifn
```php
    if (!${1}) {

        ${2}

    }
```
####p-ifil
```php
    <?php if (${1}): ?>

        ${0}

    <?php endif; ?>
```
####p-ife
```php
    if (${1}) {

        ${2}

    } else {

        ${3}

    }

    ${0}
```
####p-ifeil
```php
    <?php if (${1}): ?>

        ${2}

    <?php else: ?>

        ${3}

    <?php endif; ?>

    ${0}
```
####p-el
```php
    else {

        ${0}

    }
```
####p-eif
```php
    elseif (${1}) {

        ${0}

    }
```
####p-switch
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
####p-case
```php
    case '${1:value}':

        ${2}

        break;
```
####p-for
```php
    for ($${2:i} = 0; $$2 < ${1:count}; $$2${3:++}) {

        ${0}

    }
```
####p-foreach
```php
    foreach ($${1:variable} as $${2:value}) {

        ${0}

    }
```
####p-foreachil
```php
    <?php foreach ($${1:variable} as $${2:value}): ?>

        ${0}

    <?php endforeach; ?>
```
####p-foreachk
```php
    foreach ($${1:variable} as $${2:key} => $${3:value}) {

        ${0}

    }
```
####p-foreachkil
```php
    <?php foreach ($${1:variable} as $${2:key} => $${3:value}): ?>

        ${0:<!-- html... -->}

    <?php endforeach; ?>
```
####p-array
```php
    $${1:arrayName} = ['${2}' => ${3}];
```
####p-try
```php
    try {

        ${0}

    } catch (${1:Exception} $e) {

    }
```
####p-lambda
```php
    ${1:static }function (${2:args}) use (${3:&$x, $y /*put vars in scope (closure) */}) {

        ${0}

    };
```
####p-pd
```php
    echo '<pre>'; var_dump(${0}); echo '</pre>';
```
####p-pdd
```php
    echo '<pre>'; var_dump(${1}); echo '</pre>'; die(${0:});
```
####p-vd
```php
    var_dump(${0});
```
####p-vdd
```php
    var_dump(${1}); die(${0:});
```
####p-pr
```php
    print_r(${0});
```
####p-prs
```php
    print_r(${0}, 1);
```
####p-vdf
```php
    error_log(print_r($${1:foo}, true), 3, '${2:/tmp/debug.log}');
```
####p-http_redirect
```php
    header ("HTTP/1.1 301 Moved Permanently");

    header ("Location: ".URL);

    exit();
```
####p-log
```php
    error_log(var_export(${1}, true));
```
####p-var
```php
    var_export(${1});
```
####p-ve
```php
    echo '<pre>' . var_export(${1}, 1) . '</pre>';
```
####p-pc
```php
    var_export($1);$0
```
####p-ags
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
####p-rett
```php
    return true;
```
####p-retf
```php
    return false;
```
####p-am
```php
    $${1:foo} = array_map(function($${2:v}) {

        ${0}

        return $$2;

    }, $$1);
```
####p-aw
```php
    array_walk($${1:foo}, function(&$${2:v}, $${3:k}) {

        $$2 = ${0};

    });
```
####p-static_var
```php
    static $${1} = null;

    if (is_null($$1)){

        $$1 = ${2};

    }
```
####p-CSVWriter
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
####p-CSVIterator
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
####p-ase
```php
    $this->assertEquals(${1:expected}, ${2:actual});
```
####p-asne
```php
    $this->assertNotEquals(${1:expected}, ${2:actual});
```
####p-asf
```php
    $this->assertFalse(${1});
```
####p-ast
```php
    $this->assertTrue(${1});
```
####p-asfex
```php
    $this->assertFileExists(${1:'path/to/file'});
```
####p-asfnex
```php
    $this->assertFileNotExists(${1:'path/to/file'});
```
####p-ascon
```php
    $this->assertContains(${1:$needle}, ${2:$haystack});
```
####p-ashk
```php
    $this->assertArrayHasKey(${1:$key}, ${2:$array});
```
####p-asnhk
```php
    this->assertArrayNotHasKey(${1:$key}, ${2:$array});
```
####p-ascha
```php
    $this->assertClassHasAttribute(${1:$attributeName}, '${2:$className}');
```
####p-asi
```php
    $this->assertInstanceOf(${1:expected}, ${2:actual});
```
####p-test
```php
    public function test${1}()

    {

        ${0}

    }
```
####p-setup
```php
    protected function setUp()

    {

        ${0}

    }
```
####p-teardown
```php
    protected function tearDown()

    {

        ${0}

    }
```
####p-exp
```php
    expects($this->${1:once}())

        ->method('${2}')

        ->with($this->equalTo(${3})${4})

        ->will($this->returnValue(${5}));
```
####p-testcmt
```php
    /**

    * @group ${1}

    */
```
####p-fail
```php
    $this->fail(${1});
```
####p-marki
```php
    $this->markTestIncomplete(${1});
```
####p-marks
```php
    $this->markTestSkipped(${1});
```
####p-te
```php
    throw new ${1:Exception}("${2:Error Processing Request}");
```
####p-fpc
```php
    file_put_contents(${1:file}, ${2:content}${3:, FILE_APPEND});$0
```
####p-sr
```php
    str_replace(${1:search}, ${2:replace}, ${3:subject})$0
```
####p-ia
```php
    in_array(${1:needle}, ${2:haystack})$0
```
####p-is
```php
    isset(${1:var})$0
```
####p-isa
```php
    isset($${1:array}[${2:key}])$0
```
####p-in
```php
    is_null($${1:var})$0
```
####p-fe
```php
    file_exists(${1:file})$0
```
