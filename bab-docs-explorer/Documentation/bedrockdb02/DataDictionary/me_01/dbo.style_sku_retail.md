# dbo.style_sku_retail

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_sku_retail_id | decimal | 9 | 0 | YES |  |  |
| style_id | decimal | 9 | 0 |  |  |  |
| sku_id | decimal | 9 | 0 |  |  |  |
| jurisdiction_id | smallint | 2 | 0 |  |  |  |
| original_selling_retail | decimal | 9 | 1 |  |  |  |
| original_valuation_retail | decimal | 9 | 1 |  |  |  |
| original_price_status_id | smallint | 2 | 1 |  |  |  |
| current_selling_retail | decimal | 9 | 1 |  |  |  |
| current_valuation_retail | decimal | 9 | 1 |  |  |  |
| current_price_status_id | smallint | 2 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.get_pc_instruction_values_$sp](../../StoredProcedures/me_01/dbo.get_pc_instruction_values_$sp.md)
- [me_01: dbo.get_pricing_$sp](../../StoredProcedures/me_01/dbo.get_pricing_$sp.md)
- [me_01: dbo.get_pricing_pg_$sp](../../StoredProcedures/me_01/dbo.get_pricing_pg_$sp.md)
- [me_01: dbo.upd_style_retails_pc_$sp](../../StoredProcedures/me_01/dbo.upd_style_retails_pc_$sp.md)

