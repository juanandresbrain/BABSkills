# dbo.style_backup

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_id | decimal | 9 | 0 |  |  |  |
| style_code | varchar | 20 | 0 |  |  |  |
| style_type | tinyint | 1 | 0 |  |  |  |
| color_flag | bit | 1 | 0 |  |  |  |
| size_flag | bit | 1 | 0 |  |  |  |
| style_status | smallint | 2 | 0 |  |  |  |
| active_flag | bit | 1 | 0 |  |  |  |
| delete_status | smallint | 2 | 0 |  |  |  |
| long_desc | varchar | 120 | 1 |  |  |  |
| short_desc | varchar | 20 | 1 |  |  |  |
| season_id | smallint | 2 | 0 |  |  |  |
| calendar_year_id | smallint | 2 | 1 |  |  |  |
| ticket_format_id | smallint | 2 | 1 |  |  |  |
| position_id | decimal | 9 | 0 |  |  |  |
| size_category_id | decimal | 9 | 1 |  |  |  |
| last_item_id | decimal | 9 | 1 |  |  |  |
| weight | decimal | 9 | 1 |  |  |  |
| height | decimal | 9 | 1 |  |  |  |
| width | decimal | 9 | 1 |  |  |  |
| depth | decimal | 9 | 1 |  |  |  |
| plu_desc | varchar | 40 | 1 |  |  |  |
| promo_flag | bit | 1 | 0 |  |  |  |
| consignment_flag | bit | 1 | 0 |  |  |  |
| inhouse_upc_flag | bit | 1 | 0 |  |  |  |
| vendor_upc_flag | bit | 1 | 0 |  |  |  |
| reorder_flag | bit | 1 | 0 |  |  |  |
| fashion_flag | bit | 1 | 0 |  |  |  |
| replenishable_flag | bit | 1 | 0 |  |  |  |
| allow_customer_back_order_flag | bit | 1 | 0 |  |  |  |
| create_date | smalldatetime | 4 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| last_modified | smalldatetime | 4 | 1 |  |  |  |
| order_multiple | int | 4 | 1 |  |  |  |
| distribution_multiple | int | 4 | 1 |  |  |  |
| target_selling_from_week | tinyint | 1 | 1 |  |  |  |
| target_selling_to_week | tinyint | 1 | 1 |  |  |  |
| target_selling_from_year | int | 4 | 1 |  |  |  |
| target_selling_to_year | int | 4 | 1 |  |  |  |
| size_grid_id | decimal | 9 | 1 |  |  |  |
| image_path | varchar | 255 | 1 |  |  |  |
| to_be_deleted_date | smalldatetime | 4 | 1 |  |  |  |
| resulting_po_predistrib_type | smallint | 2 | 1 |  |  |  |
| document_source | smallint | 2 | 0 |  |  |  |

