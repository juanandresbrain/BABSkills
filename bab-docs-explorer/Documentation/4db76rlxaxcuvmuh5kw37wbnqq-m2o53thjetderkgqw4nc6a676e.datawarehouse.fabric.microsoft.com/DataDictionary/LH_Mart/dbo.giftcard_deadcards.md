# dbo.giftcard_deadcards

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| actual_date | datetime2 | 8 | 1 |  |  |  |
| alternate_merchant_number | int | 4 | 1 |  |  |  |
| account_number | varchar | 8000 | 1 |  |  |  |
| request_code | float | 8 | 1 |  |  |  |
| description | varchar | 8000 | 1 |  |  |  |
| internal_request_code | float | 8 | 1 |  |  |  |
| transaction_amount | decimal | 9 | 1 |  |  |  |
| balance | decimal | 9 | 1 |  |  |  |
| Activation_Store | varchar | 8000 | 1 |  |  |  |
| found | bit | 1 | 1 |  |  |  |
| current_value | decimal | 9 | 1 |  |  |  |
