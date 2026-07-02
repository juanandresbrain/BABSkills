# dbo.sp_get_script

**Database:** msdb  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_get_script"]
    dbo_xp_get_script(["dbo.xp_get_script"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.xp_get_script |

## Stored Procedure Code

```sql
CREATE PROCEDURE sp_get_script
    @name sysname
AS
BEGIN
    exec master.dbo.xp_get_script @name
END
```

