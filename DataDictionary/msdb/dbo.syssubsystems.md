# dbo.syssubsystems

**Database:** msdb  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| subsystem_id | int | 4 | 0 |  |  |  |
| subsystem | nvarchar | 80 | 0 |  |  |  |
| description_id | int | 4 | 1 |  |  |  |
| subsystem_dll | nvarchar | 510 | 1 |  |  |  |
| agent_exe | nvarchar | 510 | 1 |  |  |  |
| start_entry_point | nvarchar | 60 | 1 |  |  |  |
| event_entry_point | nvarchar | 60 | 1 |  |  |  |
| stop_entry_point | nvarchar | 60 | 1 |  |  |  |
| max_worker_threads | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_enum_proxy_for_subsystem](../../StoredProcedures/msdb/dbo.sp_enum_proxy_for_subsystem.md)
- [msdb: dbo.sp_help_proxy](../../StoredProcedures/msdb/dbo.sp_help_proxy.md)
- [msdb: dbo.sp_verify_subsystem_identifiers](../../StoredProcedures/msdb/dbo.sp_verify_subsystem_identifiers.md)
- [msdb: dbo.sp_verify_subsystems](../../StoredProcedures/msdb/dbo.sp_verify_subsystems.md)

