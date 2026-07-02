# dbo.import_pc_job_detail

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| job_id | int | 4 | 0 |  |  |  |
| job_step_id | smallint | 2 | 0 |  |  |  |
| time_stamp | smalldatetime | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.import_pc_batch_$sp](../../StoredProcedures/me_01/dbo.import_pc_batch_$sp.md)

