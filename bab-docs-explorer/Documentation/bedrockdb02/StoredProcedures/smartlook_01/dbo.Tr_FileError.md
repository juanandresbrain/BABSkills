# dbo.Tr_FileError

**Database:** smartlook_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.Tr_FileError"]
    dbo_Tr_Directory(["dbo.Tr_Directory"]) --> SP
    dbo_Tr_Parameter(["dbo.Tr_Parameter"]) --> SP
    dbo_Tr_PollFile(["dbo.Tr_PollFile"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Tr_Directory |
| dbo.Tr_Parameter |
| dbo.Tr_PollFile |

## Stored Procedure Code

```sql

```

