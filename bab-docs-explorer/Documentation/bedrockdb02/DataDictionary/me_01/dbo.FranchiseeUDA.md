# dbo.FranchiseeUDA

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

- [me_01: dbo.spMerchandisingOutputFranchiseeUDA](../../StoredProcedures/me_01/dbo.spMerchandisingOutputFranchiseeUDA.md)
- [me_01: dbo.spMerchandisingSelectFranchiseeUDA](../../StoredProcedures/me_01/dbo.spMerchandisingSelectFranchiseeUDA.md)

