# dbo.dave_ecard_report_purchases

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_no | int | 4 | 0 |  |  |  |
| av_transaction_id | numeric | 9 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| gross_line_amount | line_amount | 9 | 1 |  |  |  |
| reference_no | varchar | 80 | 1 |  |  |  |
| tender_total | money | 8 | 0 |  |  |  |
