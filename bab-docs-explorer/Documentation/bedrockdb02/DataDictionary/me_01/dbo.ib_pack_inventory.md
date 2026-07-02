# dbo.ib_pack_inventory

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ib_pack_inventory_id | decimal | 9 | 0 | YES |  |  |
| pack_id | decimal | 9 | 0 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| transaction_type_code | smallint | 2 | 0 |  |  |  |
| other_location_id | smallint | 2 | 1 |  |  |  |
| document_number | nvarchar | 40 | 1 |  |  |  |
| transaction_units | int | 4 | 0 |  |  |  |
| distribution_id | bigint | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.import_asn_third_step_$sp](../../StoredProcedures/me_01/dbo.import_asn_third_step_$sp.md)
- [me_01: dbo.insert_packs_$sp](../../StoredProcedures/me_01/dbo.insert_packs_$sp.md)
- [me_01: dbo.inventory_pack_update_$sp](../../StoredProcedures/me_01/dbo.inventory_pack_update_$sp.md)
- [me_01: dbo.pi_pack_rmv_future_oh_loc_$sp](../../StoredProcedures/me_01/dbo.pi_pack_rmv_future_oh_loc_$sp.md)
- [me_01: dbo.post_beg_inv_loc_$sp](../../StoredProcedures/me_01/dbo.post_beg_inv_loc_$sp.md)
- [me_01: dbo.post_inventory_loc_$sp](../../StoredProcedures/me_01/dbo.post_inventory_loc_$sp.md)

