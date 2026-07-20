# dbo.vwDW_WeeklyOnhand

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_code | varchar | 8000 | 1 |  |  |  |
| jurisdiction_code | varchar | 8000 | 1 |  |  |  |
| LegalEntity | int | 4 | 1 |  |  |  |
| store_key | varchar | 8000 | 1 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| inventory_status_id | smallint | 2 | 1 |  |  |  |
| price_status_id | smallint | 2 | 1 |  |  |  |
| merch_year_wk | int | 4 | 1 |  |  |  |
| style_id | decimal | 9 | 1 |  |  |  |
| location_id | smallint | 2 | 1 |  |  |  |
| on_hand_units | int | 4 | 1 |  |  |  |
| on_hand_units_woa | int | 4 | 1 |  |  |  |
| allocation_units | int | 4 | 1 |  |  |  |
| on_hand_retail | decimal | 9 | 1 |  |  |  |
| on_hand_retail_native | decimal | 9 | 1 |  |  |  |
| on_hand_retail_te | decimal | 9 | 1 |  |  |  |
| on_hand_retail_old | decimal | 13 | 1 |  |  |  |
| current_retail_native | decimal | 9 | 1 |  |  |  |
| current_retail | decimal | 9 | 1 |  |  |  |
| location_code | varchar | 8000 | 1 |  |  |  |
| on_hand_cost | decimal | 9 | 1 |  |  |  |
| on_hand_cost_native | decimal | 9 | 1 |  |  |  |
| INS_DT | varchar | 8000 | 1 |  |  |  |
