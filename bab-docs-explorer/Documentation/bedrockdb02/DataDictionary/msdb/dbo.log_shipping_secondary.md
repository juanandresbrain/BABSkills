# dbo.log_shipping_secondary

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| secondary_id | uniqueidentifier | 16 | 0 | YES |  |  |
| primary_server | sysname | 256 | 0 |  |  |  |
| primary_database | sysname | 256 | 0 |  |  |  |
| backup_source_directory | nvarchar | 1000 | 0 |  |  |  |
| backup_destination_directory | nvarchar | 1000 | 0 |  |  |  |
| file_retention_period | int | 4 | 0 |  |  |  |
| copy_job_id | uniqueidentifier | 16 | 0 |  |  |  |
| restore_job_id | uniqueidentifier | 16 | 0 |  |  |  |
| monitor_server | sysname | 256 | 0 |  |  |  |
| monitor_server_security_mode | bit | 1 | 0 |  |  |  |
| user_specified_monitor | bit | 1 | 1 |  |  |  |
| last_copied_file | nvarchar | 1000 | 1 |  |  |  |
| last_copied_date | datetime | 8 | 1 |  |  |  |

