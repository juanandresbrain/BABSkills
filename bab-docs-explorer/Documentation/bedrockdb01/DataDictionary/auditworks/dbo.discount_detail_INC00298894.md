# dbo.discount_detail_INC00298894

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | tran_id_datatype | 9 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| applied_by_line_id | numeric | 5 | 0 |  |  |  |
| pos_discount_level | smallint | 2 | 0 |  |  |  |
| pos_discount_type | smallint | 2 | 0 |  |  |  |
| pos_discount_amount | line_amount | 9 | 0 |  |  |  |
| applied_flag | tinyint | 1 | 0 |  |  |  |
| pos_discount_serial_no | nvarchar | 40 | 1 |  |  |  |
