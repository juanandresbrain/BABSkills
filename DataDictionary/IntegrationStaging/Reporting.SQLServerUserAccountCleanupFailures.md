# Reporting.SQLServerUserAccountCleanupFailures

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ServerName | nvarchar | 256 | 1 |  |  |  |
| CommandExecuted | nvarchar | 8000 | 1 |  |  |  |
| ErrorMessage | nvarchar | 8000 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: Reporting.spEmailErrosWhenDroppingInvalidSQLServerLogins](../../StoredProcedures/IntegrationStaging/Reporting.spEmailErrosWhenDroppingInvalidSQLServerLogins.md)

