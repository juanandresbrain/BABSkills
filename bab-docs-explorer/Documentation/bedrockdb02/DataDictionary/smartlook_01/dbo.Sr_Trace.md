# dbo.Sr_Trace

**Database:** smartlook_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| trace_id | numeric | 13 | 0 |  |  |  |
| execution_id | int | 4 | 1 |  |  |  |
| exe_name | varchar | 30 | 1 |  |  |  |
| class_name | varchar | 30 | 1 |  |  |  |
| function_name | varchar | 30 | 1 |  |  |  |
| message | varchar | 255 | 1 |  |  |  |
| indent_level | int | 4 | 1 |  |  |  |
| trace_datetime | datetime | 8 | 1 |  |  |  |
| extended_message | text | 16 | 1 |  |  |  |
| severity | smallint | 2 | 0 |  |  |  |

## Referenced By Stored Procedures

- [fn_01: dbo.Sr_CleanTrace](../../StoredProcedures/fn_01/dbo.Sr_CleanTrace.md)
- [fn_01: dbo.Sr_DebugTrace](../../StoredProcedures/fn_01/dbo.Sr_DebugTrace.md)
- [fn_01: dbo.Sr_TraceError](../../StoredProcedures/fn_01/dbo.Sr_TraceError.md)
- [smartlook_01: dbo.Sr_DebugTrace](../../StoredProcedures/smartlook_01/dbo.Sr_DebugTrace.md)
- [smartlook_01: dbo.Sr_TraceError](../../StoredProcedures/smartlook_01/dbo.Sr_TraceError.md)

