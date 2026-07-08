# dbo.CUSTOMER

**Database:** tpcc  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| c_id | int | 4 | 0 |  |  |  |
| c_d_id | tinyint | 1 | 0 |  |  |  |
| c_w_id | int | 4 | 0 |  |  |  |
| c_discount | smallmoney | 4 | 1 |  |  |  |
| c_credit_lim | money | 8 | 1 |  |  |  |
| c_last | char | 16 | 1 |  |  |  |
| c_first | char | 16 | 1 |  |  |  |
| c_credit | char | 2 | 1 |  |  |  |
| c_balance | money | 8 | 1 |  |  |  |
| c_ytd_payment | money | 8 | 1 |  |  |  |
| c_payment_cnt | smallint | 2 | 1 |  |  |  |
| c_delivery_cnt | smallint | 2 | 1 |  |  |  |
| c_street_1 | char | 20 | 1 |  |  |  |
| c_street_2 | char | 20 | 1 |  |  |  |
| c_city | char | 20 | 1 |  |  |  |
| c_state | char | 2 | 1 |  |  |  |
| c_zip | char | 9 | 1 |  |  |  |
| c_phone | char | 16 | 1 |  |  |  |
| c_since | datetime | 8 | 1 |  |  |  |
| c_middle | char | 2 | 1 |  |  |  |
| c_data | char | 500 | 1 |  |  |  |
