# dbo.avtransactions_2008

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | numeric | 9 | 0 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| transaction_no | int | 4 | 0 |  |  |  |
| reference_no | varchar | 80 | 1 |  |  |  |
| reference_no_for_crm | int | 4 | 1 |  |  |  |
| transaction_date | datetime | 8 | 0 |  |  |  |
| gross_line_amount | numeric | 9 | 1 |  |  |  |
