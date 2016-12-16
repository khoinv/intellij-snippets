####ci_controller
```php
    <?php if ( ! defined('BASEPATH')) exit('No direct script access allowed');



    class ${1:ClassName} extends CI_Controller

    {

        function __construct()

        {

            parent::__construct();

            ${2:// code...}

        }



        function ${3:index}()

        {

            ${4:// code...}

        }

    }
```
####ci_model
```php
    <?php if ( ! defined('BASEPATH')) exit('No direct script access allowed');



    class ${1:ClassName_model} extends CI_Model

    {

        function __construct()

        {

            parent::__construct();

            ${2:// code...}

        }

    } 
```
####ci_model_crudl
```php
    <?php if ( ! defined('BASEPATH')) exit('No direct script access allowed');



    class ${1:ClassName_model} extends CI_Model

    {

        private $table = '${2:table_name}';



        function __construct()

        {

            parent::__construct();

            ${3:// code...}

        }



        public function create($data)

        {

            if($this->db->insert($this->table, $data))

                return true;

            else

                return false;

        }



        public function read($id)

        {

            return $this->db->get_where($this->table, array('id', $id))->result();

        }



        public function update($id, $data)

        {

            if($this->db->update($this->table, $data, array('id' => $id)))

                return true;

            else

                return false;

        }



        public function delete($id)

        {

            if(is_array($id))

            {

                $this->db->trans_start();

                foreach($id as $elem)

                    $this->db->delete($this->table, array('id' => $elem));

                $this->db->trans_complete();

            }

            else

            {

                if($this->db->delete($this->table, array('id' => $id)))

                    return true;

                else

                    return false;

            }

        }



        public function listRows($limit = null, $offset = 0)

        {

            if(!is_null($limit))

                $this->db->limit($limit, $offset);

            return $this->db->get($this->table)->result();

        }

    }
```
####ci_load-view
```php
    $this->load->view("${1:view_name}", $${2:data});${3}
```
####ci_db-insert
```php
    $this->db->insert("${1:table}", $${2:data});${3}
```
####ci_db-select
```php
    $this->db->select("${1:id, ...}");${2}
```
####ci_db-from
```php
    $this->db->from("${1:table}");${2}
```
####ci_db-join
```php
    $this->db->join("${1:table}", "${2:condition}", "${3:type}");${4}
```
####ci_db-where
```php
    $this->db->where("${1:key}", "${2:value}");${3}
```
####ci_db-or_where
```php
    $this->db->or_where("${1:key}", "${2:value}");${3}
```
####ci_db-get
```php
    $this->db->get("${1:table}", ${2:limit}, ${3:offset});${4}
```
####ci_db-delete
```php
    $this->db->delete("${1:table}", "${2:where}");${3}
```
####ci_db-update
```php
    $this->db->update("${1:table}", $${2:set}, $${3:where});${4}
```
####ci_input-post
```php
    $this->input->post("${1:index}");${2}
```
####ci_input-get
```php
    $this->input->get("${1:index}");${2}
```
####ci_input-cookie
```php
    $this->input->cookie("${1:index}");${2}
```
####ci_input-server
```php
    $this->input->server("${1:index}");${2}
```
####ci_input-user_agent
```php
    $this->input->user_agent();${1}
```
####ci_input-is_ajax_request
```php
    $this->input->is_ajax_request();${1}
```
####ci_input-is_cli_request
```php
    $this->input->is_cli_request();${1}
```
####ci_form_validation-set_rules
```php
    $this->form_validation->set_rules("${1:field}", "${2:label}", "${3:trim|required}");${4}
```
####ci_form_open
```php
    form_open("${1:action}");${2}
```
####ci_form_open_multipart
```php
    form_open_multipart("${1:action}");${2}
```
####ci_form_hidden
```php
    form_hidden("${1:name}", "${2:value}");${3}
```
####ci_form_input
```php
    form_input("${1:name}", "${2:value}");${3}
```
####ci_form_password
```php
    form_password("${1:name}", "${2:value}");${3}
```
####ci_form_upload
```php
    form_upload("${1:name}", "${2:value}");${3}
```
####ci_form_textarea
```php
    form_textarea("${1:name}", "${2:value}");${3}
```
####ci_form_dropdown
```php
    form_dropdown("${1:name}", $${2:options}, $${3:selected);${4}
```
####ci_form_checkbox
```php
    form_checkbox("${1:name}", "${2:value}");${3}
```
####ci_form_radio
```php
    form_radio("${1:name}", "${2:value}");${3}
```
####ci_form_submit
```php
    form_submit("${1:name}", "${2:value}");${3}
```
####ci_form_reset
```php
    form_reset("${1:name}", "${2:value}");${3}
```
####ci_form_button
```php
    form_button("${1:name}", "${2:value}");${3}
```
####ci_form_label
```php
    form_label("${1:label text}", "${2:id}");${3}
```
####ci_form_close
```php
    form_close();${1}
```
####ci_validation_errors
```php
    validation_errors();${1}
```
####ci_session_userdata
```php
    $this->session->userdata("${1:item}");${2}
```
####ci_session_set_userdata
```php
    $this->session->set_userdata($${1:array});${2}
```
####ci_session_flashdata
```php
    $this->session->flashdata("${1:item}");${2}
```
