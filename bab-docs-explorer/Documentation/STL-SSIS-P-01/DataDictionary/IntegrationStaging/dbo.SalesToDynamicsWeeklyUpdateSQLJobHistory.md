# dbo.SalesToDynamicsWeeklyUpdateSQLJobHistory

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| server | varchar | 52 | 1 |  |  |  |
| JobName | varchar | 152 | 1 |  |  |  |
| RunDateTime | varchar | 52 | 1 |  |  |  |
| RunDurationMinutes | int | 4 | 1 |  |  |  |
| Run_Status | varchar | 10 | 1 |  |  |  |
| DataSet | varchar | 52 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: dbo.spSalesToDynamicsWeeklyUpdateJobHistoryEmail](../../StoredProcedures/IntegrationStaging/dbo.spSalesToDynamicsWeeklyUpdateJobHistoryEmail.md)

