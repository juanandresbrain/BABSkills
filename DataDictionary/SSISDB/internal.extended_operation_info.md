# internal.extended_operation_info

**Database:** SSISDB  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| info_id | bigint | 8 | 0 | YES |  |  |
| operation_id | bigint | 8 | 0 |  | YES |  |
| object_name | nvarchar | 520 | 0 |  |  |  |
| object_type | smallint | 2 | 1 |  |  |  |
| reference_id | bigint | 8 | 1 |  |  |  |
| status | int | 4 | 0 |  |  |  |
| start_time | datetimeoffset | 10 | 0 |  |  |  |
| end_time | datetimeoffset | 10 | 1 |  |  |  |

## Referenced By Stored Procedures

- [SSISDB: catalog.startup](../../StoredProcedures/SSISDB/catalog.startup.md)
- [SSISDB: internal.sync_validation_status](../../StoredProcedures/SSISDB/internal.sync_validation_status.md)
- [SSISDB: internal.update_validation_status](../../StoredProcedures/SSISDB/internal.update_validation_status.md)

