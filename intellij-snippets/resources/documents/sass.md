####$
```css
    $${1:variable}: ${0:value}
```
####imp
```css
    @import '${0}'
```
####mix
```css
    @mixin ${1:name}(${2})

        ${0}
```
####inc
```css
    @include ${1:mixin}(${2})
```
####ext
```css
    @extend ${0}
```
####fun
```css
    @function ${1:name}(${2:args})

        ${0}
```
####if
```css
    @if ${1:condition}

        ${0}
```
####ife
```css
    @if ${1:condition}

        ${2}

    @else

        ${0}
```
####eif
```css
    @else if ${1:condition}

        ${0}
```
####for
```css
    @for ${1:$i} from ${2:1} through ${3:3}

        ${0}
```
####each
```css
    @each ${1:$item} in ${2:items}

        ${0}
```
