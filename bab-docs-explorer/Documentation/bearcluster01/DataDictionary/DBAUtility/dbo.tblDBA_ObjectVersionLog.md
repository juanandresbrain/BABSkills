# dbo.tblDBA_ObjectVersionLog

**Database:** DBAUtility  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ProcVersionID | int | 4 | 0 | YES |  |  |
| InstanceName | varchar | 200 | 0 |  |  |  |
| ObjectName | varchar | 200 | 0 |  |  |  |
| ObjectType | varchar | 50 | 1 |  |  |  |
| InstallDate | datetime | 8 | 0 |  |  |  |
| VersionDate | datetime | 8 | 1 |  |  |  |
| usesRevision | bit | 1 | 1 |  |  |  |

## Referenced By Stored Procedures

- [DBAUtility: dbo.spDBA_ObjectVersionLog](../../StoredProcedures/DBAUtility/dbo.spDBA_ObjectVersionLog.md)
- [DBAUtility: dbo.spDBA_Transfer_ObjectVersionRepository](../../StoredProcedures/DBAUtility/dbo.spDBA_Transfer_ObjectVersionRepository.md)

