# dbo.tblReceiptFilePostSummary

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PROCESS_START | varchar | 30 | 1 |  |  |  |
| WHSE | varchar | 20 | 0 |  |  |  |
| PO | varchar | 20 | 0 |  |  |  |
| STYLE | varchar | 20 | 0 |  |  |  |
| QTY | int | 4 | 0 |  |  |  |
| POSTED | varchar | 3 | 0 |  |  |  |
| POSTED_DATE | varchar | 30 | 0 |  |  |  |
| ERROR | varchar | 3 | 0 |  |  |  |
| ERROR_MSG | varchar | 1000 | 0 |  |  |  |
| imp_file_name | varchar | 200 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingSelectPOReceiptSummary](../../StoredProcedures/me_01/dbo.spMerchandisingSelectPOReceiptSummary.md)

