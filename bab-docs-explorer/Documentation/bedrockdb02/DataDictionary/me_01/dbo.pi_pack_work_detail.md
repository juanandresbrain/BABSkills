# dbo.pi_pack_work_detail

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| inventory_control_loc_id | decimal | 9 | 0 | YES |  |  |
| inventory_control_id | decimal | 9 | 0 | YES |  |  |
| pack_id | decimal | 9 | 0 | YES |  |  |
| cost | decimal | 9 | 1 |  |  |  |
| units_counted | int | 4 | 0 |  |  |  |
| book_pack_units | int | 4 | 1 |  |  |  |
| cost_local | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.pi_update_inventory_tables_$sp](../../StoredProcedures/me_01/dbo.pi_update_inventory_tables_$sp.md)

