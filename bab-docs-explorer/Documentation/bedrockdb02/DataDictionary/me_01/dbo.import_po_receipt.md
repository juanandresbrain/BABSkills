# dbo.import_po_receipt

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| import_po_receipt_id | decimal | 9 | 0 | YES |  |  |
| action | nvarchar | 2 | 0 |  |  |  |
| po_receipt_no | nvarchar | 40 | 0 |  |  |  |
| po_receipt_description | nvarchar | 120 | 1 |  |  |  |
| receive_date | smalldatetime | 4 | 0 |  |  |  |
| location_code | nvarchar | 40 | 0 |  |  |  |
| po_no | nvarchar | 40 | 0 |  |  |  |
| received_by | nvarchar | 120 | 1 |  |  |  |
| unit_weight_code | nvarchar | 20 | 1 |  |  |  |
| weight | decimal | 9 | 1 |  |  |  |
| container_type_code | nvarchar | 6 | 1 |  |  |  |
| no_of_containers | smallint | 2 | 1 |  |  |  |
| packing_list_no | nvarchar | 40 | 1 |  |  |  |
| packing_list_date | smalldatetime | 4 | 1 |  |  |  |
| advance_shipping_notice_no | nvarchar | 40 | 1 |  |  |  |
| ship_via_code | nvarchar | 4 | 1 |  |  |  |
| carrier_code | nvarchar | 8 | 1 |  |  |  |
| pro_bill_no | nvarchar | 60 | 1 |  |  |  |
| freight_amount | decimal | 9 | 1 |  |  |  |
| payment_method | nvarchar | 2 | 1 |  |  |  |
| appointment_no | nvarchar | 12 | 1 |  |  |  |
| priority | nvarchar | 2 | 1 |  |  |  |
| bol_total_cartons | int | 4 | 1 |  |  |  |
| destination | nvarchar | 2 | 0 |  |  |  |
| imp_file_name | nvarchar | 400 | 0 |  |  |  |
| external_doc_no | varchar | 20 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingReportPOReceiptErrors](../../StoredProcedures/me_01/dbo.spMerchandisingReportPOReceiptErrors.md)
- [me_01: dbo.spMerchandisingSelectPOReceiptSummary](../../StoredProcedures/me_01/dbo.spMerchandisingSelectPOReceiptSummary.md)

