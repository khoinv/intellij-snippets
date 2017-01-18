## IntelliJ-snippets
This repository contains snippets files for various programing languages.

In the first step, all of snippets was converted from [vim-snippets](https://github.com/honza/vim-snippets) and [bootstrap-snippets](https://github.com/bonsaiben/bootstrap-snippets) - that using snipMate format.
I am very happy if someone contribute with me to improve it better!
#### Screencasts
![bootstrap.gif](https://github.com/khoinv/intellij-snippets/blob/master/screencasts/bootstrap.gif?raw=true)

#### How to use
- Clone this repository to your local environment

```bash
    git clone https://github.com/khoinv/intellij-snippets.git
    cd IntelliJ-snippets && git submodule update --init --recursive
```

- Copy all of file in intellij-snippets/resources/templates/* to your templates folder depend on your OS
    - Live templates are stored in the following location:
    - Windows: <your_user_home_directory>.IntelliJ IDEA<version_number>\config\templates
    - Linux: ~IntelliJ IDEA<version>\config\templates
    - OS X: ~/Library/Preferences/IntelliJ IDEA<version>/templates
- Restart IntelliJ Editor if it is running
- Type snippet name fllowed by pressing Tab or Enter to get template code. If snippets list do not show up press ```<CMD>J```.
- To move between variable locations  in tamplate code you can use ```<Tab>``` or ```<Enter>```. But if emmet mode is enabled, when you type ```abc<Tab>``` it will be converted to a html tag like ```<abc></abc>```, so you shoud you ```<Enter>``` instead of ```<Tab>``` to swich between variable locations.

#### This template may be works for the following JetBrains products
- IntelliJ IDEA(EC and Ultimate)(tested)
- WebStorm and PhpStorm(not tested)
- PyCharm(not tested)
- RubyMine(not tested)

#### Snippets list
- [angular.md](intellij-snippets/resources/documents/angular.md)
- [bootstrap.md](intellij-snippets/resources/documents/bootstrap.md)
- [codeigniter.md](intellij-snippets/resources/documents/codeigniter.md)
- [css.md](intellij-snippets/resources/documents/css.md)
- [django.md](intellij-snippets/resources/documents/django.md)
- [eruby.md](intellij-snippets/resources/documents/eruby.md)
- [go.md](intellij-snippets/resources/documents/go.md)
- [html.md](intellij-snippets/resources/documents/html.md)
- [java.md](intellij-snippets/resources/documents/java.md)
- [javascript-d3.md](intellij-snippets/resources/documents/javascript-d3.md)
- [javascript.md](intellij-snippets/resources/documents/javascript.md)
- [javascript2.md](intellij-snippets/resources/documents/javascript2)
- [javascritp.es6.md](intellij-snippets/resources/documents/javascript.es6.md)
- [jquery.md](intellij-snippets/resources/documents/jquery.md)
- [laravel.md](intellij-snippets/resources/documents/laravel.md)
- [markdown.md](intellij-snippets/resources/documents/markdown.md)
- [node.md](intellij-snippets/resources/documents/node.md)
- [php.md](intellij-snippets/resources/documents/php.md)
- [rails.md](intellij-snippets/resources/documents/rails.md)
- [react.md](intellij-snippets/resources/documents/react.md)
- [ruby.md](intellij-snippets/resources/documents/ruby.md)
- [sass.md](intellij-snippets/resources/documents/sass.md)
- [scala.md](intellij-snippets/resources/documents/scala.md)
- [sql.md](intellij-snippets/resources/documents/sql.md)


## How to customize my snippets style
- In vim-snippets repository has various snippets language, and you can convert it to intelliJ snippet if you need.
- Using convert(inFile, outFile, prefix, language, [supportLanguages]) in convert.py
- SupportLanguages OPTIONS
    - HTML
    - XML
    - JSON
    - JAVA_CODE
    - CSS
    - CUCUMBER_FEATURE_FILE
    - JAVA_SCRIPT
    - TypeScript
    - SQL
    - ColdFusion
    - PHP
    - GROOVY
    - MAVEN
    - ASPECTJ
    - ACTION_SCRIPT
    - MXML
    - CoffeeScript
    - JSP
    - OGNL
    - GSP
    - SCALA
    - SBT
    - SSP
    - KOTLIN
    - HAML
    - Python
    - Django
    - RUBY
    - RHTML
    - GO
- Note: If you want make a snippet that support all languages, let supportLanguages value is 'OTHER'
- Change prefix to what you want, prefix option can be empty

## TODO
- Make it become a Plugin
