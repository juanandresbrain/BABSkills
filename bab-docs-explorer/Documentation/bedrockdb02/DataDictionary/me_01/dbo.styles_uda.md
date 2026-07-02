# dbo.styles_uda

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| id | int | 4 | 0 |  |  |  |
| datestamp | varchar | 20 | 1 |  |  |  |
| style | varchar | 6 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandising_Report_NewStyleUDA](../../StoredProcedures/me_01/dbo.spMerchandising_Report_NewStyleUDA.md)
- [me_01: dbo.spMerchandising_Select_NewStyleUDAMinus](../../StoredProcedures/me_01/dbo.spMerchandising_Select_NewStyleUDAMinus.md)
- [me_01: dbo.spMerchandising_Select_NewStyleUDAPlus](../../StoredProcedures/me_01/dbo.spMerchandising_Select_NewStyleUDAPlus.md)

