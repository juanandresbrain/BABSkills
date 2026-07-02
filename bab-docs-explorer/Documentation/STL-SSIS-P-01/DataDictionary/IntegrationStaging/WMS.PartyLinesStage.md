# WMS.PartyLinesStage

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PartyId | nvarchar | 20 | 1 |  |  |  |
| ItemNumber | nvarchar | 20 | 1 |  |  |  |
| Quantity | int | 4 | 1 |  |  |  |
| LineNumber | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spMergePartyLines](../../StoredProcedures/IntegrationStaging/WMS.spMergePartyLines.md)

