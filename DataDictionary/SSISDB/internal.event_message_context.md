# internal.event_message_context

**Database:** SSISDB  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| context_id | bigint | 8 | 0 | YES |  |  |
| operation_id | bigint | 8 | 0 |  | YES |  |
| event_message_id | bigint | 8 | 0 |  | YES |  |
| context_depth | int | 4 | 1 |  |  |  |
| package_path | nvarchar | -1 | 1 |  |  |  |
| context_type | smallint | 2 | 1 |  |  |  |
| context_source_name | nvarchar | 8000 | 1 |  |  |  |
| context_source_id | nvarchar | 76 | 1 |  |  |  |
| property_name | nvarchar | 8000 | 1 |  |  |  |
| property_value | sql_variant | 8016 | 1 |  |  |  |

## Referenced By Stored Procedures

- [SSISDB: internal.append_message_context](../../StoredProcedures/SSISDB/internal.append_message_context.md)

