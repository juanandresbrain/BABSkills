# dbo.job_error

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| job_type | int | 4 | 0 |  |  |  |
| job_id | int | 4 | 0 |  |  |  |
| proc_name | nvarchar | 160 | 0 |  |  |  |
| line_id | smallint | 2 | 1 |  |  |  |
| error_timestamp | smalldatetime | 4 | 0 |  |  |  |
| sql_err_num | decimal | 17 | 1 |  |  |  |
| object_name | nvarchar | 60 | 1 |  |  |  |
| operation_name | nvarchar | 60 | 1 |  |  |  |
| error_msg | nvarchar | 4000 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.job_error_handler_$sp](../../StoredProcedures/me_01/dbo.job_error_handler_$sp.md)
- [ma_01: dbo.job_error_handler_$sp](../../StoredProcedures/ma_01/dbo.job_error_handler_$sp.md)

