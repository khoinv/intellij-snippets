####js-sim
```cs
    ${1:public }static int Main(string[] args) {

        ${0}

        return 0;

    }
```
####js-simc
```cs
    public class Application {

        ${1:public }static int Main(string[] args) {

            ${0}

            return 0;

        }

    }
```
####js-svm
```cs
    ${1:public }static void Main(string[] args) {

        ${0}

    }
```
####js-if
```cs
    if (${1:true}) {

        ${0}

    }
```
####js-el
```cs
    else {

        ${0}

    }
```
####js-ifs
```cs
    if (${1})

        ${0}
```
####js-t
```cs
    ${1} ? ${2} : ${0}
```
####js-?
```cs
    ${1} ? ${2} : ${0}
```
####js-do
```cs
    do {

        ${0}

    } while (${1:true});
```
####js-wh
```cs
    while (${1:true}) {

        ${0}

    }
```
####js-for
```cs
    for (int ${1:i} = 0; $1 < ${2:count}; $1${3:++}) {

        ${0}

    }
```
####js-forr
```cs
    for (int ${1:i} = ${2:length}; $1 >= 0; $1--) {

        ${0}

    }
```
####js-fore
```cs
    foreach (${1:var} ${2:entry} in ${3}) {

        ${0}

    }
```
####js-foreach
```cs
    foreach (${1:var} ${2:entry} in ${3}) {

        ${0}

    }
```
####js-each
```cs
    foreach (${1:var} ${2:entry} in ${3}) {

        ${0}

    }
```
####js-interface
```cs
    public interface ${1:`vim_snippets#Filename()`} {

        ${0}

    }
```
####js-if+
```cs
    public interface ${1:`vim_snippets#Filename()`} {

        ${0}

    }
```
####js-class
```cs
    public class ${1:`vim_snippets#Filename()`} {

        ${0}

    }
```
####js-cls
```cs
    ${2:public} class ${1:`vim_snippets#Filename()`} {

        ${0}

    }
```
####js-cls+
```cs
    public class ${1:`vim_snippets#Filename()`} {

        ${0}

    }
```
####js-cls+^
```cs
    public static class ${1:`vim_snippets#Filename()`} {

        ${0}

    }
```
####js-cls&
```cs
    internal class ${1:`vim_snippets#Filename()`} {

        ${0}

    }
```
####js-cls&^
```cs
    internal static class ${1:`vim_snippets#Filename()`} {

        ${0}

    }
```
####js-cls|
```cs
    protected class ${1:`vim_snippets#Filename()`} {

        ${0}

    }
```
####js-cls|%
```cs
    protected abstract class ${1:`vim_snippets#Filename()`} {

        ${0}

    }
```
####js-ctor
```cs
    public ${1:`vim_snippets#Filename()`}() {

        ${0}

    }
```
####js-prop
```cs
    ${1:public} ${2:int} ${3} { get; set; }
```
####js-p
```cs
    ${1:public} ${2:int} ${3} { get; set; }
```
####js-p+
```cs
    public ${1:int} ${2} { get; set; }
```
####js-p+&
```cs
    public ${1:int} ${2} { get; internal set; }
```
####js-p+|
```cs
    public ${1:int} ${2} { get; protected set; }
```
####js-p+-
```cs
    public ${1:int} ${2} { get; private set; }
```
####js-p&
```cs
    internal ${1:int} ${2} { get; set; }
```
####js-p&|
```cs
    internal ${1:int} ${2} { get; protected set; }
```
####js-p&-
```cs
    internal ${1:int} ${2} { get; private set; }
```
####js-p|
```cs
    protected ${1:int} ${2} { get; set; }
```
####js-p|-
```cs
    protected ${1:int} ${2} { get; private set; }
```
####js-p-
```cs
    private ${1:int} ${2} { get; set; }
```
####js-pi
```cs
    ${1:public} int ${2} { get; set; }
```
####js-pi+
```cs
    public int ${1} { get; set; }
```
####js-pi+&
```cs
    public int ${1} { get; internal set; }
```
####js-pi+|
```cs
    public int ${1} { get; protected set; }
```
####js-pi+-
```cs
    public int ${1} { get; private set; }
```
####js-pi&
```cs
    internal int ${1} { get; set; }
```
####js-pi&|
```cs
    internal int ${1} { get; protected set; }
```
####js-pi&-
```cs
    internal int ${1} { get; private set; }
```
####js-pi|
```cs
    protected int ${1} { get; set; }
```
####js-pi|-
```cs
    protected int ${1} { get; private set; }
```
####js-pi-
```cs
    private int ${1} { get; set; }
```
####js-pb
```cs
    ${1:public} bool ${2} { get; set; }
```
####js-pb+
```cs
    public bool ${1} { get; set; }
```
####js-pb+&
```cs
    public bool ${1} { get; internal set; }
```
####js-pb+|
```cs
    public bool ${1} { get; protected set; }
```
####js-pb+-
```cs
    public bool ${1} { get; private set; }
```
####js-pb&
```cs
    internal bool ${1} { get; set; }
```
####js-pb&|
```cs
    internal bool ${1} { get; protected set; }
```
####js-pb&-
```cs
    internal bool ${1} { get; private set; }
```
####js-pb|
```cs
    protected bool ${1} { get; set; }
```
####js-pb|-
```cs
    protected bool ${1} { get; private set; }
```
####js-pb-
```cs
    private bool ${1} { get; set; }
```
####js-ps
```cs
    ${1:public} string ${2} { get; set; }
