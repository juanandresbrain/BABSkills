# dbo.tmpEmlSQLJobHistory

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| server | varchar | 11 | 0 |  |  |  |
| JobName | nvarchar | 256 | 0 |  |  |  |
| RunDateTime | varchar | 30 | 1 |  |  |  |
| RunDurationMinutes | int | 4 | 1 |  |  |  |
| Run_Status | varchar | 10 | 1 |  |  |  |
| DataSet | varchar | 8 | 1 |  |  |  |

