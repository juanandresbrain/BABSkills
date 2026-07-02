# dbo.pi_work_loc_info

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| inventory_control_loc_id | decimal | 9 | 0 | YES |  |  |
| inventory_control_id | decimal | 9 | 0 | YES |  |  |
| last_ib_inventory_id | decimal | 9 | 1 |  |  |  |
| last_ib_pack_inventory_id | decimal | 9 | 1 |  |  |  |
| detail_count | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.pi_update_inventory_tables_$sp](../../StoredProcedures/me_01/dbo.pi_update_inventory_tables_$sp.md)

