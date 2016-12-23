####j-po
```java
    protected ${0}
```
####j-pu
```java
    public ${0}
```
####j-pr
```java
    private ${0}
```
####j-before
```java
    @Before

    static void ${1:intercept}(${2:args}) { ${0} }
```
####j-mm
```java
    @ManyToMany

    ${0}
```
####j-mo
```java
    @ManyToOne

    ${0}
```
####j-om
```java
    @OneToMany${1:(cascade=CascadeType.ALL)}

    ${0}
```
####j-oo
```java
    @OneToOne

    ${1}
```
####j-im
```java
    import ${0}
```
####j-j.b
```java
    java.beans.
```
####j-j.i
```java
    java.io.
```
####j-j.m
```java
    java.math.
```
####j-j.n
```java
    java.net.
```
####j-j.u
```java
    java.util.
```
####j-ext
```java
    extends ${0}
```
####j-imp
```java
    implements ${0}
```
####j-/*
```java
    /*

     * ${0}

     */
```
####j-co
```java
    static public final ${1:String} ${2:var} = ${3};
```
####j-cos
```java
    static public final String ${1:var} = "${2}";
```
####j-case
```java
    case ${1}:

        ${0}
```
####j-def
```java
    default:

        ${0}
```
####j-el
```java
    else
```
####j-eif
```java
    else if (${1}) ${0}
```
####j-if
```java
    if (${1}) ${0}
```
####j-sw
```java
    switch (${1}) {

        ${0}

    }
```
####j-m
```java
    ${1:void} ${2:method}(${3}) ${4:throws }
```
####j-v
```java
    ${1:String} ${2:var}${3: = null}${4};
```
####j-d.al
```java
    List<${1:Object}> ${2:list} = new ArrayList<$1>();${0}
```
####j-d.hm
```java
    Map<${1:Object}, ${2:Object}> ${3:map} = new HashMap<$1, $2>();${0}
```
####j-d.hs
```java
    Set<${1:Object}> ${2:set} = new HashSet<$1>();${0}
```
####j-d.st
```java
    Stack<${1:Object}> ${2:stack} = new Stack<$1>();${0}
```
####j-ab
```java
    abstract ${0}
```
####j-fi
```java
    final ${0}
```
####j-st
```java
    static ${0}
```
####j-sy
```java
    synchronized ${0}
```
####j-err
```java
    System.err.print("${0:Message}");
```
####j-errf
```java
    System.err.printf("${1:Message}", ${0:exception});
```
####j-errln
```java
    System.err.println("${0:Message}");
```
####j-as
```java
    assert ${1:test} : "${2:Failure message}";
```
####j-ae
```java
    assertEquals("${1:Failure message}", ${2:expected}, ${3:actual});
```
####j-aae
```java
    assertArrayEquals("${1:Failure message}", ${2:expecteds}, ${3:actuals});
```
####j-af
```java
    assertFalse("${1:Failure message}", ${2:condition});
```
####j-at
```java
    assertTrue("${1:Failure message}", ${2:condition});
```
####j-an
```java
    assertNull("${1:Failure message}", ${2:object});
```
####j-ann
```java
    assertNotNull("${1:Failure message}", ${2:object});
```
####j-ass
```java
    assertSame("${1:Failure message}", ${2:expected}, ${3:actual});
```
####j-asns
```java
    assertNotSame("${1:Failure message}", ${2:expected}, ${3:actual});
```
####j-fa
```java
    fail("${1:Failure message}");
```
####j-ca
```java
    catch(${1:Exception} ${2:e}) ${0}
```
####j-thr
```java
    throw ${0}
```
####j-ths
```java
    throws ${0}
```
####j-try
```java
    try {

        ${0}

    } catch(${1:Exception} ${2:e}) {

    }
```
####j-tryf
```java
    try {

        ${0}

    } catch(${1:Exception} ${2:e}) {

    } finally {

    }
```
####j-findall
```java
    List<${1:listName}> ${2:items} = ${1}.findAll();
```
####j-findbyid
```java
    ${1:var} ${2:item} = ${1}.findById(${3});
```
####j-/**
```java
    /**

     * ${0}

     */
```
####j-@br
```java
    @brief ${0:Description}
```
####j-@pa
```java
    @param ${0:param}
```
####j-@re
```java
    @return ${0:param}
```
####j-debug
```java
    Logger.debug(${1:param});
```
####j-error
```java
    Logger.error(${1:param});
```
####j-info
```java
    Logger.info(${1:param});
```
####j-warn
```java
    Logger.warn(${1:param});
```
####j-enfor
```java
    for (${1} : ${2}) ${0}
```
####j-for
```java
    for (${1}; ${2}; ${3}) ${0}
```
####j-wh
```java
    while (${1}) ${0}
```
####j-psvm
```java
    public static void main (String[] args) {

        ${0}

    }
```
####j-main
```java
    public static void main (String[] args) {

        ${0}

    }
```
####j-sout
```java
    System.out.println(${0});
```
####j-serr
```java
    System.err.println(${0});
```
####j-print
```java
    System.out.print("${0:Message}");
```
####j-printf
```java
    System.out.printf("${1:Message}", ${0:args});
```
####j-println
```java
    System.out.println(${0});
```
####j-printlna
```java
    System.out.println(Arrays.toString(${0}));
```
####j-ren
```java
    render(${1:param});
```
####j-rena
```java
    renderArgs.put("${1}", ${2});
```
####j-renb
```java
    renderBinary(${1:param});
```
####j-renj
```java
    renderJSON(${1:param});
```
####j-renx
```java
    renderXml(${1:param});
```
####j-set
```java
    ${1:public} void set${3:}(${2:String} ${0:}){

        this.$4 = $4;

    }
```
####j-get
```java
    ${1:public} ${2:String} get${3:}(){

        return this.${0:};

    }
```
####j-re
```java
    return ${0}
```
####j-br
```java
    break;
```
####j-t
```java
    public void test${1:Name}() throws Exception {

        ${0}

    }
```
####j-test
```java
    @Test

    public void test${1:Name}() throws Exception {

        ${0}

    }
```
####j-Sc
```java
    Scanner
```
####j-action
```java
    public static void ${1:index}(${2:args}) { ${0} }
```
####j-rnf
```java
    notFound(${1:param});
```
####j-rnfin
```java
    notFoundIfNull(${1:param});
```
####j-rr
```java
    redirect(${1:param});
```
####j-ru
```java
    unauthorized(${1:param});
```
