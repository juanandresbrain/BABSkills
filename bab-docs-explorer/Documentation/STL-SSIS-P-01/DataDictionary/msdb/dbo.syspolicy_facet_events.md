# dbo.syspolicy_facet_events

**Database:** msdb  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| management_facet_id | int | 4 | 0 |  | YES |  |
| event_name | sysname | 256 | 0 |  |  |  |
| target_type | sysname | 256 | 0 |  |  |  |
| target_type_alias | sysname | 256 | 0 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_syspolicy_dispatch_event](../../StoredProcedures/msdb/dbo.sp_syspolicy_dispatch_event.md)

