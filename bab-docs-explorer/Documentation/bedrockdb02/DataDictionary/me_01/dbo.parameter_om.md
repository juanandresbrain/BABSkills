# dbo.parameter_om

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| parameter_om_id | numeric | 9 | 0 | YES |  |  |
| customer_order_no_mask | nvarchar | 40 | 0 |  |  |  |
| first_customer_order_no | nvarchar | 40 | 0 |  |  |  |
| last_customer_order_no | nvarchar | 40 | 0 |  |  |  |
| last_generated_order_no | nvarchar | 40 | 1 |  |  |  |
| customer_order_no_rec_flag | bit | 1 | 0 |  |  |  |
| order_history_months | tinyint | 1 | 0 |  |  |  |
| allow_vendor_order_flag | bit | 1 | 0 |  |  |  |
| allow_xfer_distrib_flag | bit | 1 | 0 |  |  |  |
| store_ship_to_cust_std_dep_pct | decimal | 5 | 0 |  |  |  |
| store_reserve_pick_std_dep_pct | decimal | 5 | 0 |  |  |  |
| store_to_loc_pick_std_dep_pct | decimal | 5 | 0 |  |  |  |
| store_to_loc_ship_std_dep_pct | decimal | 5 | 0 |  |  |  |
| store_ship_to_cust_min_dep_pct | decimal | 5 | 0 |  |  |  |
| store_reserve_pick_min_dep_pct | decimal | 5 | 0 |  |  |  |
| store_to_loc_pick_min_dep_pct | decimal | 5 | 0 |  |  |  |
| store_to_loc_ship_min_dep_pct | decimal | 5 | 0 |  |  |  |
| wh_ship_to_cust_std_dep_pct | decimal | 5 | 0 |  |  |  |
| wh_to_loc_pick_std_dep_pct | decimal | 5 | 0 |  |  |  |
| wh_to_loc_ship_std_dep_pct | decimal | 5 | 0 |  |  |  |
| wh_ship_to_cust_min_dep_pct | decimal | 5 | 0 |  |  |  |
| wh_to_loc_pick_min_dep_pct | decimal | 5 | 0 |  |  |  |
| wh_to_loc_ship_min_dep_pct | decimal | 5 | 0 |  |  |  |
| dc_ship_to_cust_std_dep_pct | decimal | 5 | 0 |  |  |  |
| dc_to_loc_pick_std_dep_pct | decimal | 5 | 0 |  |  |  |
| dc_to_loc_ship_std_dep_pct | decimal | 5 | 0 |  |  |  |
| dc_ship_to_cust_min_dep_pct | decimal | 5 | 0 |  |  |  |
| dc_to_loc_pick_min_dep_pct | decimal | 5 | 0 |  |  |  |
| dc_to_loc_ship_min_dep_pct | decimal | 5 | 0 |  |  |  |
| vendor_ship_cust_std_dep_pct | decimal | 5 | 0 |  |  |  |
| vendor_to_loc_pick_std_dep_pct | decimal | 5 | 0 |  |  |  |
| vendor_to_loc_ship_std_dep_pct | decimal | 5 | 0 |  |  |  |
| vendor_ship_cust_min_dep_pct | decimal | 5 | 0 |  |  |  |
| vendor_to_loc_pick_min_dep_pct | decimal | 5 | 0 |  |  |  |
| vendor_to_loc_ship_min_dep_pct | decimal | 5 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| im_to_isom_pathway | nvarchar | 510 | 1 |  |  |  |
| pos_sale_attribution | smallint | 2 | 0 |  |  |  |
| web_sale_attribution | smallint | 2 | 0 |  |  |  |
| email_return_address | nvarchar | 60 | 1 |  |  |  |
| user_def_disc_inv_status_id | smallint | 2 | 0 |  |  |  |

