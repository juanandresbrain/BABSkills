# dbo.tmpCNPOReceiptImport

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| location_code | varchar | 4 | 1 |  |  |  |
| receipt_date | date | 3 | 1 |  |  |  |
| po_no | varchar | 20 | 1 |  |  |  |
| style_code | varchar | 12 | 1 |  |  |  |
| qty | int | 4 | 1 |  |  |  |
| dam | varchar | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingOutputCNPOReceipts](../../StoredProcedures/me_01/dbo.spMerchandisingOutputCNPOReceipts.md)

