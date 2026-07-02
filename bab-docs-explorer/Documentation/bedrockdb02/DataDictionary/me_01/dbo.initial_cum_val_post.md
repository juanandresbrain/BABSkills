# dbo.initial_cum_val_post

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| merch_hierarchy_group_id | int | 4 | 0 | YES |  |  |
| location_id | smallint | 2 | 0 | YES |  |  |
| cost | decimal | 9 | 0 |  |  |  |
| retail | decimal | 9 | 0 |  |  |  |
| cost_local | decimal | 9 | 1 |  |  |  |
| jurisdiction_id | smallint | 2 | 0 | YES |  |  |
| retail_local | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.initvalccpergrpgrp_$sp](../../StoredProcedures/me_01/dbo.initvalccpergrpgrp_$sp.md)
- [me_01: dbo.initvalccpergrpgrpdel_$sp](../../StoredProcedures/me_01/dbo.initvalccpergrpgrpdel_$sp.md)
- [me_01: dbo.initvalccpergrploc_$sp](../../StoredProcedures/me_01/dbo.initvalccpergrploc_$sp.md)
- [me_01: dbo.initvalccpergrplocdel_$sp](../../StoredProcedures/me_01/dbo.initvalccpergrplocdel_$sp.md)
- [me_01: dbo.initvalccperlocgrp_$sp](../../StoredProcedures/me_01/dbo.initvalccperlocgrp_$sp.md)
- [me_01: dbo.initvalccperlocgrpdel_$sp](../../StoredProcedures/me_01/dbo.initvalccperlocgrpdel_$sp.md)
- [me_01: dbo.initvalccperlocloc_$sp](../../StoredProcedures/me_01/dbo.initvalccperlocloc_$sp.md)
- [me_01: dbo.initvalccperloclocdel_$sp](../../StoredProcedures/me_01/dbo.initvalccperloclocdel_$sp.md)
- [me_01: dbo.startup_sl_history_$sp](../../StoredProcedures/me_01/dbo.startup_sl_history_$sp.md)

