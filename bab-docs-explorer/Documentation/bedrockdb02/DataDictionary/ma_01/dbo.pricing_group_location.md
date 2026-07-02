# dbo.pricing_group_location

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| pricing_group_location_id | decimal | 9 | 0 | YES |  |  |
| pricing_group_id | smallint | 2 | 0 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.get_crnt_perm_price_no_prec_out_$sp](../../StoredProcedures/me_01/dbo.get_crnt_perm_price_no_prec_out_$sp.md)
- [me_01: dbo.get_current_retail_$sp](../../StoredProcedures/me_01/dbo.get_current_retail_$sp.md)
- [me_01: dbo.get_imrd_oh_orig_retail_$sp](../../StoredProcedures/me_01/dbo.get_imrd_oh_orig_retail_$sp.md)
- [me_01: dbo.get_pricing_$sp](../../StoredProcedures/me_01/dbo.get_pricing_$sp.md)
- [me_01: dbo.import_pc_batch_tickets_$sp](../../StoredProcedures/me_01/dbo.import_pc_batch_tickets_$sp.md)
- [me_01: dbo.import_pc_populate_temp_pc_$sp](../../StoredProcedures/me_01/dbo.import_pc_populate_temp_pc_$sp.md)
- [me_01: dbo.import_pc_populate_temp_pc_from_ib_$sp](../../StoredProcedures/me_01/dbo.import_pc_populate_temp_pc_from_ib_$sp.md)
- [me_01: dbo.move_pg_exceptions_to_locations_$sp](../../StoredProcedures/me_01/dbo.move_pg_exceptions_to_locations_$sp.md)
- [me_01: dbo.pc_calc_total_affected_units_$sp](../../StoredProcedures/me_01/dbo.pc_calc_total_affected_units_$sp.md)
- [me_01: dbo.pcm_get_tickets_$sp](../../StoredProcedures/me_01/dbo.pcm_get_tickets_$sp.md)
- [me_01: dbo.pcm_pre_issue_pc_$sp](../../StoredProcedures/me_01/dbo.pcm_pre_issue_pc_$sp.md)
- [me_01: dbo.plu_get_location_info_$sp](../../StoredProcedures/me_01/dbo.plu_get_location_info_$sp.md)

