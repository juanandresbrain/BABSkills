# dbo.tblDBA_ObjectVersionLog

**Database:** DBAUtility_new  
**Server:** papamart  

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
