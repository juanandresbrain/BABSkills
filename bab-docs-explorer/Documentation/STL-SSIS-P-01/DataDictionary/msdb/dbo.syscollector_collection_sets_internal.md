# dbo.syscollector_collection_sets_internal

**Database:** msdb  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| collection_set_id | int | 4 | 0 | YES |  |  |
| collection_set_uid | uniqueidentifier | 16 | 0 |  |  |  |
| schedule_uid | uniqueidentifier | 16 | 1 |  |  |  |
| name | sysname | 256 | 0 |  |  |  |
| name_id | int | 4 | 1 |  |  |  |
| target | nvarchar | -1 | 1 |  |  |  |
| is_running | bit | 1 | 0 |  |  |  |
| proxy_id | int | 4 | 1 |  | YES |  |
| is_system | bit | 1 | 0 |  |  |  |
| collection_job_id | uniqueidentifier | 16 | 1 |  | YES |  |
| upload_job_id | uniqueidentifier | 16 | 1 |  | YES |  |
| collection_mode | smallint | 2 | 0 |  |  |  |
| logging_level | smallint | 2 | 0 |  |  |  |
| description | nvarchar | 8000 | 1 |  |  |  |
| description_id | int | 4 | 1 |  |  |  |
| days_until_expiration | smallint | 2 | 0 |  |  |  |
| dump_on_any_error | bit | 1 | 0 |  |  |  |
| dump_on_codes | nvarchar | -1 | 1 |  |  |  |

