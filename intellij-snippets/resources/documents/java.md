####jv-po
```java
    protected ${0}
```
####jv-pu
```java
    public ${0}
```
####jv-pr
```java
    private ${0}
```
####jv-before
```java
    @Before

    static void ${1:intercept}(${2:args}) { ${0} }
```
####jv-mm
```java
    @ManyToMany

    ${0}
```
####jv-mo
```java
    @ManyToOne

    ${0}
```
####jv-om
```java
    @OneToMany${1:(cascade=CascadeType.ALL)}

    ${0}
```
####jv-oo
```java
    @OneToOne

    ${1}
```
####jv-im
```java
    import ${0}
```
####jv-j.b
```java
    java.beans.
```
####jv-j.i
```java
    java.io.
```
####jv-j.m
```java
    java.math.
```
####jv-j.n
```java
    java.net.
```
####jv-j.u
```java
    java.util.
```
####jv-cl
```java
    class ${1:`vim_snippets#Filename("$1", "untitled")`} ${0}
```
####jv-pcl
```java
    public class ${1:`vim_snippets#Filename("$1", "untitled")`} ${0}
```
####jv-in
```java
    interface ${1:`vim_snippets#Filename("$1", "untitled")`} ${2:extends Parent}
```
####jv-tc
```java
    public class ${1:`vim_snippets#Filename("$1")`} extends ${0:TestCase}
```
####jv-ext
```java
    extends ${0}
```
####jv-imp
```java
    implements ${0}
```
####jv-/*
```java
    /*

     * ${0}

     */
```
####jv-co
```java
    static public final ${1:String} ${2:var} = ${3};
```
####jv-cos
```java
    static public final String ${1:var} = "${2}";
```
####jv-case
```java
    case ${1}:

        ${0}
```
####jv-def
```java
    default:

        ${0}
```
####jv-el
```java
    else
```
####jv-eif
```java
    else if (${1}) ${0}
```
####jv-if
```java
    if (${1}) ${0}
```
####jv-sw
```java
    switch (${1}) {

        ${0}

    }
```
####jv-m
```java
    ${1:void} ${2:method}(${3}) ${4:throws }
```
####jv-v
```java
    ${1:String} ${2:var}${3: = null}${4};
```
####jv-d.al
```java
    List<${1:Object}> ${2:list} = new ArrayList<$1>();${0}
```
####jv-d.hm
```java
    Map<${1:Object}, ${2:Object}> ${3:map} = new HashMap<$1, $2>();${0}
```
####jv-d.hs
```java
    Set<${1:Object}> ${2:set} = new HashSet<$1>();${0}
```
####jv-d.st
```java
    Stack<${1:Object}> ${2:stack} = new Stack<$1>();${0}
```
####jv-singlet
```java
    private static class Holder {

        private static final ${1:`vim_snippets#Filename("$1")`} INSTANCE = new $1();

    }



    private $1() { }



    public static $1 getInstance() {

        return Holder.INSTANCE;

    }
```
####jv-ab
```java
    abstract ${0}
```
####jv-fi
```java
    final ${0}
```
####jv-st
```java
    static ${0}
```
####jv-sy
```java
    synchronized ${0}
```
####jv-err
```java
    System.err.print("${0:Message}");
```
####jv-errf
```java
    System.err.printf("${1:Message}", ${0:exception});
```
####jv-errln
```java
    System.err.println("${0:Message}");
```
####jv-as
```java
    assert ${1:test} : "${2:Failure message}";
```
####jv-ae
```java
    assertEquals("${1:Failure message}", ${2:expected}, ${3:actual});
```
####jv-aae
```java
    assertArrayEquals("${1:Failure message}", ${2:expecteds}, ${3:actuals});
```
####jv-af
```java
    assertFalse("${1:Failure message}", ${2:condition});
```
####jv-at
```java
    assertTrue("${1:Failure message}", ${2:condition});
