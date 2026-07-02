# dbo.dist_location

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| distribution_id | bigint | 8 | 0 | YES |  |  |
| location_id | smallint | 2 | 0 | YES |  |  |
| expected_receipt_date | smalldatetime | 4 | 0 |  |  |  |
| suggested_quantity | int | 4 | 0 |  |  |  |
| instruction | smallint | 2 | 0 |  |  |  |
| instruction_value | int | 4 | 0 |  |  |  |
| dist_volume_grade_id | int | 4 | 1 |  |  |  |
| dist_sell_thru_grade_id | int | 4 | 1 |  |  |  |
| dist_grp_instruction_id | int | 4 | 1 |  |  |  |
| effective_inventory | int | 4 | 0 |  |  |  |
| hist_effective_inventory | int | 4 | 0 |  |  |  |
| unit_sales | int | 4 | 0 |  |  |  |
| hist_unit_sales | int | 4 | 0 |  |  |  |
| retail_sales | int | 4 | 0 |  |  |  |
| hist_retail_sales | int | 4 | 0 |  |  |  |
| on_hand | int | 4 | 0 |  |  |  |
| hist_on_hand | int | 4 | 0 |  |  |  |
| number_weeks_sales | decimal | 5 | 0 |  |  |  |
| remaining_sales | int | 4 | 0 |  |  |  |
| prior_dist_flag | bit | 1 | 0 |  |  |  |
| prior_dist_quantity | int | 4 | 0 |  |  |  |
| desired_quantity | int | 4 | 0 |  |  |  |
| ots_flag | bit | 1 | 0 |  |  |  |
| eligibility | smallint | 2 | 1 |  |  |  |
| total_distributed_detail_qty | int | 4 | 0 |  |  |  |
| total_suggested_detail_qty | int | 4 | 0 |  |  |  |
| location_need | int | 4 | 0 |  |  |  |
| gmroi | decimal | 5 | 0 |  |  |  |
| sales_plan_weighting | float | 8 | 1 |  |  |  |
| unit_need_weighting | float | 8 | 1 |  |  |  |
| suggested_qty_pct | float | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.delete_po_receipt_documents_$sp](../../StoredProcedures/me_01/dbo.delete_po_receipt_documents_$sp.md)
- [me_01: dbo.import_asn_seventh_step_$sp](../../StoredProcedures/me_01/dbo.import_asn_seventh_step_$sp.md)
- [me_01: dbo.no_wms_create_ss_$sp](../../StoredProcedures/me_01/dbo.no_wms_create_ss_$sp.md)
- [me_01: dbo.retrieve_dist_$sp](../../StoredProcedures/me_01/dbo.retrieve_dist_$sp.md)
- [me_01: dbo.xfers_from_distro_$sp](../../StoredProcedures/me_01/dbo.xfers_from_distro_$sp.md)

