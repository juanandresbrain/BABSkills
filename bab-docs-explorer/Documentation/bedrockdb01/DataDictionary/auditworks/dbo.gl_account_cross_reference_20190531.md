# dbo.gl_account_cross_reference_20190531

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| gl_account_id | int | 4 | 0 |  |  |  |
| gl_account_no | nvarchar | 320 | 0 |  |  |  |
| gl_account_description | nvarchar | 100 | 1 |  |  |  |
| subledger_rollup_type | tinyint | 1 | 1 |  |  |  |
| invalid_account_flag | tinyint | 1 | 1 |  |  |  |