```
####jv-an
```java
    assertNull("${1:Failure message}", ${2:object});
```
####jv-ann
```java
    assertNotNull("${1:Failure message}", ${2:object});
```
####jv-ass
```java
    assertSame("${1:Failure message}", ${2:expected}, ${3:actual});
```
####jv-asns
```java
    assertNotSame("${1:Failure message}", ${2:expected}, ${3:actual});
```
####jv-fa
```java
    fail("${1:Failure message}");
```
####jv-ca
```java
    catch(${1:Exception} ${2:e}) ${0}
```
####jv-thr
```java
    throw ${0}
```
####jv-ths
```java
    throws ${0}
```
####jv-try
```java
    try {

        ${0}

    } catch(${1:Exception} ${2:e}) {

    }
```
####jv-tryf
```java
    try {

        ${0}

    } catch(${1:Exception} ${2:e}) {

    } finally {

    }
```
####jv-findall
```java
    List<${1:listName}> ${2:items} = ${1}.findAll();
```
####jv-findbyid
```java
    ${1:var} ${2:item} = ${1}.findById(${3});
```
####jv-/**
```java
    /**

     * ${0}

     */
```
####jv-@au
```java
    @author `system("grep \`id -un\` /etc/passwd | cut -d \":\" -f5 | cut -d \",\" -f1")`
```
####jv-@br
```java
    @brief ${0:Description}
```
####jv-@fi
```java
    @file ${0:`vim_snippets#Filename("$1")`}.java
```
####jv-@pa
```java
    @param ${0:param}
```
####jv-@re
```java
    @return ${0:param}
```
####jv-debug
```java
    Logger.debug(${1:param});
```
####jv-error
```java
    Logger.error(${1:param});
```
####jv-info
```java
    Logger.info(${1:param});
```
####jv-warn
```java
    Logger.warn(${1:param});
```
####jv-enfor
```java
    for (${1} : ${2}) ${0}
```
####jv-for
```java
    for (${1}; ${2}; ${3}) ${0}
```
####jv-wh
```java
    while (${1}) ${0}
```
####jv-psvm
```java
    public static void main (String[] args) {

        ${0}

    }
```
####jv-main
```java
    public static void main (String[] args) {

        ${0}

    }
```
####jv-sout
```java
    System.out.println(${0});
```
####jv-serr
```java
    System.err.println(${0});
```
####jv-print
```java
    System.out.print("${0:Message}");
```
####jv-printf
```java
    System.out.printf("${1:Message}", ${0:args});
```
####jv-println
```java
    System.out.println(${0});
```
####jv-printlna
```java
    System.out.println(Arrays.toString(${0}));
```
####jv-ren
```java
    render(${1:param});
```
####jv-rena
```java
    renderArgs.put("${1}", ${2});
```
####jv-renb
```java
    renderBinary(${1:param});
```
####jv-renj
```java
    renderJSON(${1:param});
```
####jv-renx
```java
    renderXml(${1:param});
```
####jv-set
```java
    ${1:public} void set${3:}(${2:String} ${0:}){

        this.$4 = $4;

    }
```
####jv-get
```java
    ${1:public} ${2:String} get${3:}(){

        return this.${0:};

    }
```
####jv-re
```java
    return ${0}
```
####jv-br
```java
    break;
```
####jv-t
```java
    public void test${1:Name}() throws Exception {

        ${0}

    }
```
####jv-test
```java
    @Test

    public void test${1:Name}() throws Exception {

        ${0}

    }
```
####jv-Sc
```java
    Scanner
```
####jv-action
```java
    public static void ${1:index}(${2:args}) { ${0} }
```
####jv-rnf
```java
    notFound(${1:param});
```
####jv-rnfin
```java
    notFoundIfNull(${1:param});
```
####jv-rr
```java
    redirect(${1:param});
```
####jv-ru
```java
    unauthorized(${1:param});
```
