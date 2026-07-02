# dbo.DatabaseIntegrityCheck

**Database:** master  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DatabaseIntegrityCheck"]
    dbo_CommandExecute(["dbo.CommandExecute"]) --> SP
    dbo_CommandLog(["dbo.CommandLog"]) --> SP
    dbo_Queue(["dbo.Queue"]) --> SP
    dbo_QueueDatabase(["dbo.QueueDatabase"]) --> SP
    sys_dm_os_host_info(["sys.dm_os_host_info"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.CommandExecute |
| dbo.CommandLog |
| dbo.Queue |
| dbo.QueueDatabase |
| sys.dm_os_host_info |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[DatabaseIntegrityCheck]
```

