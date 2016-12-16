####sql-tbl
```sql
    create table ${1:table} (

        ${0:columns}

    );
```
####sql-col
```sql
    ${1:name}    ${2:type}    ${3:default ''}    ${0:not null}
```
####sql-ccol
```sql
    ${1:name}    varchar2(${2:size})    ${3:default ''}    ${0:not null}
```
####sql-ncol
```sql
    ${1:name}    number    ${3:default 0}    ${0:not null}
```
####sql-dcol
```sql
    ${1:name}    date    ${3:default sysdate}    ${0:not null}
```
####sql-ind
```sql
    create index ${0:$1_$2} on ${1:table}(${2:column});
```
####sql-uind
```sql
    create unique index ${1:name} on ${2:table}(${0:column});
```
####sql-tblcom
```sql
    comment on table ${1:table} is '${0:comment}';
```
####sql-colcom
```sql
    comment on column ${1:table}.${2:column} is '${0:comment}';
```
####sql-addcol
```sql
    alter table ${1:table} add (${2:column} ${0:type});
```
####sql-seq
```sql
    create sequence ${1:name} start with ${2:1} increment by ${3:1} minvalue ${0:1};
```
