# dbo.Sr_Server

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| server_id | int | 4 | 0 | YES |  |  |
| server_name | nvarchar | 60 | 1 |  |  |  |
| any_job | bit | 1 | 0 |  |  |  |
| max_jobs | smallint | 2 | 0 |  |  |  |
| curr_status | smallint | 2 | 0 |  |  |  |
| requested_status | smallint | 2 | 1 |  |  |  |
| machine_id | int | 4 | 0 |  |  |  |
| autostart | smallint | 2 | 0 |  |  |  |
| application_module | varchar | 500 | 1 |  |  |  |
| used_for_reporting | bit | 1 | 1 |  |  |  |
| reporting_server_description | nvarchar | 100 | 1 |  |  |  |
| blackout_period_details | varchar | 255 | 1 |  |  |  |

## Referenced By Stored Procedures

- [fn_01: dbo.Sr_AddServer](../../StoredProcedures/fn_01/dbo.Sr_AddServer.md)
- [fn_01: dbo.Sr_ExecutionStart](../../StoredProcedures/fn_01/dbo.Sr_ExecutionStart.md)
- [fn_01: dbo.Sr_GetNextJob](../../StoredProcedures/fn_01/dbo.Sr_GetNextJob.md)
- [fn_01: dbo.Sr_KillJob](../../StoredProcedures/fn_01/dbo.Sr_KillJob.md)
- [fn_01: dbo.Sr_RemoveServer](../../StoredProcedures/fn_01/dbo.Sr_RemoveServer.md)
- [fn_01: dbo.Sr_StatusRequest](../../StoredProcedures/fn_01/dbo.Sr_StatusRequest.md)
- [smartlook_01: dbo.Sr_AddServer](../../StoredProcedures/smartlook_01/dbo.Sr_AddServer.md)
- [smartlook_01: dbo.Sr_ExecutionStart](../../StoredProcedures/smartlook_01/dbo.Sr_ExecutionStart.md)
- [smartlook_01: dbo.Sr_GetNextJob](../../StoredProcedures/smartlook_01/dbo.Sr_GetNextJob.md)
- [smartlook_01: dbo.Sr_KillJob](../../StoredProcedures/smartlook_01/dbo.Sr_KillJob.md)
- [smartlook_01: dbo.Sr_RemoveServer](../../StoredProcedures/smartlook_01/dbo.Sr_RemoveServer.md)
- [smartlook_01: dbo.Sr_StatusRequest](../../StoredProcedures/smartlook_01/dbo.Sr_StatusRequest.md)

