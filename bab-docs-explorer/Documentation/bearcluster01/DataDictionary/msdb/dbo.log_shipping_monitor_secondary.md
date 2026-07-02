# dbo.log_shipping_monitor_secondary

**Database:** msdb  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| secondary_server | sysname | 256 | 0 |  |  |  |
| secondary_database | sysname | 256 | 0 | YES |  |  |
| secondary_id | uniqueidentifier | 16 | 0 | YES |  |  |
| primary_server | sysname | 256 | 0 |  |  |  |
| primary_database | sysname | 256 | 0 |  |  |  |
| restore_threshold | int | 4 | 0 |  |  |  |
| threshold_alert | int | 4 | 0 |  |  |  |
| threshold_alert_enabled | bit | 1 | 0 |  |  |  |
| last_copied_file | nvarchar | 1000 | 1 |  |  |  |
| last_copied_date | datetime | 8 | 1 |  |  |  |
| last_copied_date_utc | datetime | 8 | 1 |  |  |  |
| last_restored_file | nvarchar | 1000 | 1 |  |  |  |
| last_restored_date | datetime | 8 | 1 |  |  |  |
| last_restored_date_utc | datetime | 8 | 1 |  |  |  |
| last_restored_latency | int | 4 | 1 |  |  |  |
| history_retention_period | int | 4 | 0 |  |  |  |

