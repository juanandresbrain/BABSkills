# dbo.ib_activity_date

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ib_activity_date_id | decimal | 9 | 0 | YES |  |  |
| style_id | decimal | 9 | 0 |  |  |  |
| color_id | smallint | 2 | 1 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| first_receipt_date | smalldatetime | 4 | 1 |  |  |  |
| last_receipt_date | smalldatetime | 4 | 1 |  |  |  |
| first_sale_date | smalldatetime | 4 | 1 |  |  |  |
| last_sale_date | smalldatetime | 4 | 1 |  |  |  |
| first_on_order_date | smalldatetime | 4 | 1 |  |  |  |
| last_on_order_date | smalldatetime | 4 | 1 |  |  |  |
| first_po_receipt_date | smalldatetime | 4 | 1 |  |  |  |
| last_po_receipt_date | smalldatetime | 4 | 1 |  |  |  |
| first_markdown_date | smalldatetime | 4 | 1 |  |  |  |
| last_markdown_date | smalldatetime | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.complete_sales_posting_$sp](../../StoredProcedures/me_01/dbo.complete_sales_posting_$sp.md)
- [me_01: dbo.import_asn_complete_$sp](../../StoredProcedures/me_01/dbo.import_asn_complete_$sp.md)
- [me_01: dbo.import_asn_fifth_step_$sp](../../StoredProcedures/me_01/dbo.import_asn_fifth_step_$sp.md)
- [me_01: dbo.process_modified_transactions_$sp](../../StoredProcedures/me_01/dbo.process_modified_transactions_$sp.md)
- [me_01: dbo.upd_ib_activity_date_pc_$sp](../../StoredProcedures/me_01/dbo.upd_ib_activity_date_pc_$sp.md)
- [DBAUtility: dbo.spPLM_GetMerchandingData](../../StoredProcedures/DBAUtility/dbo.spPLM_GetMerchandingData.md)
- [DBAUtility: dbo.spPLM_GetMerchandingData_dev](../../StoredProcedures/DBAUtility/dbo.spPLM_GetMerchandingData_dev.md)
- [ma_01: dbo.nsb_style_analysis_$sp](../../StoredProcedures/ma_01/dbo.nsb_style_analysis_$sp.md)
- [ma_01: dbo.rpt_style_analysis_$sp](../../StoredProcedures/ma_01/dbo.rpt_style_analysis_$sp.md)
- [ma_01: dbo.rpt_style_color_sell_thru_$sp](../../StoredProcedures/ma_01/dbo.rpt_style_color_sell_thru_$sp.md)

