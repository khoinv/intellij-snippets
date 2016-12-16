####v
```go
    ${1} := ${2}
```
####vr
```go
    var ${1:t} ${0:string}
```
####var
```go
    var ${1} ${2} = ${3}
```
####vars
```go
    var (

        ${1} ${2} = ${3}

    )
```
####ap
```go
    append(${1:slice}, ${0:value})
```
####bl
```go
    bool
```
####bt
```go
    byte
```
####br
```go
    break
```
####ch
```go
    chan ${0:int}
```
####cs
```go
    case ${1:value}:

        ${0}
```
####c
```go
    const ${1:NAME} = ${0:0}
```
####co
```go
    const (

        ${1:NAME1} = iota

        ${0:NAME2}

    )
```
####cn
```go
    continue
```
####df
```go
    defer ${0:func}()
```
####dfr
```go
    defer func() {

        if err := recover(); err != nil {

            ${0}

        }

    }()
```
####i
```go
    int
```
####im
```go
    import (

        "${1:package}"

    )
```
####in
```go
    interface{}
```
####inf
```go
    interface ${1:name} {

        ${2:/* methods */}

    }
```
####if
```go
    if ${1:/* condition */} {

        ${2}

    }
```
####ife
```go
    if ${1:/* condition */} {

        ${2}

    } else {

        ${0}

    }
```
####el
```go
    else {

        ${1}

    }
```
####ir
```go
    if err != nil {

        return err

    }

    ${0}
```
####f
```go
    false
```
####ft
```go
    fallthrough
```
####fl
```go
    float32
```
####f3
```go
    float32
```
####f6
```go
    float64
```
####ie
```go
    if ${1:/* condition */} {

        ${2}

    } else {

        ${3}

    }

    ${0}
```
####for
```go
    for ${1}{

        ${0}

    }
```
####fori
```go
    for ${2:i} := 0; $2 < ${1:count}; $2${3:++} {

        ${0}

    }
```
####forr
```go
    for ${1:e} := range ${2:collection} {

        ${0}

    }
```
####fun
```go
    func ${1:funcName}(${2}) ${3:error} {

        ${4}

    }

    ${0}
```
####fum
```go
    func (${1:receiver} ${2:type}) ${3:funcName}(${4}) ${5:error} {

        ${6}

    }

    ${0}
```
####lf
```go
    log.Printf("%${1:s}", ${2:var})
```
####lp
```go
    log.Println("${1}")
```
####mk
```go
    make(${1:[]string}, ${0:0})
```
####mp
```go
    map[${1:string}]${0:int}
```
####main
```go
    func main() {

        ${1}

    }

    ${0}
```
####nw
```go
    new(${0:type})
```
####pa
```go
    package ${1:main}
```
####pn
```go
    panic("${0:msg}")
```
####pr
```go
    fmt.Printf("%${1:s}\n", ${2:var})
```
####pl
```go
    fmt.Println("${1:s}")
```
####rn
```go
    range ${0}
```
####rt
```go
    return ${0}
```
####rs
```go
    result
```
####sl
```go
    select {

    case ${1:v1} := <-${2:chan1}

        ${3}

    default:

        ${0}

    }
```
####sr
```go
    string
```
####st
```go
    struct ${1:name} {

        ${2:/* data */}

    }

    ${0}
```
####sw
```go
    switch ${1:var} {

    case ${2:value1}:

        ${3}

    case ${4:value2}:

        ${5}

    default:

        ${0}

    }
```
####sp
```go
    fmt.Sprintf("%${1:s}", ${2:var})
```
####t
```go
    true
```
####g
```go
    go ${1:funcName}(${0})
```
####ga
```go
    go func(${1} ${2:type}) {

        ${3:/* code */}

    }(${0})
```
####test
```go
    func Test${1:name}(t *testing.T) {

        ${2}

    }

    ${0}
```
