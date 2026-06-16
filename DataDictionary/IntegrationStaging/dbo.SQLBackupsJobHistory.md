# dbo.SQLBackupsJobHistory

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ServerName | nvarchar | 200 | 1 |  |  |  |
| JobName | nvarchar | 256 | 1 |  |  |  |
| job_id | uniqueidentifier | 16 | 1 |  |  |  |
| BackupLocation | nvarchar | 100 | 1 |  |  |  |
| NextRunDate | datetime | 8 | 1 |  |  |  |
| LastRunDate | datetime | 8 | 1 |  |  |  |
| LastRunStatus | varchar | 20 | 1 |  |  |  |
| LastRunDuration | varchar | 8 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: dbo.spMergeSQLBackupsJobHistory](../../StoredProcedures/IntegrationStaging/dbo.spMergeSQLBackupsJobHistory.md)

