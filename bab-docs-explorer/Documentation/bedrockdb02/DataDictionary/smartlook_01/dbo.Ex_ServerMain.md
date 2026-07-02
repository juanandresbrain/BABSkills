# dbo.Ex_ServerMain

**Database:** smartlook_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| thread_index | int | 4 | 0 |  |  |  |
| sequence_number | int | 4 | 0 |  |  |  |
| job_id | int | 4 | 0 |  |  |  |
| topic_id | int | 4 | 0 |  |  |  |
| object_id | int | 4 | 0 |  |  |  |
| db_group_id | int | 4 | 0 |  |  |  |
| locked | int | 4 | 0 |  |  |  |
| scheduled_executions | int | 4 | 0 |  |  |  |
| done_executions | int | 4 | 0 |  |  |  |
| executing | bit | 1 | 0 |  |  |  |
| active | bit | 1 | 0 |  |  |  |
| in_sync | bit | 1 | 0 |  |  |  |
| auto_execute | bit | 1 | 0 |  |  |  |
| avg_duration | int | 4 | 1 |  |  |  |
| description | varchar | 255 | 1 |  |  |  |
| data | text | 16 | 1 |  |  |  |
| previous_status | tinyint | 1 | 1 |  |  |  |

## Referenced By Stored Procedures

- [fn_01: dbo.Ex_ExecutionDone](../../StoredProcedures/fn_01/dbo.Ex_ExecutionDone.md)
- [fn_01: dbo.Ex_ExecutionStart](../../StoredProcedures/fn_01/dbo.Ex_ExecutionStart.md)
- [fn_01: dbo.Ex_LockJob](../../StoredProcedures/fn_01/dbo.Ex_LockJob.md)
- [fn_01: dbo.Ex_UnLockJob](../../StoredProcedures/fn_01/dbo.Ex_UnLockJob.md)
- [fn_01: dbo.Sv_UpdateNextID](../../StoredProcedures/fn_01/dbo.Sv_UpdateNextID.md)
- [smartlook_01: dbo.Ex_ExecutionDone](../../StoredProcedures/smartlook_01/dbo.Ex_ExecutionDone.md)
- [smartlook_01: dbo.Ex_ExecutionStart](../../StoredProcedures/smartlook_01/dbo.Ex_ExecutionStart.md)
- [smartlook_01: dbo.Ex_LockJob](../../StoredProcedures/smartlook_01/dbo.Ex_LockJob.md)
- [smartlook_01: dbo.Ex_UnLockJob](../../StoredProcedures/smartlook_01/dbo.Ex_UnLockJob.md)
- [smartlook_01: dbo.Sv_UpdateNextID](../../StoredProcedures/smartlook_01/dbo.Sv_UpdateNextID.md)

