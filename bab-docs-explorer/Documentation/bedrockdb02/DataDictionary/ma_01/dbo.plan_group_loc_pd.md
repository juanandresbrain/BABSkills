# dbo.plan_group_loc_pd

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| plan_version_id | smallint | 2 | 0 | YES |  |  |
| hierarchy_group_id | int | 4 | 0 | YES |  |  |
| merch_year_pd | int | 4 | 0 | YES |  |  |
| location_id | smallint | 2 | 0 | YES |  |  |
| plan_element_id | smallint | 2 | 0 | YES |  |  |
| plan_value | decimal | 9 | 1 |  |  |  |
| plan_local_value | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.nsb_core_location_$sp](../../StoredProcedures/ma_01/dbo.nsb_core_location_$sp.md)
- [ma_01: dbo.nsb_otb_location_$sp](../../StoredProcedures/ma_01/dbo.nsb_otb_location_$sp.md)
- [ma_01: dbo.nsb_par_location_$sp](../../StoredProcedures/ma_01/dbo.nsb_par_location_$sp.md)
- [ma_01: dbo.rpt_core_location_home_$sp](../../StoredProcedures/ma_01/dbo.rpt_core_location_home_$sp.md)
- [ma_01: dbo.rpt_core_location_local_$sp](../../StoredProcedures/ma_01/dbo.rpt_core_location_local_$sp.md)
- [ma_01: dbo.rpt_otb_cost_retail_$sp](../../StoredProcedures/ma_01/dbo.rpt_otb_cost_retail_$sp.md)
- [ma_01: dbo.rpt_otb_location_$sp](../../StoredProcedures/ma_01/dbo.rpt_otb_location_$sp.md)
- [ma_01: dbo.rpt_par_location_home_$sp](../../StoredProcedures/ma_01/dbo.rpt_par_location_home_$sp.md)
- [ma_01: dbo.rpt_par_location_local_$sp](../../StoredProcedures/ma_01/dbo.rpt_par_location_local_$sp.md)
- [ma_01: dbo.startup_plan_group_loc_pd_$sp](../../StoredProcedures/ma_01/dbo.startup_plan_group_loc_pd_$sp.md)

