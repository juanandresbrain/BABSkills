# dbo.job_debug

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| job_id | int | 4 | 0 |  |  |  |
| proc_name | nvarchar | 160 | 0 |  |  |  |
| debug_line_id | smallint | 2 | 0 |  |  |  |
| log_timestamp | smalldatetime | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.job_progress_handler_$sp](../../StoredProcedures/me_01/dbo.job_progress_handler_$sp.md)
- [ma_01: dbo.job_progress_handler_$sp](../../StoredProcedures/ma_01/dbo.job_progress_handler_$sp.md)

