# dbo.uk_giftcard_sales

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| alternate_merchant_number | int | 4 | 1 |  |  |  |
| FDMS_local_timestamp | datetime | 8 | 1 |  |  |  |
| promotion_code | int | 4 | 1 |  |  |  |
| account_number | varchar | 19 | 1 |  |  |  |
| transaction_amount | money | 8 | 1 |  |  |  |
| userid | varchar | 8 | 1 |  |  |  |
| activation_month | varchar | 61 | 1 |  |  |  |
| request_code | int | 4 | 1 |  |  |  |
| internal_request_code | int | 4 | 1 |  |  |  |
| processed_date | datetime | 8 | 1 |  |  |  |
| void | bit | 1 | 1 |  |  |  |
