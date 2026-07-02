# dbo.import_po_receipt_sku

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| import_po_receipt_sku_id | decimal | 9 | 0 | YES |  |  |
| import_po_receipt_id | decimal | 9 | 0 |  |  |  |
| action | nvarchar | 2 | 0 |  |  |  |
| allocation_no | nvarchar | 40 | 1 |  |  |  |
| upc_number | nvarchar | 40 | 0 |  |  |  |
| units_received | int | 4 | 0 |  |  |  |
| units_damaged | int | 4 | 1 |  |  |  |
| pack_code | nvarchar | 40 | 1 |  |  |  |
| style_code | nvarchar | 40 | 1 |  |  |  |
| color_code | nvarchar | 6 | 1 |  |  |  |
| primary_size_label | nvarchar | 16 | 1 |  |  |  |
| secondary_size_label | nvarchar | 16 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingReportPOReceiptErrors](../../StoredProcedures/me_01/dbo.spMerchandisingReportPOReceiptErrors.md)
- [me_01: dbo.spMerchandisingSelectPOReceiptSummary](../../StoredProcedures/me_01/dbo.spMerchandisingSelectPOReceiptSummary.md)

