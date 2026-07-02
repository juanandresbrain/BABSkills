# dbo.Sr_History

**Database:** smartlook_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| execution_id | int | 4 | 0 |  |  |  |
| job_id | int | 4 | 0 |  |  |  |
| server_id | int | 4 | 0 |  |  |  |
| thread_index | int | 4 | 0 |  |  |  |
| topic_id | int | 4 | 0 |  |  |  |
| db_group_id | int | 4 | 0 |  |  |  |
| object_id | int | 4 | 0 |  |  |  |
| include_in_average | bit | 1 | 0 |  |  |  |
| start_datetime | datetime | 8 | 0 |  |  |  |
| end_datetime | datetime | 8 | 1 |  |  |  |
| duration | int | 4 | 1 |  |  |  |
| sucessful | bit | 1 | 0 |  |  |  |
| exit_code | int | 4 | 1 |  |  |  |
| parent_job_id | int | 4 | 0 |  |  |  |
| machine_id | int | 4 | 0 |  |  |  |
| trace | smallint | 2 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingWhsePickReviewSummary](../../StoredProcedures/me_01/dbo.spMerchandisingWhsePickReviewSummary.md)
- [fn_01: dbo.Cs_GetCsFileID](../../StoredProcedures/fn_01/dbo.Cs_GetCsFileID.md)
- [fn_01: dbo.Cs_TransmissionStart](../../StoredProcedures/fn_01/dbo.Cs_TransmissionStart.md)
- [fn_01: dbo.Ex_OutputStat_ByJob](../../StoredProcedures/fn_01/dbo.Ex_OutputStat_ByJob.md)
- [fn_01: dbo.Sr_ExecutionDone](../../StoredProcedures/fn_01/dbo.Sr_ExecutionDone.md)
- [fn_01: dbo.Sr_ExecutionStart](../../StoredProcedures/fn_01/dbo.Sr_ExecutionStart.md)
- [fn_01: dbo.Sr_HistoryCleanup](../../StoredProcedures/fn_01/dbo.Sr_HistoryCleanup.md)
- [fn_01: dbo.Sr_KillJob](../../StoredProcedures/fn_01/dbo.Sr_KillJob.md)
- [fn_01: dbo.Sr_MachineDone](../../StoredProcedures/fn_01/dbo.Sr_MachineDone.md)
- [fn_01: dbo.Sr_MachineDoneInterrupted](../../StoredProcedures/fn_01/dbo.Sr_MachineDoneInterrupted.md)
- [fn_01: dbo.Sr_MachineStart](../../StoredProcedures/fn_01/dbo.Sr_MachineStart.md)
- [fn_01: dbo.Sr_ServerDone](../../StoredProcedures/fn_01/dbo.Sr_ServerDone.md)
- [fn_01: dbo.Sr_ServerStart](../../StoredProcedures/fn_01/dbo.Sr_ServerStart.md)
- [fn_01: dbo.Sv_UpdateNextID](../../StoredProcedures/fn_01/dbo.Sv_UpdateNextID.md)
- [smartlook_01: dbo.Cs_GetCsFileID](../../StoredProcedures/smartlook_01/dbo.Cs_GetCsFileID.md)
- [smartlook_01: dbo.Cs_TransmissionStart](../../StoredProcedures/smartlook_01/dbo.Cs_TransmissionStart.md)
- [smartlook_01: dbo.Sr_ExecutionDone](../../StoredProcedures/smartlook_01/dbo.Sr_ExecutionDone.md)
- [smartlook_01: dbo.Sr_ExecutionStart](../../StoredProcedures/smartlook_01/dbo.Sr_ExecutionStart.md)
- [smartlook_01: dbo.Sr_HistoryCleanup](../../StoredProcedures/smartlook_01/dbo.Sr_HistoryCleanup.md)
- [smartlook_01: dbo.Sr_KillJob](../../StoredProcedures/smartlook_01/dbo.Sr_KillJob.md)
- [smartlook_01: dbo.Sr_MachineDone](../../StoredProcedures/smartlook_01/dbo.Sr_MachineDone.md)
- [smartlook_01: dbo.Sr_MachineDoneInterrupted](../../StoredProcedures/smartlook_01/dbo.Sr_MachineDoneInterrupted.md)
- [smartlook_01: dbo.Sr_MachineStart](../../StoredProcedures/smartlook_01/dbo.Sr_MachineStart.md)
- [smartlook_01: dbo.Sr_ServerDone](../../StoredProcedures/smartlook_01/dbo.Sr_ServerDone.md)
- [smartlook_01: dbo.Sr_ServerStart](../../StoredProcedures/smartlook_01/dbo.Sr_ServerStart.md)
- [smartlook_01: dbo.Sv_UpdateNextID](../../StoredProcedures/smartlook_01/dbo.Sv_UpdateNextID.md)

