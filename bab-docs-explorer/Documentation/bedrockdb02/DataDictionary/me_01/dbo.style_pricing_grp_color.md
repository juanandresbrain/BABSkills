# dbo.style_pricing_grp_color

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_pricing_grp_color_id | decimal | 9 | 0 | YES |  |  |
| style_id | decimal | 9 | 0 |  |  |  |
| pricing_group_id | smallint | 2 | 0 |  |  |  |
| style_color_id | decimal | 9 | 0 |  |  |  |
| jurisdiction_id | smallint | 2 | 0 |  |  |  |
| original_selling_retail | decimal | 9 | 1 |  |  |  |
| original_valuation_retail | decimal | 9 | 1 |  |  |  |
| original_price_status_id | smallint | 2 | 1 |  |  |  |
| current_selling_retail | decimal | 9 | 1 |  |  |  |
| current_valuation_retail | decimal | 9 | 1 |  |  |  |
| current_price_status_id | smallint | 2 | 1 |  |  |  |
| mix_match_rule_id1 | decimal | 9 | 1 |  |  |  |
| mix_match_rule_id2 | decimal | 9 | 1 |  |  |  |
| mix_match_rule_id3 | decimal | 9 | 1 |  |  |  |
| mix_match_rule_id4 | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.ecom_get_style_list_$sp](../../StoredProcedures/me_01/dbo.ecom_get_style_list_$sp.md)
- [me_01: dbo.get_imrd_oh_orig_retail_$sp](../../StoredProcedures/me_01/dbo.get_imrd_oh_orig_retail_$sp.md)
- [me_01: dbo.get_pricing_$sp](../../StoredProcedures/me_01/dbo.get_pricing_$sp.md)
- [me_01: dbo.get_pricing_pg_$sp](../../StoredProcedures/me_01/dbo.get_pricing_pg_$sp.md)
- [me_01: dbo.import_pc_populate_temp_pc_from_ib_$sp](../../StoredProcedures/me_01/dbo.import_pc_populate_temp_pc_from_ib_$sp.md)
- [me_01: dbo.move_pg_exceptions_to_locations_$sp](../../StoredProcedures/me_01/dbo.move_pg_exceptions_to_locations_$sp.md)

