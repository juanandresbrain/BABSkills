# dbo.parameter_plan_elements

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| curr_plan_version_id | smallint | 2 | 0 | YES |  |  |
| oh_unit_element_id | smallint | 2 | 0 |  |  |  |
| oh_retail_element_id | smallint | 2 | 0 |  |  |  |
| md_element_id | smallint | 2 | 0 |  |  |  |
| sales_unit_element_id | smallint | 2 | 0 |  |  |  |
| sales_retail_element_id | smallint | 2 | 0 |  |  |  |
| shrink_unit_element_id | smallint | 2 | 0 |  |  |  |
| shrink_retail_element_id | smallint | 2 | 0 |  |  |  |
| sales_cost_element_id | smallint | 2 | 0 |  |  |  |
| receipt_unit_element_id | smallint | 2 | 0 |  |  |  |
| receipt_retail_element_id | smallint | 2 | 0 |  |  |  |
| oh_cost_element_id | smallint | 2 | 0 |  |  |  |
| receipt_cost_element_id | smallint | 2 | 0 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.nsb_core_chain_$sp](../../StoredProcedures/ma_01/dbo.nsb_core_chain_$sp.md)
- [ma_01: dbo.nsb_core_location_$sp](../../StoredProcedures/ma_01/dbo.nsb_core_location_$sp.md)
- [ma_01: dbo.nsb_mar_chain_md_$sp](../../StoredProcedures/ma_01/dbo.nsb_mar_chain_md_$sp.md)
- [ma_01: dbo.nsb_mar_location_md_$sp](../../StoredProcedures/ma_01/dbo.nsb_mar_location_md_$sp.md)
- [ma_01: dbo.nsb_otb_chain_$sp](../../StoredProcedures/ma_01/dbo.nsb_otb_chain_$sp.md)
- [ma_01: dbo.nsb_otb_location_$sp](../../StoredProcedures/ma_01/dbo.nsb_otb_location_$sp.md)
- [ma_01: dbo.nsb_par_chain_$sp](../../StoredProcedures/ma_01/dbo.nsb_par_chain_$sp.md)
- [ma_01: dbo.nsb_par_chain_rim_$sp](../../StoredProcedures/ma_01/dbo.nsb_par_chain_rim_$sp.md)
- [ma_01: dbo.nsb_par_location_$sp](../../StoredProcedures/ma_01/dbo.nsb_par_location_$sp.md)
- [ma_01: dbo.rpt_core_chain_$sp](../../StoredProcedures/ma_01/dbo.rpt_core_chain_$sp.md)
- [ma_01: dbo.rpt_core_location_home_$sp](../../StoredProcedures/ma_01/dbo.rpt_core_location_home_$sp.md)
- [ma_01: dbo.rpt_core_location_local_$sp](../../StoredProcedures/ma_01/dbo.rpt_core_location_local_$sp.md)
- [ma_01: dbo.rpt_mar_chain_md_$sp](../../StoredProcedures/ma_01/dbo.rpt_mar_chain_md_$sp.md)
- [ma_01: dbo.rpt_mar_location_md_home_$sp](../../StoredProcedures/ma_01/dbo.rpt_mar_location_md_home_$sp.md)
- [ma_01: dbo.rpt_mar_location_md_local_$sp](../../StoredProcedures/ma_01/dbo.rpt_mar_location_md_local_$sp.md)
- [ma_01: dbo.rpt_otb_chain_$sp](../../StoredProcedures/ma_01/dbo.rpt_otb_chain_$sp.md)
- [ma_01: dbo.rpt_otb_location_$sp](../../StoredProcedures/ma_01/dbo.rpt_otb_location_$sp.md)
- [ma_01: dbo.rpt_par_chain_$sp](../../StoredProcedures/ma_01/dbo.rpt_par_chain_$sp.md)
- [ma_01: dbo.rpt_par_chain_rim_$sp](../../StoredProcedures/ma_01/dbo.rpt_par_chain_rim_$sp.md)
- [ma_01: dbo.rpt_par_location_home_$sp](../../StoredProcedures/ma_01/dbo.rpt_par_location_home_$sp.md)
- [ma_01: dbo.rpt_par_location_local_$sp](../../StoredProcedures/ma_01/dbo.rpt_par_location_local_$sp.md)

