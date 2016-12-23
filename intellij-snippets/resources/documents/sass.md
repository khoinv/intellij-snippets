####s-$
```css
    $${1:variable}: ${0:value}
```
####s-imp
```css
    @import '${0}'
```
####s-mix
```css
    @mixin ${1:name}(${2})

        ${0}
```
####s-inc
```css
    @include ${1:mixin}(${2})
```
####s-ext
```css
    @extend ${0}
```
####s-fun
```css
    @function ${1:name}(${2:args})

        ${0}
```
####s-if
```css
    @if ${1:condition}

        ${0}
```
####s-ife
```css
    @if ${1:condition}

        ${2}

    @else

        ${0}
```
####s-eif
```css
    @else if ${1:condition}

        ${0}
```
####s-for
```css
    @for ${1:$i} from ${2:1} through ${3:3}

        ${0}
```
####s-each
```css
    @each ${1:$item} in ${2:items}

        ${0}
```
