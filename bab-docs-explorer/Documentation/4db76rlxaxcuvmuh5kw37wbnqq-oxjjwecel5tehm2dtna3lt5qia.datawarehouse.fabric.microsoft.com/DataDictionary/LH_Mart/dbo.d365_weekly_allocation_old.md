# dbo.d365_weekly_allocation_old

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_code | varchar | 8000 | 1 |  |  |  |
| color_code | varchar | 8000 | 1 |  |  |  |
| product_key | bigint | 8 | 1 |  |  |  |
| location_code | varchar | 8000 | 1 |  |  |  |
| store_key | int | 4 | 1 |  |  |  |
| merch_year_wk | varchar | 8000 | 1 |  |  |  |
| allocation_units | decimal | 17 | 1 |  |  |  |
| INS_DT | datetime2 | 8 | 1 |  |  |  |
| UPDT_DT | datetime2 | 8 | 1 |  |  |  |
