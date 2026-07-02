# dbo.style_location_sku_cs

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_location_sku_id | decimal | 9 | 0 | YES |  |  |
| style_id | decimal | 9 | 0 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| style_color_id | decimal | 9 | 0 |  |  |  |
| size_master_id | int | 4 | 0 |  |  |  |
| sku_id | decimal | 9 | 0 |  |  |  |
| jurisdiction_id | smallint | 2 | 0 |  |  |  |
| original_selling_retail | decimal | 9 | 1 |  |  |  |
| original_valuation_retail | decimal | 9 | 1 |  |  |  |
| original_price_status_id | smallint | 2 | 1 |  |  |  |
| current_selling_retail | decimal | 9 | 1 |  |  |  |
| current_valuation_retail | decimal | 9 | 1 |  |  |  |
| current_price_status_id | smallint | 2 | 1 |  |  |  |

