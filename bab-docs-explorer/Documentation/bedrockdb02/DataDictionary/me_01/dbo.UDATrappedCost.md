# dbo.UDATrappedCost

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| UPC | nvarchar | 52 | 0 |  |  |  |
| location_code | nvarchar | 40 | 0 |  |  |  |
| units | varchar | 1 | 0 |  |  |  |
| Cost | decimal | 17 | 1 |  |  |  |
| LocalCost | decimal | 17 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingSelectTrappedCostUDA](../../StoredProcedures/me_01/dbo.spMerchandisingSelectTrappedCostUDA.md)

