# dbo.sysmail_help_status_sp

**Database:** msdb  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sysmail_help_status_sp"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table references detected._

## Stored Procedure Code

```sql
CREATE PROCEDURE sysmail_help_status_sp
  WITH EXECUTE AS 'dbo'
AS
BEGIN
    IF NOT EXISTS (SELECT * FROM sys.service_queues WHERE name = N'ExternalMailQueue' AND is_receive_enabled = 1)
       SELECT 'STOPPED' AS Status
    ELSE
       SELECT 'STARTED' AS Status
END
```

