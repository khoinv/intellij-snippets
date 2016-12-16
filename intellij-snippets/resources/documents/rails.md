####rail-art
```ruby
    assert_redirected_to ${1:action}: '${2:index}'
```
####rail-artnp
```ruby
    assert_redirected_to ${1:parent}_${2:child}_path(${3:@$1}, ${0:@$2})
```
####rail-artnpp
```ruby
    assert_redirected_to ${1:parent}_${2:child}_path(${0:@$1})
```
####rail-artp
```ruby
    assert_redirected_to ${1:model}_path(${0:@$1})
```
####rail-artpp
```ruby
    assert_redirected_to ${0:model}s_path
```
####rail-asd
```ruby
    assert_difference '${1:Model}.${2:count}', ${3:1} do

        ${0}

    end
```
####rail-asnd
```ruby
    assert_no_difference '${1:Model}.${2:count}' do

        ${0}

    end
```
####rail-asre
```ruby
    assert_response :${1:success}, @response.body
```
####rail-asrj
```ruby
    assert_rjs :${1:replace}, '${0:dom id}'
```
####rail-ass
```ruby
    assert_select '${1:path}', ${2:text}: '${3:inner_html}' ${4:do}

        ${0}

    end
```
####rail-ba
```ruby
    before_action :${0:method}
```
####rail-bf
```ruby
    before_filter :${0:method}
```
####rail-bt
```ruby
    belongs_to :${0:association}
```
####rail-btp
```ruby
    belongs_to :${1:association}, polymorphic: true
```
####rail-crw
```ruby
    cattr_accessor :${0:attr_names}
```
####rail-defcreate
```ruby
    def create

        @${1:model_class_name} = ${2:ModelClassName}.new($1_params)



        respond_to do |format|

            if @$1.save

                flash[:notice] = '$2 was successfully created.'

                format.html { redirect_to(@$1) }

                format.xml  { render xml: @$1, status: :created, location: @$1 }

            else

                format.html { render action: 'new' }

                format.xml  { render xml: @$1.errors, status: :unprocessable_entity }

            end

        end

    end
```
####rail-defdestroy
```ruby
    def destroy

        @${1:model_class_name} = ${2:ModelClassName}.find(params[:id])

        @$1.destroy



        respond_to do |format|

            format.html { redirect_to($1s_url) }

            format.xml  { head :ok }

        end

    end
```
####rail-defedit
```ruby
    def edit

        @${1:model_class_name} = ${0:ModelClassName}.find(params[:id])

    end
```
####rail-defindex
```ruby
    def index

        @${1:model_class_name} = ${2:ModelClassName}.all



        respond_to do |format|

            format.html # index.html.erb

            format.xml  { render xml: @$1s }

        end

    end
```
####rail-defnew
```ruby
    def new

        @${1:model_class_name} = ${2:ModelClassName}.new



        respond_to do |format|

            format.html # new.html.erb

            format.xml  { render xml: @$1 }

        end

    end
```
####rail-defshow
```ruby
    def show

        @${1:model_class_name} = ${2:ModelClassName}.find(params[:id])



        respond_to do |format|

            format.html # show.html.erb

            format.xml  { render xml: @$1 }

        end

    end
```
####rail-defupdate
```ruby
    def update

        @${1:model_class_name} = ${2:ModelClassName}.find(params[:id])



        respond_to do |format|

            if @$1.update($1_params)

                flash[:notice] = '$2 was successfully updated.'

                format.html { redirect_to(@$1) }

                format.xml  { head :ok }

            else

                format.html { render action: 'edit' }

                format.xml  { render xml: @$1.errors, status: :unprocessable_entity }

            end

        end

    end
```
####rail-defparams
```ruby
    def ${1:model_class_name}_params

        params.require(:$1).permit()

    end
```
####rail-dele
```ruby
    delegate :${1:methods}, to: :${0:object}
```
####rail-dele
```ruby
    delegate :${1:methods}, to: :${2:object}, prefix: :${3:prefix}, allow_nil: ${0:allow_nil}
```
####rail-amc
```ruby
    alias_method_chain :${1:method_name}, :${0:feature}
```
####rail-flash
```ruby
    flash[:${1:notice}] = '${0}'
```
####rail-habtm
```ruby
    has_and_belongs_to_many :${1:object}, join_table: '${2:table_name}', foreign_key: '${3}_id'
```
####rail-hm
```ruby
    has_many :${0:object}
```
####rail-hmd
```ruby
    has_many :${1:other}s, class_name: '${2:$1}', foreign_key: '${3:$1}_id', dependent: :destroy
```
####rail-hmt
```ruby
    has_many :${1:object}, through: :${0:object}
```
####rail-ho
```ruby
    has_one :${0:object}
```
####rail-hod
```ruby
    has_one :${1:object}, dependent: :${0:destroy}
```
####rail-i18
```ruby
    I18n.t('${1:type.key}')
```
####rail-ist
```ruby
    <%= image_submit_tag('${1:agree.png}', id: '${2:id}'${0}) %>
```
####rail-log
```ruby
    Rails.logger.${1:debug} ${0}
```
####rail-log2
```ruby
    RAILS_DEFAULT_LOGGER.${1:debug} ${0}
```
####rail-logd
```ruby
    logger.debug { '${1:message}' }
```
####rail-loge
```ruby
    logger.error { '${1:message}' }
```
####rail-logf
```ruby
    logger.fatal { '${1:message}' }
```
####rail-logi
```ruby
    logger.info { '${1:message}' }
```
####rail-logw
```ruby
    logger.warn { '${1:message}' }
```
####rail-mapc
```ruby
    ${1:map}.${2:connect} '${0:controller/:action/:id}'
```
####rail-mapca
```ruby
    ${1:map}.catch_all '*${2:anything}', controller: '${3:default}', action: '${4:error}'
```
####rail-mapr
```ruby
    ${1:map}.resource :${0:resource}
```
####rail-maprs
```ruby
    ${1:map}.resources :${0:resource}
```
####rail-mapwo
```ruby
    ${1:map}.with_options ${2:controller}: '${3:thing}' do |$3|

        ${0}

    end


```
####rail-mbv
```ruby
    before_validation :${0:method}
```
####rail-mbc
```ruby
    before_create :${0:method}
```
####rail-mbu
```ruby
    before_update :${0:method}
```
####rail-mbs
```ruby
    before_save :${0:method}
```
####rail-mbd
```ruby
    before_destroy :${0:method}


```
####rail-mav
```ruby
    after_validation :${0:method}
```
####rail-maf
```ruby
    after_find :${0:method}
```
####rail-mat
```ruby
    after_touch :${0:method}
```
####rail-macr
```ruby
    after_create :${0:method}
```
####rail-mau
```ruby
    after_update :${0:method}
```
####rail-mas
```ruby
    after_save :${0:method}
```
####rail-mad
```ruby
    after_destroy :${0:method}


```
####rail-marc
```ruby
    around_create :${0:method}
```
####rail-maru
```ruby
    around_update :${0:method}
```
####rail-mars
```ruby
    around_save :${0:method}
```
####rail-mard
```ruby
    around_destroy :${0:method}


```
####rail-mcht
```ruby
    change_table :${1:table_name} do |t|

        ${0}

    end
```
####rail-mp
```ruby
    map(&:${0:id})
```
####rail-mrw
```ruby
    mattr_accessor :${0:attr_names}
```
####rail-oa
```ruby
    order('${0:field}')
```
####rail-od
```ruby
    order('${0:field} DESC')
```
####rail-pa
```ruby
    params[:${1:id}]
```
####rail-ra
```ruby
    render action: '${0:action}'
```
####rail-ral
```ruby
    render action: '${1:action}', layout: '${0:layoutname}'
```
####rail-rest
```ruby
    respond_to do |format|

        format.${1:html} { ${0} }

    end
```
####rail-rf
```ruby
    render file: '${0:filepath}'
```
####rail-rfu
```ruby
    render file: '${1:filepath}', use_full_path: ${0:false}
```
####rail-ri
```ruby
    render inline: "${0:<%= 'hello' %>}"
```
####rail-ril
```ruby
    render inline: "${1:<%= 'hello' %>}", locals: { ${2:name}: '${3:value}'${0} }
```
####rail-rit
```ruby
    render inline: "${1:<%= 'hello' %>}", type: ${0::rxml}
```
####rail-rjson
```ruby
    render json: '${0:text to render}'
```
####rail-rl
```ruby
    render layout: '${0:layoutname}'
```
####rail-rn
```ruby
    render nothing: ${0:true}
```
####rail-rns
```ruby
    render nothing: ${1:true}, status: ${0:401}
```
####rail-rp
```ruby
    render partial: '${0:item}'
```
####rail-rpc
```ruby
    render partial: '${1:item}', collection: ${0:@$1s}
```
####rail-rpl
```ruby
    render partial: '${1:item}', locals: { ${2:$1}: ${0:@$1} }
```
####rail-rpo
```ruby
    render partial: '${1:item}', object: ${0:@$1}
```
####rail-rps
```ruby
    render partial: '${1:item}', status: ${0:500}
```
####rail-rt
```ruby
    render text: '${0:text to render}'
```
####rail-rtl
```ruby
    render text: '${1:text to render}', layout: '${0:layoutname}'
```
####rail-rtlt
```ruby
    render text: '${1:text to render}', layout: ${0:true}
```
####rail-rts
```ruby
    render text: '${1:text to render}', status: ${0:401}
```
####rail-ru
```ruby
    render :update do |${1:page}|

        $1.${0}

    end
```
####rail-rxml
```ruby
    render xml: '${0:text to render}'
```
####rail-sc
```ruby
    scope :${1:name}, -> { where(${2:field}: ${0:value}) }
```
####rail-sl
```ruby
    scope :${1:name}, lambda do |${2:value}|

        where('${3:field = ?}', ${0:value})

    end
```
####rail-sha1
```ruby
    Digest::SHA1.hexdigest(${0:string})
```
####rail-sweeper
```ruby
    class ${1:ModelClassName}Sweeper < ActionController::Caching::Sweeper

        observe $1



        def after_save(${0:model_class_name})

            expire_cache($2)

        end



        def after_destroy($2)

            expire_cache($2)

        end



        def expire_cache($2)

            expire_page

        end

    end
```
####rail-va
```ruby
    validates_associated :${0:attribute}
```
####rail-va
```ruby
    validates :${0:terms}, acceptance: true
```
####rail-vc
```ruby
    validates :${0:attribute}, confirmation: true
```
####rail-ve
```ruby
    validates :${1:attribute}, exclusion: { in: ${0:%w( mov avi )} }
```
####rail-vf
```ruby
    validates :${1:attribute}, format: { with: /${0:regex}/ }
```
####rail-vi
```ruby
    validates :${1:attribute}, inclusion: { in: %w(${0: mov avi }) }
```
####rail-vl
```ruby
    validates :${1:attribute}, length: { in: ${2:3}..${0:20} }
```
####rail-vn
```ruby
    validates :${0:attribute}, numericality: true
```
####rail-vp
```ruby
    validates :${0:attribute}, presence: true
```
####rail-vu
```ruby
    validates :${0:attribute}, uniqueness: true
```
####rail-format
```ruby
    format.${1:js|xml|html} { ${0} }
```
####rail-wc
```ruby
    where(${1:'conditions'}${0:, bind_var})
```
####rail-wf
```ruby
    where(${1:field}: ${0:value})
```
####rail-xdelete
```ruby
    xhr :delete, :${1:destroy}, id: ${2:1}
```
####rail-xget
```ruby
    xhr :get, :${1:show}, id: ${2:1}
```
####rail-xpost
```ruby
    xhr :post, :${1:create}, ${2:object}: ${3:object}
```
####rail-xput
```ruby
    xhr :put, :${1:update}, id: ${2:1}, ${3:object}: ${4:object}
```
####rail-test
```ruby
    test '${1:should do something}' do

        ${0}

    end
```
####rail-mac
```ruby
    add_column :${1:table_name}, :${2:column_name}, :${0:data_type}
```
####rail-mai
```ruby
    add_index :${1:table_name}, :${0:column_name}
```
####rail-mrc
```ruby
    remove_column :${1:table_name}, :${0:column_name}
```
####rail-mrnc
```ruby
    rename_column :${1:table_name}, :${2:old_column_name}, :${0:new_column_name}
```
####rail-mcc
```ruby
    change_column :${1:table}, :${2:column}, :${0:type}
```
####rail-mnc
```ruby
    t.${1:string} :${2:title}${3:, null: false}
```
####rail-mct
```ruby
    create_table :${1:table_name} do |t|

        ${0}

    end
```
####rail-migration
```ruby
    class `substitute( substitute(vim_snippets#Filename(), '^\d\+_', '',''), '\(_\|^\)\(.\)', '\u\2', 'g')` < ActiveRecord::Migration

        def up

            ${0}

        end



        def down

        end

    end
```
####rail-migration
```ruby
    class `substitute( substitute(vim_snippets#Filename(), '^\d\+_', '',''), '\(_\|^\)\(.\)', '\u\2', 'g')` < ActiveRecord::Migration

        def change

            ${0}

        end

    end
```
####rail-trc
```ruby
    t.remove :${0:column}
```
####rail-tre
```ruby
    t.rename :${1:old_column_name}, :${2:new_column_name}

    ${0}
```
####rail-tref
```ruby
    t.references :${0:model}
```
####rail-tcb
```ruby
    t.boolean :${1:title}

    ${0}
```
####rail-tcbi
```ruby
    t.binary :${1:title}, limit: ${2:2}.megabytes

    ${0}
```
####rail-tcd
```ruby
    t.decimal :${1:title}, precision: ${2:10}, scale: ${3:2}

    ${0}
```
####rail-tcda
```ruby
    t.date :${1:title}

    ${0}
```
####rail-tcdt
```ruby
    t.datetime :${1:title}

    ${0}
```
####rail-tcf
```ruby
    t.float :${1:title}

    ${0}
```
####rail-tch
```ruby
    t.change :${1:name}, :${2:string}, ${3:limit}: ${4:80}

    ${0}
```
####rail-tci
```ruby
    t.integer :${1:title}

    ${0}
```
####rail-tcl
```ruby
    t.integer :lock_version, null: false, default: 0

    ${0}
```
####rail-tcr
```ruby
    t.references :${1:taggable}, polymorphic: { default: '${2:Photo}' }

    ${0}
```
####rail-tcs
```ruby
    t.string :${1:title}

    ${0}
```
####rail-tct
```ruby
    t.text :${1:title}

    ${0}
```
####rail-tcti
```ruby
    t.time :${1:title}

    ${0}
```
####rail-tcts
```ruby
    t.timestamp :${1:title}

    ${0}
```
####rail-tctss
```ruby
    t.timestamps

    ${0}
```
####rail-isfp
```ruby
    it { should filter_param :${0:key} }
```
####rail-isrt
```ruby
    it { should redirect_to ${0:url} }
```
####rail-isrtp
```ruby
    it { should render_template ${0} }
```
####rail-isrwl
```ruby
    it { should render_with_layout ${0} }
```
####rail-isrf
```ruby
    it { should rescue_from ${0:exception} }
```
####rail-isrw
```ruby
    it { should respond_with ${0:status} }
```
####rail-isr
```ruby
    it { should route(:${1:method}, '${0:path}') }
```
####rail-isss
```ruby
    it { should set_session :${0:key} }
```
####rail-issf
```ruby
    it { should set_the_flash('${0}') }
```
####rail-isama
```ruby
    it { should allow_mass_assignment_of :${0} }
```
####rail-isav
```ruby
    it { should allow_value(${1}).for :${0} }
```
####rail-isee
```ruby
    it { should ensure_exclusion_of :${0} }
```
####rail-isei
```ruby
    it { should ensure_inclusion_of :${0} }
```
####rail-isel
```ruby
    it { should ensure_length_of :${0} }
```
####rail-isva
```ruby
    it { should validate_acceptance_of :${0} }
```
####rail-isvc
```ruby
    it { should validate_confirmation_of :${0} }
```
####rail-isvn
```ruby
    it { should validate_numericality_of :${0} }
```
####rail-isvp
```ruby
    it { should validate_presence_of :${0} }
```
####rail-isvu
```ruby
    it { should validate_uniqueness_of :${0} }
```
####rail-isana
```ruby
    it { should accept_nested_attributes_for :${0} }
```
####rail-isbt
```ruby
    it { should belong_to :${0} }
```
####rail-isbtcc
```ruby
    it { should belong_to(:${1}).counter_cache ${0:true} }
```
####rail-ishbtm
```ruby
    it { should have_and_belong_to_many :${0} }
```
####rail-isbv
```ruby
    it { should be_valid }
```
####rail-ishc
```ruby
    it { should have_db_column :${0} }
```
####rail-ishi
```ruby
    it { should have_db_index :${0} }
```
####rail-ishm
```ruby
    it { should have_many :${0} }
```
####rail-ishmt
```ruby
    it { should have_many(:${1}).through :${0} }
```
####rail-isho
```ruby
    it { should have_one :${0} }
```
####rail-ishro
```ruby
    it { should have_readonly_attribute :${0} }
```
####rail-iss
```ruby
    it { should serialize :${0} }
```
####rail-isres
```ruby
    it { should respond_to :${0} }
```
####rail-isresw
```ruby
    it { should respond_to(:${1}).with(${0}).arguments }
```
