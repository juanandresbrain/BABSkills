# dbo.tmpUKPOReceiptImport

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| receipt_date | smalldatetime | 4 | 1 |  |  |  |
| po_no | varchar | 7 | 1 |  |  |  |
| style_code | varchar | 12 | 1 |  |  |  |
| qty | int | 4 | 1 |  |  |  |
| dam | varchar | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingOutputUKPOReceipts](../../StoredProcedures/me_01/dbo.spMerchandisingOutputUKPOReceipts.md)
- [me_01: dbo.spMerchandisingSelectUKPOReceipts](../../StoredProcedures/me_01/dbo.spMerchandisingSelectUKPOReceipts.md)

