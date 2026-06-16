# ComHub.ComhubFTPLog

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ComhubFileName | varchar | 1000 | 1 |  |  |  |
| UploadDateTime | datetime | 8 | 1 |  |  |  |
| Success | int | 4 | 1 |  |  |  |
| xmlTypeId | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: ComHub.spFTPCommercehubCostcoWebConfirmations](../../StoredProcedures/IntegrationStaging/ComHub.spFTPCommercehubCostcoWebConfirmations.md)
- [IntegrationStaging: ComHub.spFTPCommercehubCostcoWebFAs](../../StoredProcedures/IntegrationStaging/ComHub.spFTPCommercehubCostcoWebFAs.md)

