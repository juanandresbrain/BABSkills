# WMS.DynamicsProductReceiptLineStage

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| dataAreaId | nvarchar | 8000 | 1 |  |  |  |
| ItemNumber | nvarchar | 8000 | 1 |  |  |  |
| LineNumber | float | 8 | 1 |  |  |  |
| OrderedPurchaseQuantity | float | 8 | 1 |  |  |  |
| ProductNumber | nvarchar | 8000 | 1 |  |  |  |
| ProductReceiptDate | datetime | 8 | 1 |  |  |  |
| ProductReceiptHeaderRecordId | bigint | 8 | 1 |  |  |  |
| ProductReceiptNumber | nvarchar | 8000 | 1 |  |  |  |
| PurchaseOrderLineNumber | bigint | 8 | 1 |  |  |  |
| PurchaseOrderNumber | nvarchar | 8000 | 1 |  |  |  |
| PurchaseUnitSymbol | nvarchar | 8000 | 1 |  |  |  |
| ReceivedInventoryQuantity | float | 8 | 1 |  |  |  |
| ReceivedInventoryStatusId | nvarchar | 8000 | 1 |  |  |  |
| ReceivedPurchaseQuantity | float | 8 | 1 |  |  |  |
| ReceivingSiteId | nvarchar | 8000 | 1 |  |  |  |
| ReceivingWarehouseId | nvarchar | 8000 | 1 |  |  |  |
| RecordId | bigint | 8 | 1 |  |  |  |
| RemainingInventoryQuantity | float | 8 | 1 |  |  |  |
| RemainingPurchaseQuantity | float | 8 | 1 |  |  |  |

