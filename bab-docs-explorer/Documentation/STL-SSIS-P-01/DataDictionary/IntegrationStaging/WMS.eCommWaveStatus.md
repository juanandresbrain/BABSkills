# WMS.eCommWaveStatus

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| WaveID | varchar | 25 | 0 | YES |  |  |
| isWaved | bit | 1 | 0 |  |  |  |
| MessageCount | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spUpdateReleaseDateAndTime](../../StoredProcedures/IntegrationStaging/WMS.spUpdateReleaseDateAndTime.md)

