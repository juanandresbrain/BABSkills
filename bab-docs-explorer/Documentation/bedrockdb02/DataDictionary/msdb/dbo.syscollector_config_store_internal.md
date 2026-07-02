# dbo.syscollector_config_store_internal

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| parameter_name | nvarchar | 256 | 0 | YES |  |  |
| parameter_value | sql_variant | 8016 | 1 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_syscollector_cleanup_collector](../../StoredProcedures/msdb/dbo.sp_syscollector_cleanup_collector.md)
- [msdb: dbo.sp_syscollector_disable_collector](../../StoredProcedures/msdb/dbo.sp_syscollector_disable_collector.md)
- [msdb: dbo.sp_syscollector_enable_collector](../../StoredProcedures/msdb/dbo.sp_syscollector_enable_collector.md)
- [msdb: dbo.sp_syscollector_get_warehouse_connection_string](../../StoredProcedures/msdb/dbo.sp_syscollector_get_warehouse_connection_string.md)
- [msdb: dbo.sp_syscollector_run_collection_set](../../StoredProcedures/msdb/dbo.sp_syscollector_run_collection_set.md)
- [msdb: dbo.sp_syscollector_set_cache_directory](../../StoredProcedures/msdb/dbo.sp_syscollector_set_cache_directory.md)
- [msdb: dbo.sp_syscollector_set_cache_window](../../StoredProcedures/msdb/dbo.sp_syscollector_set_cache_window.md)
- [msdb: dbo.sp_syscollector_set_warehouse_database_name](../../StoredProcedures/msdb/dbo.sp_syscollector_set_warehouse_database_name.md)
- [msdb: dbo.sp_syscollector_set_warehouse_instance_name](../../StoredProcedures/msdb/dbo.sp_syscollector_set_warehouse_instance_name.md)
- [msdb: dbo.sp_syscollector_start_collection_set](../../StoredProcedures/msdb/dbo.sp_syscollector_start_collection_set.md)
- [msdb: dbo.sp_syscollector_verify_collector_state](../../StoredProcedures/msdb/dbo.sp_syscollector_verify_collector_state.md)

