# dbo.UPC_Complete

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| UPC_Pre | varchar | 12 | 1 |  |  |  |
| UPC_Complete | varchar | 14 | 1 |  |  |  |
| Style_Code | varchar | 6 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingOutputStylesMissingUPC](../../StoredProcedures/me_01/dbo.spMerchandisingOutputStylesMissingUPC.md)

