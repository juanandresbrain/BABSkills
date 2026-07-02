# dbo.ClearSessionSnapshot

**Database:** ReportServerES  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.ClearSessionSnapshot"]
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

