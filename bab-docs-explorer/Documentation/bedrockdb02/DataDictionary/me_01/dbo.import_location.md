# dbo.import_location

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| import_location_id | smallint | 2 | 0 | YES |  |  |
| entity_type | nvarchar | 4 | 0 |  |  |  |
| action_type | nchar | 2 | 0 |  |  |  |
| location_code | nvarchar | 40 | 0 |  |  |  |
| location_group | nvarchar | 40 | 0 |  |  |  |
| location_type | tinyint | 1 | 0 |  |  |  |
| location_name | nvarchar | 120 | 0 |  |  |  |
| location_short_name | nvarchar | 16 | 1 |  |  |  |
| generate_plu_file_flag | nchar | 2 | 1 |  |  |  |
| register_code | nvarchar | 12 | 1 |  |  |  |
| polling_reference | int | 4 | 1 |  |  |  |
| gl_company_id | tinyint | 1 | 1 |  |  |  |
| gl_location_number | nvarchar | 40 | 1 |  |  |  |
| selling_space | decimal | 9 | 1 |  |  |  |
| non_selling_space | decimal | 9 | 1 |  |  |  |
| target_sales | decimal | 9 | 1 |  |  |  |
| occupancy_cost | decimal | 9 | 1 |  |  |  |
| shrinkage_factor | decimal | 5 | 1 |  |  |  |
| warehouse_system_flag | nchar | 2 | 1 |  |  |  |
| active_flag | nchar | 2 | 1 |  |  |  |
| open_date | smalldatetime | 4 | 1 |  |  |  |
| comparative_date | smalldatetime | 4 | 1 |  |  |  |
| closed_date | smalldatetime | 4 | 1 |  |  |  |
| closed_reason | nvarchar | 60 | 1 |  |  |  |
| reopen_date | smalldatetime | 4 | 1 |  |  |  |
| remodel_start_date | smalldatetime | 4 | 1 |  |  |  |
| remodel_end_date | smalldatetime | 4 | 1 |  |  |  |
| open_to_receive_date | smalldatetime | 4 | 1 |  |  |  |
| tkt_override_tkt_price_flag | nchar | 2 | 1 |  |  |  |
| tkt_safety_stock_amt | int | 4 | 1 |  |  |  |
| tkt_safety_stock_percent | decimal | 5 | 1 |  |  |  |
| tkt_safety_stock_max_safe_unit | int | 4 | 1 |  |  |  |
| tkt_days_to_keep_printed_tkts | smallint | 2 | 1 |  |  |  |
| tkt_days_to_keep_non_print_tkt | smallint | 2 | 1 |  |  |  |
| tkt_override_tkt_upc_val_flag | nchar | 2 | 1 |  |  |  |
| tkt_upc_type_order | smallint | 2 | 1 |  |  |  |
| pricing_group_code | nvarchar | 20 | 1 |  |  |  |
| replenish_flag | nchar | 2 | 1 |  |  |  |
| reserve_wh_for_alloc_loc_code | nvarchar | 40 | 1 |  |  |  |
| address_name | nvarchar | 120 | 1 |  |  |  |
| address_line1 | nvarchar | 100 | 1 |  |  |  |
| address_line2 | nvarchar | 100 | 1 |  |  |  |
| address_city | nvarchar | 100 | 1 |  |  |  |
| address_state | nvarchar | 40 | 1 |  |  |  |
| address_country_code | nvarchar | 6 | 1 |  |  |  |
| address_zip_code | nvarchar | 30 | 1 |  |  |  |
| address_email | nvarchar | 120 | 1 |  |  |  |
| allow_customer_transfer_flag | nchar | 2 | 1 |  |  |  |
| allow_customer_shipment_flag | nchar | 2 | 1 |  |  |  |
| allow_customer_pickup_flag | nchar | 2 | 1 |  |  |  |
| jurisdiction_code | nvarchar | 40 | 1 |  |  |  |
| language_description | nvarchar | 60 | 1 |  |  |  |
| tax_registration_number1 | nvarchar | 40 | 1 |  |  |  |
| tax_registration_number2 | nvarchar | 40 | 1 |  |  |  |
| uses_oim_flag | nvarchar | 2 | 1 |  |  |  |
| auto_receive_shipments_flag | nvarchar | 2 | 1 |  |  |  |
| allow_customer_order_flag | bit | 1 | 1 |  |  |  |
| routing_priority | int | 4 | 1 |  |  |  |
| send_inv_move_to_es_flag | bit | 1 | 1 |  |  |  |
| generate_thin_plu_file_flag | nvarchar | 2 | 1 |  |  |  |
| pos_server_code | nvarchar | 20 | 1 |  |  |  |
| es_allow_customer_pickup_order_flag | bit | 1 | 1 |  |  |  |

