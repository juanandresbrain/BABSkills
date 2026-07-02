# dbo.GetUserID

**Database:** ReportServerES  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.GetUserID"]
    dbo_GetUserIDByName(["dbo.GetUserIDByName"]) --> SP
    dbo_GetUserIDBySid(["dbo.GetUserIDBySid"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.GetUserIDByName |
| dbo.GetUserIDBySid |

## Stored Procedure Code

```sql

```

