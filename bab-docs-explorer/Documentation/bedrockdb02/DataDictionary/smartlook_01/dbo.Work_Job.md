# dbo.Work_Job

**Database:** smartlook_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| job_id | int | 4 | 1 |  |  |  |
| last_date_time | smalldatetime | 4 | 1 |  |  |  |
| object_id | int | 4 | 1 |  |  |  |
| object_type | int | 4 | 1 |  |  |  |
| db_group_id | int | 4 | 1 |  |  |  |
| machine_id | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [fn_01: dbo.Sr_GetNextJob](../../StoredProcedures/fn_01/dbo.Sr_GetNextJob.md)
- [smartlook_01: dbo.Sr_GetNextJob](../../StoredProcedures/smartlook_01/dbo.Sr_GetNextJob.md)

