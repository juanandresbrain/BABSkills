# dbo.tmpStoreForceExtractRunHistory

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| JobName | varchar | 100 | 1 |  |  |  |
| StartDateTime | datetime | 8 | 1 |  |  |  |
| EndDateTime | datetime | 8 | 1 |  |  |  |
| DurationMinutes | int | 4 | 1 |  |  |  |
| RunStatus | varchar | 20 | 1 |  |  |  |

