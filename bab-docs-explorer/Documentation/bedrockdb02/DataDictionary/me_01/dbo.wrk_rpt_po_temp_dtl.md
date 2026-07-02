# dbo.wrk_rpt_po_temp_dtl

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| run_no | int | 4 | 0 | YES |  |  |
| po_detail_id | int | 4 | 0 | YES |  |  |
| po_id | decimal | 9 | 0 | YES |  |  |
| po_line_id | smallint | 2 | 0 |  |  |  |
| po_location_id | smallint | 2 | 0 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| po_shipment_id | smallint | 2 | 0 |  |  |  |
| pack_id | decimal | 9 | 1 |  |  |  |
| sku_id | decimal | 9 | 0 | YES |  |  |
| total_ordered_retail_val | decimal | 9 | 1 |  |  |  |
| pseudo_style_flag | bit | 1 | 0 |  |  |  |
| ordered_units | int | 4 | 1 |  |  |  |
| pack_ordered_units | smallint | 2 | 1 |  |  |  |
| expected_receipt_date | smalldatetime | 4 | 1 |  |  |  |
| line_no | decimal | 9 | 1 |  |  |  |
| style_id | decimal | 9 | 1 |  |  |  |
| style_color_id | decimal | 9 | 1 |  |  |  |
| color_id | smallint | 2 | 1 |  |  |  |
| size_master_id | int | 4 | 1 |  |  |  |
| receipt_detail_flag | bit | 1 | 0 |  |  |  |
| net_final_unit_cost | decimal | 9 | 1 |  |  |  |
| net_unit_cost_domestic | decimal | 9 | 1 |  |  |  |
| total_ordered_retail_val_excl_taxes | decimal | 9 | 1 |  |  |  |
| total_received_retail_val | decimal | 9 | 1 |  |  |  |
| total_received_cost | decimal | 9 | 1 |  |  |  |
| received_units | int | 4 | 1 |  |  |  |
| run_date | smalldatetime | 4 | 0 |  |  |  |
| units_per_pack | int | 4 | 0 |  |  |  |
| unit_first_cost | decimal | 9 | 1 |  |  |  |
| unit_retail_val | decimal | 9 | 1 |  |  |  |
| upc_number | nvarchar | 28 | 1 |  |  |  |
| upc_last_activity_date | smalldatetime | 4 | 1 |  |  |  |
| style_color_long_desc | nvarchar | 40 | 1 |  |  |  |
| retail_style_color_id | decimal | 9 | 1 |  |  |  |
| upc_activation_date | smalldatetime | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.rpt_get_po_line_by_size_$sp](../../StoredProcedures/me_01/dbo.rpt_get_po_line_by_size_$sp.md)
- [me_01: dbo.rpt_get_po_line_shp_by_sz_$sp](../../StoredProcedures/me_01/dbo.rpt_get_po_line_shp_by_sz_$sp.md)
- [me_01: dbo.rpt_get_pos_$sp](../../StoredProcedures/me_01/dbo.rpt_get_pos_$sp.md)

