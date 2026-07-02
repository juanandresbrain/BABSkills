# dbo.job_header_25Nov25

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| job_id | int | 4 | 0 | YES |  |  |
| job_type | int | 4 | 0 |  |  |  |
| range_start | decimal | 13 | 0 |  |  |  |
| range_end | decimal | 13 | 0 |  |  |  |
| batch_start | smallint | 2 | 0 |  |  |  |
| batch_end | smallint | 2 | 0 |  |  |  |
| start_time | smalldatetime | 4 | 1 |  |  |  |
| end_time | smalldatetime | 4 | 1 |  |  |  |
| completed_flag | bit | 1 | 0 |  |  |  |
| debug_flag | bit | 1 | 0 |  |  |  |
| dbms_job_id | decimal | 9 | 1 |  |  |  |

