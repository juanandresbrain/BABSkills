# dbo.syspolicy_execution_internal

**Database:** msdb  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| policy_id | int | 4 | 1 |  |  |  |
| synchronous | bit | 1 | 1 |  |  |  |
| event_data | xml | -1 | 1 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_syspolicy_dispatch_event](../../StoredProcedures/msdb/dbo.sp_syspolicy_dispatch_event.md)

