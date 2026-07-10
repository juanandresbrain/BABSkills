# dbo.discount_product_facts

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | decimal | 9 | 0 |  |  |  |
| store_key | int | 4 | 0 |  |  |  |
| date_key | int | 4 | 0 |  |  |  |
| coupon_key | int | 4 | 0 |  |  |  |
| line_object_key | int | 4 | 1 |  |  |  |
| transaction_line_seq | decimal | 5 | 1 |  |  |  |
| units | int | 4 | 1 |  |  |  |
| unit_gross_amount | decimal | 5 | 1 |  |  |  |
| reference_no | varchar | 20 | 1 |  |  |  |
| product_key | int | 4 | 1 |  |  |  |
| process_name | varchar | 50 | 1 |  |  |  |
| process_date | datetime | 8 | 1 |  |  |  |
| uid | int | 4 | 0 | YES |  |  |
| transaction_no | int | 4 | 1 |  |  |  |
