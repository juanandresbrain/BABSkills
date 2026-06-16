# HR.UltiProEmployeeActivationStage

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| EmployeeIdentifier | varchar | 7 | 1 |  |  |  |
| ClientUserName | varchar | 100 | 1 |  |  |  |
| Activated | int | 4 | 1 |  |  |  |
| UltiProResponse | nvarchar | 8000 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| ActivatedDate | datetime | 8 | 1 |  |  |  |
| Success | int | 4 | 1 |  |  |  |

