# internal.alwayson_support_state

**Database:** SSISDB  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| server_name | nvarchar | 512 | 0 | YES |  |  |
| state | tinyint | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [SSISDB: internal.add_replica_info](../../StoredProcedures/SSISDB/internal.add_replica_info.md)
- [SSISDB: internal.delete_replica_info](../../StoredProcedures/SSISDB/internal.delete_replica_info.md)
- [SSISDB: internal.refresh_replica_status](../../StoredProcedures/SSISDB/internal.refresh_replica_status.md)
- [SSISDB: internal.update_replica_info](../../StoredProcedures/SSISDB/internal.update_replica_info.md)

