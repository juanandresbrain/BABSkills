# dbo.sl_history

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| merch_hierarchy_group_id | int | 4 | 0 | YES |  |  |
| history_period_id | decimal | 9 | 0 | YES |  |  |
| location_id | smallint | 2 | 0 | YES |  |  |
| sl_component_id | decimal | 9 | 0 | YES |  |  |
| history_value | decimal | 9 | 0 |  |  |  |
| history_value_local | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.get_stock_ledger_cim_$sp](../../StoredProcedures/me_01/dbo.get_stock_ledger_cim_$sp.md)
- [me_01: dbo.get_stock_ledger_cim_lg_$sp](../../StoredProcedures/me_01/dbo.get_stock_ledger_cim_lg_$sp.md)
- [me_01: dbo.get_stock_ledger_rim_$sp](../../StoredProcedures/me_01/dbo.get_stock_ledger_rim_$sp.md)
- [me_01: dbo.rim_post_$sp](../../StoredProcedures/me_01/dbo.rim_post_$sp.md)
- [me_01: dbo.roll_onhand_$sp](../../StoredProcedures/me_01/dbo.roll_onhand_$sp.md)
- [me_01: dbo.startup_sl_history_$sp](../../StoredProcedures/me_01/dbo.startup_sl_history_$sp.md)
- [me_01: dbo.startup_sl_history_single_jurisdiction_$sp](../../StoredProcedures/me_01/dbo.startup_sl_history_single_jurisdiction_$sp.md)

