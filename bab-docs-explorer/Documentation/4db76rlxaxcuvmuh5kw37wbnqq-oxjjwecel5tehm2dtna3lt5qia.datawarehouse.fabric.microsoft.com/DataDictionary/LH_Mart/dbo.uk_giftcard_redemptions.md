# dbo.uk_giftcard_redemptions

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| alternate_merchant_number | int | 4 | 1 |  |  |  |
| request_code | int | 4 | 1 |  |  |  |
| internal_request_code | int | 4 | 1 |  |  |  |
| promotion_code | int | 4 | 1 |  |  |  |
| FDMS_local_timestamp | datetime2 | 8 | 1 |  |  |  |
| account_number | varchar | 8000 | 1 |  |  |  |
| base_amount | decimal | 9 | 1 |  |  |  |
| transaction_amount | decimal | 9 | 1 |  |  |  |
| userid | varchar | 8000 | 1 |  |  |  |
| redemption_month | varchar | 8000 | 1 |  |  |  |
| processed_date | datetime2 | 8 | 1 |  |  |  |
| void | bit | 1 | 1 |  |  |  |
| activation_month | varchar | 8000 | 1 |  |  |  |
