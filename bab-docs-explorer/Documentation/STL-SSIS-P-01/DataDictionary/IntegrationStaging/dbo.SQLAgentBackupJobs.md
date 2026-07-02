# dbo.SQLAgentBackupJobs

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ServerName | varchar | 100 | 1 |  |  |  |
| job_id | uniqueidentifier | 16 | 1 |  |  |  |
| JobName | nvarchar | 8000 | 1 |  |  |  |
| step_uid | uniqueidentifier | 16 | 1 |  |  |  |
| step_id | int | 4 | 1 |  |  |  |
| step_name | nvarchar | 8000 | 1 |  |  |  |
| subsystem | nvarchar | 80 | 1 |  |  |  |
| Command | nvarchar | -1 | 1 |  |  |  |

