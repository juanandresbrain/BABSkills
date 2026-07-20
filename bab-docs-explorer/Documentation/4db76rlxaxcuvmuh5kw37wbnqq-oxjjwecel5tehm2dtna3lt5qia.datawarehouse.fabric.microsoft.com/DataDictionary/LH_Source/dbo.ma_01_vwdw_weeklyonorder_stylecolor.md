# dbo.ma_01_vwdw_weeklyonorder_stylecolor

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| product_key | varchar | 8000 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
| date_key | int | 4 | 1 |  |  |  |
| merch_year_wk | int | 4 | 1 |  |  |  |
| on_order_units | int | 4 | 1 |  |  |  |
| on_order_retail | decimal | 13 | 1 |  |  |  |
| on_order_retail_old | decimal | 9 | 1 |  |  |  |
| style_id | decimal | 9 | 1 |  |  |  |
| sku_id | decimal | 9 | 1 |  |  |  |
| allocation_units | int | 4 | 1 |  |  |  |
| on_order_retail_us_te | decimal | 9 | 1 |  |  |  |
| on_order_retail_us_te_OOUnitsCalc | decimal | 13 | 1 |  |  |  |
