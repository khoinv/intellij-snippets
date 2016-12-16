####d3-iti
```javascript
it('${1:description}', inject(function($2) {

    $0

}));

endsnippet


```
####d3-befi
```javascript
beforeEach(inject(function($1) {

    $0

}));

endsnippet


```
####d3-aconf
```javascript
config(function($1) {

    $0

});

endsnippet


```
####d3-acont
```javascript
controller('${1:name}', [${2}function(${2/('|")([A-Z_$]+)?\1?((, ?)$)?/$2(?3::$4)/ig}) {

    $0

}]);

endsnippet


```
####d3-aconts
```javascript
controller('${1:name}', [${2:'$scope', }function(${2/('|")([A-Z_$]+)?\1?((, ?)$)?/$2(?3::$4)/ig}) {

    $0

}]);

endsnippet


```
####d3-adir
```javascript
directive('${1}', [${2}function(${2/('|")([A-Z_$]+)?\1?((, ?)$)?/$2(?3::$4)/ig}) {

    return {

        restrict: '${3:EA}',

        link: function(scope, element, attrs) {

            ${0}

        }

    };

}]);

endsnippet


```
####d3-adirs
```javascript
directive('${1}', [${2:'$scope', }function(${2/('|")([A-Z_$]+)?\1?((, ?)$)?/$2(?3::$4)/ig}) {

    return {

        restrict: '${3:EA}',

        link: function(scope, element, attrs) {

            ${0}

        }

    };

}]);

endsnippet


```
####d3-afact
```javascript
factory('${1:name}', [${2}function(${2/('|")([A-Z_$]+)?\1?((, ?)$)?/$2(?3::$4)/ig}) {

    $0

}]);

endsnippet


```
####d3-afacts
```javascript
factory('${1:name}', [${2:'$scope', }function(${2/('|")([A-Z_$]+)?\1?((, ?)$)?/$2(?3::$4)/ig}) {

    $0

}]);

endsnippet


```
####d3-aserv
```javascript
service('${1:name}', [${2}function(${2/('|")([A-Z_$]+)?\1?((, ?)$)?/$2(?3::$4)/ig}) {

    $0

}]);

endsnippet


```
