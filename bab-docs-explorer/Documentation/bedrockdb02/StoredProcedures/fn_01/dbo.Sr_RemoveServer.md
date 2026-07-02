# dbo.Sr_RemoveServer

**Database:** fn_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.Sr_RemoveServer"]
    dbo_Sr_Job(["dbo.Sr_Job"]) --> SP
    dbo_Sr_Server(["dbo.Sr_Server"]) --> SP
    dbo_Sr_Server_LANG(["dbo.Sr_Server_LANG"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Sr_Job |
| dbo.Sr_Server |
| dbo.Sr_Server_LANG |

## Stored Procedure Code

```sql

```

