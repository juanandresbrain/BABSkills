# dbo.sysmail_alter_user_credential_sp

**Database:** msdb  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sysmail_alter_user_credential_sp"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table references detected._

## Stored Procedure Code

```sql
CREATE PROCEDURE dbo.sysmail_alter_user_credential_sp
   @credential_name sysname,
   @username      nvarchar(128),
   @password      nvarchar(128)
AS
   SET NOCOUNT ON
   DECLARE @rc int
   DECLARE @sql NVARCHAR(max)

   -- alter credential DDL
   SET @sql = N'ALTER CREDENTIAL ' + QUOTENAME(@credential_name)
         + N' WITH IDENTITY = ' + QUOTENAME(@username, '''')
         + N', SECRET = ' + QUOTENAME(ISNULL(@password, N''), '''')

   EXEC @rc = sp_executesql @statement = @sql
   IF(@rc <> 0)
      RETURN @rc

   RETURN(0)
```

