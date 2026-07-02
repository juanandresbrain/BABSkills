# dbo.parameter_ml

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| parameter_ml_id | tinyint | 1 | 0 | YES |  |  |
| search_by_hierarchy_level_flag | bit | 1 | 0 |  |  |  |
| search_by_vendor_flag | bit | 1 | 0 |  |  |  |
| search_by_vendor_style_flag | bit | 1 | 0 |  |  |  |
| search_by_upc_flag | bit | 1 | 0 |  |  |  |
| search_by_style_flag | bit | 1 | 0 |  |  |  |
| search_by_alternate_code_flag | bit | 1 | 0 |  |  |  |
| exclude_from_hier_level_search | nvarchar | 510 | 1 |  |  |  |
| search_by_group_code_flag | bit | 1 | 0 |  |  |  |
| group_code_min_input | tinyint | 1 | 1 |  |  |  |
| search_by_group_name_flag | bit | 1 | 0 |  |  |  |
| group_name_min_input | tinyint | 1 | 1 |  |  |  |
| default_hierarchy_level | nvarchar | 40 | 1 |  |  |  |
| alternate_group_code_min_input | tinyint | 1 | 1 |  |  |  |
| vendor_name_min_input | tinyint | 1 | 1 |  |  |  |
| vendor_style_min_input | tinyint | 1 | 1 |  |  |  |
| search_by_style_code_flag | bit | 1 | 0 |  |  |  |
| style_code_min_input | tinyint | 1 | 1 |  |  |  |
| search_by_style_long_desc_flag | bit | 1 | 0 |  |  |  |
| style_description_min_input | tinyint | 1 | 1 |  |  |  |
| search_by_style_attribute_flag | bit | 1 | 0 |  |  |  |
| view_attachments_flag | bit | 1 | 0 |  |  |  |
| view_fullsize_flag | bit | 1 | 0 |  |  |  |
| view_compare_at_price_flag | bit | 1 | 0 |  |  |  |
| view_cost_button_flag | bit | 1 | 0 |  |  |  |
| view_merch_group_flag | bit | 1 | 0 |  |  |  |
| view_picture_default | smallint | 2 | 1 |  |  |  |
| view_promo_end_date_flag | bit | 1 | 0 |  |  |  |
| view_promo_price_flag | bit | 1 | 0 |  |  |  |
| view_retail_price_flag | bit | 1 | 0 |  |  |  |
| view_style_flag | bit | 1 | 0 |  |  |  |
| view_vendor_flag | bit | 1 | 0 |  |  |  |
| view_vendor_style_flag | bit | 1 | 0 |  |  |  |
| view_weight_flag | bit | 1 | 0 |  |  |  |
| weight_mask | nvarchar | 40 | 1 |  |  |  |
| return_to_main_menu_flag | bit | 1 | 0 |  |  |  |
| view_details_flag | bit | 1 | 0 |  |  |  |
| similar_upc_display_string | nvarchar | 40 | 1 |  |  |  |
| view_similar_upc_qty_flag | bit | 1 | 0 |  |  |  |
| pass_upc_flag | bit | 1 | 0 |  |  |  |
| check_upc_length_flag | bit | 1 | 0 |  |  |  |
| upc_min_input | smallint | 2 | 1 |  |  |  |
| upc_max_input | smallint | 2 | 1 |  |  |  |
| view_inventory_flag | bit | 1 | 0 |  |  |  |
| inv_status_code_list | nvarchar | 510 | 1 |  |  |  |
| view_loc_price_history_flag | bit | 1 | 0 |  |  |  |
| view_loc_inv_flag | bit | 1 | 0 |  |  |  |
| il_inv_status_code_list | nvarchar | 510 | 1 |  |  |  |
| view_upc_flag | bit | 1 | 0 |  |  |  |
| view_colour_flag | bit | 1 | 0 |  |  |  |
| view_size_flag | bit | 1 | 0 |  |  |  |
| view_on_hand_flag | bit | 1 | 0 |  |  |  |
| default_upc_process_tab | smallint | 2 | 1 |  |  |  |
| view_price_history_flag | bit | 1 | 0 |  |  |  |
| view_locate_flag | bit | 1 | 0 |  |  |  |
| allow_search_everywhere_flag | bit | 1 | 0 |  |  |  |
| allow_search_spec_stores_flag | bit | 1 | 0 |  |  |  |
| allow_search_zone_flag | bit | 1 | 0 |  |  |  |
| sort_by_onhand_flag | bit | 1 | 0 |  |  |  |
| include_stores_flag | bit | 1 | 0 |  |  |  |
| include_warehouses_flag | bit | 1 | 0 |  |  |  |
| include_distr_centres_flag | bit | 1 | 0 |  |  |  |
| include_head_office_flag | bit | 1 | 0 |  |  |  |
| default_search_method | tinyint | 1 | 1 |  |  |  |
| max_store_no_search_qty | smallint | 2 | 1 |  |  |  |
| default_transfer_zone | nvarchar | 60 | 1 |  |  |  |
| ph_lowest_price_indicator | nvarchar | 16 | 1 |  |  |  |
| ph_view_future_prices_flag | bit | 1 | 0 |  |  |  |
| lph_lowest_price_indicator | nvarchar | 16 | 1 |  |  |  |
| lph_view_future_prices_flag | bit | 1 | 0 |  |  |  |
| inv_view_grid_alloc_flag | bit | 1 | 0 |  |  |  |
| inv_view_grid_inv_flag | bit | 1 | 0 |  |  |  |
| loc_inv_view_grid_alloc_flag | bit | 1 | 0 |  |  |  |
| loc_inv_view_grid_inv_flag | bit | 1 | 0 |  |  |  |
| allow_requests_flag | bit | 1 | 0 |  |  |  |
| allow_dc_requests_flag | bit | 1 | 0 |  |  |  |
| allow_ho_requests_flag | bit | 1 | 0 |  |  |  |
| allow_store_requests_flag | bit | 1 | 0 |  |  |  |
| allow_wh_requests_flag | bit | 1 | 0 |  |  |  |
| pos_window_title | nvarchar | 80 | 1 |  |  |  |
| pos_window_classes | nvarchar | 80 | 1 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| last_item_id | decimal | 9 | 1 |  |  |  |
| display_cost_type | smallint | 2 | 1 |  |  |  |
| style_attribute_id | decimal | 9 | 1 |  |  |  |
| style_custom_property_id | decimal | 9 | 1 |  |  |  |

