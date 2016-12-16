####sl-if
```scala
    if (${1})

        ${0}
```
####sl-ifn
```scala
    if (!${1})

        ${0}
```
####sl-ife
```scala
    if (${1})

        ${2}

    else

        ${0}
```
####sl-ifelif
```scala
    if (${1})

        ${2}

    else if (${3})

        ${0}
```
####sl-eif
```scala
    else if (${3})

        ${0}
```
####sl-wh
```scala
    while (${1:obj}) {

        ${0}

    }
```
####sl-for
```scala
    for (${1:item} <- ${2:obj}) {

        ${0}

    }
```
####sl-fori
```scala
    for (${1:i} <- ${2:0} to ${3:obj}.length) {

        ${0}

    }
```
####sl-fory
```scala
    for {

        ${1:item} <- ${2:obj}

    } yield ${0}
```
####sl-try
```scala
    try {

        ${1}

    } catch {

        case e: FileNotFoundException => ${2}

        case e: IOException => ${3}

    } finally {

        ${0}

    }
```
####sl-match
```scala
    ${1: obj} match {

        case ${2:e} => ${3}

        case _ => ${0}

    }
```
####sl-case
```scala
    case ${1:value} => ${0}
```
####sl-arg
```scala
    ${1:a}: ${2:T}${0:, arg}
```
####sl-args
```scala
    ${1:args}: ${0:T}*
```
####sl-def
```scala
    def ${1:name}(${2:arg}) = ${0:}
```
####sl-prdef
```scala
    private def ${1:name}(${2:arg}) = ${0:}
```
####sl-ovdef
```scala
    override def ${1:name}(${2:arg}) = ${0:}
```
####sl-fcf
```scala
    (${1:a}: ${2:T}) => $1 ${0}
```
####sl-=>
```scala
    ${1:name} => ${0}
```
####sl-rec
```scala
    def ${1:name}(${0:arg}) =

        if($2) $2

        else $1($2)
```
####sl-crdef
```scala
    def ${1:name}(${2:arg})(${3:arg}) = ${0:}
```
####sl-main
```scala
    def main(args: Array[String]):${1:T} = ${0:}
```
####sl-T
```scala
    dbl
```
####sl-T
```scala
    int
```
####sl-T
```scala
    lng
```
####sl-T
```scala
    chr
```
####sl-T
```scala
    str
```
####sl-T
```scala
    arr
```
####sl-T
```scala
    buf
```
####sl-T
```scala
    list
```
####sl-T
```scala
    tpl
```
####sl-T
```scala
    set
```
####sl-T
```scala
    map
```
####sl-T
```scala
    hset
```
####sl-T
```scala
    hmap
```
####sl-T
```scala
    bool
```
####sl-bool
```scala
    Boolean
```
####sl-anyr
```scala
    AnyRef
```
####sl-dbl
```scala
    Double
```
####sl-int
```scala
    Int
```
####sl-str
```scala
    String
```
####sl-chr
```scala
    Char
```
####sl-lng
```scala
    Long
```
####sl-arr
```scala
    Array${1:[T]}${0:()}
```
####sl-buf
```scala
    Buffer${1:[T]}${0:()}
```
####sl-list
```scala
    List${1:[T]}${0:()}
```
####sl-tpl
```scala
    Tuple${1:2}[${2:T},${0:T}]
```
####sl-set
```scala
    Set${1:[T]}${0:()}
```
####sl-hset
```scala
    HashSet${1:[T]}${0:()}
```
####sl-mhset
```scala
    mutable.HashSet${1:[T]}${0:()}
```
####sl-keyval
```scala
    ${1:key}->${2:val}${0:, keyval}
```
####sl-map
```scala
    Map[${1:T},${2:T}]${0:(keyval)}
```
####sl-hmap
```scala
    HashMap[${1:T},${2:T}]${0:(keyval)}
```
####sl-mmap
```scala
    mutable.Map[${1:T},${2:T}]${0:(keyval)}
```
####sl-mhmap
```scala
    mutable.HashMap[${1:T},${2:T}]${0:(keyval)}
```
####sl-as
```scala
    ${1:name}.asInstanceOf[${2:T}]
```
####sl-is
```scala
    ${1:name}.isInstanceOf[${2:T}]


```
####sl-(a
```scala
    (${1:a} => ${0})
```
####sl-{(
```scala
    {(${1:a},${2:b}) =>

        ${0}

    }
```
####sl-filter
```scala
    ${0:name}.filter (a
```
####sl-mapf
```scala
    ${0:name}.map (a
```
####sl-flatmap
```scala
    ${1:name}.flatMap${0:[T]}(a
```
####sl-fldl
```scala
    ${1:name}.foldLeft(${0:first}) {(
```
####sl-fldr
```scala
    ${1:name}.foldRight(${0:first}) {(
```
####sl-/:
```scala
    (${1:first}/:${2:name})(${0})
```
####sl-:\
```scala
    (${1:first}:\${2:name})(${0})
```
####sl-redl
```scala
    ${1:name}.reduceLeft[${0:T}] {(
```
####sl-redr
```scala
    ${1:name}.reduceRight[${0:T}] {(
```
####sl-zipwi
```scala
    ${0:name}.view.zipWithIndex
```
####sl-spl
```scala
    ${1:name}.split("${0:,}")
```
####sl-val
```scala
    val ${1:name}${2:: T} = ${0:value}
```
####sl-var
```scala
    var ${1:name}${2:: T} = ${0:value}
```
####sl-extends
```scala
    extends ${0:what}
```
####sl-with
```scala
    with ${1:what}${0: with}
```
####sl-athis
```scala
    def this(arg) = this(arg)
```
####sl-abstract
```scala
    abstract class ${1:name}${2:(arg)}${3: extends }${4: with} {

        ${5:override def toString = "$1"}

        ${0}

    }
```
####sl-class
```scala
    class ${1:name}${2:(arg)}${3: extends }${4: with} {

        ${5:override def toString = "$1"}

        ${0}

    }
```
####sl-object
```scala
    object ${1:name}${2:(arg)}${3: extends }${4: with} ${0:}
```
####sl-trait
```scala
    trait ${1:name}${2: extends }${3: with} {

        ${0:}

    }
```
####sl-ordered
```scala
    class ${1:name}${2:(arg)} extends Ordered[$1] ${3: with} {

        ${4:override def toString = "$1"}

        def compare(that: $1) = ${5:this - that}

        ${0}

    }
```
####sl-casecl
```scala
    case class ${1:name}${2:(arg)}${3: extends }${4: with} ${0:}
```
####sl-scalatest
```scala
    ${1:import org.scalatest.Suite}

    ${0:import org.scalatest.FunSuite}
```
####sl-assert
```scala
    assert(${1:a} === ${0:b})
```
####sl-ensuring
```scala
    ifel ensuring(${1:a}==${0:b})
```
####sl-expect
```scala
    expect(${1:what}) {

        ${0}

    }
```
####sl-intercept
```scala
    intercept[${1:IllegalArgumentException}] {

        ${0}

    }
```
####sl-test
```scala
    test("${1:description}") {

        ${0}

    }
```
####sl-suite
```scala
    class ${0:name} extends Suite {

        def test() {

    }
```
####sl-fsuite
```scala
    class ${1:name} extends FunSuite {

        test("${0:description}") {

    }
```
####sl-webproject
```scala
    import sbt._



    class ${1:Name}(info: ProjectInfo) extends DefaultWebProject(info) {

        val liftVersion = "${0:2.3}"



        override def libraryDependencies = Set(



        ) ++ super.libraryDependencies



        val snapshots = ScalaToolsSnapshots

    }
```
####sl-liftjar
```scala
    "net.liftweb" %% "${0:lib}" % liftVersion % "compile->default",
```
####sl-jettyjar
```scala
    "org.mortbay.jetty" % "jetty" % "${0:version}" % "test->default",
```
####sl-liftimports
```scala
    import _root_.net.liftweb.http._

    import S._

    import _root_.net.liftweb.util._

    import Helpers._

    import _root_.scala.xml._
```
