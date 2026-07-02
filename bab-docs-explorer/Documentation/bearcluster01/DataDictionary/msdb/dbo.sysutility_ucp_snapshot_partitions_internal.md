# dbo.sysutility_ucp_snapshot_partitions_internal

**Database:** msdb  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| time_id | int | 4 | 1 |  |  |  |
| latest_consistent_snapshot_id | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_sysutility_ucp_remove](../../StoredProcedures/msdb/dbo.sp_sysutility_ucp_remove.md)

