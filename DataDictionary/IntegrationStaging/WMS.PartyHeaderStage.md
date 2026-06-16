# WMS.PartyHeaderStage

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PartyId | nvarchar | 20 | 1 |  |  |  |
| StoreNumber | nvarchar | 10 | 1 |  |  |  |
| SubmittedBy | nvarchar | 100 | 1 |  |  |  |
| PartyDate | datetime | 8 | 1 |  |  |  |
| SourceFile | nvarchar | 100 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spMergePartyHeader](../../StoredProcedures/IntegrationStaging/WMS.spMergePartyHeader.md)

