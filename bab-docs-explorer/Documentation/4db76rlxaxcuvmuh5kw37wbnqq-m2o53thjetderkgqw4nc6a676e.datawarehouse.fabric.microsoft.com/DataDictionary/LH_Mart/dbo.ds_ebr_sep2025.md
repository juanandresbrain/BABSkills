# dbo.ds_ebr_sep2025

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CustomerNumber | varchar | 8000 | 1 |  |  |  |
| countrycode | varchar | 8000 | 1 |  |  |  |
| postalcode | varchar | 8000 | 1 |  |  |  |
| num_txns | bigint | 8 | 1 |  |  |  |
| spend_gross_amount | decimal | 17 | 1 |  |  |  |
| last_txn_actual_date | datetime2 | 8 | 1 |  |  |  |
| first_txn_actual_date | datetime2 | 8 | 1 |  |  |  |
| num_web_txns | bigint | 8 | 1 |  |  |  |
| num_retail_txns | bigint | 8 | 1 |  |  |  |
| previous_period_active | bit | 1 | 1 |  |  |  |
| current_period_active | bit | 1 | 1 |  |  |  |
| previous_period_gross_amount | decimal | 17 | 1 |  |  |  |
| current_period_gross_amount | decimal | 17 | 1 |  |  |  |
| likely_customer_birthday_date_txn_flag | bit | 1 | 1 |  |  |  |
| likely_birthday_product_txn_flag | bit | 1 | 1 |  |  |  |
| customer_status | varchar | 8000 | 1 |  |  |  |
