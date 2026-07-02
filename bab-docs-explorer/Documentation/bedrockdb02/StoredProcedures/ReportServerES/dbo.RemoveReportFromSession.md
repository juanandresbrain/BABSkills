# dbo.RemoveReportFromSession

**Database:** ReportServerES  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.RemoveReportFromSession"]
    dbo_DereferenceSessionSnapshot(["dbo.DereferenceSessionSnapshot"]) --> SP
    dbo_GetUserID(["dbo.GetUserID"]) --> SP
    dbo_PersistedStream(["dbo.PersistedStream"]) --> SP
    dbo_SessionData(["dbo.SessionData"]) --> SP
    dbo_SessionLock(["dbo.SessionLock"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.DereferenceSessionSnapshot |
| dbo.GetUserID |
| dbo.PersistedStream |
| dbo.SessionData |
| dbo.SessionLock |

## Stored Procedure Code

```sql

```

