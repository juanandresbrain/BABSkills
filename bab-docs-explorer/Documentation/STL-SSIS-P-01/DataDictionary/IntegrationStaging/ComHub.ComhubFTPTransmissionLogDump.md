# ComHub.ComhubFTPTransmissionLogDump

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ftpLog | varchar | 4000 | 1 |  |  |  |
| LogDateTime | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: ComHub.spFTPCommercehubCostcoWebConfirmations](../../StoredProcedures/IntegrationStaging/ComHub.spFTPCommercehubCostcoWebConfirmations.md)
- [IntegrationStaging: ComHub.spFTPCommercehubCostcoWebFAs](../../StoredProcedures/IntegrationStaging/ComHub.spFTPCommercehubCostcoWebFAs.md)
- [IntegrationStaging: ComHub.spFTPGetCommercehubCostcoPOs](../../StoredProcedures/IntegrationStaging/ComHub.spFTPGetCommercehubCostcoPOs.md)

