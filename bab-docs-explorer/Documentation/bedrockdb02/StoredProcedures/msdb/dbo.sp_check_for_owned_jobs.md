# dbo.sp_check_for_owned_jobs

**Database:** msdb  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_check_for_owned_jobs"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table references detected._

## Stored Procedure Code

```sql
CREATE PROCEDURE sp_check_for_owned_jobs
  @login_name sysname,
  @table_name sysname
AS
BEGIN
  SET NOCOUNT ON

  -- This procedure is called by sp_droplogin to check if the login being dropped
  -- still owns jobs.  The return value (the number of jobs owned) is passed back
  -- via the supplied table name [this cumbersome approach is necessary because
  -- sp_check_for_owned_jobs is invoked via an EXEC() and because we always want
  -- sp_droplogin to work, even if msdb and/or sysjobs does not exist].

  IF (EXISTS (SELECT *
              FROM msdb.dbo.sysobjects
              WHERE (name = N'sysjobs')
                AND (type = 'U')))
  BEGIN
    DECLARE @sql NVARCHAR(1024)
    SET @sql = N'INSERT INTO ' + QUOTENAME(@table_name, N'[') + N' SELECT COUNT(*) FROM msdb.dbo.sysjobs WHERE (owner_sid = SUSER_SID(N' + QUOTENAME(@login_name, '''') + ', 0))' --force case insensitive comparation for NT users
    EXEC sp_executesql @statement = @sql  
  END
END
```

