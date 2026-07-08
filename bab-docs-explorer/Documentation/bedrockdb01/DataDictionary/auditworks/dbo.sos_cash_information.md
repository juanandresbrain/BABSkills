# dbo.sos_cash_information

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| cashier_no | int | 4 | 0 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| cash_sales_amount | money | 8 | 0 |  |  |  |
| cash_return_amount | money | 8 | 0 |  |  |  |
| cash_post_void_amount | money | 8 | 0 |  |  |  |
| net_petty_cash_disbursements | money | 8 | 0 |  |  |  |
