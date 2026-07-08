# dbo.audit_dw_extradiscounts_oursblanc_20101026

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_no | int | 4 | 1 |  |  |  |
| transaction_date | datetime | 8 | 1 |  |  |  |
| transaction_id | numeric | 9 | 1 |  |  |  |
| line_id | numeric | 5 | 1 |  |  |  |
| line_sequence | numeric | 5 | 1 |  |  |  |
| gross_line_amount | numeric | 17 | 1 |  |  |  |
| pos_discount_amount | numeric | 17 | 1 |  |  |  |
