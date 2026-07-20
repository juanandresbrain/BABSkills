# dbo.style

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

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
| delete_status | int | 4 | 1 |  |  |  |
| long_desc | varchar | 8000 | 1 |  |  |  |
| short_desc | varchar | 8000 | 1 |  |  |  |
| season_id | int | 4 | 1 |  |  |  |
| calendar_year_id | int | 4 | 1 |  |  |  |
| ticket_format_id | int | 4 | 1 |  |  |  |
| position_id | decimal | 9 | 1 |  |  |  |
| size_category_id | decimal | 9 | 1 |  |  |  |
| last_item_id | decimal | 9 | 1 |  |  |  |
| weight | decimal | 9 | 1 |  |  |  |
| height | decimal | 9 | 1 |  |  |  |
| width | decimal | 9 | 1 |  |  |  |
| depth | decimal | 9 | 1 |  |  |  |
| plu_desc | varchar | 8000 | 1 |  |  |  |
| promo_flag | bit | 1 | 1 |  |  |  |
| consignment_flag | bit | 1 | 1 |  |  |  |
| inhouse_upc_flag | bit | 1 | 1 |  |  |  |
| vendor_upc_flag | bit | 1 | 1 |  |  |  |
| reorder_flag | bit | 1 | 1 |  |  |  |
| fashion_flag | bit | 1 | 1 |  |  |  |
| replenishable_flag | bit | 1 | 1 |  |  |  |
| allow_customer_back_order_flag | bit | 1 | 1 |  |  |  |
| create_date | datetime2 | 8 | 1 |  |  |  |
| updatestamp | int | 4 | 1 |  |  |  |
| last_modified | datetime2 | 8 | 1 |  |  |  |
| order_multiple | int | 4 | 1 |  |  |  |
| distribution_multiple | int | 4 | 1 |  |  |  |
| target_selling_from_week | int | 4 | 1 |  |  |  |
| target_selling_to_week | int | 4 | 1 |  |  |  |
| target_selling_from_year | int | 4 | 1 |  |  |  |
| target_selling_to_year | int | 4 | 1 |  |  |  |
| size_grid_id | decimal | 9 | 1 |  |  |  |
| image_path | varchar | 8000 | 1 |  |  |  |
| to_be_deleted_date | datetime2 | 8 | 1 |  |  |  |
| resulting_po_predistrib_type | int | 4 | 1 |  |  |  |
| document_source | int | 4 | 1 |  |  |  |
| allow_customer_order_flag | bit | 1 | 1 |  |  |  |
| threshold | int | 4 | 1 |  |  |  |
| concept_code | varchar | 8000 | 1 |  |  |  |
| export_status | int | 4 | 1 |  |  |  |
| eom_available_to_sell_datetime | datetime2 | 8 | 1 |  |  |  |
| protected_flag | bit | 1 | 1 |  |  |  |
