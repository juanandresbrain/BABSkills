# dbo.IHarticles

**Database:** CRDM_Distributor  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| article_id | int | 4 | 0 | YES |  |  |
| name | sysname | 256 | 0 |  |  |  |
| publication_id | smallint | 2 | 0 |  |  |  |
| table_id | int | 4 | 0 |  |  |  |
| publisher_id | smallint | 2 | 0 |  |  |  |
| creation_script | nvarchar | 510 | 1 |  |  |  |
| del_cmd | nvarchar | 510 | 1 |  |  |  |
| filter | int | 4 | 0 |  |  |  |
| filter_clause | ntext | 16 | 1 |  |  |  |
| ins_cmd | nvarchar | 510 | 1 |  |  |  |
| pre_creation_cmd | tinyint | 1 | 0 |  |  |  |
| status | tinyint | 1 | 0 |  |  |  |
| type | tinyint | 1 | 0 |  |  |  |
| upd_cmd | nvarchar | 510 | 1 |  |  |  |
| schema_option | binary | 8 | 1 |  |  |  |
| dest_owner | sysname | 256 | 1 |  |  |  |
| dest_table | sysname | 256 | 0 |  |  |  |
| tablespace_name | nvarchar | 510 | 1 |  |  |  |
| objid | int | 4 | 1 |  |  |  |
| sync_objid | int | 4 | 1 |  |  |  |
| description | nvarchar | 510 | 1 |  |  |  |
| publisher_status | int | 4 | 1 |  |  |  |
| article_view_owner | nvarchar | 510 | 1 |  |  |  |
| article_view | nvarchar | 510 | 1 |  |  |  |
| ins_scripting_proc | int | 4 | 1 |  |  |  |
| del_scripting_proc | int | 4 | 1 |  |  |  |
| upd_scripting_proc | int | 4 | 1 |  |  |  |
| custom_script | nvarchar | 4096 | 1 |  |  |  |
| fire_triggers_on_snapshot | bit | 1 | 0 |  |  |  |
| instance_id | int | 4 | 0 |  |  |  |
| use_default_datatypes | bit | 1 | 0 |  |  |  |
