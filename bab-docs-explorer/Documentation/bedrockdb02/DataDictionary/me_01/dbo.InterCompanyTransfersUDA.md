# dbo.InterCompanyTransfersUDA

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| UPC | nvarchar | 52 | 0 |  |  |  |
| short_desc | nvarchar | 40 | 1 |  |  |  |
| location_code | nvarchar | 40 | 0 |  |  |  |
| from_locn | nvarchar | 40 | 0 |  |  |  |
| units | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingOutputSelectInterCompanyTransfersUDA](../../StoredProcedures/me_01/dbo.spMerchandisingOutputSelectInterCompanyTransfersUDA.md)
- [me_01: dbo.spMerchandisingSelectInterCompanyTransfersUDA](../../StoredProcedures/me_01/dbo.spMerchandisingSelectInterCompanyTransfersUDA.md)

