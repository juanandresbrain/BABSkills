# dbo.vwOpenRequests

**Database:** BABWForgetMe_Restore  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwOpenRequests"]
    dbo_ActionStatus(["dbo.ActionStatus"]) --> VIEW
    dbo_vwRequestsNeedingManualData(["dbo.vwRequestsNeedingManualData"]) --> VIEW
    dbo_vwRequestsNeedingReview(["dbo.vwRequestsNeedingReview"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ActionStatus |
| dbo.vwRequestsNeedingManualData |
| dbo.vwRequestsNeedingReview |

## View Code

```sql
CREATE VIEW [dbo].[vwOpenRequests]
AS
SELECT        dbo.ActionStatus.RecordKey, dbo.ActionStatus.EmailAddress, dbo.ActionStatus.ActionRequestID, dbo.ActionStatus.ValidationDate, dbo.ActionStatus.CompletionDate, dbo.ActionStatus.RecordsFlaggedDate,
              cASE ISNULL(isnull(dbo.vwRequestsNeedingManualData.RecordKey,dbo.vwRequestsNeedingReview.RecordKey),'Complete')  When 'Complete' then 'Review Complete' 
			  Else 'Review Incomplete'
			  End AS ReviewStatus
FROM            dbo.ActionStatus lEFT JOIN
                         dbo.vwRequestsNeedingManualData ON dbo.ActionStatus.RecordKey = dbo.vwRequestsNeedingManualData.RecordKey lEFT JOIN
                         dbo.vwRequestsNeedingReview ON dbo.ActionStatus.RecordKey = dbo.vwRequestsNeedingReview.RecordKey
WHERE         (dbo.ActionStatus.RecordsFlaggedDate IS NOT NULL) AND (dbo.ActionStatus.ValidationDate IS NOT NULL)
```

