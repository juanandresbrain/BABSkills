# dbo.log_shipping_monitor_primary

**Database:** msdb  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| primary_id | uniqueidentifier | 16 | 0 | YES |  |  |
| primary_server | sysname | 256 | 0 |  |  |  |
| primary_database | sysname | 256 | 0 |  |  |  |
| backup_threshold | int | 4 | 0 |  |  |  |
| threshold_alert | int | 4 | 0 |  |  |  |
| threshold_alert_enabled | bit | 1 | 0 |  |  |  |
| last_backup_file | nvarchar | 1000 | 1 |  |  |  |
| last_backup_date | datetime | 8 | 1 |  |  |  |
| last_backup_date_utc | datetime | 8 | 1 |  |  |  |
| history_retention_period | int | 4 | 0 |  |  |  |

