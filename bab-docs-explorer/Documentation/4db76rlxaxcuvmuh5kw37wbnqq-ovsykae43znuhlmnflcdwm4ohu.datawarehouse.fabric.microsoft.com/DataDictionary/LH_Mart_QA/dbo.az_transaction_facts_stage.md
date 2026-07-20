# dbo.az_transaction_facts_stage

**Database:** LH_Mart_QA  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | varchar | 200 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| time_key | int | 4 | 1 |  |  |  |
| transaction_type_key | varchar | 8000 | 1 |  |  |  |
| currency_key | int | 4 | 1 |  |  |  |
| transaction_key | varchar | 200 | 1 |  |  |  |
| party_key | int | 4 | 1 |  |  |  |
| cashier_key | int | 4 | 1 |  |  |  |
| transaction_no | varchar | 200 | 1 |  |  |  |
| register_no | smallint | 2 | 1 |  |  |  |
| line_count | bigint | 8 | 1 |  |  |  |
| party_flag | int | 4 | 1 |  |  |  |
| GAAP_transaction_flag | int | 4 | 1 |  |  |  |
| donation_only_flag | int | 4 | 1 |  |  |  |
| giftcard_only_flag | int | 4 | 1 |  |  |  |
| party_deposit_only_flag | int | 4 | 1 |  |  |  |
| GAAP_sales_amount | decimal | 17 | 1 |  |  |  |
| net_sales_amount | decimal | 17 | 1 |  |  |  |
| total_units | bigint | 8 | 1 |  |  |  |
| unit_net_amount | decimal | 17 | 1 |  |  |  |
| unit_gross_amount | decimal | 17 | 1 |  |  |  |
| receipt_total_amount | decimal | 13 | 1 |  |  |  |
| merchandise_uga | decimal | 17 | 1 |  |  |  |
| merchandise_units | bigint | 8 | 1 |  |  |  |
| donations_units | bigint | 8 | 1 |  |  |  |
| party_deposit_units | bigint | 8 | 1 |  |  |  |
| giftcard_units | bigint | 8 | 1 |  |  |  |
| animal_units | bigint | 8 | 1 |  |  |  |
| non_animal_units | bigint | 8 | 1 |  |  |  |
| footwear_units | bigint | 8 | 1 |  |  |  |
| accessories_units | bigint | 8 | 1 |  |  |  |
| sounds_units | bigint | 8 | 1 |  |  |  |
| clothing_units | bigint | 8 | 1 |  |  |  |
| other_units | bigint | 8 | 1 |  |  |  |
| sports_units | bigint | 8 | 1 |  |  |  |
| prestuffed_units | bigint | 8 | 1 |  |  |  |
| fin_GAAP_sales_amount | decimal | 17 | 1 |  |  |  |
| upsell_discount_amount | decimal | 17 | 1 |  |  |  |
| Store_transaction_flag | int | 4 | 1 |  |  |  |
| Store_sales_amount | decimal | 17 | 1 |  |  |  |
| Store_units | bigint | 8 | 1 |  |  |  |
| fin_Store_sales_amount | decimal | 17 | 1 |  |  |  |
| Enterprise_selling_amount | decimal | 17 | 1 |  |  |  |
| Enterprise_selling_only_flag | int | 4 | 1 |  |  |  |
| Gaap_units | bigint | 8 | 1 |  |  |  |
| Enterprise_selling_units | bigint | 8 | 1 |  |  |  |
| party_master | int | 4 | 1 |  |  |  |
| ReturnUGA | decimal | 17 | 1 |  |  |  |
| ReturnUnits | bigint | 8 | 1 |  |  |  |
| isShipFromStore | int | 4 | 1 |  |  |  |
| isPickupFromStore | int | 4 | 1 |  |  |  |
| isCurbside | int | 4 | 1 |  |  |  |
| isSameDayShipt | int | 4 | 1 |  |  |  |
| WebOrderNumber | varchar | 8000 | 1 |  |  |  |
| isWebGift | int | 4 | 1 |  |  |  |
