# dbo.awl_pos_tax_detail

**Database:** auditworks_work  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| entry_date_time | datetime | 8 | 0 |  |  |  |
| transaction_series | nchar | 2 | 0 |  |  |  |
| transaction_no | int | 4 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| tax_rate_id | numeric | 9 | 0 |  |  |  |
| tax_jurisdiction_id | numeric | 9 | 0 |  |  |  |
| tax_level | tinyint | 1 | 0 |  |  |  |
| tax_amount_collected | money | 8 | 0 |  |  |  |
| row_sequence_no | numeric | 9 | 0 | YES |  |  |
