# WEB.AltImageTags

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| BABWProductID | nvarchar | 4000 | 1 |  |  |  |
| ImagePath | nvarchar | 8000 | 1 |  |  |  |
| AltText | nvarchar | 8000 | 1 |  |  |  |
| TitleText | nvarchar | 8000 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WEB.spMergeAltImageTags](../../StoredProcedures/IntegrationStaging/WEB.spMergeAltImageTags.md)

