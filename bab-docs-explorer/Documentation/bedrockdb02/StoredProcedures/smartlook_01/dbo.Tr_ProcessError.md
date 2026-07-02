# dbo.Tr_ProcessError

**Database:** smartlook_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.Tr_ProcessError"]
    dbo_Sr_Job(["dbo.Sr_Job"]) --> SP
    dbo_Tr_Directory(["dbo.Tr_Directory"]) --> SP
    dbo_Tr_PollFile(["dbo.Tr_PollFile"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Sr_Job |
| dbo.Tr_Directory |
| dbo.Tr_PollFile |

## Stored Procedure Code

```sql

```

