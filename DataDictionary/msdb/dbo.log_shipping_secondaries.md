# dbo.log_shipping_secondaries

**Database:** msdb  

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

