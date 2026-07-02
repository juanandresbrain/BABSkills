# dbo.syscachedcredentials

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| login_name | sysname | 256 | 0 | YES |  |  |
| has_server_access | bit | 1 | 0 |  |  |  |
| is_sysadmin_member | bit | 1 | 0 |  |  |  |
| cachedate | datetime | 8 | 0 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_sqlagent_has_server_access](../../StoredProcedures/msdb/dbo.sp_sqlagent_has_server_access.md)

