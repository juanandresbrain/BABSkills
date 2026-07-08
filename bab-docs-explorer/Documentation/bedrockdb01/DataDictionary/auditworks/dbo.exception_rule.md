# dbo.exception_rule

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| exception_rule | smallint | 2 | 0 |  |  |  |
| exception_name | nvarchar | 100 | 0 |  |  |  |
| exception_type | tinyint | 1 | 0 |  |  |  |
| transaction_line_flag | tinyint | 1 | 0 |  |  |  |
| user_id | T_LONG_INTEGER | 4 | 1 |  |  |  |
| ACTV | numeric | 5 | 0 |  |  |  |
| SQL_TXT | nvarchar | -1 | 1 |  |  |  |
| SQL_QRY | nvarchar | -1 | 1 |  |  |  |
| SQL_QRY_OBJ | text | 16 | 1 |  |  |  |
| extended_archive_days | smallint | 2 | 0 |  |  |  |
