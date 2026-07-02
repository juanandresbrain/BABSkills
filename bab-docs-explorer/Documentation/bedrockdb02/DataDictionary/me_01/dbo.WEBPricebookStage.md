# dbo.WEBPricebookStage

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_code | varchar | 6 | 1 |  |  |  |
| CurrentPrice | decimal | 9 | 1 |  |  |  |
| OriginalPrice | decimal | 9 | 1 |  |  |  |
| SalePrice | decimal | 9 | 1 |  |  |  |
| Catalog | varchar | 2 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spWEBPricebookStage](../../StoredProcedures/me_01/dbo.spWEBPricebookStage.md)
- [me_01: dbo.spWEBPricebookStage_Bak20220705](../../StoredProcedures/me_01/dbo.spWEBPricebookStage_Bak20220705.md)
- [me_01: dbo.spWEBPricebookStage_TCOnDemand](../../StoredProcedures/me_01/dbo.spWEBPricebookStage_TCOnDemand.md)

