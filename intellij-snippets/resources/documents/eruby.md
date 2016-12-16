####er-rc
```ruby
    <% ${0} %>
```
####er-rce
```ruby
    <%= ${1} %>
```
####er-%
```ruby
    <% ${0} %>
```
####er-=
```ruby
    <%= ${1} %>
```
####er-end
```ruby
    <% end %>
```
####er-ead
```ruby
    <% ${1}.each do |${2}| %>

        ${0}

    <% end %>
```
####er-for
```ruby
    <% for ${2:item} in ${1} %>

        ${0}

    <% end %>
```
####er-rp
```ruby
    <%= render partial: '${0:item}' %>
```
####er-rpl
```ruby
    <%= render partial: '${1:item}', locals: { :${2:name} => '${3:value}'${0} } %>
```
####er-rps
```ruby
    <%= render partial: '${1:item}', status: ${0:500} %>
```
####er-rpc
```ruby
    <%= render partial: '${1:item}', collection: ${0:items} %>
```
####er-lia
```ruby
    <%= link_to '${1:link text...}', action: '${0:index}' %>
```
####er-liai
```ruby
    <%= link_to '${1:link text...}', action: '${2:edit}', id: ${0:@item} %>
```
####er-lic
```ruby
    <%= link_to '${1:link text...}', controller: '${0:items}' %>
```
####er-lica
```ruby
    <%= link_to '${1:link text...}', controller: '${2:items}', action: '${0:index}' %>
```
####er-licai
```ruby
    <%= link_to '${1:link text...}', controller: '${2:items}', action: '${3:edit}', id: ${0:@item} %>
```
####er-yield
```ruby
    <%= yield ${1::content_symbol} %>
```
####er-conf
```ruby
    <% content_for :${1:head} do %>

        ${0}

    <% end %>
```
####er-cs
```ruby
    <%= collection_select <+object+>, <+method+>, <+collection+>, <+value_method+>, <+text_method+><+, <+[options]+>, <+[html_options]+>+> %>
```
####er-ct
```ruby
    <%= content_tag '${1:DIV}', ${2:content}${0:,options} %>
```
####er-ff
```ruby
    <%= form_for @${1:model} do |f| %>

        ${0}

    <% end %>
```
####er-ffi
```ruby
    <%= ${1:f}.input :${0:attribute} %>
```
####er-ffcb
```ruby
    <%= ${1:f}.check_box :${0:attribute} %>
```
####er-ffe
```ruby
    <% error_messages_for :${1:model} %>



    <%= form_for @${2:model} do |f| %>

        ${0}

    <% end %>
```
####er-ffff
```ruby
    <%= ${1:f}.file_field :${0:attribute} %>
```
####er-ffhf
```ruby
    <%= ${1:f}.hidden_field :${0:attribute} %>
```
####er-ffl
```ruby
    <%= ${1:f}.label :${2:attribute}, '${0:$2}' %>
```
####er-ffpf
```ruby
    <%= ${1:f}.password_field :${0:attribute} %>
```
####er-ffrb
```ruby
    <%= ${1:f}.radio_button :${2:attribute}, :${0:tag_value} %>
```
####er-ffs
```ruby
    <%= ${1:f}.submit "${0:submit}" %>
```
####er-ffta
```ruby
    <%= ${1:f}.text_area :${0:attribute} %>
```
####er-fftf
```ruby
    <%= ${1:f}.text_field :${0:attribute} %>
```
####er-fields
```ruby
    <%= fields_for :${1:model}, @$1 do |${2:f}| %>

        ${0}

    <% end %>
```
####er-i18
```ruby
    I18n.t('${1:type.key}')
```
####er-it
```ruby
    <%= image_tag "${1}"${0} %>
```
####er-jit
```ruby
    <%= javascript_include_tag ${0::all} %>
```
####er-jsit
```ruby
    <%= javascript_include_tag "${0}" %>
```
####er-lim
```ruby
    <%= link_to ${1:model}.${2:name}, ${3:$1}_path(${0:$1}) %>
```
####er-linp
```ruby
    <%= link_to "${1:Link text...}", ${2:parent}_${3:child}_path(${4:@$2}, ${0:@$3}) %>
```
####er-linpp
```ruby
    <%= link_to "${1:Link text...}", ${2:parent}_${3:child}_path(${0:@$2}) %>
```
####er-lip
```ruby
    <%= link_to "${1:Link text...}", ${2:model}_path(${0:@$2}) %>
```
####er-lipp
```ruby
    <%= link_to "${1:Link text...}", ${0:model}s_path %>
```
####er-lt
```ruby
    <%= link_to "${1:name}", ${0:dest} %>
```
####er-ntc
```ruby
    <%= number_to_currency(${1}) %>
```
####er-ofcfs
```ruby
    <%= options_from_collection_for_select ${1:collection}, ${2:value_method}, ${3:text_method}, ${0:selected_value} %>
```
####er-ofs
```ruby
    <%= options_for_select ${1:collection}, ${2:value_method} %>
```
####er-rf
```ruby
    <%= render file: "${1:file}"${0} %>
```
####er-rt
```ruby
    <%= render template: "${1:file}"${0} %>
```
####er-slt
```ruby
    <%= stylesheet_link_tag ${1::all}, cache: ${0:true} %>
```
####er-sslt
```ruby
    <%= stylesheet_link_tag "${0}" %>
```
####er-if
```ruby
    <% if ${1} %>

        ${0}

    <% end %>
```
####er-ife
```ruby
    <% if ${1} %>

        ${2}

    <% else %>

        ${0}

    <% end %>
```
