# dbo.tmpDBSpoSummary

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| purchaseorder | varchar | 20 | 0 |  |  |  |
| style | varchar | 20 | 0 |  |  |  |
| description | varchar | 120 | 1 |  |  |  |
| qty | decimal | 17 | 1 |  |  |  |
| NewShipLine (not exported) | int | 4 | 0 |  |  |  |
| OriginalLine (exported) | int | 4 | 0 |  |  |  |
| shipDate | varchar | 30 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingDBSchenkerPOExport_8_EmailSummaryAndException](../../StoredProcedures/me_01/dbo.spMerchandisingDBSchenkerPOExport_8_EmailSummaryAndException.md)

