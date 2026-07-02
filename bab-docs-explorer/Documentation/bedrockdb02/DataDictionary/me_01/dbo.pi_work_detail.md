# dbo.pi_work_detail

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| inventory_control_loc_id | decimal | 9 | 0 | YES |  |  |
| inventory_control_id | decimal | 9 | 0 | YES |  |  |
| sku_id | decimal | 9 | 0 | YES |  |  |
| units_counted | int | 4 | 0 |  |  |  |
| extended_units_counted | int | 4 | 1 |  |  |  |
| cost | decimal | 9 | 1 |  |  |  |
| total_cost | decimal | 9 | 1 |  |  |  |
| total_retail | decimal | 9 | 1 |  |  |  |
| total_valuation_retail | decimal | 9 | 1 |  |  |  |
| total_oh_book_units | int | 4 | 1 |  |  |  |
| total_oh_book_cost | decimal | 9 | 1 |  |  |  |
| total_oh_book_val_retail | decimal | 9 | 1 |  |  |  |
| total_oh_book_sell_retail | decimal | 9 | 1 |  |  |  |
| total_oh_in_transit_units | int | 4 | 1 |  |  |  |
| total_oh_in_transit_cost | decimal | 9 | 1 |  |  |  |
| total_oh_in_tran_val_retail | decimal | 9 | 1 |  |  |  |
| total_oh_in_tran_sell_retail | decimal | 9 | 1 |  |  |  |
| discrepancy_units | int | 4 | 1 |  |  |  |
| discrepancy_cost | decimal | 9 | 1 |  |  |  |
| discrepancy_val_retail | decimal | 9 | 1 |  |  |  |
| discrepancy_sell_retail | decimal | 9 | 1 |  |  |  |
| pending_shrink_units | int | 4 | 1 |  |  |  |
| pending_shrink_cost | decimal | 9 | 1 |  |  |  |
| pending_shrink_val_retail | decimal | 9 | 1 |  |  |  |
| pending_shrink_sell_retail | decimal | 9 | 1 |  |  |  |
| average_cost | decimal | 9 | 1 |  |  |  |
| valuation_unit_retail | decimal | 9 | 1 |  |  |  |
| selling_unit_retail | decimal | 9 | 1 |  |  |  |
| price_status_id | int | 4 | 1 |  |  |  |
| cost_local | decimal | 9 | 1 |  |  |  |
| total_cost_local | decimal | 9 | 1 |  |  |  |
| total_oh_book_cost_local | decimal | 9 | 1 |  |  |  |
| total_oh_in_transit_cost_local | decimal | 9 | 1 |  |  |  |
| average_cost_local | decimal | 9 | 1 |  |  |  |
| discrepancy_cost_local | decimal | 9 | 1 |  |  |  |
| pending_shrink_cost_local | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.pi_update_inventory_tables_$sp](../../StoredProcedures/me_01/dbo.pi_update_inventory_tables_$sp.md)

