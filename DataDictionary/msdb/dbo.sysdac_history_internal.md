# dbo.sysdac_history_internal

**Database:** msdb  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| action_id | int | 4 | 0 | YES |  |  |
| sequence_id | int | 4 | 0 | YES |  |  |
| instance_id | uniqueidentifier | 16 | 0 |  |  |  |
| action_type | tinyint | 1 | 0 |  |  |  |
| action_type_name | varchar | 19 | 1 |  |  |  |
| dac_object_type | tinyint | 1 | 0 |  |  |  |
| dac_object_type_name | varchar | 8 | 1 |  |  |  |
| action_status | tinyint | 1 | 0 |  |  |  |
| action_status_name | varchar | 11 | 1 |  |  |  |
| required | bit | 1 | 1 |  |  |  |
| dac_object_name_pretran | sysname | 256 | 0 |  |  |  |
| dac_object_name_posttran | sysname | 256 | 0 |  |  |  |
| sqlscript | nvarchar | -1 | 1 |  |  |  |
| payload | varbinary | -1 | 1 |  |  |  |
| comments | varchar | -1 | 0 |  |  |  |
| error_string | nvarchar | -1 | 1 |  |  |  |
| created_by | sysname | 256 | 0 |  |  |  |
| date_created | datetime | 8 | 0 |  |  |  |
| date_modified | datetime | 8 | 0 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_sysdac_delete_history](../../StoredProcedures/msdb/dbo.sp_sysdac_delete_history.md)

