# dbo.startup_error_log

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| startup_multi_currency_main_log_id | int | 4 | 0 |  |  |  |
| proc_name | nvarchar | 160 | 0 |  |  |  |
| line_id | smallint | 2 | 1 |  |  |  |
| error_timestamp | smalldatetime | 4 | 0 |  |  |  |
| sql_err_num | decimal | 17 | 1 |  |  |  |
| object_name | nvarchar | 60 | 1 |  |  |  |
| error_msg | nvarchar | 4000 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.startup_error_handler_$sp](../../StoredProcedures/me_01/dbo.startup_error_handler_$sp.md)
- [ma_01: dbo.startup_error_handler_$sp](../../StoredProcedures/ma_01/dbo.startup_error_handler_$sp.md)

