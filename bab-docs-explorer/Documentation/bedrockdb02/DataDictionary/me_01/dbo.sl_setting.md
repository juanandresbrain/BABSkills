# dbo.sl_setting

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| sl_setting_type | smallint | 2 | 0 | YES |  |  |
| last_id | decimal | 9 | 0 |  |  |  |
| batch_size | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.reclass_hist_$sp](../../StoredProcedures/me_01/dbo.reclass_hist_$sp.md)
- [me_01: dbo.reclass_hist_oh_$sp](../../StoredProcedures/me_01/dbo.reclass_hist_oh_$sp.md)
- [me_01: dbo.spMerchandisingOutputSLlastPosting](../../StoredProcedures/me_01/dbo.spMerchandisingOutputSLlastPosting.md)
- [me_01: dbo.startup_sl_history_$sp](../../StoredProcedures/me_01/dbo.startup_sl_history_$sp.md)

