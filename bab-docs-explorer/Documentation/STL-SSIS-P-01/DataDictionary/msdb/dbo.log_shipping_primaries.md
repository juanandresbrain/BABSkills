# dbo.log_shipping_primaries

**Database:** msdb  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| primary_id | int | 4 | 0 | YES |  |  |
| primary_server_name | sysname | 256 | 0 |  |  |  |
| primary_database_name | sysname | 256 | 0 |  |  |  |
| maintenance_plan_id | uniqueidentifier | 16 | 1 |  |  |  |
| backup_threshold | int | 4 | 0 |  |  |  |
| threshold_alert | int | 4 | 0 |  |  |  |
| threshold_alert_enabled | bit | 1 | 0 |  |  |  |
| last_backup_filename | nvarchar | 1000 | 1 |  |  |  |
| last_updated | datetime | 8 | 1 |  |  |  |
| planned_outage_start_time | int | 4 | 0 |  |  |  |
| planned_outage_end_time | int | 4 | 0 |  |  |  |
| planned_outage_weekday_mask | int | 4 | 0 |  |  |  |
| source_directory | nvarchar | 1000 | 1 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_log_shipping_monitor_backup](../../StoredProcedures/msdb/dbo.sp_log_shipping_monitor_backup.md)

