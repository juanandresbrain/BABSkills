# dbo.issue_list

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| issue_id | numeric | 9 | 0 | YES |  |  |
| issue_type | int | 4 | 0 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| detection_datetime | datetime | 8 | 0 |  |  |  |
| tax_level | tinyint | 1 | 0 |  |  |  |
| tax_amount_collected | money | 8 | 0 |  |  |  |
| tax_amount_expected | money | 8 | 0 |  |  |  |
| verified | tinyint | 1 | 0 |  |  |  |
| verification_message | nvarchar | 510 | 1 |  |  |  |
| verified_date | smalldatetime | 4 | 1 |  |  |  |
| verification_remark | nvarchar | 510 | 1 |  |  |  |
| verified_by_user_id | int | 4 | 1 |  |  |  |
| override_flag | tinyint | 1 | 1 |  |  |  |
| transaction_category | tinyint | 1 | 1 |  |  |  |
| line_object | smallint | 2 | 1 |  |  |  |
| line_action | tinyint | 1 | 1 |  |  |  |
| code_type | tinyint | 1 | 1 |  |  |  |
| code | smallint | 2 | 1 |  |  |  |
| gl_account_no | nvarchar | 320 | 1 |  |  |  |
| memo | nvarchar | 510 | 1 |  |  |  |
