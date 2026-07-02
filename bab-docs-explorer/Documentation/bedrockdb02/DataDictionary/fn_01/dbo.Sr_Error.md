# dbo.Sr_Error

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| error_id | numeric | 13 | 0 |  |  |  |
| execution_id | int | 4 | 0 |  |  |  |
| error_code | int | 4 | 1 |  |  |  |
| exe_name | varchar | 30 | 1 |  |  |  |
| class_name | varchar | 30 | 1 |  |  |  |
| function_name | varchar | 30 | 1 |  |  |  |
| message | varchar | 255 | 1 |  |  |  |
| error_datetime | datetime | 8 | 1 |  |  |  |
| extended_message | text | 16 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingWhsePickReviewSummary](../../StoredProcedures/me_01/dbo.spMerchandisingWhsePickReviewSummary.md)
- [fn_01: dbo.Sr_ExecutionDone](../../StoredProcedures/fn_01/dbo.Sr_ExecutionDone.md)
- [fn_01: dbo.Sr_ExecutionError](../../StoredProcedures/fn_01/dbo.Sr_ExecutionError.md)
- [smartlook_01: dbo.Sr_ExecutionDone](../../StoredProcedures/smartlook_01/dbo.Sr_ExecutionDone.md)
- [smartlook_01: dbo.Sr_ExecutionError](../../StoredProcedures/smartlook_01/dbo.Sr_ExecutionError.md)

