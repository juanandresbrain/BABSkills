# dbo.plan_element

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| plan_element_id | smallint | 2 | 0 | YES |  |  |
| plan_element_number | nvarchar | 40 | 0 |  |  |  |
| plan_element_label | nvarchar | 120 | 0 |  |  |  |
| otb_element_id | tinyint | 1 | 1 |  |  |  |
| otb_operator | smallint | 2 | 1 |  |  |  |
| plan_exp_table_group_id | smallint | 2 | 0 |  |  |  |
| export_flag | bit | 1 | 0 |  |  |  |
| units_flag | bit | 1 | 0 |  |  |  |
| use_previous_period_flag | bit | 1 | 0 |  |  |  |
| sql_statement | nvarchar | 2000 | 1 |  |  |  |
| default_export_flag | bit | 1 | 0 |  |  |  |
| plan_version_code | nchar | 2 | 0 |  |  |  |
| sql_statement_local | nvarchar | 2000 | 1 |  |  |  |
| element_type | smallint | 2 | 1 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.nsb_par_chain_$sp](../../StoredProcedures/ma_01/dbo.nsb_par_chain_$sp.md)
- [ma_01: dbo.nsb_par_chain_rim_$sp](../../StoredProcedures/ma_01/dbo.nsb_par_chain_rim_$sp.md)
- [ma_01: dbo.nsb_par_location_$sp](../../StoredProcedures/ma_01/dbo.nsb_par_location_$sp.md)
- [ma_01: dbo.rpt_otb_cost_retail_$sp](../../StoredProcedures/ma_01/dbo.rpt_otb_cost_retail_$sp.md)
- [ma_01: dbo.rpt_par_chain_$sp](../../StoredProcedures/ma_01/dbo.rpt_par_chain_$sp.md)
- [ma_01: dbo.rpt_par_chain_rim_$sp](../../StoredProcedures/ma_01/dbo.rpt_par_chain_rim_$sp.md)
- [ma_01: dbo.rpt_par_location_home_$sp](../../StoredProcedures/ma_01/dbo.rpt_par_location_home_$sp.md)
- [ma_01: dbo.rpt_par_location_local_$sp](../../StoredProcedures/ma_01/dbo.rpt_par_location_local_$sp.md)
- [ma_01: dbo.startup_plan_group_loc_pd_$sp](../../StoredProcedures/ma_01/dbo.startup_plan_group_loc_pd_$sp.md)
- [ma_01: dbo.startup_plan_group_loc_wk_$sp](../../StoredProcedures/ma_01/dbo.startup_plan_group_loc_wk_$sp.md)

