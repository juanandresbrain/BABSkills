# dbo.giftcards_redeemed_idw

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Gift Card Number | nvarchar | 510 | 1 |  |  |  |
| PSP | nvarchar | 510 | 1 |  |  |  |
| Order Number | nvarchar | 510 | 1 |  |  |  |
| Account | nvarchar | 510 | 1 |  |  |  |
| Creation Date | nvarchar | 510 | 1 |  |  |  |
| Time Zone | nvarchar | 510 | 1 |  |  |  |
| Value | money | 8 | 1 |  |  |  |
| Currency | nvarchar | 510 | 1 |  |  |  |
| Status | nvarchar | 510 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
| transaction_id | int | 4 | 1 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| currency_key | int | 4 | 1 |  |  |  |
| MID | nvarchar | 510 | 1 |  |  |  |
| dayssincelastactivation | int | 4 | 1 |  |  |  |
| dsla_date_key | int | 4 | 1 |  |  |  |
| lift_amount | money | 8 | 1 |  |  |  |
| total_tender | money | 8 | 1 |  |  |  |
| total_redemtpion | money | 8 | 1 |  |  |  |
| activation_discount_amount | money | 8 | 1 |  |  |  |
| source | nvarchar | 510 | 1 |  |  |  |
| VLVerified | bit | 1 | 1 |  |  |  |
| SendData | int | 4 | 1 |  |  |  |
