# dbo.ib_fixed_average_cost_pseudo_style

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_id | decimal | 9 | 0 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| average_cost | decimal | 9 | 1 |  |  |  |
| average_cost_local | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.complete_sales_posting_$sp](../../StoredProcedures/me_01/dbo.complete_sales_posting_$sp.md)
- [me_01: dbo.pop_fixed_avg_cost_for_pseudo_style_$sp](../../StoredProcedures/me_01/dbo.pop_fixed_avg_cost_for_pseudo_style_$sp.md)
- [me_01: dbo.populate_temp_sale_master_$sp](../../StoredProcedures/me_01/dbo.populate_temp_sale_master_$sp.md)
- [me_01: dbo.prep_fixed_avg_cost_calculation_$sp](../../StoredProcedures/me_01/dbo.prep_fixed_avg_cost_calculation_$sp.md)

