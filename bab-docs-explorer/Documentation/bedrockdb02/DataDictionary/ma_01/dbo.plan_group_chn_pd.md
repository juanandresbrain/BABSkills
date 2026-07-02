# dbo.plan_group_chn_pd

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| plan_version_id | smallint | 2 | 0 | YES |  |  |
| hierarchy_group_id | int | 4 | 0 | YES |  |  |
| merch_year_pd | int | 4 | 0 | YES |  |  |
| plan_element_id | smallint | 2 | 0 | YES |  |  |
| plan_value | decimal | 9 | 1 |  |  |  |
| plan_local_value | decimal | 9 | 1 |  |  |  |
| planning_jurisdiction_id | smallint | 2 | 0 | YES |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.nsb_core_chain_$sp](../../StoredProcedures/ma_01/dbo.nsb_core_chain_$sp.md)
- [ma_01: dbo.nsb_otb_chain_$sp](../../StoredProcedures/ma_01/dbo.nsb_otb_chain_$sp.md)
- [ma_01: dbo.nsb_par_chain_$sp](../../StoredProcedures/ma_01/dbo.nsb_par_chain_$sp.md)
- [ma_01: dbo.nsb_par_chain_rim_$sp](../../StoredProcedures/ma_01/dbo.nsb_par_chain_rim_$sp.md)
- [ma_01: dbo.rpt_core_chain_$sp](../../StoredProcedures/ma_01/dbo.rpt_core_chain_$sp.md)
- [ma_01: dbo.rpt_otb_chain_$sp](../../StoredProcedures/ma_01/dbo.rpt_otb_chain_$sp.md)
- [ma_01: dbo.rpt_par_chain_$sp](../../StoredProcedures/ma_01/dbo.rpt_par_chain_$sp.md)
- [ma_01: dbo.rpt_par_chain_rim_$sp](../../StoredProcedures/ma_01/dbo.rpt_par_chain_rim_$sp.md)
- [ma_01: dbo.startup_plan_group_chn_$sp](../../StoredProcedures/ma_01/dbo.startup_plan_group_chn_$sp.md)

