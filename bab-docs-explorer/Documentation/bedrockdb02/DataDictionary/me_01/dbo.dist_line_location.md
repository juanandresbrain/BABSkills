# dbo.dist_line_location

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| distribution_id | bigint | 8 | 0 | YES |  |  |
| location_id | smallint | 2 | 0 | YES |  |  |
| quantity | int | 4 | 0 |  |  |  |
| eligibility | smallint | 2 | 1 |  |  |  |
| instruction | smallint | 2 | 0 |  |  |  |
| instruction_value | int | 4 | 0 |  |  |  |
| style_color_id | decimal | 9 | 0 | YES |  |  |
| hist_effective_inventory | int | 4 | 1 |  |  |  |
| hist_unit_sales | int | 4 | 1 |  |  |  |
| number_weeks_sales | int | 4 | 1 |  |  |  |
| location_need | int | 4 | 1 |  |  |  |
| sales_plan | int | 4 | 1 |  |  |  |
| sales_plan_pct | float | 8 | 1 |  |  |  |
| location_need_pct | float | 8 | 1 |  |  |  |
| location_need_weighting | float | 8 | 1 |  |  |  |
| sales_plan_weighting | float | 8 | 1 |  |  |  |
| suggested_qty_pct | float | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.delete_po_receipt_documents_$sp](../../StoredProcedures/me_01/dbo.delete_po_receipt_documents_$sp.md)
- [me_01: dbo.retrieve_dist_$sp](../../StoredProcedures/me_01/dbo.retrieve_dist_$sp.md)

