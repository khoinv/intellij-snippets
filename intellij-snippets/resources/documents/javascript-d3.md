####d3-.attr
```javascript
    .attr("${1}", ${2})
```
####d3-.style
```javascript
    .style("${1}", ${2})
```
####d3-axis
```javascript
    d3.svg.axis()

      .orient(${1})

      .scale(${2})
```
####d3-fd
```javascript
    function(d) { ${1} }
```
####d3-fdi
```javascript
    function(d, i) { ${1} }
```
####d3-marginconvention
```javascript
    var ${1:margin} = { top: ${2:10}, right: ${3:10}, bottom: ${4:10}, left: ${5:10} };

    var ${6:width} = ${7:970} - $1.left - $1.right;

    var ${8:height} = ${9:500} - $1.top - $1.bottom;

    

    var ${10:svg} = d3.select("${11}").append("svg")

      .attr("width", $6 + $1.left + $1.right)

      .attr("height", $8 + $1.top + $1.bottom)

        .append("g")

      .attr("transform", "translate(" + $1.left + "," + $1.top + ")")
```
####d3-nest
```javascript
    d3.nest()

      .key(${1})

      .entries(${2})
```
