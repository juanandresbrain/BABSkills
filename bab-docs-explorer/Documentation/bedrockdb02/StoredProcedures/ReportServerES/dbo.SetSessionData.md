# dbo.SetSessionData

**Database:** ReportServerES  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.SetSessionData"]
    dbo_DereferenceSessionSnapshot(["dbo.DereferenceSessionSnapshot"]) --> SP
    dbo_GetUserID(["dbo.GetUserID"]) --> SP
    dbo_PersistedStream(["dbo.PersistedStream"]) --> SP
    dbo_SessionData(["dbo.SessionData"]) --> SP
    dbo_SnapshotData(["dbo.SnapshotData"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.DereferenceSessionSnapshot |
| dbo.GetUserID |
| dbo.PersistedStream |
| dbo.SessionData |
| dbo.SnapshotData |

## Stored Procedure Code

```sql

```

