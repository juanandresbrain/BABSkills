# WMS.PurchaseOrderMerchToDynamicsStage

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PONumber | varchar | 20 | 1 |  |  |  |
| POLineNumber | int | 4 | 1 |  |  |  |
| ItemNumber | varchar | 10 | 1 |  |  |  |
| Quantity | int | 4 | 1 |  |  |  |
| DeliveryDate | datetime | 8 | 1 |  |  |  |
| VendorCode | varchar | 10 | 1 |  |  |  |
| UnitCost | numeric | 17 | 1 |  |  |  |
| FactoryCode | varchar | 10 | 1 |  |  |  |
| POMainLIne | int | 4 | 1 |  |  |  |
| NetFinalPrice | numeric | 9 | 1 |  |  |  |
| CancelDate | date | 3 | 1 |  |  |  |
| Warehouse | varchar | 4 | 1 |  |  |  |
| Company | varchar | 4 | 1 |  |  |  |
| StartShipDate | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spMergePurchaseOrderMerchToDynamics](../../StoredProcedures/IntegrationStaging/WMS.spMergePurchaseOrderMerchToDynamics.md)

