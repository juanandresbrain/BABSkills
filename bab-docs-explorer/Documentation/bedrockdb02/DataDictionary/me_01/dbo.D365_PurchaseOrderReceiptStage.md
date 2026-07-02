# dbo.D365_PurchaseOrderReceiptStage

**Database:** me_01  
**Server:** bedrockdb02  

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

- [me_01: dbo.spMerchandising_Report_wcReceipts](../../StoredProcedures/me_01/dbo.spMerchandising_Report_wcReceipts.md)
- [me_01: dbo.spMerchandisingImportCNPOReceipts](../../StoredProcedures/me_01/dbo.spMerchandisingImportCNPOReceipts.md)
- [me_01: dbo.spMerchandisingSelectUKPOReceipts](../../StoredProcedures/me_01/dbo.spMerchandisingSelectUKPOReceipts.md)

