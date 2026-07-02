# dbo.Sr_JobCheckpointInfo

**Database:** smartlook_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| job_id | int | 4 | 0 | YES | YES |  |
| execution_id | int | 4 | 0 | YES |  |  |
| checkpoint_no | int | 4 | 0 | YES |  |  |
| checkpoint_info | text | 16 | 1 |  |  |  |
| record_time | datetime | 8 | 0 |  |  |  |

## Referenced By Stored Procedures

- [fn_01: dbo.Sr_JobNeedRerun](../../StoredProcedures/fn_01/dbo.Sr_JobNeedRerun.md)
- [smartlook_01: dbo.Sr_JobNeedRerun](../../StoredProcedures/smartlook_01/dbo.Sr_JobNeedRerun.md)

