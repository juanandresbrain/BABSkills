# dbo.sp_ssis_addfolder

**Database:** msdb  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_ssis_addfolder"]
    dbo_sysssispackagefolders(["dbo.sysssispackagefolders"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.sysssispackagefolders |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[sp_ssis_addfolder]
  @parentfolderid uniqueidentifier,
  @name sysname,
  @folderid uniqueidentifier = NULL
AS
   --Check security
   IF (IS_MEMBER('db_ssisltduser')<>1) AND (IS_MEMBER('db_ssisadmin')<>1) AND (IS_SRVROLEMEMBER('sysadmin')<>1)
   BEGIN
       RAISERROR (14591, -1, -1, @name)
       RETURN 1  -- Failure
   END

   --// Security check passed, INSERT now
   INSERT INTO sysssispackagefolders (folderid, parentfolderid, foldername)
   VALUES (ISNULL(@folderid, NEWID()), @parentfolderid, @name)
```

