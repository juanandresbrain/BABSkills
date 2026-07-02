# dbo.inventory_control_loc

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| inventory_control_loc_id | decimal | 9 | 0 | YES |  |  |
| inventory_control_id | decimal | 9 | 0 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| inv_control_loc_status | smallint | 2 | 0 |  |  |  |
| state_no | int | 4 | 0 |  |  |  |
| to_be_posted_flag | bit | 1 | 0 |  |  |  |
| posted_date | smalldatetime | 4 | 1 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| last_item_id | decimal | 9 | 1 |  |  |  |
| last_ib_inventory_id | decimal | 9 | 1 |  |  |  |
| last_ib_pack_inventory_id | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.delete_inv_control_documents_$sp](../../StoredProcedures/me_01/dbo.delete_inv_control_documents_$sp.md)
- [me_01: dbo.extend_pack_skus_$sp](../../StoredProcedures/me_01/dbo.extend_pack_skus_$sp.md)
- [me_01: dbo.freeze_inventory_$sp](../../StoredProcedures/me_01/dbo.freeze_inventory_$sp.md)
- [me_01: dbo.ins_missing_skus_depart_$sp](../../StoredProcedures/me_01/dbo.ins_missing_skus_depart_$sp.md)
- [me_01: dbo.ins_missing_skus_enterpr_$sp](../../StoredProcedures/me_01/dbo.ins_missing_skus_enterpr_$sp.md)
- [me_01: dbo.ins_missing_skus_style_$sp](../../StoredProcedures/me_01/dbo.ins_missing_skus_style_$sp.md)
- [me_01: dbo.insert_packs_$sp](../../StoredProcedures/me_01/dbo.insert_packs_$sp.md)
- [me_01: dbo.insert_packs_bi_$sp](../../StoredProcedures/me_01/dbo.insert_packs_bi_$sp.md)
- [me_01: dbo.insert_pseudo_$sp](../../StoredProcedures/me_01/dbo.insert_pseudo_$sp.md)
- [me_01: dbo.insert_pseudo_bi_$sp](../../StoredProcedures/me_01/dbo.insert_pseudo_bi_$sp.md)
- [me_01: dbo.insert_pseudo_bi_ols_$sp](../../StoredProcedures/me_01/dbo.insert_pseudo_bi_ols_$sp.md)
- [me_01: dbo.insert_pseudo_ols_$sp](../../StoredProcedures/me_01/dbo.insert_pseudo_ols_$sp.md)
- [me_01: dbo.insert_skus_$sp](../../StoredProcedures/me_01/dbo.insert_skus_$sp.md)
- [me_01: dbo.insert_skus_bi_$sp](../../StoredProcedures/me_01/dbo.insert_skus_bi_$sp.md)
- [me_01: dbo.insert_skus_bi_ols_$sp](../../StoredProcedures/me_01/dbo.insert_skus_bi_ols_$sp.md)
- [me_01: dbo.insert_skus_ols_$sp](../../StoredProcedures/me_01/dbo.insert_skus_ols_$sp.md)
- [me_01: dbo.pi_move_store_count_$sp](../../StoredProcedures/me_01/dbo.pi_move_store_count_$sp.md)
- [me_01: dbo.pi_process_loc_$sp](../../StoredProcedures/me_01/dbo.pi_process_loc_$sp.md)
- [me_01: dbo.pi_process_loc_ols_$sp](../../StoredProcedures/me_01/dbo.pi_process_loc_ols_$sp.md)
- [me_01: dbo.pi_update_inventory_tables_$sp](../../StoredProcedures/me_01/dbo.pi_update_inventory_tables_$sp.md)

