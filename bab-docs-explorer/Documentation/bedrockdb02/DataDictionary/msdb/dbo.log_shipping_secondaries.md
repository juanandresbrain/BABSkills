# dbo.log_shipping_secondaries

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| primary_id | int | 4 | 1 |  | YES |  |
| secondary_server_name | sysname | 256 | 0 |  |  |  |
| secondary_database_name | sysname | 256 | 0 |  |  |  |
| last_copied_filename | nvarchar | 1000 | 1 |  |  |  |
| last_loaded_filename | nvarchar | 1000 | 1 |  |  |  |
| last_copied_last_updated | datetime | 8 | 1 |  |  |  |
| last_loaded_last_updated | datetime | 8 | 1 |  |  |  |
| secondary_plan_id | uniqueidentifier | 16 | 1 |  |  |  |
| copy_enabled | bit | 1 | 1 |  |  |  |
| load_enabled | bit | 1 | 1 |  |  |  |
| out_of_sync_threshold | int | 4 | 1 |  |  |  |
| threshold_alert | int | 4 | 1 |  |  |  |
| threshold_alert_enabled | bit | 1 | 1 |  |  |  |
| planned_outage_start_time | int | 4 | 1 |  |  |  |
| planned_outage_end_time | int | 4 | 1 |  |  |  |
| planned_outage_weekday_mask | int | 4 | 1 |  |  |  |
| allow_role_change | bit | 1 | 1 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_add_log_shipping_secondary](../../StoredProcedures/msdb/dbo.sp_add_log_shipping_secondary.md)
- [msdb: dbo.sp_change_monitor_role](../../StoredProcedures/msdb/dbo.sp_change_monitor_role.md)
- [msdb: dbo.sp_delete_log_shipping_monitor_info](../../StoredProcedures/msdb/dbo.sp_delete_log_shipping_monitor_info.md)
- [msdb: dbo.sp_delete_log_shipping_primary](../../StoredProcedures/msdb/dbo.sp_delete_log_shipping_primary.md)
- [msdb: dbo.sp_delete_log_shipping_secondary](../../StoredProcedures/msdb/dbo.sp_delete_log_shipping_secondary.md)
- [msdb: dbo.sp_get_log_shipping_monitor_info](../../StoredProcedures/msdb/dbo.sp_get_log_shipping_monitor_info.md)
- [msdb: dbo.sp_log_shipping_monitor_restore](../../StoredProcedures/msdb/dbo.sp_log_shipping_monitor_restore.md)
- [msdb: dbo.sp_update_log_shipping_monitor_info](../../StoredProcedures/msdb/dbo.sp_update_log_shipping_monitor_info.md)

