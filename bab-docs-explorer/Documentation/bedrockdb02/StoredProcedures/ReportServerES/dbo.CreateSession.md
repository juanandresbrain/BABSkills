# dbo.CreateSession

**Database:** ReportServerES  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.CreateSession"]
    dbo_GetUserID(["dbo.GetUserID"]) --> SP
    dbo_PersistedStream(["dbo.PersistedStream"]) --> SP
    dbo_SessionData(["dbo.SessionData"]) --> SP
    dbo_SessionLock(["dbo.SessionLock"]) --> SP
    dbo_SnapshotData(["dbo.SnapshotData"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.GetUserID |
| dbo.PersistedStream |
| dbo.SessionData |
| dbo.SessionLock |
| dbo.SnapshotData |

## Stored Procedure Code

```sql

```

