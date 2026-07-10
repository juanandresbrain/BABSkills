# dbo.A360_discounts

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ID | int | 4 | 0 |  |  |  |
| units | int | 4 | 1 |  |  |  |
| unit_gross_amount | numeric | 17 | 1 |  |  |  |
| transaction_id | varchar | 50 | 1 |  |  |  |
| customerNumber | varchar | 50 | 1 |  |  |  |
| certificate_no | varchar | 255 | 1 |  |  |  |
| couponNumber | varchar | 255 | 1 |  |  |  |
| coupon_desc | varchar | 255 | 1 |  |  |  |
| category | varchar | 255 | 1 |  |  |  |
| event_name | varchar | 255 | 1 |  |  |  |
