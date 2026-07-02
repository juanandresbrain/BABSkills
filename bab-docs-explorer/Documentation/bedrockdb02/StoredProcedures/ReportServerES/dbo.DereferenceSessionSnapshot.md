# dbo.DereferenceSessionSnapshot

**Database:** ReportServerES  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DereferenceSessionSnapshot"]
    dbo_SessionData(["dbo.SessionData"]) --> SP
    dbo_SnapshotData(["dbo.SnapshotData"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.SessionData |
| dbo.SnapshotData |

## Stored Procedure Code

```sql

```

