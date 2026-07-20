# dbo.ma_01_style

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_id | decimal | 9 | 1 |  |  |  |
| style_code | varchar | 8000 | 1 |  |  |  |
| style_type | int | 4 | 1 |  |  |  |
| color_flag | bit | 1 | 1 |  |  |  |
| size_flag | bit | 1 | 1 |  |  |  |
| style_status | int | 4 | 1 |  |  |  |
| active_flag | bit | 1 | 1 |  |  |  |
| long_desc | varchar | 8000 | 1 |  |  |  |
| short_desc | varchar | 8000 | 1 |  |  |  |
| primary_vendor_id | decimal | 9 | 1 |  |  |  |
| season_id | int | 4 | 1 |  |  |  |
| calendar_id | int | 4 | 1 |  |  |  |
| ticket_format_id | decimal | 9 | 1 |  |  |  |
| position_id | decimal | 9 | 1 |  |  |  |
| main_style_group_id | decimal | 9 | 1 |  |  |  |
| weight | decimal | 9 | 1 |  |  |  |
| height | decimal | 9 | 1 |  |  |  |
| width | decimal | 9 | 1 |  |  |  |
| depth | decimal | 9 | 1 |  |  |  |
| promo_flag | bit | 1 | 1 |  |  |  |
| consignment_flag | bit | 1 | 1 |  |  |  |
| inhouse_upc_flag | bit | 1 | 1 |  |  |  |
| vendor_upc_flag | bit | 1 | 1 |  |  |  |
| reorder_flag | bit | 1 | 1 |  |  |  |
| fashion_flag | bit | 1 | 1 |  |  |  |
| create_date | datetime2 | 8 | 1 |  |  |  |
| order_multiple | int | 4 | 1 |  |  |  |
| distribution_multiple | int | 4 | 1 |  |  |  |
| target_selling_from_week | int | 4 | 1 |  |  |  |
| target_selling_to_week | int | 4 | 1 |  |  |  |
| target_selling_from_year | int | 4 | 1 |  |  |  |
| target_selling_to_year | int | 4 | 1 |  |  |  |
| original_retail | decimal | 9 | 1 |  |  |  |
| current_retail | decimal | 9 | 1 |  |  |  |
| price_status_id | int | 4 | 1 |  |  |  |
| compare_at_retail | decimal | 9 | 1 |  |  |  |
| replenishable_flag | bit | 1 | 1 |  |  |  |
| allow_customer_back_order_flag | bit | 1 | 1 |  |  |  |
| last_receipt_date | datetime2 | 8 | 1 |  |  |  |
| last_po_cost | decimal | 9 | 1 |  |  |  |
| size_category_id | int | 4 | 1 |  |  |  |
| primary_vendor_code | varchar | 8000 | 1 |  |  |  |
| primary_vendor_name | varchar | 8000 | 1 |  |  |  |
| primary_vendor_style | varchar | 8000 | 1 |  |  |  |
| primary_vendor_cur_cost | decimal | 9 | 1 |  |  |  |
| allow_customer_order_flag | bit | 1 | 1 |  |  |  |
| threshold | int | 4 | 1 |  |  |  |
