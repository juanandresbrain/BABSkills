# dbo.ib_price

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ib_price_id | decimal | 9 | 1 |  |  |  |
| style_id | decimal | 9 | 1 |  |  |  |
| color_id | int | 4 | 1 |  |  |  |
| location_id | int | 4 | 1 |  |  |  |
| jurisdiction_id | int | 4 | 1 |  |  |  |
| pricing_group_id | int | 4 | 1 |  |  |  |
| temp_price_flag | bit | 1 | 1 |  |  |  |
| start_date | datetime2 | 8 | 1 |  |  |  |
| end_date | datetime2 | 8 | 1 |  |  |  |
| valuation_retail_price | decimal | 9 | 1 |  |  |  |
| selling_retail_price | decimal | 9 | 1 |  |  |  |
| price_status_id | int | 4 | 1 |  |  |  |
| document_number | varchar | 8000 | 1 |  |  |  |
| cancel_promo_flag | bit | 1 | 1 |  |  |  |
| effective_date | datetime2 | 8 | 1 |  |  |  |
| price_change_type | int | 4 | 1 |  |  |  |
| insert_guid | varchar | 8000 | 1 |  |  |  |
| style_color_id | decimal | 9 | 1 |  |  |  |
| sku_id | decimal | 9 | 1 |  |  |  |
