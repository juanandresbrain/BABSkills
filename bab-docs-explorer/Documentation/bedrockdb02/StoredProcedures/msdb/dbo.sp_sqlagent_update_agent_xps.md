# dbo.sp_sqlagent_update_agent_xps

**Database:** msdb  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_sqlagent_update_agent_xps"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table references detected._

## Stored Procedure Code

```sql
CREATE PROCEDURE sp_sqlagent_update_agent_xps
  @new_value        bit = 1  -- the new value for the "Agent XPs" configuration option.
AS
BEGIN
  declare @agent_enabled bit 
  declare @show_advanced bit 
  
  select @show_advanced = cast(value_in_use as bit) 
    from sys.configurations 
    where name = N'show advanced options' 
  
  select @agent_enabled = cast(value_in_use as bit) 
    from sys.configurations 
    where name = N'Agent XPs' 
    
  if @new_value <> @agent_enabled 
  begin 
    if 1 <> @show_advanced 
    begin 
      exec sys.sp_configure @configname = N'show advanced options', @configvalue = 1 
      reconfigure with override 
    end 
    
    exec sys.sp_configure @configname = N'Agent XPs', @configvalue = @new_value 
    reconfigure with override 
    if 1 <> @show_advanced 
    begin 
      exec sys.sp_configure @configname = N'show advanced options', @configvalue = 0 
      reconfigure with override 
    end 
  end
END
```

