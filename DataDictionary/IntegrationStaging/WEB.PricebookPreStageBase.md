# WEB.PricebookPreStageBase

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| BaseID | varchar | 5 | 1 |  |  |  |
| stylecode | varchar | 6 | 1 |  |  |  |
| CurrentPrice | decimal | 9 | 1 |  |  |  |
| OriginalPrice | decimal | 9 | 1 |  |  |  |
| Jurisdiction | varchar | 5 | 1 |  |  |  |
| AVAILB | varchar | 5 | 1 |  |  |  |
| StartDate | smalldatetime | 4 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WEB.spMergePricebookPreStage](../../StoredProcedures/IntegrationStaging/WEB.spMergePricebookPreStage.md)

