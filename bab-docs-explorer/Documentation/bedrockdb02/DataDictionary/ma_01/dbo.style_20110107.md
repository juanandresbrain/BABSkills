# dbo.style_20110107

**Database:** ma_01  
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
| long_desc | varchar | 120 | 1 |  |  |  |
| short_desc | varchar | 20 | 1 |  |  |  |
| primary_vendor_id | decimal | 9 | 1 |  |  |  |
| season_id | smallint | 2 | 0 |  |  |  |
| calendar_id | smallint | 2 | 1 |  |  |  |
| ticket_format_id | decimal | 9 | 1 |  |  |  |
| position_id | decimal | 9 | 0 |  |  |  |
| main_style_group_id | decimal | 9 | 0 |  |  |  |
| weight | decimal | 9 | 1 |  |  |  |
| height | decimal | 9 | 1 |  |  |  |
| width | decimal | 9 | 1 |  |  |  |
| depth | decimal | 9 | 1 |  |  |  |
| promo_flag | bit | 1 | 0 |  |  |  |
| consignment_flag | bit | 1 | 0 |  |  |  |
| inhouse_upc_flag | bit | 1 | 0 |  |  |  |
| vendor_upc_flag | bit | 1 | 0 |  |  |  |
| reorder_flag | bit | 1 | 0 |  |  |  |
| fashion_flag | bit | 1 | 0 |  |  |  |
| create_date | smalldatetime | 4 | 0 |  |  |  |
| order_multiple | int | 4 | 1 |  |  |  |
| distribution_multiple | int | 4 | 1 |  |  |  |
| target_selling_from_week | tinyint | 1 | 1 |  |  |  |
| target_selling_to_week | tinyint | 1 | 1 |  |  |  |
| target_selling_from_year | int | 4 | 1 |  |  |  |
| target_selling_to_year | int | 4 | 1 |  |  |  |
| original_retail | decimal | 9 | 1 |  |  |  |
| current_retail | decimal | 9 | 1 |  |  |  |
| price_status_id | smallint | 2 | 1 |  |  |  |
| compare_at_retail | decimal | 9 | 1 |  |  |  |
| replenishable_flag | bit | 1 | 0 |  |  |  |
| allow_customer_back_order_flag | bit | 1 | 0 |  |  |  |
| last_receipt_date | smalldatetime | 4 | 1 |  |  |  |
| last_po_cost | decimal | 9 | 1 |  |  |  |
| size_category_id | int | 4 | 1 |  |  |  |
| primary_vendor_code | varchar | 20 | 0 |  |  |  |
| primary_vendor_name | varchar | 50 | 0 |  |  |  |
| primary_vendor_style | varchar | 40 | 1 |  |  |  |
| primary_vendor_cur_cost | decimal | 9 | 1 |  |  |  |

