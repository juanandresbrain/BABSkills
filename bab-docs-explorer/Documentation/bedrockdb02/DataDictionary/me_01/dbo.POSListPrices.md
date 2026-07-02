# dbo.POSListPrices

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Jurisdiction | varchar | 2 | 1 |  |  |  |
| style_code | nvarchar | 40 | 0 |  |  |  |
| ListPrice | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spPOSPricebookStage_BAK20231101](../../StoredProcedures/me_01/dbo.spPOSPricebookStage_BAK20231101.md)

