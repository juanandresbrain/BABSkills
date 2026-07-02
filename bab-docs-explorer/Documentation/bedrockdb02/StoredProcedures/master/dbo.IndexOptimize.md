# dbo.IndexOptimize

**Database:** master  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.IndexOptimize"]
    dbo_CommandExecute(["dbo.CommandExecute"]) --> SP
    dbo_Queue(["dbo.Queue"]) --> SP
    dbo_QueueDatabase(["dbo.QueueDatabase"]) --> SP
    sys_dm_os_host_info(["sys.dm_os_host_info"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.CommandExecute |
| dbo.Queue |
| dbo.QueueDatabase |
| sys.dm_os_host_info |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[IndexOptimize]
```

