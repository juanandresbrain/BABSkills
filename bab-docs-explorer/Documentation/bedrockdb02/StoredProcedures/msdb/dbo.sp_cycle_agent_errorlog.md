# dbo.sp_cycle_agent_errorlog

**Database:** msdb  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_cycle_agent_errorlog"]
    dbo_sp_sqlagent_notify(["dbo.sp_sqlagent_notify"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.sp_sqlagent_notify |

## Stored Procedure Code

```sql
CREATE PROCEDURE sp_cycle_agent_errorlog
AS
BEGIN
   exec sp_sqlagent_notify N'L'
END
```

