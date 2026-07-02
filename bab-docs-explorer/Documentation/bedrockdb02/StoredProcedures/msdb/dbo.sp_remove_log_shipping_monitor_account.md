# dbo.sp_remove_log_shipping_monitor_account

**Database:** msdb  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_remove_log_shipping_monitor_account"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table references detected._

## Stored Procedure Code

```sql
CREATE PROCEDURE sp_remove_log_shipping_monitor_account
AS
BEGIN
  SET NOCOUNT ON
  EXECUTE sp_dropuser N'log_shipping_monitor_probe'
  EXECUTE sp_droplogin N'log_shipping_monitor_probe'
END
```

