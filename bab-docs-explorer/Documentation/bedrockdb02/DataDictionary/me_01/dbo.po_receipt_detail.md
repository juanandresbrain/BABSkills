# dbo.po_receipt_detail

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| po_receipt_detail_id | decimal | 9 | 0 | YES |  |  |
| po_receipt_id | decimal | 9 | 0 |  |  |  |
| pack_id | decimal | 9 | 1 |  |  |  |
| sku_id | decimal | 9 | 1 |  |  |  |
| style_id | decimal | 9 | 1 |  |  |  |
| style_color_id | decimal | 9 | 1 |  |  |  |
| carton_no | nvarchar | 40 | 1 |  |  |  |
| units_received | int | 4 | 1 |  |  |  |
| units_damaged | int | 4 | 1 |  |  |  |
| total_retail | decimal | 9 | 1 |  |  |  |
| total_net_final_cost | decimal | 9 | 1 |  |  |  |
| total_gross_cost | decimal | 9 | 1 |  |  |  |
| total_valuation_retail | decimal | 9 | 1 |  |  |  |
| units_shipped | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.delete_po_receipt_documents_$sp](../../StoredProcedures/me_01/dbo.delete_po_receipt_documents_$sp.md)
- [me_01: dbo.import_asn_second_step_$sp](../../StoredProcedures/me_01/dbo.import_asn_second_step_$sp.md)
- [me_01: dbo.pom_check_released_units_$sp](../../StoredProcedures/me_01/dbo.pom_check_released_units_$sp.md)
- [me_01: dbo.populate_ib_cost_retail_$sp](../../StoredProcedures/me_01/dbo.populate_ib_cost_retail_$sp.md)
- [me_01: dbo.spMerchandisingEmailPOReceiptMexico](../../StoredProcedures/me_01/dbo.spMerchandisingEmailPOReceiptMexico.md)
- [me_01: dbo.spMerchandisingPrintTransferCAPO](../../StoredProcedures/me_01/dbo.spMerchandisingPrintTransferCAPO.md)
- [me_01: dbo.spMerchandisingSelectPOReceiptSummary](../../StoredProcedures/me_01/dbo.spMerchandisingSelectPOReceiptSummary.md)
- [me_01: dbo.spMerchandisingSelectTransferCAPO](../../StoredProcedures/me_01/dbo.spMerchandisingSelectTransferCAPO.md)

