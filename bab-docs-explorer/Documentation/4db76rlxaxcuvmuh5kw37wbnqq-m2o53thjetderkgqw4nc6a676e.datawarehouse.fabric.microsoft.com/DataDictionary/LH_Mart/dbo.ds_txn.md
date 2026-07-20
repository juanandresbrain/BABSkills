# dbo.ds_txn

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | int | 4 | 1 |  |  |  |
| is_web_txn | bit | 1 | 1 |  |  |  |
| customernumber | varchar | 8000 | 1 |  |  |  |
| actual_date | datetime2 | 8 | 1 |  |  |  |
| actual_date_day_only | date | 3 | 1 |  |  |  |
| ModeAge | decimal | 5 | 1 |  |  |  |
| ModeCalculatedBirthDate | date | 3 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
| demo_postal_code | varchar | 8000 | 1 |  |  |  |
| units | bigint | 8 | 1 |  |  |  |
| gross_amount | decimal | 9 | 1 |  |  |  |
| net_amount | decimal | 9 | 1 |  |  |  |
| has_birthday_bear | bit | 1 | 1 |  |  |  |
| is_party_txn | bit | 1 | 1 |  |  |  |
| has_mini_bean | bit | 1 | 1 |  |  |  |
| disc_amount | decimal | 9 | 1 |  |  |  |
| ext_cost | decimal | 17 | 1 |  |  |  |
| net_margin | decimal | 17 | 1 |  |  |  |
| coupon_desc | varchar | 8000 | 1 |  |  |  |
| coupon_key | varchar | 8000 | 1 |  |  |  |
