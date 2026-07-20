# dbo.d365_weeklyonorder

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| createdon | datetime2 | 8 | 1 |  |  |  |
| style_id | varchar | 8000 | 1 |  |  |  |
| location_id | varchar | 8000 | 1 |  |  |  |
| on_order_units | decimal | 17 | 1 |  |  |  |
| on_order_cost_native | decimal | 17 | 1 |  |  |  |
| on_order_cost_native_currency | varchar | 8000 | 1 |  |  |  |
| legal_entity | varchar | 8000 | 1 |  |  |  |
| product_type | bigint | 8 | 1 |  |  |  |
| property_id | varchar | 8000 | 1 |  |  |  |
| product_key | varchar | 200 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| merch_year_wk | varchar | 8000 | 1 |  |  |  |
| on_order_retail | decimal | 17 | 1 |  |  |  |
| allocation_units | decimal | 17 | 1 |  |  |  |
| on_order_retail_old | int | 4 | 1 |  |  |  |
| on_order_retail_us_te | int | 4 | 1 |  |  |  |
| on_order_retail_us_te_oounitscalc | int | 4 | 1 |  |  |  |
| INS_DT | datetime2 | 8 | 1 |  |  |  |
