# dbo.ds_txn_detail

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | int | 4 | 1 |  |  |  |
| CustomerNumber | varchar | 8000 | 1 |  |  |  |
| actual_date | datetime2 | 8 | 1 |  |  |  |
| actual_date_day_only | date | 3 | 1 |  |  |  |
| product_key | int | 4 | 1 |  |  |  |
| units | int | 4 | 1 |  |  |  |
| unit_gross_amount | decimal | 5 | 1 |  |  |  |
| unit_net_amount | decimal | 5 | 1 |  |  |  |
| is_party_txn | bit | 1 | 1 |  |  |  |
| age | decimal | 5 | 1 |  |  |  |
| CalculatedBirthDate | date | 3 | 1 |  |  |  |
| animalbirthdate | date | 3 | 1 |  |  |  |
| is_birthday_bear | bit | 1 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
| store_postal_code | varchar | 8000 | 1 |  |  |  |
| is_mini_bean | bit | 1 | 1 |  |  |  |
| tdf_key | int | 4 | 1 |  |  |  |
| unit_disc_amount | decimal | 5 | 1 |  |  |  |
| ext_cost | decimal | 9 | 1 |  |  |  |
| sku | bigint | 8 | 1 |  |  |  |
