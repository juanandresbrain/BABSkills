# dbo.sp_sysutility_ucp_create

**Database:** msdb  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_sysutility_ucp_create"]
    dbo_sp_sysutility_ucp_validate_prerequisites(["dbo.sp_sysutility_ucp_validate_prerequisites"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.sp_sysutility_ucp_validate_prerequisites |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[sp_sysutility_ucp_create]
WITH EXECUTE AS OWNER
AS
BEGIN
    /* Validate that the UCP can be created on the local instance. */
    EXEC [dbo].[sp_sysutility_ucp_validate_prerequisites]
END
```

