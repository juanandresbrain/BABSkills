# dbo.parameter_sl_accum_dep

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| parameter_sl_accum_dep_id | smallint | 2 | 0 | YES |  |  |
| effective_period_id | decimal | 9 | 0 |  |  |  |
| cum_val_loc_level_id | int | 4 | 0 |  |  |  |
| cum_val_merch_level_id | int | 4 | 0 |  |  |  |
| period_of_accumulation | tinyint | 1 | 0 |  |  |  |
| reset_rule_type | tinyint | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.get_stock_ledger_rim_$sp](../../StoredProcedures/me_01/dbo.get_stock_ledger_rim_$sp.md)

