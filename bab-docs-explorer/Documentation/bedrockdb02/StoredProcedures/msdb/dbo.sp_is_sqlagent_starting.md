# dbo.sp_is_sqlagent_starting

**Database:** msdb  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_is_sqlagent_starting"]
    dbo_xp_sqlagent_is_starting(["dbo.xp_sqlagent_is_starting"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.xp_sqlagent_is_starting |

## Stored Procedure Code

```sql
CREATE PROCEDURE sp_is_sqlagent_starting
AS
BEGIN
  DECLARE @retval INT

  SELECT @retval = 0
  EXECUTE master.dbo.xp_sqlagent_is_starting @retval OUTPUT
  IF (@retval = 1)
    RAISERROR(14258, -1, -1)

  RETURN(@retval)
END
```

