# ERP.PurchaseOrderHeader

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PurchaseOrderNumber | varchar | 50 | 1 |  |  |  |
| ConfirmationNumber | varchar | 50 | 1 |  |  |  |
| TransportMethodDesc | varchar | 50 | 1 |  |  |  |
| FOBDesc | varchar | 50 | 1 |  |  |  |
| ShipFromId | varchar | 50 | 1 |  |  |  |
| Rep2Id | varchar | 50 | 1 |  |  |  |
| CurrencyDesc | varchar | 50 | 1 |  |  |  |
| OrderCreateDate | datetime | 8 | 1 |  |  |  |
| PaymentTerms | varchar | 50 | 1 |  |  |  |
| Entity | nvarchar | 20 | 1 |  |  |  |
| IsCurrent | int | 4 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |
| SendData | int | 4 | 1 |  |  |  |
| Exported_TPM | datetime | 8 | 1 |  |  |  |
| Exported_DBS | datetime | 8 | 1 |  |  |  |
| Exported_UK | datetime | 8 | 1 |  |  |  |
| Exported_CN | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: ERP.spMergePurchaseOrderHeader](../../StoredProcedures/IntegrationStaging/ERP.spMergePurchaseOrderHeader.md)
- [IntegrationStaging: ERP.spMergePurchaseOrderHeader_Bak20210125](../../StoredProcedures/IntegrationStaging/ERP.spMergePurchaseOrderHeader_Bak20210125.md)
- [IntegrationStaging: ERP.spMergePurchaseOrderReceipt](../../StoredProcedures/IntegrationStaging/ERP.spMergePurchaseOrderReceipt.md)
- [IntegrationStaging: ERP.spOutputD365PurchaseOrderReceiptXMLByEntity](../../StoredProcedures/IntegrationStaging/ERP.spOutputD365PurchaseOrderReceiptXMLByEntity.md)
- [IntegrationStaging: ERP.spOutputD365PurchaseOrderReceiptXMLByEntityBAK20230123](../../StoredProcedures/IntegrationStaging/ERP.spOutputD365PurchaseOrderReceiptXMLByEntityBAK20230123.md)
- [IntegrationStaging: ERP.spOutputTPMPurchaseOrderXML](../../StoredProcedures/IntegrationStaging/ERP.spOutputTPMPurchaseOrderXML.md)
- [IntegrationStaging: ERP.spOutputTPMPurchaseOrderXML_BAK20210927](../../StoredProcedures/IntegrationStaging/ERP.spOutputTPMPurchaseOrderXML_BAK20210927.md)
- [IntegrationStaging: ERP.spPurchaseOrderDBS_FileCreateFTP](../../StoredProcedures/IntegrationStaging/ERP.spPurchaseOrderDBS_FileCreateFTP.md)
- [IntegrationStaging: ERP.spPurchaseOrderUpdateSendDataBAK20210929](../../StoredProcedures/IntegrationStaging/ERP.spPurchaseOrderUpdateSendDataBAK20210929.md)

