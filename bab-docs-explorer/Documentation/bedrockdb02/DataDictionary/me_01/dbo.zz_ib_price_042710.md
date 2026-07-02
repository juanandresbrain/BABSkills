# dbo.zz_ib_price_042710

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_id | decimal | 9 | 0 |  |  |  |
| color_id | smallint | 2 | 1 |  |  |  |
| location_id | smallint | 2 | 1 |  |  |  |
| jurisdiction_id | smallint | 2 | 0 |  |  |  |
| pricing_group_id | smallint | 2 | 1 |  |  |  |
| temp_price_flag | bit | 1 | 0 |  |  |  |
| start_date | smalldatetime | 4 | 0 |  |  |  |
| end_date | smalldatetime | 4 | 1 |  |  |  |
| valuation_retail_price | decimal | 9 | 0 |  |  |  |
| selling_retail_price | decimal | 9 | 0 |  |  |  |
| price_status_id | smallint | 2 | 0 |  |  |  |
| document_number | int | 4 | 1 |  |  |  |
| cancel_promo_flag | bit | 1 | 0 |  |  |  |
| effective_date | varchar | 11 | 1 |  |  |  |
| price_change_type | smallint | 2 | 1 |  |  |  |

