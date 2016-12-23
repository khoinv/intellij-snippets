####js6-const
```javascript
    const ${1} = ${0};
```
####js6-let
```javascript
    let ${1} = ${0};
```
####js6-im
```javascript
    import ${1} from '${2:$1}';
```
####js6-imas
```javascript
    import * as ${1} from '${2:$1}';
```
####js6-imm
```javascript
    import { ${1} } from '${2}';
```
####js6-cla
```javascript
    class ${1} {

        ${0}

    }
```
####js6-clax
```javascript
    class ${1} extends ${2} {

        ${0}

    }
```
####js6-clac
```javascript
    class ${1} {

        constructor(${2}) {

            ${0}

        }

    }
```
####js6-foro
```javascript
    for (const ${1:prop} of ${2:object}) {

        ${0:$1}

    }
```
####js6-fun*
```javascript
    function* ${1:function_name}(${2}) {

        ${0}

    }
```
####js6-c=>
```javascript
    const ${1:function_name} = (${2}) => {

        ${0}

    }
```
####js6-caf
```javascript
    const ${1:function_name} = (${2}) => {

        ${0}

    }
```
####js6-=>
```javascript
    (${1}) => {

        ${0}

    }
```
####js6-af
```javascript
    (${1}) => {

        ${0}

    }
```
####js6-sym
```javascript
    const ${1} = Symbol('${0}');
```
####js6-ed
```javascript
    export default ${0}
```
