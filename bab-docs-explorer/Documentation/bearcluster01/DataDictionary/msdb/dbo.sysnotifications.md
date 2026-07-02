# dbo.sysnotifications

**Database:** msdb  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| alert_id | int | 4 | 0 |  |  |  |
| operator_id | int | 4 | 0 |  |  |  |
| notification_method | tinyint | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [DBAUtility: dbo.CreateBackUpFromJob_DELETE20141203](../../StoredProcedures/DBAUtility/dbo.CreateBackUpFromJob_DELETE20141203.md)

