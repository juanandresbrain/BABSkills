# dbo.spRPT_ObjectVersion

**Database:** DBAUtilityMaster  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spRPT_ObjectVersion"]
    dbo_tblDBA_ObjectVersionRepository(["dbo.tblDBA_ObjectVersionRepository"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tblDBA_ObjectVersionRepository |

## Stored Procedure Code

```sql
CREATE PROC [dbo].[spRPT_ObjectVersion]
AS
SELECT InstanceName, ObjectName, ObjectType, InstallDate, VersionDate, usesRevision 
FROM DBAUtilityMaster.dbo.tblDBA_ObjectVersionRepository
```

