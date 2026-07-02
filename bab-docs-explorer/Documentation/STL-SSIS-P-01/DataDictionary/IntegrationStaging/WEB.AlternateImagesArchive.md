# WEB.AlternateImagesArchive

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ImageName | varchar | 100 | 1 |  |  |  |
| BABWProductID | varchar | 6 | 1 |  |  |  |
| ArchiveDate | datetime | 8 | 1 |  |  |  |
| ChangeType | varchar | 10 | 1 |  |  |  |
| CurrentBatch | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WEB.spMergeAlternateImages](../../StoredProcedures/IntegrationStaging/WEB.spMergeAlternateImages.md)

