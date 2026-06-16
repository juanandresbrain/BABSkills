# internal.operation_messages

**Database:** SSISDB  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| operation_message_id | bigint | 8 | 0 | YES |  |  |
| operation_id | bigint | 8 | 0 |  | YES |  |
| message_time | datetimeoffset | 10 | 0 |  |  |  |
| message_type | smallint | 2 | 0 |  |  |  |
| message_source_type | smallint | 2 | 1 |  |  |  |
| message | nvarchar | -1 | 1 |  |  |  |
| extended_info_id | bigint | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [SSISDB: catalog.startup](../../StoredProcedures/SSISDB/catalog.startup.md)
- [SSISDB: internal.append_event_message](../../StoredProcedures/SSISDB/internal.append_event_message.md)
- [SSISDB: internal.append_operation_message](../../StoredProcedures/SSISDB/internal.append_operation_message.md)
- [SSISDB: internal.insert_message_caught](../../StoredProcedures/SSISDB/internal.insert_message_caught.md)

