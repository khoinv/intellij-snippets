####djauto
```python
    ${1:FIELDNAME} = models.AutoField(${0})
```
####djbigint
```python
    ${1:FIELDNAME} = models.BigIntegerField(${0})
```
####djbinary
```python
    ${1:FIELDNAME} = models.BinaryField(${0})
```
####djbool
```python
    ${1:FIELDNAME} = models.BooleanField(${0:default=True})
```
####djchar
```python
    ${1:FIELDNAME} = models.CharField(max_length=${2}${0:, blank=True})
```
####djcomma
```python
    ${1:FIELDNAME} = models.CommaSeparatedIntegerField(max_length=${2}${0:, blank=True})
```
####djdate
```python
    ${1:FIELDNAME} = models.DateField(${2:auto_now_add=True, auto_now=True}${0:, blank=True, null=True})
```
####djdatetime
```python
    ${1:FIELDNAME} = models.DateTimeField(${2:auto_now_add=True, auto_now=True}${0:, blank=True, null=True})
```
####djdecimal
```python
    ${1:FIELDNAME} = models.DecimalField(max_digits=${2}, decimal_places=${0})
```
####djemail
```python
    ${1:FIELDNAME} = models.EmailField(max_length=${2:75}${0:, blank=True})
```
####djfile
```python
    ${1:FIELDNAME} = models.FileField(upload_to=${2:path/for/upload}${0:, max_length=100})
```
####djfilepath
```python
    ${1:FIELDNAME} = models.FilePathField(path=${2:"/abs/path/to/dir"}${3:, max_length=100}${4:, match="*.ext"}${5:, recursive=True}${0:, blank=True, })
```
####djfloat
```python
    ${1:FIELDNAME} = models.FloatField(${0})
```
####djimage
```python
    ${1:FIELDNAME} = models.ImageField(upload_to=${2:path/for/upload}${3:, height_field=height, width_field=width}${0:, max_length=100})
```
####djint
```python
    ${1:FIELDNAME} = models.IntegerField(${0})
```
####djip
```python
    ${1:FIELDNAME} = models.IPAddressField(${0})
```
####djnullbool
```python
    ${1:FIELDNAME} = models.NullBooleanField(${0})
```
####djposint
```python
    ${1:FIELDNAME} = models.PositiveIntegerField(${0})
```
####djpossmallint
```python
    ${1:FIELDNAME} = models.PositiveSmallIntegerField(${0})
```
####djslug
```python
    ${1:FIELDNAME} = models.SlugField(max_length=${2:50}${0:, blank=True})
```
####djsmallint
```python
    ${1:FIELDNAME} = models.SmallIntegerField(${0})
```
####djtext
```python
    ${1:FIELDNAME} = models.TextField(${0:blank=True})
```
####djtime
```python
    ${1:FIELDNAME} = models.TimeField(${2:auto_now_add=True, auto_now=True}${0:, blank=True, null=True})
```
####djurl
```python
    ${1:FIELDNAME} = models.URLField(${2:verify_exists=False}${3:, max_length=200}${0:, blank=True})
```
####djxml
```python
    ${1:FIELDNAME} = models.XMLField(schema_path=${2:None}${0:, blank=True})
```
####djfk
```python
    ${1:FIELDNAME} = models.ForeignKey(${2:OtherModel}${3:, related_name=''}${4:, limit_choices_to=}${0:, to_field=''})
```
####djm2m
```python
    ${1:FIELDNAME} = models.ManyToManyField(${2:OtherModel}${3:, related_name=''}${4:, limit_choices_to=}${5:, symmetrical=False}${6:, through=''}${0:, db_table=''})
```
####djo2o
```python
    ${1:FIELDNAME} = models.OneToOneField(${2:OtherModel}${3:, parent_link=True}${4:, related_name=''}${5:, limit_choices_to=}${0:, to_field=''})


```
####djform
```python
    class ${1:FormName}(forms.Form):

        """${2:docstring}"""

        ${0}


```
####djmodel
```python
    class ${1:ModelName}(models.Model):

        """${2:docstring}"""

        ${3}



        class Meta:

            ${4}



        def __unicode__(self):

            ${5}



        def save(self, *args, **kwargs):

            ${6}



        @models.permalink

        def get_absolute_url(self):

            return ('${7:view_or_url_name}' ${0})


```
####djmodeladmin
```python
    class ${1:ModelName}Admin(admin.ModelAdmin):

        ${0}



    admin.site.register($1, $1Admin)


```
####djtabularinline
```python
    class ${0:ModelName}Inline(admin.TabularInline):

        model = $1


```
####djstackedinline
```python
    class ${0:ModelName}Inline(admin.StackedInline):

        model = $1


```
