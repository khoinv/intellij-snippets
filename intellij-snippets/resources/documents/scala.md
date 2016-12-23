####s-if
```scala
    if (${1})

        ${0}
```
####s-ifn
```scala
    if (!${1})

        ${0}
```
####s-ife
```scala
    if (${1})

        ${2}

    else

        ${0}
```
####s-ifelif
```scala
    if (${1})

        ${2}

    else if (${3})

        ${0}
```
####s-eif
```scala
    else if (${3})

        ${0}
```
####s-wh
```scala
    while (${1:obj}) {

        ${0}

    }
```
####s-for
```scala
    for (${1:item} <- ${2:obj}) {

        ${0}

    }
```
####s-fori
```scala
    for (${1:i} <- ${2:0} to ${3:obj}.length) {

        ${0}

    }
```
####s-fory
```scala
    for {

        ${1:item} <- ${2:obj}

    } yield ${0}
```
####s-try
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
####s-match
```scala
    ${1: obj} match {

        case ${2:e} => ${3}

        case _ => ${0}

    }
```
####s-case
```scala
    case ${1:value} => ${0}
```
####s-arg
```scala
    ${1:a}: ${2:T}${0:, arg}
```
####s-args
```scala
    ${1:args}: ${0:T}*
```
####s-def
```scala
    def ${1:name}(${2:arg}) = ${0:}
```
####s-prdef
```scala
    private def ${1:name}(${2:arg}) = ${0:}
```
####s-ovdef
```scala
    override def ${1:name}(${2:arg}) = ${0:}
```
####s-fcf
```scala
    (${1:a}: ${2:T}) => $1 ${0}
```
####s-=>
```scala
    ${1:name} => ${0}
```
####s-rec
```scala
    def ${1:name}(${0:arg}) =

        if($2) $2

        else $1($2)
```
####s-crdef
```scala
    def ${1:name}(${2:arg})(${3:arg}) = ${0:}
```
####s-main
```scala
    def main(args: Array[String]):${1:T} = ${0:}
```
####s-T
```scala
    dbl
```
####s-T
```scala
    int
```
####s-T
```scala
    lng
```
####s-T
```scala
    chr
```
####s-T
```scala
    str
```
####s-T
```scala
    arr
```
####s-T
```scala
    buf
```
####s-T
```scala
    list
```
####s-T
```scala
    tpl
```
####s-T
```scala
    set
```
####s-T
```scala
    map
```
####s-T
```scala
    hset
```
####s-T
```scala
    hmap
```
####s-T
```scala
    bool
```
####s-bool
```scala
    Boolean
```
####s-anyr
```scala
    AnyRef
```
####s-dbl
```scala
    Double
```
####s-int
```scala
    Int
```
####s-str
```scala
    String
```
####s-chr
```scala
    Char
```
####s-lng
```scala
    Long
```
####s-arr
```scala
    Array${1:[T]}${0:()}
```
####s-buf
```scala
    Buffer${1:[T]}${0:()}
```
####s-list
```scala
    List${1:[T]}${0:()}
```
####s-tpl
```scala
    Tuple${1:2}[${2:T},${0:T}]
```
####s-set
```scala
    Set${1:[T]}${0:()}
```
####s-hset
```scala
    HashSet${1:[T]}${0:()}
```
####s-mhset
```scala
    mutable.HashSet${1:[T]}${0:()}
```
####s-keyval
```scala
    ${1:key}->${2:val}${0:, keyval}
```
####s-map
```scala
    Map[${1:T},${2:T}]${0:(keyval)}
```
####s-hmap
```scala
    HashMap[${1:T},${2:T}]${0:(keyval)}
```
####s-mmap
```scala
    mutable.Map[${1:T},${2:T}]${0:(keyval)}
```
####s-mhmap
```scala
    mutable.HashMap[${1:T},${2:T}]${0:(keyval)}
```
####s-as
```scala
    ${1:name}.asInstanceOf[${2:T}]
```
####s-is
```scala
    ${1:name}.isInstanceOf[${2:T}]


```
####s-(a
```scala
    (${1:a} => ${0})
```
####s-{(
```scala
    {(${1:a},${2:b}) =>

        ${0}

    }
```
####s-filter
```scala
    ${0:name}.filter (a
```
####s-mapf
```scala
    ${0:name}.map (a
```
####s-flatmap
```scala
    ${1:name}.flatMap${0:[T]}(a
```
####s-fldl
```scala
    ${1:name}.foldLeft(${0:first}) {(
```
####s-fldr
```scala
    ${1:name}.foldRight(${0:first}) {(
```
####s-/:
```scala
    (${1:first}/:${2:name})(${0})
```
####s-:\
```scala
    (${1:first}:\${2:name})(${0})
```
####s-redl
```scala
    ${1:name}.reduceLeft[${0:T}] {(
```
####s-redr
```scala
    ${1:name}.reduceRight[${0:T}] {(
```
####s-zipwi
```scala
    ${0:name}.view.zipWithIndex
```
####s-spl
```scala
    ${1:name}.split("${0:,}")
```
####s-val
```scala
    val ${1:name}${2:: T} = ${0:value}
```
####s-var
```scala
    var ${1:name}${2:: T} = ${0:value}
```
####s-extends
```scala
    extends ${0:what}
```
####s-with
```scala
    with ${1:what}${0: with}
```
####s-athis
```scala
    def this(arg) = this(arg)
```
####s-abstract
```scala
    abstract class ${1:name}${2:(arg)}${3: extends }${4: with} {

        ${5:override def toString = "$1"}

        ${0}

    }
```
####s-class
```scala
    class ${1:name}${2:(arg)}${3: extends }${4: with} {

        ${5:override def toString = "$1"}

        ${0}

    }
```
####s-object
```scala
    object ${1:name}${2:(arg)}${3: extends }${4: with} ${0:}
```
####s-trait
```scala
    trait ${1:name}${2: extends }${3: with} {

        ${0:}

    }
```
####s-ordered
```scala
    class ${1:name}${2:(arg)} extends Ordered[$1] ${3: with} {

        ${4:override def toString = "$1"}

        def compare(that: $1) = ${5:this - that}

        ${0}

    }
```
####s-casecl
```scala
    case class ${1:name}${2:(arg)}${3: extends }${4: with} ${0:}
```
####s-scalatest
```scala
    ${1:import org.scalatest.Suite}

    ${0:import org.scalatest.FunSuite}
```
####s-assert
```scala
    assert(${1:a} === ${0:b})
```
####s-ensuring
```scala
    ifel ensuring(${1:a}==${0:b})
```
####s-expect
```scala
    expect(${1:what}) {

        ${0}

    }
```
####s-intercept
```scala
    intercept[${1:IllegalArgumentException}] {

        ${0}

    }
```
####s-test
```scala
    test("${1:description}") {

        ${0}

    }
```
####s-suite
```scala
    class ${0:name} extends Suite {

        def test() {

    }
```
####s-fsuite
```scala
    class ${1:name} extends FunSuite {

        test("${0:description}") {

    }
```
####s-webproject
```scala
    import sbt._



    class ${1:Name}(info: ProjectInfo) extends DefaultWebProject(info) {

        val liftVersion = "${0:2.3}"



        override def libraryDependencies = Set(



        ) ++ super.libraryDependencies



        val snapshots = ScalaToolsSnapshots

    }
```
####s-liftjar
```scala
    "net.liftweb" %% "${0:lib}" % liftVersion % "compile->default",
```
####s-jettyjar
```scala
    "org.mortbay.jetty" % "jetty" % "${0:version}" % "test->default",
```
####s-liftimports
```scala
    import _root_.net.liftweb.http._

    import S._

    import _root_.net.liftweb.util._

    import Helpers._

    import _root_.scala.xml._
```
