# dbo.if_discount_detail_20230402

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| if_entry_no | if_entry_datatype | 9 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| applied_by_line_id | numeric | 9 | 0 |  |  |  |
| pos_discount_level | smallint | 2 | 0 |  |  |  |
| pos_discount_type | smallint | 2 | 0 |  |  |  |
| pos_discount_amount | line_amount_18_4 | 9 | 0 |  |  |  |
| applied_flag | tinyint | 1 | 0 |  |  |  |
| pos_discount_serial_no | nvarchar | 40 | 1 |  |  |  |
