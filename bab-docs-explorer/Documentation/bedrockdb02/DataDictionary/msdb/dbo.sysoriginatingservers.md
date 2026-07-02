# dbo.sysoriginatingservers

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| originating_server_id | int | 4 | 1 |  |  |  |
| originating_server | sysname | 256 | 0 |  |  |  |
| master_server | bit | 1 | 1 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_msx_defect](../../StoredProcedures/msdb/dbo.sp_msx_defect.md)
- [msdb: dbo.sp_msx_enlist](../../StoredProcedures/msdb/dbo.sp_msx_enlist.md)

