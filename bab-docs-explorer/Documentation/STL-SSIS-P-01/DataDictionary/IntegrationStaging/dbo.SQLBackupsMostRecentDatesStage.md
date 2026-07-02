# dbo.SQLBackupsMostRecentDatesStage

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ServerName | nvarchar | 256 | 1 |  |  |  |
| DatabaseName | nvarchar | 256 | 1 |  |  |  |
| DatabaseType | varchar | 6 | 1 |  |  |  |
| FullBackupDate | datetime | 8 | 1 |  |  |  |
| DifferentialBackupDate | datetime | 8 | 1 |  |  |  |
| SQLServerServiceAccount | nvarchar | 104 | 1 |  |  |  |
| SQLAgentServerAccount | nvarchar | 104 | 1 |  |  |  |

