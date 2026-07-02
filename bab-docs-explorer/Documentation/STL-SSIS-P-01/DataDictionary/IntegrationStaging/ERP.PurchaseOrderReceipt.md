# ERP.PurchaseOrderReceipt

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
| Qty | int | 4 | 1 |  |  |  |
| UOM | varchar | 10 | 1 |  |  |  |
| ReceiptDate | date | 3 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| Transmitted | int | 4 | 1 |  |  |  |
| entity | nvarchar | 20 | 1 |  |  |  |
| BOL | varchar | 52 | 1 |  |  |  |
| AptosPONumber | nvarchar | 40 | 1 |  |  |  |
| POLineNumber | int | 4 | 1 |  |  |  |
| ItemID | nvarchar | 14 | 1 |  |  |  |
| ReceivedQty | int | 4 | 1 |  |  |  |
| CanceledQty | int | 4 | 1 |  |  |  |
| Warehouse | nvarchar | 10 | 1 |  |  |  |
| ASN | nvarchar | 100 | 1 |  |  |  |
| TrailerNbr | varchar | 50 | 1 |  |  |  |
| MessageQueueDateUTC | datetime | 8 | 1 |  |  |  |
| MessageID | nvarchar | 200 | 1 |  |  |  |
| MessageSequence | bigint | 8 | 1 |  |  |  |
| MessageRowIndex | int | 4 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |
| PostedToAptosDate | datetime | 8 | 1 |  |  |  |
| PostedToDynamics1200ShipmentDate | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: ERP.spMergePurchaseOrderReceipt](../../StoredProcedures/IntegrationStaging/ERP.spMergePurchaseOrderReceipt.md)
- [IntegrationStaging: ERP.spOutputD365PurchaseOrderReceiptXMLByEntity](../../StoredProcedures/IntegrationStaging/ERP.spOutputD365PurchaseOrderReceiptXMLByEntity.md)
- [IntegrationStaging: ERP.spOutputD365PurchaseOrderReceiptXMLByEntityBAK20230123](../../StoredProcedures/IntegrationStaging/ERP.spOutputD365PurchaseOrderReceiptXMLByEntityBAK20230123.md)

