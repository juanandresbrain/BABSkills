# dbo.WMDistroExportStage

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | bigint | 8 | 1 |  |  |  |
| SourceID | varchar | 20 | 1 |  |  |  |
| destid | varchar | 21 | 1 |  |  |  |
| style_code | varchar | 20 | 1 |  |  |  |
| quantity | int | 4 | 1 |  |  |  |
| rec_type | varchar | 6 | 1 |  |  |  |
| sequencenbr | bigint | 8 | 1 |  |  |  |
| cartonlabeltype | varchar | 3 | 0 |  |  |  |
| distribution_number | varchar | 50 | 1 |  |  |  |
| reasoncode | nvarchar | 510 | 1 |  |  |  |
| priority | int | 4 | 1 |  |  |  |
| TpeFreightTerms | varchar | 1 | 0 |  |  |  |
| CartonBreakAttribute | varchar | 2 | 1 |  |  |  |
| ref_field_1 | int | 4 | 1 |  |  |  |
| average_cost | numeric | 17 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingExportStoreDistributionsWM](../../StoredProcedures/me_01/dbo.spMerchandisingExportStoreDistributionsWM.md)

