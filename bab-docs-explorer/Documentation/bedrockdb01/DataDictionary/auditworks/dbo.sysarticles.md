# dbo.sysarticles

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| artid | int | 4 | 0 | YES |  |  |
| creation_script | nvarchar | 510 | 1 |  |  |  |
| del_cmd | nvarchar | 510 | 1 |  |  |  |
| description | nvarchar | 510 | 1 |  |  |  |
| dest_table | sysname | 256 | 0 |  |  |  |
| filter | int | 4 | 0 |  |  |  |
| filter_clause | ntext | 16 | 1 |  |  |  |
| ins_cmd | nvarchar | 510 | 1 |  |  |  |
| name | sysname | 256 | 0 |  |  |  |
| objid | int | 4 | 0 |  |  |  |
| pubid | int | 4 | 0 |  |  |  |
| pre_creation_cmd | tinyint | 1 | 0 |  |  |  |
| status | tinyint | 1 | 0 |  |  |  |
| sync_objid | int | 4 | 0 |  |  |  |
| type | tinyint | 1 | 0 |  |  |  |
| upd_cmd | nvarchar | 510 | 1 |  |  |  |
| schema_option | binary | 8 | 1 |  |  |  |
| dest_owner | sysname | 256 | 1 |  |  |  |
| ins_scripting_proc | int | 4 | 1 |  |  |  |
| del_scripting_proc | int | 4 | 1 |  |  |  |
| upd_scripting_proc | int | 4 | 1 |  |  |  |
| custom_script | nvarchar | 4096 | 1 |  |  |  |
| fire_triggers_on_snapshot | bit | 1 | 0 |  |  |  |
