# dbo.d365_weeklyonhand

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| createdon | date | 3 | 1 |  |  |  |
| style_id | varchar | 8000 | 1 |  |  |  |
| location_id | varchar | 8000 | 1 |  |  |  |
| inventory_status_id | varchar | 8000 | 1 |  |  |  |
| on_hand_units | decimal | 17 | 1 |  |  |  |
| on_hand_unit_cost | decimal | 17 | 1 |  |  |  |
| allocation_units | decimal | 17 | 1 |  |  |  |
| on_hand_cost_native_currency | varchar | 8000 | 1 |  |  |  |
| product_type | bigint | 8 | 1 |  |  |  |
| property_id | varchar | 8000 | 1 |  |  |  |
| current_retail | decimal | 9 | 1 |  |  |  |
| original_retail | decimal | 9 | 1 |  |  |  |
| onorder_retail | decimal | 9 | 1 |  |  |  |
| price_with_vat | decimal | 9 | 1 |  |  |  |
| jurisdiction_code | varchar | 8000 | 1 |  |  |  |
| dataareaid | varchar | 8000 | 1 |  |  |  |
| product_key | bigint | 8 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
| location_code | varchar | 8000 | 1 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| merch_year_wk | varchar | 8000 | 1 |  |  |  |
| price_status_id | int | 4 | 1 |  |  |  |
| on_hand_retail | int | 4 | 1 |  |  |  |
| on_hand_retail_native | int | 4 | 1 |  |  |  |
| on_hand_retail_te | int | 4 | 1 |  |  |  |
| current_retail_native | int | 4 | 1 |  |  |  |
| on_hand_cost_native | int | 4 | 1 |  |  |  |
| INS_DT | datetime2 | 8 | 1 |  |  |  |
