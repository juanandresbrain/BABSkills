# dbo.me_01_location

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| location_id | int | 4 | 1 |  |  |  |
| location_type | int | 4 | 1 |  |  |  |
| location_code | varchar | 8000 | 1 |  |  |  |
| location_name | varchar | 8000 | 1 |  |  |  |
| location_short_name | varchar | 8000 | 1 |  |  |  |
| register_type_id | int | 4 | 1 |  |  |  |
| generate_plu_file_flag | bit | 1 | 1 |  |  |  |
| location_status_id | int | 4 | 1 |  |  |  |
| active_flag | bit | 1 | 1 |  |  |  |
| gl_company_id | int | 4 | 1 |  |  |  |
| gl_location_number | varchar | 8000 | 1 |  |  |  |
| jurisdiction_id | int | 4 | 1 |  |  |  |
| selling_space | decimal | 9 | 1 |  |  |  |
| non_selling_space | decimal | 9 | 1 |  |  |  |
| target_sales | decimal | 9 | 1 |  |  |  |
| occupancy_cost | decimal | 9 | 1 |  |  |  |
| language_id | int | 4 | 1 |  |  |  |
| shrinkage_factor | decimal | 5 | 1 |  |  |  |
| warehouse_system_flag | bit | 1 | 1 |  |  |  |
| replenish_flag | bit | 1 | 1 |  |  |  |
| allow_customer_shipment_flag | bit | 1 | 1 |  |  |  |
| allow_customer_pickup_flag | bit | 1 | 1 |  |  |  |
| allow_customer_transfer_flag | bit | 1 | 1 |  |  |  |
| open_date | datetime2 | 8 | 1 |  |  |  |
| comparative_date | datetime2 | 8 | 1 |  |  |  |
| closed_date | datetime2 | 8 | 1 |  |  |  |
| closed_reason | varchar | 8000 | 1 |  |  |  |
| reopen_date | datetime2 | 8 | 1 |  |  |  |
| remodel_start_date | datetime2 | 8 | 1 |  |  |  |
| remodel_end_date | datetime2 | 8 | 1 |  |  |  |
| open_to_receive_date | datetime2 | 8 | 1 |  |  |  |
| updatestamp | int | 4 | 1 |  |  |  |
| tkt_override_tkt_price_flag | bit | 1 | 1 |  |  |  |
| tkt_safety_stock_amt | int | 4 | 1 |  |  |  |
| tkt_safety_stock_percent | decimal | 5 | 1 |  |  |  |
| tkt_safety_stock_max_safe_unit | int | 4 | 1 |  |  |  |
| tkt_days_to_keep_printed_tkts | int | 4 | 1 |  |  |  |
| tkt_days_to_keep_non_print_tkt | int | 4 | 1 |  |  |  |
| tkt_override_tkt_upc_val_flag | bit | 1 | 1 |  |  |  |
| tkt_upc_type_order | int | 4 | 1 |  |  |  |
| polling_reference | int | 4 | 1 |  |  |  |
| reserve_wh_for_alloc_loc_id | int | 4 | 1 |  |  |  |
| last_item_id | decimal | 9 | 1 |  |  |  |
| tax_registration_number1 | varchar | 8000 | 1 |  |  |  |
| tax_registration_number2 | varchar | 8000 | 1 |  |  |  |
| uses_oim_flag | bit | 1 | 1 |  |  |  |
| auto_receive_shipments_flag | bit | 1 | 1 |  |  |  |
| pos_server_flag | bit | 1 | 1 |  |  |  |
| pos_server_id | int | 4 | 1 |  |  |  |
| allow_customer_order_flag | bit | 1 | 1 |  |  |  |
| routing_priority | int | 4 | 1 |  |  |  |
| send_inv_move_to_es_flag | bit | 1 | 1 |  |  |  |
| generate_thin_plu_file_flag | bit | 1 | 1 |  |  |  |
| es_allow_customer_pickup_order_flag | bit | 1 | 1 |  |  |  |
| receive_eom_po_flag | bit | 1 | 1 |  |  |  |
| selling_location | bit | 1 | 1 |  |  |  |
