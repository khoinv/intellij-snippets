####nd-#!
```javascript
    #!/usr/bin/env node
```
####nd-ex
```javascript
    module.exports = ${1};
```
####nd-re
```javascript
    ${1:const} ${2} = require('${3:module_name}');
```
####nd-on
```javascript
    on('${1:event_name}', function(${2:stream}) {

      ${3}

    });
```
####nd-emit
```javascript
    emit('${1:event_name}', ${2:args});
```
####nd-once
```javascript
    once('${1:event_name}', function(${2:stream}) {

      ${3}

    });
```
####nd-http
```javascript
    http.createServer(${1:handler}).listen(${2:port_number});
```
####nd-net
```javascript
    net.createServer(function(${1:socket}){

        ${1}.on('data', function('data'){

          ${2}

        ]});

        ${1}.on('end', function(){

          ${3}

        });

    }).listen(${4:8124});
```
####nd-pipe
```javascript
    pipe(${1:stream})${2}
```
####nd-eget
```javascript
    ${1:app}.get('${2:route}', ${3:handler});
```
####nd-epost
```javascript
    ${1:app}.post('${2:route}', ${3:handler});
```
####nd-eput
```javascript
    ${1:app}.put('${2:route}', ${3:handler});
```
####nd-edel
```javascript
    ${1:app}.delete('${2:route}', ${3:handler});
```
####nd-stdin
```javascript
    process.stdin
```
####nd-stdout
```javascript
    process.stdout
```
