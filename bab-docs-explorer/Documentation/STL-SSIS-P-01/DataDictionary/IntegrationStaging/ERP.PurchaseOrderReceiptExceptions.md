# ERP.PurchaseOrderReceiptExceptions

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ReceiptID | int | 4 | 0 |  |  |  |
| PurchaseOrderNumber | varchar | 50 | 1 |  |  |  |
| ReceiptLocation | varchar | 10 | 1 |  |  |  |
| ItemID | varchar | 50 | 1 |  |  |  |
| CaseNumber | varchar | 50 | 1 |  |  |  |
| ConvertedQty | decimal | 9 | 1 |  |  |  |
| UnitQty | int | 4 | 1 |  |  |  |
| Factor | decimal | 9 | 1 |  |  |  |
| UOM | varchar | 10 | 1 |  |  |  |
| ReceiptDate | date | 3 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| entity | nvarchar | 20 | 1 |  |  |  |
| BOL | varchar | 52 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: ERP.spMergePurchaseOrderReceipt](../../StoredProcedures/IntegrationStaging/ERP.spMergePurchaseOrderReceipt.md)

