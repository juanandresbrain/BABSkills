# dbo.price_change_instruction

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| price_change_id | decimal | 9 | 0 | YES |  |  |
| price_change_instruction_id | decimal | 9 | 0 | YES |  |  |
| name | nvarchar | 400 | 1 |  |  |  |
| merch_instruction_type | smallint | 2 | 0 |  |  |  |
| merch_hierarchy_group_id | int | 4 | 1 |  |  |  |
| style_id | decimal | 9 | 1 |  |  |  |
| style_color_id | decimal | 9 | 1 |  |  |  |
| sku_id | decimal | 9 | 1 |  |  |  |
| location_instruction_type | smallint | 2 | 0 |  |  |  |
| location_id | smallint | 2 | 1 |  |  |  |
| jurisdiction_id | smallint | 2 | 1 |  |  |  |
| calculation_method | smallint | 2 | 0 |  |  |  |
| calculation_value | decimal | 9 | 0 |  |  |  |
| base_calculation_on | smallint | 2 | 1 |  |  |  |
| price_status_id | smallint | 2 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.copy_location_price_change_instruction_details_$sp](../../StoredProcedures/me_01/dbo.copy_location_price_change_instruction_details_$sp.md)
- [me_01: dbo.delete_pc_documents_$sp](../../StoredProcedures/me_01/dbo.delete_pc_documents_$sp.md)
- [me_01: dbo.get_pc_references_$sp](../../StoredProcedures/me_01/dbo.get_pc_references_$sp.md)
- [me_01: dbo.imw_price_change_v1_$sp](../../StoredProcedures/me_01/dbo.imw_price_change_v1_$sp.md)
- [me_01: dbo.upd_promo_events_$sp](../../StoredProcedures/me_01/dbo.upd_promo_events_$sp.md)

