# dbo.SetSessionCredentials

**Database:** ReportServerES  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.SetSessionCredentials"]
    dbo_DereferenceSessionSnapshot(["dbo.DereferenceSessionSnapshot"]) --> SP
    dbo_GetUserID(["dbo.GetUserID"]) --> SP
    dbo_SessionData(["dbo.SessionData"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.DereferenceSessionSnapshot |
| dbo.GetUserID |
| dbo.SessionData |

## Stored Procedure Code

```sql

```

