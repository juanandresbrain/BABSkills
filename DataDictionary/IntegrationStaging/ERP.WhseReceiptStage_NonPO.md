# ERP.WhseReceiptStage_NonPO

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ReferenceNumber | varchar | 50 | 1 |  |  |  |
| BOL | varchar | 52 | 1 |  |  |  |
| ReceiptLocation | varchar | 10 | 1 |  |  |  |
| ItemID | varchar | 50 | 1 |  |  |  |
| CaseNumber | varchar | 50 | 1 |  |  |  |
| Qty | int | 4 | 1 |  |  |  |
| ReceiptDate | date | 3 | 1 |  |  |  |
| entity | nvarchar | 20 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: ERP.spMergeWhseReceipt_NonPO](../../StoredProcedures/IntegrationStaging/ERP.spMergeWhseReceipt_NonPO.md)

