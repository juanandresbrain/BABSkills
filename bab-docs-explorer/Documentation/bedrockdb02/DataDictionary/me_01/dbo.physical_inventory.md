# dbo.physical_inventory

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| id | int | 4 | 0 |  |  |  |
| inventory_control_no | varchar | 20 | 1 |  |  |  |
| location_code | varchar | 20 | 1 |  |  |  |
| style_code | varchar | 20 | 1 |  |  |  |
| color_code | varchar | 3 | 1 |  |  |  |
| hierarchy_group_code | varchar | 20 | 1 |  |  |  |
| upc_number | varchar | 14 | 1 |  |  |  |
| hierarchy_group_short_label | varchar | 20 | 1 |  |  |  |
| item_type | varchar | 10 | 1 |  |  |  |
| counted_quantity | int | 4 | 1 |  |  |  |
| counted_cost | numeric | 9 | 1 |  |  |  |
| transaction_units | int | 4 | 1 |  |  |  |
| transaction_cost | numeric | 9 | 1 |  |  |  |
| short_desc | varchar | 20 | 1 |  |  |  |
| delta_units | int | 4 | 1 |  |  |  |
| delta_cost | numeric | 9 | 1 |  |  |  |
| country | varchar | 2 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.update_phys_inv_table_$sp](../../StoredProcedures/me_01/dbo.update_phys_inv_table_$sp.md)
- [me_01: dbo.update_phys_inv_table_$sp_091609](../../StoredProcedures/me_01/dbo.update_phys_inv_table_$sp_091609.md)

