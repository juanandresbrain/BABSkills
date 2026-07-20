# dbo.giftcard_destroy

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| alternate_merchant_number | int | 4 | 1 |  |  |  |
| Month | int | 4 | 1 |  |  |  |
| actual_date | datetime2 | 8 | 1 |  |  |  |
| account_number | varchar | 8000 | 1 |  |  |  |
| transaction_amount | float | 8 | 1 |  |  |  |
| userid | varchar | 8000 | 1 |  |  |  |
| found | bit | 1 | 1 |  |  |  |
| current_value | decimal | 9 | 1 |  |  |  |
