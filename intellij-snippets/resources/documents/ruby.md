####rb-enc
```ruby
    # encoding: utf-8
```
####rb-frozen
```ruby
    # frozen_string_literal: true
```
####rb-#!
```ruby
    #!/usr/bin/env ruby
```
####rb-=b
```ruby
    =begin rdoc

        ${0}

    =end
```
####rb-prot
```ruby
    protected



    ${0}
```
####rb-priv
```ruby
    private



    ${0}
```
####rb-y
```ruby
    :yields: ${0:arguments}
```
####rb-rb
```ruby
    #!/usr/bin/env ruby -wKU
```
####rb-beg
```ruby
    begin

        ${0}

    rescue ${1:Exception} => ${2:e}

    end
```
####rb-req
```ruby
    require '${1}'
```
####rb-reqr
```ruby
    require_relative '${1}'
```
####rb-#
```ruby
    # =>
```
####rb-case
```ruby
    case ${1:object}

    when ${2:condition}

        ${0}

    end
```
####rb-when
```ruby
    when ${1:condition}

        ${0}
```
####rb-def
```ruby
    def ${1:method_name}

        ${0}

    end
```
####rb-deft
```ruby
    def test_${1:case_name}

        ${0}

    end
```
####rb-descendants
```ruby
    class Class

        def descendants

            ObjectSpace.each_object(::Class).select { |klass| klass < self }

        end

    end
```
####rb-if
```ruby
    if ${1:condition}

        ${0}

    end
```
####rb-ife
```ruby
    if ${1:condition}

        ${2}

    else

        ${0}

    end
```
####rb-eif
```ruby
    elsif ${1:condition}

        ${0}
```
####rb-ifee
```ruby
    if ${1:condition}

        $2

    elsif ${3:condition}

        $4

    else

        $0

    end
```
####rb-unless
```ruby
    unless ${1:condition}

        ${0}

    end
```
####rb-unlesse
```ruby
    unless ${1:condition}

        $2

    else

        $0

    end
```
####rb-unlesee
```ruby
    unless ${1:condition}

        $2

    elsif ${3:condition}

        $4

    else

        $0

    end
```
####rb-wh
```ruby
    while ${1:condition}

        ${0}

    end
```
####rb-for
```ruby
    for ${1:e} in ${2:c}

        ${0}

    end
```
####rb-until
```ruby
    until ${1:condition}

        ${0}

    end
```
####rb-cla
```ruby
    class ${1:`substitute(vim_snippets#Filename(), '\(_\|^\)\(.\)', '\u\2', 'g')`}

        ${0}

    end
```
####rb-clai
```ruby
    class ${1:`substitute(vim_snippets#Filename(), '\(_\|^\)\(.\)', '\u\2', 'g')`}

        def initialize(${2:args})

            ${0}

        end

    end
```
####rb-cla<
```ruby
    class ${1:`substitute(vim_snippets#Filename(), '\(_\|^\)\(.\)', '\u\2', 'g')`} < ${2:ParentClass}

        def initialize(${3:args})

            ${0}

        end

    end
```
####rb-blankslate
```ruby
    class ${0:BlankSlate}

        instance_methods.each { |meth| undef_method(meth) unless meth =~ /\A__/ }

    end
```
####rb-claself
```ruby
    class << ${1:self}

        ${0}

    end
```
####rb-cla-
```ruby
    class ${1:`substitute(vim_snippets#Filename(), '\(_\|^\)\(.\)', '\u\2', 'g')`} < DelegateClass(${2:ParentClass})

        def initialize(${3:args})

            super(${4:del_obj})



            ${0}

        end

    end
```
####rb-mod
```ruby
    module ${1:`substitute(vim_snippets#Filename(), '\(_\|^\)\(.\)', '\u\2', 'g')`}

        ${0}

    end
```
####rb-mod
```ruby
    module ${1:`substitute(vim_snippets#Filename(), '\(_\|^\)\(.\)', '\u\2', 'g')`}

        module ClassMethods

            ${0}

        end



        module InstanceMethods



        end



        def self.included(receiver)

            receiver.extend         ClassMethods

            receiver.send :include, InstanceMethods

        end

    end
```
####rb-r
```ruby
    attr_reader :${0:attr_names}
```
####rb-w
```ruby
    attr_writer :${0:attr_names}
```
####rb-rw
```ruby
    attr_accessor :${0:attr_names}
```
####rb-atp
```ruby
    attr_protected :${0:attr_names}
```
####rb-ata
```ruby
    attr_accessible :${0:attr_names}
```
####rb-ana
```ruby
    accepts_nested_attributes_for :${0:association}
```
####rb-ivc
```ruby
    @${1:variable_name} ||= ${0:cached_value}
```
####rb-Enum
```ruby
    include Enumerable



    def each(&block)

        ${0}

    end
```
####rb-Comp
```ruby
    include Comparable



    def <=>(other)

        ${0}

    end
```
####rb-Forw-
```ruby
    extend Forwardable
```
####rb-defs
```ruby
    def self.${1:class_method_name}

        ${0}

    end
```
####rb-definit
```ruby
    def initialize(${1:args})

        ${0}

    end
```
####rb-defmm
```ruby
    def method_missing(meth, *args, &blk)

        ${0}

    end
```
####rb-defd
```ruby
    def_delegator :${1:@del_obj}, :${2:del_meth}, :${0:new_name}
```
####rb-defds
```ruby
    def_delegators :${1:@del_obj}, :${0:del_methods}
```
####rb-am
```ruby
    alias_method :${1:new_name}, :${0:old_name}
```
####rb-app
```ruby
    if __FILE__ == $PROGRAM_NAME

        ${0}

    end
```
####rb-usai
```ruby
    if ARGV.${1}

        abort "Usage: #{$PROGRAM_NAME} ${2:ARGS_GO_HERE}"${0}

    end
```
####rb-usau
```ruby
    unless ARGV.${1}

        abort "Usage: #{$PROGRAM_NAME} ${2:ARGS_GO_HERE}"${0}

    end
```
####rb-array
```ruby
    Array.new(${1:10}) { |${2:i}| ${0} }
```
####rb-hash
```ruby
    Hash.new { |${1:hash}, ${2:key}| $1[$2] = ${0} }
```
####rb-file
```ruby
    File.foreach(${1:'path/to/file'}) { |${2:line}| ${0} }
```
####rb-file
```ruby
    File.read(${1:'path/to/file'})
```
####rb-Dir
```ruby
    Dir.glob(${1:'dir/glob/*'}) { |${2:file}| ${0} }
```
####rb-Dir
```ruby
    Dir[${1:'glob/**/*.rb'}]
```
####rb-dir
```ruby
    Filename.dirname(__FILE__)
```
####rb-deli
```ruby
    delete_if { |${1:e}| ${0} }
```
####rb-fil
```ruby
    fill(${1:range}) { |${2:i}| ${0} }
```
####rb-flao
```ruby
    reduce(Array.new) { |${1:arr}, ${2:a}| $1.push(*$2) }
```
####rb-zip
```ruby
    zip(${1:enums}) { |${2:row}| ${0} }
```
####rb-dow
```ruby
    downto(${1:0}) { |${2:n}| ${0} }
```
####rb-ste
```ruby
    step(${1:2}) { |${2:n}| ${0} }
```
####rb-tim
```ruby
    times { |${1:n}| ${0} }
```
####rb-upt
```ruby
    upto(${1:1.0/0.0}) { |${2:n}| ${0} }
```
####rb-loo
```ruby
    loop { ${0} }
```
####rb-ea
```ruby
    each { |${1:e}| ${0} }
```
####rb-ead
```ruby
    each do |${1:e}|

        ${0}

    end
```
####rb-eab
```ruby
    each_byte { |${1:byte}| ${0} }
```
####rb-eac-
```ruby
    each_char { |${1:chr}| ${0} }
```
####rb-eac-
```ruby
    each_cons(${1:2}) { |${2:group}| ${0} }
```
####rb-eai
```ruby
    each_index { |${1:i}| ${0} }
```
####rb-eaid
```ruby
    each_index do |${1:i}|

        ${0}

    end
```
####rb-eak
```ruby
    each_key { |${1:key}| ${0} }
```
####rb-eakd
```ruby
    each_key do |${1:key}|

        ${0}

    end
```
####rb-eal
```ruby
    each_line { |${1:line}| ${0} }
```
####rb-eald
```ruby
    each_line do |${1:line}|

        ${0}

    end
```
####rb-eap
```ruby
    each_pair { |${1:name}, ${2:val}| ${0} }
```
####rb-eapd
```ruby
    each_pair do |${1:name}, ${2:val}|

        ${0}

    end
```
####rb-eas-
```ruby
    each_slice(${1:2}) { |${2:group}| ${0} }
```
####rb-easd-
```ruby
    each_slice(${1:2}) do |${2:group}|

        ${0}

    end
```
####rb-eav
```ruby
    each_value { |${1:val}| ${0} }
```
####rb-eavd
```ruby
    each_value do |${1:val}|

        ${0}

    end
```
####rb-eawi
```ruby
    each_with_index { |${1:e}, ${2:i}| ${0} }
```
####rb-eawid
```ruby
    each_with_index do |${1:e}, ${2:i}|

        ${0}

    end
```
####rb-eawo
```ruby
    each_with_object(${1:init}) { |${2:e}, ${3:var}| ${0} }
```
####rb-eawod
```ruby
    each_with_object(${1:init}) do |${2:e}, ${3:var}|

        ${0}

    end
```
####rb-reve
```ruby
    reverse_each { |${1:e}| ${0} }
```
####rb-reved
```ruby
    reverse_each do |${1:e}|

        ${0}

    end
```
####rb-inj
```ruby
    inject(${1:init}) { |${2:mem}, ${3:var}| ${0} }
```
####rb-injd
```ruby
    inject(${1:init}) do |${2:mem}, ${3:var}|

        ${0}

    end
```
####rb-red
```ruby
    reduce(${1:init}) { |${2:mem}, ${3:var}| ${0} }
```
####rb-redd
```ruby
    reduce(${1:init}) do |${2:mem}, ${3:var}|

        ${0}

    end
```
####rb-map
```ruby
    map { |${1:e}| ${0} }
```
####rb-mapd
```ruby
    map do |${1:e}|

        ${0}

    end
```
####rb-mapwi-
```ruby
    enum_with_index.map { |${1:e}, ${2:i}| ${0} }
```
####rb-sor
```ruby
    sort { |a, b| ${0} }
```
####rb-sorb
```ruby
    sort_by { |${1:e}| ${0} }
```
####rb-ran
```ruby
    sort_by { rand }
```
####rb-all
```ruby
    all? { |${1:e}| ${0} }
```
####rb-any
```ruby
    any? { |${1:e}| ${0} }
```
####rb-cl
```ruby
    classify { |${1:e}| ${0} }
```
####rb-col
```ruby
    collect { |${1:e}| ${0} }
```
####rb-cold
```ruby
    collect do |${1:e}|

        ${0}

    end
```
####rb-det
```ruby
    detect { |${1:e}| ${0} }
```
####rb-detd
```ruby
    detect do |${1:e}|

        ${0}

    end
```
####rb-fet
```ruby
    fetch(${1:name}) { |${2:key}| ${0} }
```
####rb-fin
```ruby
    find { |${1:e}| ${0} }
```
####rb-find
```ruby
    find do |${1:e}|

        ${0}

    end
```
####rb-fina
```ruby
    find_all { |${1:e}| ${0} }
```
####rb-finad
```ruby
    find_all do |${1:e}|

        ${0}

    end
```
####rb-gre
```ruby
    grep(${1:/pattern/}) { |${2:match}| ${0} }
```
####rb-sub
```ruby
    ${1:g}sub(${2:/pattern/}) { |${3:match}| ${0} }
```
####rb-sca
```ruby
    scan(${1:/pattern/}) { |${2:match}| ${0} }
```
####rb-scad
```ruby
    scan(${1:/pattern/}) do |${2:match}|

        ${0}

    end
```
####rb-max
```ruby
    max { |a, b| ${0} }
```
####rb-min
```ruby
    min { |a, b| ${0} }
```
####rb-par
```ruby
    partition { |${1:e}| ${0} }
```
####rb-pard
```ruby
    partition do |${1:e}|

        ${0}

    end
```
####rb-rej
```ruby
    reject { |${1:e}| ${0} }
```
####rb-rejd
```ruby
    reject do |${1:e}|

        ${0}

    end
```
####rb-sel
```ruby
    select { |${1:e}| ${0} }
```
####rb-seld
```ruby
    select do |${1:e}|

        ${0}

    end
```
####rb-lam
```ruby
    lambda { |${1:args}| ${0} }
```
####rb-->
```ruby
    -> { ${0} }
```
####rb-->a
```ruby
    ->(${1:args}) { ${0} }
```
####rb-do
```ruby
    do

        ${0}

    end
```
####rb-dov
```ruby
    do |${1:v}|

        ${2}

    end
```
####rb-:
```ruby
    ${1:key}: ${2:'value'}
```
####rb-ope
```ruby
    open('${1:path/or/url/or/pipe}', '${2:w}') { |${3:io}| ${0} }
```
####rb-fpath
```ruby
    File.join(File.dirname(__FILE__), *['${1:rel path here}'])
```
####rb-unif
```ruby
    ARGF.each_line${1} do |${2:line}|

        ${0}

    end
```
####rb-optp
```ruby
    require 'optparse'



    options = { ${0:default: 'args'} }



    ARGV.options do |opts|

        opts.banner = "Usage: #{File.basename($PROGRAM_NAME)}"

    end
```
####rb-opt
```ruby
    opts.on('-${1:o}', '--${2:long-option-name}', ${3:String}, '${4:Option description.}') do |${5:opt}|

        ${0}

    end
```
####rb-tc
```ruby
    require 'test/unit'



    require '${1:library_file_name}'



    class Test${2:$1} < Test::Unit::TestCase

        def test_${3:case_name}

            ${0}

        end

    end
```
####rb-ts
```ruby
    require 'test/unit'



    require 'tc_${1:test_case_file}'

    require 'tc_${2:test_case_file}'
```
####rb-as
```ruby
    assert ${1:test}, '${2:Failure message.}'
```
####rb-ase
```ruby
    assert_equal ${1:expected}, ${2:actual}
```
####rb-asne
```ruby
    assert_not_equal ${1:unexpected}, ${2:actual}
```
####rb-asid
```ruby
    assert_in_delta ${1:expected_float}, ${2:actual_float}, ${3:2**-20}
```
####rb-asi
```ruby
    assert_includes ${1:collection}, ${2:object}
```
####rb-asio
```ruby
    assert_instance_of ${1:ExpectedClass}, ${2:actual_instance}
```
####rb-asko
```ruby
    assert_kind_of ${1:ExpectedKind}, ${2:actual_instance}
```
####rb-asn
```ruby
    assert_nil ${1:instance}
```
####rb-asnn
```ruby
    assert_not_nil ${1:instance}
```
####rb-asm
```ruby
    assert_match(/${1:expected_pattern}/, ${2:actual_string})
```
####rb-asnm
```ruby
    assert_no_match(/${1:unexpected_pattern}/, ${2:actual_string})
```
####rb-aso
```ruby
    assert_operator ${1:left}, :${2:operator}, ${3:right}
```
####rb-asr
```ruby
    assert_raise ${1:Exception} { ${0} }
```
####rb-asrd
```ruby
    assert_raise ${1:Exception} do

        ${0}

    end
```
####rb-asnr
```ruby
    assert_nothing_raised ${1:Exception} { ${0} }
```
####rb-asnrd
```ruby
    assert_nothing_raised ${1:Exception} do

        ${0}

    end
```
####rb-asrt
```ruby
    assert_respond_to ${1:object}, :${2:method}
```
####rb-ass
```ruby
    assert_same ${1:expected}, ${2:actual}
```
####rb-ass
```ruby
    assert_send [${1:object}, :${2:message}, ${3:args}]
```
####rb-asns
```ruby
    assert_not_same ${1:unexpected}, ${2:actual}
```
####rb-ast
```ruby
    assert_throws :${1:expected}, -> { ${0} }
```
####rb-astd
```ruby
    assert_throws :${1:expected} do

        ${0}

    end
```
####rb-asnt
```ruby
    assert_nothing_thrown { ${0} }
```
####rb-asntd
```ruby
    assert_nothing_thrown do

        ${0}

    end
```
####rb-fl
```ruby
    flunk '${1:Failure message.}'
```
####rb-bm-
```ruby
    TESTS = ${1:10_000}

    Benchmark.bmbm do |results|

        ${0}

    end
```
####rb-rep
```ruby
    results.report('${1:name}:') { TESTS.times { ${0} } }
```
####rb-Md
```ruby
    File.open('${1:path/to/file.dump}', 'wb') { |${2:file}| Marshal.dump(${3:obj}, $2) }
```
####rb-Ml
```ruby
    File.open('${1:path/to/file.dump}', 'rb') { |${2:file}| Marshal.load($2) }
```
####rb-deec
```ruby
    Marshal.load(Marshal.dump(${1:obj_to_copy}))
```
####rb-Pn-
```ruby
    PStore.new('${1:file_name.pstore}')
```
####rb-tra
```ruby
    transaction(${1:true}) { ${0} }
```
####rb-xml-
```ruby
    REXML::Document.new(File.read('${1:path/to/file}'))
```
####rb-xpa
```ruby
    elements.each('${1://Xpath}') do |${2:node}|

        ${0}

    end
```
####rb-clafn
```ruby
    split('::').inject(Object) { |par, const| par.const_get(const) }
```
####rb-sinc
```ruby
    class << self; self end
```
####rb-nam
```ruby
    namespace :${1:`vim_snippets#Filename()`} do

        ${0}

    end
```
####rb-tas
```ruby
    desc '${1:Task description}'

    task ${2:task_name: [:dependent, :tasks]} do

        ${0}

    end
```
####rb-b
```ruby
    { |${1:var}| ${0} }
```
####rb-begin
```ruby
    begin

        fail 'A test exception.'

    rescue Exception => e

        puts e.message

        puts e.backtrace.inspect

    else

        # other exception

    ensure

        # always executed

    end


```
####rb-debug
```ruby
    require 'byebug'; byebug
```
####rb-debug19
```ruby
    require 'debugger'; debugger
```
####rb-debug18
```ruby
    require 'ruby-debug'; debugger
```
####rb-pry
```ruby
    require 'pry'; binding.pry
```
####rb-strf
```ruby
    strftime('${1:%Y-%m-%d %H:%M:%S %z}')${0}
```
####rb-mb
```ruby
    must_be ${0}
```
####rb-wb
```ruby
    wont_be ${0}
```
####rb-mbe
```ruby
    must_be_empty
```
####rb-wbe
```ruby
    wont_be_empty
```
####rb-mbio
```ruby
    must_be_instance_of ${0:Class}
```
####rb-wbio
```ruby
    wont_be_instance_of ${0:Class}
```
####rb-mbko
```ruby
    must_be_kind_of ${0:Class}
```
####rb-wbko
```ruby
    wont_be_kind_of ${0:Class}
```
####rb-mbn
```ruby
    must_be_nil
```
####rb-wbn
```ruby
    wont_be_nil
```
####rb-mbsa
```ruby
    must_be_same_as ${0:other}
```
####rb-wbsa
```ruby
    wont_be_same_as ${0:other}
```
####rb-mbsi
```ruby
    -> { ${0} }.must_be_silent
```
####rb-mbwd
```ruby
    must_be_within_delta ${1:0.1}, ${2:0.1}
```
####rb-wbwd
```ruby
    wont_be_within_delta ${1:0.1}, ${2:0.1}
```
####rb-mbwe
```ruby
    must_be_within_epsilon ${1:0.1}, ${2:0.1}
```
####rb-wbwe
```ruby
    wont_be_within_epsilon ${1:0.1}, ${2:0.1}
```
####rb-me
```ruby
    must_equal ${0:other}
```
####rb-we
```ruby
    wont_equal ${0:other}
```
####rb-mi
```ruby
    must_include ${0:what}
```
####rb-wi
```ruby
    wont_include ${0:what}
```
####rb-mm
```ruby
    must_match /${0:regex}/
```
####rb-wm
```ruby
    wont_match /${0:regex}/
```
####rb-mout
```ruby
    -> { ${1} }.must_output '${0}'
```
####rb-mra
```ruby
    -> { ${1} }.must_raise ${0:Exception}
```
####rb-mrt
```ruby
    must_respond_to :${0:method}
```
####rb-wrt
```ruby
    wont_respond_to :${0:method}
```
####rb-msend
```ruby
    must_send [ ${1:what}, :${2:method}, ${3:args} ]
```
####rb-mthrow
```ruby
    -> { throw :${1:error} }.must_throw :${2:error}
```
####rb-desc
```ruby
    describe ${1:`substitute(substitute(vim_snippets#Filename(), '_spec$', '', ''), '\(_\|^\)\(.\)', '\u\2', 'g')`} do

        ${0}

    end
```
####rb-descm
```ruby
    describe '${1:#method}' do

        ${0:pending 'Not implemented'}

    end
```
####rb-cont
```ruby
    context '${1:message}' do

        ${0}

    end
```
####rb-bef
```ruby
    before :${1:each} do

        ${0}

    end
```
####rb-aft
```ruby
    after :${1:each} do

        ${0}

    end
```
####rb-let
```ruby
    let(:${1:object}) { ${0} }
```
####rb-let!
```ruby
    let!(:${1:object}) { ${0} }
```
####rb-subj
```ruby
    subject { ${0} }
```
####rb-s.
```ruby
    subject.${0:method}
```
####rb-spec
```ruby
    specify { subject.${0} }
```
####rb-exp
```ruby
    expect(${1:object}).to ${0}
```
####rb-expb
```ruby
    expect { ${1:object} }.to ${0}
```
####rb-experr
```ruby
    expect { ${1:object} }.to raise_error ${2:StandardError}, /${0:message_regex}/
```
####rb-shared
```ruby
    shared_examples ${0:'shared examples name'}
```
####rb-ibl
```ruby
    it_behaves_like ${0:'shared examples name'}
```
####rb-it
```ruby
    it '${1:spec_name}' do

        ${0}

    end
```
####rb-its
```ruby
    its(:${1:method}) { should ${0} }
```
####rb-is
```ruby
    it { should ${0} }
```
####rb-isn
```ruby
    it { should_not ${0} }
```
####rb-iexp
```ruby
    it { expect(${1:object}).${1} ${0} }
```
####rb-iexpb
```ruby
    it { expect { ${1:object} }.${1} ${0} }
```
####rb-iiexp
```ruby
    it { is_expected.to ${0} }
```
####rb-iiexpn
```ruby
    it { is_expected.not_to ${0} }
```
