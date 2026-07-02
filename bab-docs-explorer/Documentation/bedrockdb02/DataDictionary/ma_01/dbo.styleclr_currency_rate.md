# dbo.styleclr_currency_rate

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| location_id | smallint | 2 | 0 | YES |  |  |
| cost_exchange_rate | float | 8 | 0 |  |  |  |
| retail_exchange_rate | float | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.import_hist_cmp_styleclr_$sp](../../StoredProcedures/ma_01/dbo.import_hist_cmp_styleclr_$sp.md)
- [ma_01: dbo.startup_styleclr_loc_wk_$sp](../../StoredProcedures/ma_01/dbo.startup_styleclr_loc_wk_$sp.md)

