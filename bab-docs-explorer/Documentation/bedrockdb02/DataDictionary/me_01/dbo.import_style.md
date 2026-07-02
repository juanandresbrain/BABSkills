# dbo.import_style

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| import_style_id | decimal | 9 | 0 | YES |  |  |
| entity_type | nvarchar | 4 | 0 |  |  |  |
| action_type | nchar | 2 | 0 |  |  |  |
| processed_flag | bit | 1 | 0 |  |  |  |
| style_code | nvarchar | 40 | 1 |  |  |  |
| merchandise_group | nvarchar | 40 | 1 |  |  |  |
| merchandise_type | smallint | 2 | 1 |  |  |  |
| style_status | smallint | 2 | 1 |  |  |  |
| long_desc | nvarchar | 240 | 1 |  |  |  |
| short_desc | nvarchar | 40 | 1 |  |  |  |
| season_code | nvarchar | 4 | 1 |  |  |  |
| year | decimal | 5 | 1 |  |  |  |
| ticket_format | nvarchar | 4 | 1 |  |  |  |
| weight | decimal | 9 | 1 |  |  |  |
| height | decimal | 9 | 1 |  |  |  |
| width | decimal | 9 | 1 |  |  |  |
| depth | decimal | 9 | 1 |  |  |  |
| plu_description | nvarchar | 80 | 1 |  |  |  |
| employee_position | nvarchar | 60 | 1 |  |  |  |
| promo_flag | nchar | 2 | 1 |  |  |  |
| inhouse_upc_flag | nchar | 2 | 1 |  |  |  |
| vendor_upc_flag | nchar | 2 | 1 |  |  |  |
| reorder_flag | nchar | 2 | 1 |  |  |  |
| fashion_flag | nchar | 2 | 1 |  |  |  |
| consignment_flag | nchar | 2 | 1 |  |  |  |
| replenishable_flag | nchar | 2 | 1 |  |  |  |
| allow_customer_back_order_flag | nchar | 2 | 1 |  |  |  |
| create_date | smalldatetime | 4 | 1 |  |  |  |
| order_multiple | int | 4 | 1 |  |  |  |
| distribution_multiple | int | 4 | 1 |  |  |  |
| target_selling_from_week | tinyint | 1 | 1 |  |  |  |
| target_selling_from_year | int | 4 | 1 |  |  |  |
| target_selling_to_week | tinyint | 1 | 1 |  |  |  |
| target_selling_to_year | int | 4 | 1 |  |  |  |
| original_selling_retail | decimal | 9 | 1 |  |  |  |
| original_price_status_code | nvarchar | 6 | 1 |  |  |  |
| compare_at_retail | decimal | 9 | 1 |  |  |  |
| size_grid_code | nvarchar | 16 | 1 |  |  |  |
| primary_vendor_code | nvarchar | 40 | 1 |  |  |  |
| primary_vendor_style | nvarchar | 80 | 1 |  |  |  |
| primary_vendor_current_cost | decimal | 9 | 1 |  |  |  |
| prim_vdr_cost_currency_code | nvarchar | 6 | 1 |  |  |  |
| import_replication_queue_id | decimal | 9 | 1 |  |  |  |
| active_flag | nchar | 2 | 1 |  |  |  |
| current_selling_retail | decimal | 9 | 1 |  |  |  |
| current_price_status_code | nvarchar | 6 | 1 |  |  |  |
| mix_match_rule_code1 | int | 4 | 1 |  |  |  |
| mix_match_rule_code2 | int | 4 | 1 |  |  |  |
| mix_match_rule_code3 | int | 4 | 1 |  |  |  |
| mix_match_rule_code4 | int | 4 | 1 |  |  |  |
| last_net_final_po_cost | decimal | 9 | 1 |  |  |  |
| last_receipt_date | smalldatetime | 4 | 1 |  |  |  |
| error_description | nvarchar | 2000 | 1 |  |  |  |
| resulting_po_predistrib_type | smallint | 2 | 1 |  |  |  |
| allow_customer_order_flag | bit | 1 | 1 |  |  |  |
| threshold | int | 4 | 1 |  |  |  |
| concept_code | nvarchar | 40 | 1 |  |  |  |
| eom_available_to_sell_datetime | datetime | 8 | 1 |  |  |  |

