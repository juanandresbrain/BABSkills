# WMS.DuplicateWebOrderDetectionStage

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| WebOrderNumber | nvarchar | 40 | 1 |  |  |  |
| SalesOrderNumber | nvarchar | 40 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spMergeDuplicateWebOrderDetection](../../StoredProcedures/IntegrationStaging/WMS.spMergeDuplicateWebOrderDetection.md)

