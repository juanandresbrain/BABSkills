# dbo.Ex_ExecutionHistory

**Database:** smartlook_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| execution_id | int | 4 | 0 |  |  |  |
| topic_id | int | 4 | 0 |  |  |  |
| db_group_id | int | 4 | 0 |  |  |  |
| object_id | int | 4 | 0 |  |  |  |
| thread_index | int | 4 | 0 |  |  |  |
| start_datetime | datetime | 8 | 0 |  |  |  |
| end_datetime | datetime | 8 | 1 |  |  |  |
| duration | int | 4 | 1 |  |  |  |
| total_records_count | int | 4 | 1 |  |  |  |
| error_code | int | 4 | 1 |  |  |  |
| error_description | varchar | 255 | 1 |  |  |  |

## Referenced By Stored Procedures

- [fn_01: dbo.Ex_ExecutionDone](../../StoredProcedures/fn_01/dbo.Ex_ExecutionDone.md)
- [fn_01: dbo.Ex_ExecutionStart](../../StoredProcedures/fn_01/dbo.Ex_ExecutionStart.md)
- [fn_01: dbo.Sv_UpdateNextID](../../StoredProcedures/fn_01/dbo.Sv_UpdateNextID.md)
- [smartlook_01: dbo.Ex_ExecutionDone](../../StoredProcedures/smartlook_01/dbo.Ex_ExecutionDone.md)
- [smartlook_01: dbo.Ex_ExecutionStart](../../StoredProcedures/smartlook_01/dbo.Ex_ExecutionStart.md)
- [smartlook_01: dbo.Sv_UpdateNextID](../../StoredProcedures/smartlook_01/dbo.Sv_UpdateNextID.md)

