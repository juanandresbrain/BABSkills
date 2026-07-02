# WEB.PricebookFactArchive

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_code | varchar | 6 | 1 |  |  |  |
| CurrentPrice | decimal | 9 | 1 |  |  |  |
| OriginalPrice | decimal | 9 | 1 |  |  |  |
| SalePrice | decimal | 9 | 1 |  |  |  |
| Catalog | varchar | 2 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |
| CheckDate | datetime | 8 | 1 |  |  |  |
| ArchiveDate | datetime | 8 | 1 |  |  |  |
| ChangeType | varchar | 10 | 1 |  |  |  |
| CurrentBatch | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WEB.spMergePricebookFact](../../StoredProcedures/IntegrationStaging/WEB.spMergePricebookFact.md)
- [IntegrationStaging: WEB.spMergePricebookFact_BAK20220705](../../StoredProcedures/IntegrationStaging/WEB.spMergePricebookFact_BAK20220705.md)

