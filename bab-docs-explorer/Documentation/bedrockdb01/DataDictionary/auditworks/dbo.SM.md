# dbo.SM

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | numeric | 9 | 0 |  |  |  |
| tax_level | tinyint | 1 | 0 |  |  |  |
| av_mod_flag | int | 4 | 1 |  |  |  |
| max_tax_paid_flag | tinyint | 1 | 1 |  |  |  |
| total_expected | numeric | 17 | 1 |  |  |  |
| total_collected | numeric | 17 | 1 |  |  |  |
| total_net_amount | numeric | 17 | 1 |  |  |  |
| total_positive_amt | numeric | 17 | 1 |  |  |  |
| total_negative_amt | numeric | 17 | 1 |  |  |  |
| row_count | int | 4 | 1 |  |  |  |
