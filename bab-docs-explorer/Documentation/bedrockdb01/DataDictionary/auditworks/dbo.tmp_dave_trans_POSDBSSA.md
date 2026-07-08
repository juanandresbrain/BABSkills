# dbo.tmp_dave_trans_POSDBSSA

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| transaction_date | datetime | 8 | 0 |  |  |  |
| transaction_no | int | 4 | 0 |  |  |  |
| line_object_type | tinyint | 1 | 0 |  |  |  |
| line_object | smallint | 2 | 0 |  |  |  |
| line_action | tinyint | 1 | 0 |  |  |  |
| gross_line_amount | numeric | 17 | 1 |  |  |  |
| count | int | 4 | 1 |  |  |  |
