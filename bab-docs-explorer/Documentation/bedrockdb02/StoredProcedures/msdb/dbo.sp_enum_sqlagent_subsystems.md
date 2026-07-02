# dbo.sp_enum_sqlagent_subsystems

**Database:** msdb  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_enum_sqlagent_subsystems"]
    dbo_sp_enum_sqlagent_subsystems_internal(["dbo.sp_enum_sqlagent_subsystems_internal"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.sp_enum_sqlagent_subsystems_internal |

## Stored Procedure Code

```sql
CREATE PROCEDURE sp_enum_sqlagent_subsystems
AS
BEGIN
  DECLARE @retval         INT
  EXEC @retval = msdb.dbo.sp_enum_sqlagent_subsystems_internal
  RETURN(@retval)
END
```

