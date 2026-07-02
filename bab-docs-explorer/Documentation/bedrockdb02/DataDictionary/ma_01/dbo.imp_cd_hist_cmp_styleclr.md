# dbo.imp_cd_hist_cmp_styleclr

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_code | nvarchar | 40 | 0 |  |  |  |
| color_code | nvarchar | 6 | 0 |  |  |  |
| merch_year_wk | int | 4 | 0 |  |  |  |
| location_code | nvarchar | 40 | 0 |  |  |  |
| component_type_code | smallint | 2 | 0 |  |  |  |
| price_status_code | nvarchar | 6 | 1 |  |  |  |
| transaction_reason_code | nvarchar | 30 | 1 |  |  |  |
| cost_factor_discount_flag | bit | 1 | 1 |  |  |  |
| units | int | 4 | 0 |  |  |  |
| retail | decimal | 9 | 0 |  |  |  |
| cost | decimal | 9 | 0 |  |  |  |
| cost_local | decimal | 9 | 0 |  |  |  |
| retail_te | decimal | 9 | 1 |  |  |  |
| retail_local | decimal | 9 | 0 |  |  |  |
| retail_te_local | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.import_hist_cmp_styleclr_$sp](../../StoredProcedures/ma_01/dbo.import_hist_cmp_styleclr_$sp.md)

