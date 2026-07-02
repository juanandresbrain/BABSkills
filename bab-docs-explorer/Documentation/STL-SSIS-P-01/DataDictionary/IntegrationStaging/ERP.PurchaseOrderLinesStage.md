# ERP.PurchaseOrderLinesStage

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PurchaseOrderNumber | varchar | 50 | 1 |  |  |  |
| ConfirmationNumber | varchar | 50 | 1 |  |  |  |
| Lines_ID | int | 4 | 1 |  |  |  |
| LineNumber | int | 4 | 1 |  |  |  |
| DestinationWarehouse | int | 4 | 1 |  |  |  |
| ItemID | varchar | 50 | 1 |  |  |  |
| CurrQty | int | 4 | 1 |  |  |  |
| UnitCost | numeric | 17 | 1 |  |  |  |
| StartShipDate | datetime | 8 | 1 |  |  |  |
| EndDeliverDateTime | datetime | 8 | 1 |  |  |  |
| CancelDate | datetime | 8 | 1 |  |  |  |
| VendExtItemID | varchar | 50 | 1 |  |  |  |
| VendExtItemDescription | varchar | 100 | 1 |  |  |  |
| FactoryCode | varchar | 10 | 1 |  |  |  |
| FactoryName | varchar | 100 | 1 |  |  |  |
| FactoryPort | varchar | 100 | 1 |  |  |  |
| FactoryAddress | varchar | 100 | 1 |  |  |  |
| FactoryCity | varchar | 100 | 1 |  |  |  |
| FactoryProvince | varchar | 100 | 1 |  |  |  |
| COOCode | varchar | 100 | 1 |  |  |  |
| Entity | nvarchar | 20 | 1 |  |  |  |
| IsCurrent | int | 4 | 1 |  |  |  |
| UOM | varchar | 10 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: ERP.spMergePurchaseOrderLines](../../StoredProcedures/IntegrationStaging/ERP.spMergePurchaseOrderLines.md)
- [IntegrationStaging: ERP.spMergePurchaseOrderLines_Bak20210125](../../StoredProcedures/IntegrationStaging/ERP.spMergePurchaseOrderLines_Bak20210125.md)
- [IntegrationStaging: ERP.spMergePurchaseOrderLinesServiceItems](../../StoredProcedures/IntegrationStaging/ERP.spMergePurchaseOrderLinesServiceItems.md)

