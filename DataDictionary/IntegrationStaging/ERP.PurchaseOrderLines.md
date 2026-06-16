# ERP.PurchaseOrderLines

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

- [IntegrationStaging: ERP.spMergePurchaseOrderLines](../../StoredProcedures/IntegrationStaging/ERP.spMergePurchaseOrderLines.md)
- [IntegrationStaging: ERP.spMergePurchaseOrderLines_Bak20210125](../../StoredProcedures/IntegrationStaging/ERP.spMergePurchaseOrderLines_Bak20210125.md)
- [IntegrationStaging: ERP.spMergePurchaseOrderReceipt](../../StoredProcedures/IntegrationStaging/ERP.spMergePurchaseOrderReceipt.md)
- [IntegrationStaging: ERP.spOutputTPMPurchaseOrderXML](../../StoredProcedures/IntegrationStaging/ERP.spOutputTPMPurchaseOrderXML.md)
- [IntegrationStaging: ERP.spOutputTPMPurchaseOrderXML_BAK20210927](../../StoredProcedures/IntegrationStaging/ERP.spOutputTPMPurchaseOrderXML_BAK20210927.md)
- [IntegrationStaging: ERP.spPurchaseOrderDBS_FileCreateFTP](../../StoredProcedures/IntegrationStaging/ERP.spPurchaseOrderDBS_FileCreateFTP.md)
- [IntegrationStaging: ERP.spPurchaseOrderReceiptXML](../../StoredProcedures/IntegrationStaging/ERP.spPurchaseOrderReceiptXML.md)
- [IntegrationStaging: ERP.spPurchaseOrderReceiptXML_Bak_20230123](../../StoredProcedures/IntegrationStaging/ERP.spPurchaseOrderReceiptXML_Bak_20230123.md)
- [IntegrationStaging: ERP.spPurchaseOrderUpdateSendDataBAK20210929](../../StoredProcedures/IntegrationStaging/ERP.spPurchaseOrderUpdateSendDataBAK20210929.md)

