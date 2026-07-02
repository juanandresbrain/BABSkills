# dbo.count_import_sku_temp

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| count_import_sku_temp_id | decimal | 9 | 0 | YES |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| sku_id | decimal | 9 | 0 |  |  |  |
| zone_label | nvarchar | 30 | 1 |  |  |  |
| units_counted | int | 4 | 0 |  |  |  |
| cost | decimal | 9 | 1 |  |  |  |
| total_retail | decimal | 9 | 1 |  |  |  |
| cost_local | decimal | 9 | 1 |  |  |  |
| total_valuation_retail | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.insert_pseudo_bi_ols_$sp](../../StoredProcedures/me_01/dbo.insert_pseudo_bi_ols_$sp.md)
- [me_01: dbo.insert_pseudo_ols_$sp](../../StoredProcedures/me_01/dbo.insert_pseudo_ols_$sp.md)
- [me_01: dbo.insert_skus_bi_ols_$sp](../../StoredProcedures/me_01/dbo.insert_skus_bi_ols_$sp.md)
- [me_01: dbo.insert_skus_ols_$sp](../../StoredProcedures/me_01/dbo.insert_skus_ols_$sp.md)
- [me_01: dbo.pi_process_loc_ols_$sp](../../StoredProcedures/me_01/dbo.pi_process_loc_ols_$sp.md)

