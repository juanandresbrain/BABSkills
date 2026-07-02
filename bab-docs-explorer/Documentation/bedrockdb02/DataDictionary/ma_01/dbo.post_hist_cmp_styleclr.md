# dbo.post_hist_cmp_styleclr

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_id | decimal | 9 | 0 |  |  |  |
| color_id | smallint | 2 | 0 |  |  |  |
| merch_year_wk | int | 4 | 0 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| price_status_id | smallint | 2 | 0 |  |  |  |
| transaction_type_code | smallint | 2 | 0 |  |  |  |
| transaction_reason_id | smallint | 2 | 1 |  |  |  |
| transaction_units | int | 4 | 0 |  |  |  |
| transaction_retail | decimal | 9 | 0 |  |  |  |
| transaction_cost | decimal | 9 | 0 |  |  |  |
| component_sellcurr_retail | decimal | 9 | 0 |  |  |  |
| transaction_retail_te | decimal | 9 | 1 |  |  |  |
| component_sellcurr_retail_te | decimal | 9 | 1 |  |  |  |
| transaction_cost_local | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.post_cmp_work_styleclr_$sp](../../StoredProcedures/ma_01/dbo.post_cmp_work_styleclr_$sp.md)
- [ma_01: dbo.post_hist_oh_cmp_styleclr_$sp](../../StoredProcedures/ma_01/dbo.post_hist_oh_cmp_styleclr_$sp.md)

