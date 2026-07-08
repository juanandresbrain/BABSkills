# dbo.tmpTransactionLinesCurrentView

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | numeric | 9 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| line_sequence | numeric | 5 | 0 |  |  |  |
| line_object_type | tinyint | 1 | 1 |  |  |  |
| line_object | smallint | 2 | 0 |  |  |  |
| line_action | tinyint | 1 | 0 |  |  |  |
| gross_line_amount | numeric | 9 | 0 |  |  |  |
| pos_discount_amount | numeric | 9 | 0 |  |  |  |
| db_cr_none | smallint | 2 | 0 |  |  |  |
| reference_type | tinyint | 1 | 0 |  |  |  |
| reference_no | nvarchar | 160 | 1 |  |  |  |
| voiding_reversal_flag | smallint | 2 | 0 |  |  |  |
