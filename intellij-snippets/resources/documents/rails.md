####rl-art
```ruby
    assert_redirected_to ${1:action}: '${2:index}'
```
####rl-artnp
```ruby
    assert_redirected_to ${1:parent}_${2:child}_path(${3:@$1}, ${0:@$2})
```
####rl-artnpp
```ruby
    assert_redirected_to ${1:parent}_${2:child}_path(${0:@$1})
```
####rl-artp
```ruby
    assert_redirected_to ${1:model}_path(${0:@$1})
```
####rl-artpp
```ruby
    assert_redirected_to ${0:model}s_path
```
####rl-asd
```ruby
    assert_difference '${1:Model}.${2:count}', ${3:1} do

        ${0}

    end
```
####rl-asnd
```ruby
    assert_no_difference '${1:Model}.${2:count}' do

        ${0}

    end
```
####rl-asre
```ruby
    assert_response :${1:success}, @response.body
```
####rl-asrj
```ruby
    assert_rjs :${1:replace}, '${0:dom id}'
```
####rl-ass
```ruby
    assert_select '${1:path}', ${2:text}: '${3:inner_html}' ${4:do}

        ${0}

    end
```
####rl-ba
```ruby
    before_action :${0:method}
```
####rl-bf
```ruby
    before_filter :${0:method}
```
####rl-bt
```ruby
    belongs_to :${0:association}
```
####rl-btp
```ruby
    belongs_to :${1:association}, polymorphic: true
```
####rl-crw
```ruby
    cattr_accessor :${0:attr_names}
```
####rl-defcreate
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
####rl-defdestroy
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
####rl-defedit
```ruby
    def edit

        @${1:model_class_name} = ${0:ModelClassName}.find(params[:id])

    end
```
####rl-defindex
```ruby
    def index

        @${1:model_class_name} = ${2:ModelClassName}.all



        respond_to do |format|

            format.html # index.html.erb

            format.xml  { render xml: @$1s }

        end

    end
```
####rl-defnew
```ruby
    def new

        @${1:model_class_name} = ${2:ModelClassName}.new



        respond_to do |format|

            format.html # new.html.erb

            format.xml  { render xml: @$1 }

        end

    end
```
####rl-defshow
```ruby
    def show

        @${1:model_class_name} = ${2:ModelClassName}.find(params[:id])



        respond_to do |format|

            format.html # show.html.erb

            format.xml  { render xml: @$1 }

        end

    end
```
####rl-defupdate
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
####rl-defparams
```ruby
    def ${1:model_class_name}_params

        params.require(:$1).permit()

    end
```
####rl-dele
```ruby
    delegate :${1:methods}, to: :${0:object}
```
####rl-dele
```ruby
    delegate :${1:methods}, to: :${2:object}, prefix: :${3:prefix}, allow_nil: ${0:allow_nil}
```
####rl-amc
```ruby
    alias_method_chain :${1:method_name}, :${0:feature}
```
####rl-flash
```ruby
    flash[:${1:notice}] = '${0}'
```
####rl-habtm
```ruby
    has_and_belongs_to_many :${1:object}, join_table: '${2:table_name}', foreign_key: '${3}_id'
```
####rl-hm
```ruby
    has_many :${0:object}
```
####rl-hmd
```ruby
    has_many :${1:other}s, class_name: '${2:$1}', foreign_key: '${3:$1}_id', dependent: :destroy
```
####rl-hmt
```ruby
    has_many :${1:object}, through: :${0:object}
```
####rl-ho
```ruby
    has_one :${0:object}
```
####rl-hod
```ruby
    has_one :${1:object}, dependent: :${0:destroy}
```
####rl-i18
```ruby
    I18n.t('${1:type.key}')
```
####rl-ist
```ruby
    <%= image_submit_tag('${1:agree.png}', id: '${2:id}'${0}) %>
```
####rl-log
```ruby
    Rails.logger.${1:debug} ${0}
```
####rl-log2
```ruby
    RAILS_DEFAULT_LOGGER.${1:debug} ${0}
```
####rl-logd
```ruby
    logger.debug { '${1:message}' }
```
####rl-loge
```ruby
    logger.error { '${1:message}' }
```
####rl-logf
```ruby
    logger.fatal { '${1:message}' }
```
####rl-logi
```ruby
    logger.info { '${1:message}' }
```
####rl-logw
```ruby
    logger.warn { '${1:message}' }
```
####rl-mapc
```ruby
    ${1:map}.${2:connect} '${0:controller/:action/:id}'
```
####rl-mapca
```ruby
    ${1:map}.catch_all '*${2:anything}', controller: '${3:default}', action: '${4:error}'
```
####rl-mapr
```ruby
    ${1:map}.resource :${0:resource}
```
####rl-maprs
```ruby
    ${1:map}.resources :${0:resource}
```
####rl-mapwo
```ruby
    ${1:map}.with_options ${2:controller}: '${3:thing}' do |$3|

        ${0}

    end


```
####rl-mbv
```ruby
    before_validation :${0:method}
```
####rl-mbc
```ruby
    before_create :${0:method}
```
####rl-mbu
```ruby
    before_update :${0:method}
```
####rl-mbs
```ruby
    before_save :${0:method}
```
####rl-mbd
```ruby
    before_destroy :${0:method}


```
####rl-mav
```ruby
    after_validation :${0:method}
```
####rl-maf
```ruby
    after_find :${0:method}
```
####rl-mat
```ruby
    after_touch :${0:method}
```
####rl-macr
```ruby
    after_create :${0:method}
```
####rl-mau
```ruby
    after_update :${0:method}
```
####rl-mas
```ruby
    after_save :${0:method}
```
####rl-mad
```ruby
    after_destroy :${0:method}


```
####rl-marc
```ruby
    around_create :${0:method}
```
####rl-maru
```ruby
    around_update :${0:method}
```
####rl-mars
```ruby
    around_save :${0:method}
```
####rl-mard
```ruby
    around_destroy :${0:method}


```
####rl-mcht
```ruby
    change_table :${1:table_name} do |t|

        ${0}

    end
```
####rl-mp
```ruby
    map(&:${0:id})
```
####rl-mrw
```ruby
    mattr_accessor :${0:attr_names}
```
####rl-oa
```ruby
    order('${0:field}')
```
####rl-od
```ruby
    order('${0:field} DESC')
```
####rl-pa
```ruby
    params[:${1:id}]
```
####rl-ra
```ruby
    render action: '${0:action}'
```
####rl-ral
```ruby
    render action: '${1:action}', layout: '${0:layoutname}'
```
####rl-rest
```ruby
    respond_to do |format|

        format.${1:html} { ${0} }

    end
```
####rl-rf
```ruby
    render file: '${0:filepath}'
```
####rl-rfu
```ruby
    render file: '${1:filepath}', use_full_path: ${0:false}
```
####rl-ri
```ruby
    render inline: "${0:<%= 'hello' %>}"
```
####rl-ril
```ruby
    render inline: "${1:<%= 'hello' %>}", locals: { ${2:name}: '${3:value}'${0} }
```
####rl-rit
```ruby
    render inline: "${1:<%= 'hello' %>}", type: ${0::rxml}
```
####rl-rjson
```ruby
    render json: '${0:text to render}'
```
####rl-rl
```ruby
    render layout: '${0:layoutname}'
```
####rl-rn
```ruby
    render nothing: ${0:true}
```
####rl-rns
```ruby
    render nothing: ${1:true}, status: ${0:401}
```
####rl-rp
```ruby
    render partial: '${0:item}'
```
####rl-rpc
```ruby
    render partial: '${1:item}', collection: ${0:@$1s}
```
####rl-rpl
```ruby
    render partial: '${1:item}', locals: { ${2:$1}: ${0:@$1} }
```
####rl-rpo
```ruby
    render partial: '${1:item}', object: ${0:@$1}
```
####rl-rps
```ruby
    render partial: '${1:item}', status: ${0:500}
```
####rl-rt
```ruby
    render text: '${0:text to render}'
```
####rl-rtl
```ruby
    render text: '${1:text to render}', layout: '${0:layoutname}'
```
####rl-rtlt
```ruby
    render text: '${1:text to render}', layout: ${0:true}
```
####rl-rts
```ruby
    render text: '${1:text to render}', status: ${0:401}
```
####rl-ru
```ruby
    render :update do |${1:page}|

        $1.${0}

    end
```
####rl-rxml
```ruby
    render xml: '${0:text to render}'
```
####rl-sc
```ruby
    scope :${1:name}, -> { where(${2:field}: ${0:value}) }
```
####rl-sl
```ruby
    scope :${1:name}, lambda do |${2:value}|

        where('${3:field = ?}', ${0:value})

    end
```
####rl-sha1
```ruby
    Digest::SHA1.hexdigest(${0:string})
```
####rl-sweeper
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
####rl-va
```ruby
    validates_associated :${0:attribute}
```
####rl-va
```ruby
    validates :${0:terms}, acceptance: true
```
####rl-vc
```ruby
    validates :${0:attribute}, confirmation: true
```
####rl-ve
```ruby
    validates :${1:attribute}, exclusion: { in: ${0:%w( mov avi )} }
```
####rl-vf
```ruby
    validates :${1:attribute}, format: { with: /${0:regex}/ }
```
####rl-vi
```ruby
    validates :${1:attribute}, inclusion: { in: %w(${0: mov avi }) }
```
####rl-vl
```ruby
    validates :${1:attribute}, length: { in: ${2:3}..${0:20} }
```
####rl-vn
```ruby
    validates :${0:attribute}, numericality: true
```
####rl-vp
```ruby
    validates :${0:attribute}, presence: true
```
####rl-vu
```ruby
    validates :${0:attribute}, uniqueness: true
```
####rl-format
```ruby
    format.${1:js|xml|html} { ${0} }
```
####rl-wc
```ruby
    where(${1:'conditions'}${0:, bind_var})
```
####rl-wf
```ruby
    where(${1:field}: ${0:value})
```
####rl-xdelete
```ruby
    xhr :delete, :${1:destroy}, id: ${2:1}
```
####rl-xget
```ruby
    xhr :get, :${1:show}, id: ${2:1}
```
####rl-xpost
```ruby
    xhr :post, :${1:create}, ${2:object}: ${3:object}
```
####rl-xput
```ruby
    xhr :put, :${1:update}, id: ${2:1}, ${3:object}: ${4:object}
```
####rl-test
```ruby
    test '${1:should do something}' do

        ${0}

    end
```
####rl-mac
```ruby
    add_column :${1:table_name}, :${2:column_name}, :${0:data_type}
```
####rl-mai
```ruby
    add_index :${1:table_name}, :${0:column_name}
```
####rl-mrc
```ruby
    remove_column :${1:table_name}, :${0:column_name}
```
####rl-mrnc
```ruby
    rename_column :${1:table_name}, :${2:old_column_name}, :${0:new_column_name}
```
####rl-mcc
```ruby
    change_column :${1:table}, :${2:column}, :${0:type}
```
####rl-mnc
```ruby
    t.${1:string} :${2:title}${3:, null: false}
```
####rl-mct
```ruby
    create_table :${1:table_name} do |t|

        ${0}

    end
```
####rl-trc
```ruby
    t.remove :${0:column}
```
####rl-tre
```ruby
    t.rename :${1:old_column_name}, :${2:new_column_name}

    ${0}
```
####rl-tref
```ruby
    t.references :${0:model}
```
####rl-tcb
```ruby
    t.boolean :${1:title}

    ${0}
```
####rl-tcbi
```ruby
    t.binary :${1:title}, limit: ${2:2}.megabytes

    ${0}
```
####rl-tcd
```ruby
    t.decimal :${1:title}, precision: ${2:10}, scale: ${3:2}

    ${0}
```
####rl-tcda
```ruby
    t.date :${1:title}

    ${0}
```
####rl-tcdt
```ruby
    t.datetime :${1:title}

    ${0}
```
####rl-tcf
```ruby
    t.float :${1:title}

    ${0}
```
####rl-tch
```ruby
    t.change :${1:name}, :${2:string}, ${3:limit}: ${4:80}

    ${0}
```
####rl-tci
```ruby
    t.integer :${1:title}

    ${0}
```
####rl-tcl
```ruby
    t.integer :lock_version, null: false, default: 0

    ${0}
```
####rl-tcr
```ruby
    t.references :${1:taggable}, polymorphic: { default: '${2:Photo}' }

    ${0}
```
####rl-tcs
```ruby
    t.string :${1:title}

    ${0}
```
####rl-tct
```ruby
    t.text :${1:title}

    ${0}
```
####rl-tcti
```ruby
    t.time :${1:title}

    ${0}
```
####rl-tcts
```ruby
    t.timestamp :${1:title}

    ${0}
```
####rl-tctss
```ruby
    t.timestamps

    ${0}
```
####rl-isfp
```ruby
    it { should filter_param :${0:key} }
```
####rl-isrt
```ruby
    it { should redirect_to ${0:url} }
```
####rl-isrtp
```ruby
    it { should render_template ${0} }
```
####rl-isrwl
```ruby
    it { should render_with_layout ${0} }
```
####rl-isrf
```ruby
    it { should rescue_from ${0:exception} }
```
####rl-isrw
```ruby
    it { should respond_with ${0:status} }
```
####rl-isr
```ruby
    it { should route(:${1:method}, '${0:path}') }
```
####rl-isss
```ruby
    it { should set_session :${0:key} }
```
####rl-issf
```ruby
    it { should set_the_flash('${0}') }
```
####rl-isama
```ruby
    it { should allow_mass_assignment_of :${0} }
```
####rl-isav
```ruby
    it { should allow_value(${1}).for :${0} }
```
####rl-isee
```ruby
    it { should ensure_exclusion_of :${0} }
```
####rl-isei
```ruby
    it { should ensure_inclusion_of :${0} }
```
####rl-isel
```ruby
    it { should ensure_length_of :${0} }
```
####rl-isva
```ruby
    it { should validate_acceptance_of :${0} }
```
####rl-isvc
```ruby
    it { should validate_confirmation_of :${0} }
```
####rl-isvn
```ruby
    it { should validate_numericality_of :${0} }
```
####rl-isvp
```ruby
    it { should validate_presence_of :${0} }
```
####rl-isvu
```ruby
    it { should validate_uniqueness_of :${0} }
```
####rl-isana
```ruby
    it { should accept_nested_attributes_for :${0} }
```
####rl-isbt
```ruby
    it { should belong_to :${0} }
```
####rl-isbtcc
```ruby
    it { should belong_to(:${1}).counter_cache ${0:true} }
```
####rl-ishbtm
```ruby
    it { should have_and_belong_to_many :${0} }
```
####rl-isbv
```ruby
    it { should be_valid }
```
####rl-ishc
```ruby
    it { should have_db_column :${0} }
```
####rl-ishi
```ruby
    it { should have_db_index :${0} }
```
####rl-ishm
```ruby
    it { should have_many :${0} }
```
####rl-ishmt
```ruby
    it { should have_many(:${1}).through :${0} }
```
####rl-isho
```ruby
    it { should have_one :${0} }
```
####rl-ishro
```ruby
    it { should have_readonly_attribute :${0} }
```
####rl-iss
```ruby
    it { should serialize :${0} }
```
####rl-isres
```ruby
    it { should respond_to :${0} }
```
####rl-isresw
```ruby
    it { should respond_to(:${1}).with(${0}).arguments }
```
