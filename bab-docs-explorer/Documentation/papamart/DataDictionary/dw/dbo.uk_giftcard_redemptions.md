# dbo.uk_giftcard_redemptions

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| alternate_merchant_number | int | 4 | 1 |  |  |  |
| request_code | int | 4 | 1 |  |  |  |
| internal_request_code | int | 4 | 1 |  |  |  |
| promotion_code | int | 4 | 1 |  |  |  |
| FDMS_local_timestamp | datetime | 8 | 1 |  |  |  |
| account_number | varchar | 19 | 1 |  |  |  |
| base_amount | money | 8 | 1 |  |  |  |
| transaction_amount | money | 8 | 1 |  |  |  |
| userid | varchar | 8 | 1 |  |  |  |
| redemption_month | varchar | 61 | 1 |  |  |  |
| processed_date | datetime | 8 | 1 |  |  |  |
| void | bit | 1 | 1 |  |  |  |
| activation_month | varchar | 6 | 1 |  |  |  |
