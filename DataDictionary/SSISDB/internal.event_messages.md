# internal.event_messages

**Database:** SSISDB  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| event_message_id | bigint | 8 | 0 | YES | YES |  |
| operation_id | bigint | 8 | 0 |  | YES |  |
| execution_path | nvarchar | -1 | 1 |  |  |  |
| package_name | nvarchar | 520 | 1 |  |  |  |
| package_location_type | nvarchar | 256 | 1 |  |  |  |
| package_path_full | nvarchar | 8000 | 1 |  |  |  |
| event_name | nvarchar | 2048 | 1 |  |  |  |
| message_source_name | nvarchar | 8000 | 1 |  |  |  |
| message_source_id | nvarchar | 76 | 1 |  |  |  |
| subcomponent_name | nvarchar | 8000 | 1 |  |  |  |
| package_path | nvarchar | -1 | 1 |  |  |  |
| threadID | int | 4 | 0 |  |  |  |
| message_code | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [SSISDB: internal.append_event_message](../../StoredProcedures/SSISDB/internal.append_event_message.md)

