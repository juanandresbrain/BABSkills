# dbo.ib_pack_inventory_total

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| pack_id | decimal | 9 | 0 | YES |  |  |
| location_id | smallint | 2 | 0 | YES |  |  |
| total_on_hand_units | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.import_asn_third_step_$sp](../../StoredProcedures/me_01/dbo.import_asn_third_step_$sp.md)
- [me_01: dbo.insert_packs_$sp](../../StoredProcedures/me_01/dbo.insert_packs_$sp.md)
- [me_01: dbo.inventory_pack_update_$sp](../../StoredProcedures/me_01/dbo.inventory_pack_update_$sp.md)
- [me_01: dbo.pi_pack_freeze_on_hand_loc_$sp](../../StoredProcedures/me_01/dbo.pi_pack_freeze_on_hand_loc_$sp.md)

