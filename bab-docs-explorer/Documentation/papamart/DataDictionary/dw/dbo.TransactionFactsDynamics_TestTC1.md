# dbo.TransactionFactsDynamics_TestTC1

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_id | int | 4 | 1 |  |  |  |
| actual_date | datetime | 8 | 1 |  |  |  |
| GAAP_sales_amount | decimal | 17 | 1 |  |  |  |
| upsell_discount_amount | money | 8 | 1 |  |  |  |
| total_discount_amount | decimal | 17 | 1 |  |  |  |
| GAAP_transaction_flag | tinyint | 1 | 1 |  |  |  |
| coupon_discount_amount | decimal | 17 | 1 |  |  |  |
