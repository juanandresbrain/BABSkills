# dbo.sp_sysutility_mi_enroll

**Database:** msdb  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_sysutility_mi_enroll"]
    dbo_sp_sysutility_mi_validate_enrollment_preconditions(["dbo.sp_sysutility_mi_validate_enrollment_preconditions"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.sp_sysutility_mi_validate_enrollment_preconditions |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[sp_sysutility_mi_enroll]
WITH EXECUTE AS OWNER
AS
BEGIN
    /* Validate that the local instance can be managed by a UCP. */
    EXEC [dbo].[sp_sysutility_mi_validate_enrollment_preconditions]
END
```

