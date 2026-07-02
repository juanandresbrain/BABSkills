# dbo.wrk_price_change_calc

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| wrk_price_change_calc_id | int | 4 | 0 | YES |  |  |
| calc_date | smalldatetime | 4 | 0 |  |  |  |
| ready_to_delete | bit | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.delete_wrk_price_change_calc_$sp](../../StoredProcedures/me_01/dbo.delete_wrk_price_change_calc_$sp.md)
- [me_01: dbo.get_pc_instruction_values_$sp](../../StoredProcedures/me_01/dbo.get_pc_instruction_values_$sp.md)
- [me_01: dbo.get_pricing_$sp](../../StoredProcedures/me_01/dbo.get_pricing_$sp.md)

