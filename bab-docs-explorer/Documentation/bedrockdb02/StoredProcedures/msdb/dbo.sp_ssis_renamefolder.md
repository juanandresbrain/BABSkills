# dbo.sp_ssis_renamefolder

**Database:** msdb  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_ssis_renamefolder"]
    dbo_sysssispackagefolders(["dbo.sysssispackagefolders"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.sysssispackagefolders |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[sp_ssis_renamefolder]
  @folderid uniqueidentifier,
  @name sysname
AS
   --Check security
   IF (IS_MEMBER('db_ssisltduser')<>1) AND (IS_MEMBER('db_ssisadmin')<>1) AND (IS_SRVROLEMEMBER('sysadmin')<>1)
   BEGIN
       RAISERROR (14591, -1, -1, @name)
       RETURN 1  -- Failure
   END

   --// Security check passed, INSERT now
   UPDATE sysssispackagefolders
   SET [foldername] = @name
   WHERE [folderid] = @folderid
```

