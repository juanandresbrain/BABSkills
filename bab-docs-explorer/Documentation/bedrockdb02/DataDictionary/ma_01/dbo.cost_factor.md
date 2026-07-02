# dbo.cost_factor

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| cost_factor_id | smallint | 2 | 0 | YES |  |  |
| cost_factor_code | nvarchar | 30 | 1 |  |  |  |
| cost_factor_description | nvarchar | 120 | 1 |  |  |  |
| import_flag | bit | 1 | 0 |  |  |  |
| domestic_flag | bit | 1 | 0 |  |  |  |
| currency_indicator | smallint | 2 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.balance_cost_factors_$sp](../../StoredProcedures/me_01/dbo.balance_cost_factors_$sp.md)
- [me_01: dbo.populate_ib_cfd_$sp](../../StoredProcedures/me_01/dbo.populate_ib_cfd_$sp.md)
- [ma_01: dbo.import_hist_cmp_group_$sp](../../StoredProcedures/ma_01/dbo.import_hist_cmp_group_$sp.md)
- [ma_01: dbo.import_hist_cmp_style_$sp](../../StoredProcedures/ma_01/dbo.import_hist_cmp_style_$sp.md)
- [ma_01: dbo.import_hist_cmp_styleclr_$sp](../../StoredProcedures/ma_01/dbo.import_hist_cmp_styleclr_$sp.md)

