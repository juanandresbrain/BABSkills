# dbo.GetSessionData

**Database:** ReportServerES  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.GetSessionData"]
    dbo_CheckSessionLock(["dbo.CheckSessionLock"]) --> SP
    dbo_GetUserID(["dbo.GetUserID"]) --> SP
    dbo_SessionData(["dbo.SessionData"]) --> SP
    dbo_SnapshotData(["dbo.SnapshotData"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.CheckSessionLock |
| dbo.GetUserID |
| dbo.SessionData |
| dbo.SnapshotData |

## Stored Procedure Code

```sql

```

