# dbo.store_performance

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_no | int | 4 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| net_sales_amount | money | 8 | 0 |  |  |  |
| gross_discountable_amount | money | 8 | 0 |  |  |  |
| gross_sales_units | real | 4 | 0 |  |  |  |
| gross_sales_qty | real | 4 | 0 |  |  |  |
| discount_amount | money | 8 | 0 |  |  |  |
| net_return_amount | money | 8 | 0 |  |  |  |
| net_fee_amount | money | 8 | 0 |  |  |  |
| net_sales_return_amount | money | 8 | 0 |  |  |  |
| units_per_transaction | real | 4 | 0 |  |  |  |
| net_sales_avg | money | 8 | 0 |  |  |  |
| discount_pct | money | 8 | 0 |  |  |  |
| net_return_pct | money | 8 | 0 |  |  |  |
| net_fee_pct | money | 8 | 0 |  |  |  |
| net_revenue_amount | money | 8 | 0 |  |  |  |
| first_date_of_week | smalldatetime | 4 | 1 |  |  |  |