```
####js-ps+
```cs
    public string ${1} { get; set; }
```
####js-ps+&
```cs
    public string ${1} { get; internal set; }
```
####js-ps+|
```cs
    public string ${1} { get; protected set; }
```
####js-ps+-
```cs
    public string ${1} { get; private set; }
```
####js-ps&
```cs
    internal string ${1} { get; set; }
```
####js-ps&|
```cs
    internal string ${1} { get; protected set; }
```
####js-ps&-
```cs
    internal string ${1} { get; private set; }
```
####js-ps|
```cs
    protected string ${1} { get; set; }
```
####js-ps|-
```cs
    protected string ${1} { get; private set; }
```
####js-ps-
```cs
    private string ${1} { get; set; }
```
####js-m
```cs
    ${1:public} ${2:void} ${3}(${4}) {

        ${0}

    }
```
####js-m+
```cs
    public ${1:void} ${2}(${3}) {

        ${0}

    }
```
####js-m&
```cs
    internal ${1:void} ${2}(${3}) {

        ${0}

    }
```
####js-m|
```cs
    protected ${1:void} ${2}(${3}) {

        ${0}

    }
```
####js-m-
```cs
    private ${1:void} ${2}(${3}) {

        ${0}

    }
```
####js-mi
```cs
    ${1:public} int ${2}(${3}) {

        ${0:return 0;}

    }
```
####js-mi+
```cs
    public int ${1}(${2}) {

        ${0:return 0;}

    }
```
####js-mi&
```cs
    internal int ${1}(${2}) {

        ${0:return 0;}

    }
```
####js-mi|
```cs
    protected int ${1}(${2}) {

        ${0:return 0;}

    }
```
####js-mi-
```cs
    private int ${1}(${2}) {

        ${0:return 0;}

    }
```
####js-mb
```cs
    ${1:public} bool ${2}(${3}) {

        ${0:return false;}

    }
```
####js-mb+
```cs
    public bool ${1}(${2}) {

        ${0:return false;}

    }
```
####js-mb&
```cs
    internal bool ${1}(${2}) {

        ${0:return false;}

    }
```
####js-mb|
```cs
    protected bool ${1}(${2}) {

        ${0:return false;}

    }
```
####js-mb-
```cs
    private bool ${1}(${2}) {

        ${0:return false;}

    }
```
####js-ms
```cs
    ${1:public} string ${2}(${3}) {

        ${0:return "";}

    }
```
####js-ms+
```cs
    public string ${1}(${2}) {

        ${0:return "";}

    }
```
####js-ms&
```cs
    internal string ${1}(${2}) {

        ${0:return "";}

    }
```
####js-ms|
```cs
    protected string ${1:}(${2:}) {

        ${0:return "";}

    }
```
####js-ms-
```cs
    private string ${1}(${2}) {

        ${0:return "";}

    }
```
####js-struct
```cs
    public struct ${1:`vim_snippets#Filename()`} {

        ${0}

    }
```
####js-enum
```cs
    enum ${1} {

        ${0}

    }

    
```
####js-enum+
```cs
    public enum ${1} {

        ${0}

    }
```
####js-#if
```cs
    #if

        ${0}

    #endif
```
####js-///
```cs
    /// <summary>

    /// ${0}

    /// </summary>
```
####js-<p
```cs
    <param name="${1}">${2:$1}</param>
```
####js-<ex
```cs
    <exception cref="${1:System.Exception}">${2}</exception>
```
####js-<r
```cs
    <returns>${1}</returns>{
```
####js-<s
```cs
    <see cref="${1}"/>
```
####js-<rem
```cs
    <remarks>${1}</remarks>
```
####js-<c
```cs
    <code>${1}</code>


```
####js-cw
```cs
    Console.WriteLine(${1});


```
####js-eq
```cs
    public override bool Equals(object obj) {

        if (obj == null || GetType() != obj.GetType()) {

            return false;

        }

        ${0:throw new NotImplementedException();}

        return base.Equals(obj);

    }
```
####js-exc
```cs
    public class ${1:MyException} : ${2:Exception} {

        public $1() { }

        public $1(string message) : base(message) { }

        public $1(string message, Exception inner) : base(message, inner) { }

        protected $1(

            System.Runtime.Serialization.SerializationInfo info,

            System.Runtime.Serialization.StreamingContext context)

                : base(info, context) { }

    }
```
####js-index
```cs
    public ${1:object} this[${2:int} index] {

        get { ${0} }

        set { ${0} }

    }
```
####js-inv
```cs
    EventHandler temp = ${1:MyEvent};

    if (${2:temp} != null) {

        $2();

    }
```
####js-lock
```cs
    lock (${1:this}) {

        ${0}

    }
```
####js-namespace
```cs
    namespace ${1:MyNamespace} {

        ${0}

    }
```
####js-prop
```cs
    public ${1:int} ${2:MyProperty} { get; set; }
```
####js-propf
```cs
    private ${1:int} ${2:myVar};

        public $1 ${3:MyProperty} {

            get { return $2; }

            set { $2 = value; }

        }
```
####js-propg
```cs
    public ${1:int} ${2:MyProperty} { get; private set; }
```
####js-switch
```cs
    switch (${1:switch_on}) {

        ${0}

        default:

    }
```
####js-try
```cs
    try {

            ${0}

    }

    catch (${1:System.Exception}) {

            throw;

    }
```
####js-tryf
```cs
    try {

        ${0}

    }

    finally {

        ${1}

    }
```
