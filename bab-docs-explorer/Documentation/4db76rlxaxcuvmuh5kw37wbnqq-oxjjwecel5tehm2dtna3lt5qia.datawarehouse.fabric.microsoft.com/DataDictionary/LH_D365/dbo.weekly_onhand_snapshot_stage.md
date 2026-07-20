# dbo.weekly_onhand_snapshot_stage

**Database:** LH_D365  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| createdon | date | 3 | 1 |  |  |  |
| style_id | varchar | 8000 | 1 |  |  |  |
| location_id | varchar | 8000 | 1 |  |  |  |
| inventory_status_id | varchar | 8000 | 1 |  |  |  |
| on_hand_units | float | 8 | 1 |  |  |  |
| on_hand_unit_cost | float | 8 | 1 |  |  |  |
| allocation_units | float | 8 | 1 |  |  |  |
| on_hand_cost_native_currency | varchar | 8000 | 1 |  |  |  |
| product_type | varchar | 8000 | 1 |  |  |  |
| property_id | varchar | 8000 | 1 |  |  |  |
| current_retail | float | 8 | 1 |  |  |  |
| original_retail | float | 8 | 1 |  |  |  |
| onorder_retail | varchar | 8000 | 1 |  |  |  |
| price_with_vat | varchar | 8000 | 1 |  |  |  |
| jurisdiction_code | varchar | 8000 | 1 |  |  |  |
| dataareaid | varchar | 8000 | 1 |  |  |  |
| product_key | varchar | 8000 | 1 |  |  |  |
| store_key | varchar | 8000 | 1 |  |  |  |
| location_code | varchar | 8000 | 1 |  |  |  |
| date_key | bigint | 8 | 1 |  |  |  |
| merch_year_wk | varchar | 8000 | 1 |  |  |  |
| price_status_id | varchar | 8000 | 1 |  |  |  |
| on_hand_retail | float | 8 | 1 |  |  |  |
| on_hand_retail_native | float | 8 | 1 |  |  |  |
| on_hand_retail_te | float | 8 | 1 |  |  |  |
| current_retail_native | float | 8 | 1 |  |  |  |
| on_hand_cost_native | float | 8 | 1 |  |  |  |
| INS_DT | datetime2 | 8 | 1 |  |  |  |
