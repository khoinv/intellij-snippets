####ng-iti
```javascript
it('${1:description}', inject(function($2) {

    $0

}));
```
####ng-befi
```javascript
beforeEach(inject(function($1) {

    $0

}));
```
####ng-aconf
```javascript
config(function($1) {

    $0

});
```
####ng-acont
```javascript
controller('${1:name}', [${2}function(${2/('|")([A-Z_$]+)?\1?((, ?)$)?/$2(?3::$4)/ig}) {

    $0

}]);
```
####ng-aconts
```javascript
controller('${1:name}', [${2:'$scope', }function(${2/('|")([A-Z_$]+)?\1?((, ?)$)?/$2(?3::$4)/ig}) {

    $0

}]);
```
####ng-adir
```javascript
directive('${1}', [${2}function(${2/('|")([A-Z_$]+)?\1?((, ?)$)?/$2(?3::$4)/ig}) {

    return {

        restrict: '${3:EA}',

        link: function(scope, element, attrs) {

            ${0}

        }

    };

}]);
```
####ng-adirs
```javascript
directive('${1}', [${2:'$scope', }function(${2/('|")([A-Z_$]+)?\1?((, ?)$)?/$2(?3::$4)/ig}) {

    return {

        restrict: '${3:EA}',

        link: function(scope, element, attrs) {

            ${0}

        }

    };

}]);
```
####ng-afact
```javascript
factory('${1:name}', [${2}function(${2/('|")([A-Z_$]+)?\1?((, ?)$)?/$2(?3::$4)/ig}) {

    $0

}]);
```
####ng-afacts
```javascript
factory('${1:name}', [${2:'$scope', }function(${2/('|")([A-Z_$]+)?\1?((, ?)$)?/$2(?3::$4)/ig}) {

    $0

}]);
```
####ng-aserv
```javascript
service('${1:name}', [${2}function(${2/('|")([A-Z_$]+)?\1?((, ?)$)?/$2(?3::$4)/ig}) {

    $0

}]);
```
####ng-aservs
```javascript
service('${1:name}', [${2:'$scope', }function(${2/('|")([A-Z_$]+)?\1?((, ?)$)?/$2(?3::$4)/ig}) {

    $0

}]);
```
