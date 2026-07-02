# dbo.log_shipping_primary_databases

**Database:** msdb  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| primary_id | uniqueidentifier | 16 | 0 | YES |  |  |
| primary_database | sysname | 256 | 0 |  |  |  |
| backup_directory | nvarchar | 1000 | 0 |  |  |  |
| backup_share | nvarchar | 1000 | 0 |  |  |  |
| backup_retention_period | int | 4 | 0 |  |  |  |
| backup_job_id | uniqueidentifier | 16 | 0 |  |  |  |
| monitor_server | sysname | 256 | 0 |  |  |  |
| user_specified_monitor | bit | 1 | 1 |  |  |  |
| monitor_server_security_mode | bit | 1 | 0 |  |  |  |
| last_backup_file | nvarchar | 1000 | 1 |  |  |  |
| last_backup_date | datetime | 8 | 1 |  |  |  |
| backup_compression | tinyint | 1 | 0 |  |  |  |

