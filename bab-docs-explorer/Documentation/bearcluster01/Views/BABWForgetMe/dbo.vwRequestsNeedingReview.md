# dbo.vwRequestsNeedingReview

**Database:** BABWForgetMe  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwRequestsNeedingReview"]
    dbo_ActionLog(["dbo.ActionLog"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ActionLog |

## View Code

```sql
CREATE VIEW [dbo].[vwRequestsNeedingReview]
AS
SELECT        RecordKey
FROM            dbo.ActionLog
WHERE        (RemoveData IS NULL) 
AND ActionTableKey <> 30
GROUP BY RecordKey
```

