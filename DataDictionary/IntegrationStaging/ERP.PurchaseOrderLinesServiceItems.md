# ERP.PurchaseOrderLinesServiceItems

**Database:** IntegrationStaging  

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
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |
| SendData | int | 4 | 1 |  |  |  |
| MergeAction | varchar | 10 | 1 |  |  |  |
| UOM | varchar | 10 | 1 |  |  |  |
| Exported_TPM | datetime | 8 | 1 |  |  |  |
| Exported_DBS | datetime | 8 | 1 |  |  |  |
| Exported_UK | datetime | 8 | 1 |  |  |  |
| Exported_CN | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: ERP.spMergePurchaseOrderLinesServiceItems](../../StoredProcedures/IntegrationStaging/ERP.spMergePurchaseOrderLinesServiceItems.md)
- [IntegrationStaging: ERP.spOutputTPMPurchaseOrderXML](../../StoredProcedures/IntegrationStaging/ERP.spOutputTPMPurchaseOrderXML.md)

