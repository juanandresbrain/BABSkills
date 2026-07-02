# dbo.sysnotifications

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| alert_id | int | 4 | 0 |  |  |  |
| operator_id | int | 4 | 0 |  |  |  |
| notification_method | tinyint | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_add_notification](../../StoredProcedures/msdb/dbo.sp_add_notification.md)
- [msdb: dbo.sp_delete_alert](../../StoredProcedures/msdb/dbo.sp_delete_alert.md)
- [msdb: dbo.sp_delete_notification](../../StoredProcedures/msdb/dbo.sp_delete_notification.md)
- [msdb: dbo.sp_delete_operator](../../StoredProcedures/msdb/dbo.sp_delete_operator.md)
- [msdb: dbo.sp_update_notification](../../StoredProcedures/msdb/dbo.sp_update_notification.md)
- [DBAUtility: dbo.CreateBackUpFromJob_DELETE20141203](../../StoredProcedures/DBAUtility/dbo.CreateBackUpFromJob_DELETE20141203.md)

