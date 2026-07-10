# dbo.spRPT_SOXReport_ServerRolesAndLogins

**Database:** DBAUtilityMaster  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spRPT_SOXReport_ServerRolesAndLogins"]
    dbo_tblDBA_SOXReport_ServerRolesAndLogins(["dbo.tblDBA_SOXReport_ServerRolesAndLogins"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tblDBA_SOXReport_ServerRolesAndLogins |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[spRPT_SOXReport_ServerRolesAndLogins]
@strYear CHAR(4), @strQuarter CHAR(2), @strServerName VARCHAR(50)
AS

SET NOCOUNT ON

SELECT name, dbname, 
sysadmin, securityadmin, serveradmin, setupadmin, processadmin, diskadmin, dbcreator, bulkadmin, RunDate, InstanceName
FROM PAPAMART.DBAUtilityMaster.dbo.tblDBA_SOXReport_ServerRolesAndLogins 
WHERE RunYear = @strYear AND RunQuarter = @strQuarter AND InstanceName = @strServerName 
AND CONVERT(DATE, RunDate) = (
	SELECT CONVERT(DATE, MAX(RunDate)) RunDate 
	FROM COREDB01_MAINT.DBAUtilityMaster.dbo.tblDBA_SOXReport_ServerRolesAndLogins 
	WHERE RunYear = @strYear AND RunQuarter = @strQuarter AND InstanceName = @strServerName 
 )
 ORDER BY name
```

