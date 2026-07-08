# dbo.dave_for_jack

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | numeric | 9 | 0 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| line_sequence | numeric | 5 | 0 |  |  |  |
| reference_no | varchar | 80 | 1 |  |  |  |
| line_note | varchar | 4000 | 0 |  |  |  |
| gross_line_amount | numeric | 9 | 0 |  |  |  |
| pos_discount_amount | numeric | 9 | 0 |  |  |  |
