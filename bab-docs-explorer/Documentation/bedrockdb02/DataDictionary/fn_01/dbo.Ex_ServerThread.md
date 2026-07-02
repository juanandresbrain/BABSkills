# dbo.Ex_ServerThread

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| thread_index | int | 4 | 0 | YES |  |  |
| active | bit | 1 | 0 |  |  |  |
| curr_status | smallint | 2 | 0 |  |  |  |
| curr_execution_id | int | 4 | 1 |  |  |  |
| requested_status | smallint | 2 | 1 |  |  |  |
| curr_pid | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [fn_01: dbo.Ex_AddThread](../../StoredProcedures/fn_01/dbo.Ex_AddThread.md)
- [fn_01: dbo.Ex_ExecutionStart](../../StoredProcedures/fn_01/dbo.Ex_ExecutionStart.md)
- [fn_01: dbo.Ex_StatusRequest](../../StoredProcedures/fn_01/dbo.Ex_StatusRequest.md)
- [smartlook_01: dbo.Ex_AddThread](../../StoredProcedures/smartlook_01/dbo.Ex_AddThread.md)
- [smartlook_01: dbo.Ex_ExecutionStart](../../StoredProcedures/smartlook_01/dbo.Ex_ExecutionStart.md)
- [smartlook_01: dbo.Ex_StatusRequest](../../StoredProcedures/smartlook_01/dbo.Ex_StatusRequest.md)

