# dbo.Sv_Schedule

**Database:** smartlook_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| object_id | int | 4 | 0 |  |  |  |
| db_group_id | int | 4 | 0 |  |  |  |
| object_type | smallint | 2 | 0 |  |  |  |
| interval_count | smallint | 2 | 0 |  |  |  |
| interval_type | smallint | 2 | 0 |  |  |  |
| start_date_time | smalldatetime | 4 | 0 |  |  |  |
| end_date_time | smalldatetime | 4 | 1 |  |  |  |
| some_days | bit | 1 | 0 |  |  |  |
| schedule_details | varchar | 255 | 1 |  |  |  |
| last_execution | smalldatetime | 4 | 1 |  |  |  |
| next_execution | smalldatetime | 4 | 0 |  |  |  |
| status | smallint | 2 | 0 |  |  |  |
| server_lock | bit | 1 | 0 |  |  |  |
| schedule_type | int | 4 | 1 |  |  |  |
| query_parameters | varchar | 255 | 1 |  |  |  |
| query_label | varchar | 80 | 1 |  |  |  |

## Referenced By Stored Procedures

- [fn_01: dbo.Sv_CompleteSchedule](../../StoredProcedures/fn_01/dbo.Sv_CompleteSchedule.md)
- [fn_01: dbo.Sv_LockSchedule](../../StoredProcedures/fn_01/dbo.Sv_LockSchedule.md)
- [fn_01: dbo.Sv_UpdateScheduleStatus](../../StoredProcedures/fn_01/dbo.Sv_UpdateScheduleStatus.md)
- [smartlook_01: dbo.Sv_CompleteSchedule](../../StoredProcedures/smartlook_01/dbo.Sv_CompleteSchedule.md)
- [smartlook_01: dbo.Sv_LockSchedule](../../StoredProcedures/smartlook_01/dbo.Sv_LockSchedule.md)
- [smartlook_01: dbo.Sv_UpdateScheduleStatus](../../StoredProcedures/smartlook_01/dbo.Sv_UpdateScheduleStatus.md)

