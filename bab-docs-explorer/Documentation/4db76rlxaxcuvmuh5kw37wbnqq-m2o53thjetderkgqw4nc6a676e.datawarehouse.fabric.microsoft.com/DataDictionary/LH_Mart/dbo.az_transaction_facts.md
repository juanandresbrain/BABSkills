# dbo.az_transaction_facts

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | varchar | 8000 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| time_key | int | 4 | 1 |  |  |  |
| transaction_type_key | int | 4 | 1 |  |  |  |
| currency_key | int | 4 | 1 |  |  |  |
| transaction_key | varchar | 8000 | 1 |  |  |  |
| party_key | int | 4 | 1 |  |  |  |
| cashier_key | int | 4 | 1 |  |  |  |
| transaction_no | varchar | 8000 | 1 |  |  |  |
| register_no | int | 4 | 1 |  |  |  |
| line_count | int | 4 | 1 |  |  |  |
| party_flag | int | 4 | 1 |  |  |  |
| GAAP_transaction_flag | int | 4 | 1 |  |  |  |
| donation_only_flag | int | 4 | 1 |  |  |  |
| giftcard_only_flag | int | 4 | 1 |  |  |  |
| party_deposit_only_flag | int | 4 | 1 |  |  |  |
| GAAP_sales_amount | decimal | 9 | 1 |  |  |  |
| net_sales_amount | decimal | 9 | 1 |  |  |  |
| total_units | int | 4 | 1 |  |  |  |
| unit_net_amount | decimal | 9 | 1 |  |  |  |
| unit_gross_amount | decimal | 9 | 1 |  |  |  |
| receipt_total_amount | decimal | 9 | 1 |  |  |  |
| merchandise_uga | decimal | 9 | 1 |  |  |  |
| merchandise_units | int | 4 | 1 |  |  |  |
| donations_units | int | 4 | 1 |  |  |  |
| party_deposit_units | int | 4 | 1 |  |  |  |
| giftcard_units | int | 4 | 1 |  |  |  |
| animal_units | int | 4 | 1 |  |  |  |
| non_animal_units | int | 4 | 1 |  |  |  |
| footwear_units | int | 4 | 1 |  |  |  |
| accessories_units | int | 4 | 1 |  |  |  |
| sounds_units | int | 4 | 1 |  |  |  |
| clothing_units | int | 4 | 1 |  |  |  |
| other_units | int | 4 | 1 |  |  |  |
| sports_units | int | 4 | 1 |  |  |  |
| prestuffed_units | int | 4 | 1 |  |  |  |
| fin_GAAP_sales_amount | decimal | 9 | 1 |  |  |  |
| upsell_discount_amount | decimal | 9 | 1 |  |  |  |
| Store_transaction_flag | int | 4 | 1 |  |  |  |
| Store_sales_amount | decimal | 9 | 1 |  |  |  |
| Store_units | int | 4 | 1 |  |  |  |
| fin_Store_sales_amount | decimal | 9 | 1 |  |  |  |
| Enterprise_selling_amount | decimal | 9 | 1 |  |  |  |
| Enterprise_selling_only_flag | int | 4 | 1 |  |  |  |
| Gaap_units | int | 4 | 1 |  |  |  |
| Enterprise_selling_units | int | 4 | 1 |  |  |  |
| party_master | int | 4 | 1 |  |  |  |
| ReturnUGA | decimal | 9 | 1 |  |  |  |
| ReturnUnits | int | 4 | 1 |  |  |  |
| isShipFromStore | int | 4 | 1 |  |  |  |
| isPickupFromStore | int | 4 | 1 |  |  |  |
| isCurbside | int | 4 | 1 |  |  |  |
| isSameDayShipt | int | 4 | 1 |  |  |  |
| WebOrderNumber | varchar | 8000 | 1 |  |  |  |
| isWebGift | int | 4 | 1 |  |  |  |
