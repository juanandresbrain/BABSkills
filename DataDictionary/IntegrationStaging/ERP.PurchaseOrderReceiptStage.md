# ERP.PurchaseOrderReceiptStage

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PurchaseOrderNumber | varchar | 50 | 1 |  |  |  |
| ReceiptLocation | varchar | 10 | 1 |  |  |  |
| BOL | varchar | 52 | 1 |  |  |  |
| ItemID | varchar | 50 | 1 |  |  |  |
| CaseNumber | varchar | 50 | 1 |  |  |  |
| Qty | int | 4 | 1 |  |  |  |
| ReceiptDate | date | 3 | 1 |  |  |  |
| entity | nvarchar | 20 | 1 |  |  |  |
| ReferencePO | varchar | 50 | 1 |  |  |  |
| AptosPONumber | nvarchar | 40 | 1 |  |  |  |
| POLineNumber | int | 4 | 1 |  |  |  |
| ItemID | nvarchar | 14 | 1 |  |  |  |
| ReceivedQty | int | 4 | 1 |  |  |  |
| CanceledQty | int | 4 | 1 |  |  |  |
| Warehouse | nvarchar | 10 | 1 |  |  |  |
| ASN | nvarchar | 40 | 1 |  |  |  |
| MessageQueueDateUTC | datetime | 8 | 1 |  |  |  |
| MessageID | nvarchar | 200 | 1 |  |  |  |
| MessageSequence | bigint | 8 | 1 |  |  |  |
| MessageRowIndex | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: ERP.spMergePurchaseOrderReceipt](../../StoredProcedures/IntegrationStaging/ERP.spMergePurchaseOrderReceipt.md)

