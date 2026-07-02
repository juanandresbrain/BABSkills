# dbo.sp_sysutility_mi_validate_enrollment_preconditions

**Database:** msdb  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_sysutility_mi_validate_enrollment_preconditions"]
    dbo_xp_qv(["dbo.xp_qv"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.xp_qv |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[sp_sysutility_mi_validate_enrollment_preconditions]
WITH EXECUTE AS OWNER
AS
BEGIN
    /* Get the Edition value */
    DECLARE @edition NVARCHAR(64)
    SELECT @edition = Convert(NVARCHAR, SERVERPROPERTY('edition'))

    /* Check SQLBOOT to ensure this instance edition can be used as a UCP. */
    DECLARE @sqlbootvalue int

    EXEC @sqlbootvalue = master.dbo.xp_qv '3090395820', @@SERVICENAME
    IF (@sqlbootvalue = 2)
        RAISERROR ('Instance can be managed by a Utility Control Point.', 0, 1) WITH NOWAIT;
    ELSE
        RAISERROR(37005, -1, -1, @edition)
        RETURN(1)
END
```

