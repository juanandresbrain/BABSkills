# WMS.DynamicsPackageAPILog

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| IntegrationName | nvarchar | 200 | 1 |  |  |  |
| Entity | nvarchar | 8 | 1 |  |  |  |
| BlobDate | datetime | 8 | 1 |  |  |  |
| BlobID | nvarchar | 200 | 1 |  |  |  |
| BlobURL | nvarchar | 8000 | 1 |  |  |  |
| TriggerDate | datetime | 8 | 1 |  |  |  |
| TriggerResponse | nvarchar | -1 | 1 |  |  |  |
| StatusDate | datetime | 8 | 1 |  |  |  |
| StatusResponse | nvarchar | 8000 | 1 |  |  |  |
| BatchID | nvarchar | 200 | 1 |  |  |  |
| RowsCount | int | 4 | 1 |  |  |  |
| Duration | varchar | 10 | 1 |  |  |  |
| AptosShipmentNumber | varchar | 20 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spEmailAptosDistributionExportValidation](../../StoredProcedures/IntegrationStaging/WMS.spEmailAptosDistributionExportValidation.md)

