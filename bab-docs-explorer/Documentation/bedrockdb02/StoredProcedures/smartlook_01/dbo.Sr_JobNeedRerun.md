# dbo.Sr_JobNeedRerun

**Database:** smartlook_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.Sr_JobNeedRerun"]
    dbo_Sr_Job(["dbo.Sr_Job"]) --> SP
    dbo_Sr_JobCheckpointInfo(["dbo.Sr_JobCheckpointInfo"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Sr_Job |
| dbo.Sr_JobCheckpointInfo |

## Stored Procedure Code

```sql

```

