# dbo.temp_price_lookup

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| temp_price_lookup_id | int | 4 | 1 |  |  |  |
| style_id | decimal | 9 | 1 |  |  |  |
| jurisdiction_id | smallint | 2 | 1 |  |  |  |
| color_id | smallint | 2 | 1 |  |  |  |
| location_id | smallint | 2 | 1 |  |  |  |
| style_color_id | decimal | 9 | 1 |  |  |  |
| sku_id | decimal | 9 | 1 |  |  |  |
| valuation_retail_price | decimal | 9 | 1 |  |  |  |
| selling_retail_price | decimal | 9 | 1 |  |  |  |
| price_status_id | smallint | 2 | 1 |  |  |  |
| start_date | smalldatetime | 4 | 1 |  |  |  |
| end_date | smalldatetime | 4 | 1 |  |  |  |
| effective_date | smalldatetime | 4 | 1 |  |  |  |
| exception_level | tinyint | 1 | 1 |  |  |  |

