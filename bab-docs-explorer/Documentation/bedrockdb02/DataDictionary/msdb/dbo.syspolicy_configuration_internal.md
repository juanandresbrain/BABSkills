# dbo.syspolicy_configuration_internal

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| name | sysname | 256 | 0 | YES |  |  |
| current_value | sql_variant | 8016 | 0 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_syspolicy_create_purge_job](../../StoredProcedures/msdb/dbo.sp_syspolicy_create_purge_job.md)
- [msdb: dbo.sp_syspolicy_set_config_enabled](../../StoredProcedures/msdb/dbo.sp_syspolicy_set_config_enabled.md)
- [msdb: dbo.sp_syspolicy_set_config_history_retention](../../StoredProcedures/msdb/dbo.sp_syspolicy_set_config_history_retention.md)
- [msdb: dbo.sp_syspolicy_set_log_on_success](../../StoredProcedures/msdb/dbo.sp_syspolicy_set_log_on_success.md)

