# ERP.PurchaseOrderReceiptPreStage

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PurchaseOrderNumber | varchar | 50 | 1 |  |  |  |
| ReceiptLocation | varchar | 10 | 1 |  |  |  |
| ReceiptDate | date | 3 | 1 |  |  |  |
| ItemID | varchar | 10 | 1 |  |  |  |
| Qty | int | 4 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| Entity | nvarchar | 20 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: ERP.spPOReceiptsImportCN](../../StoredProcedures/IntegrationStaging/ERP.spPOReceiptsImportCN.md)
- [IntegrationStaging: ERP.spPOReceiptsImportUK](../../StoredProcedures/IntegrationStaging/ERP.spPOReceiptsImportUK.md)
- [IntegrationStaging: ERP.spPOReceiptsImportWC](../../StoredProcedures/IntegrationStaging/ERP.spPOReceiptsImportWC.md)

