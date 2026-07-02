# dbo.sp_sysutility_ucp_validate_prerequisites

**Database:** msdb  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_sysutility_ucp_validate_prerequisites"]
    dbo_fn_sysutility_ucp_get_edition_is_ucp_capable_internal(["dbo.fn_sysutility_ucp_get_edition_is_ucp_capable_internal"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.fn_sysutility_ucp_get_edition_is_ucp_capable_internal |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[sp_sysutility_ucp_validate_prerequisites]
WITH EXECUTE AS OWNER
AS
BEGIN
   IF (dbo.fn_sysutility_ucp_get_edition_is_ucp_capable_internal() = 1)
   BEGIN
      RAISERROR ('Instance is able to be used as a Utility Control Point.', 0, 1) WITH NOWAIT;
   END
   ELSE BEGIN
      DECLARE @edition nvarchar(128);
      SELECT @edition = CONVERT(nvarchar(128), SERVERPROPERTY('Edition'));
      RAISERROR(37004, -1, -1, @edition);
      RETURN(1);
   END;
END
```

