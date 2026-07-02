# dbo.vwAllRequests

**Database:** BABWForgetMe_Restore  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwAllRequests"]
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
CREATE VIEW [dbo].[vwAllRequests]
AS




SELECT        dbo.ActionStatus.RecordKey, 
			  dbo.ActionStatus.EmailAddress, 
			  dbo.ActionStatus.ActionRequestID, 
			  dbo.ActionStatus.ValidationDate, 
			  dbo.ActionStatus.CompletionDate, 
			  dbo.ActionStatus.RecordsFlaggedDate,
              CASE ISNULL(isnull(dbo.vwRequestsNeedingManualData.RecordKey,dbo.vwRequestsNeedingReview.RecordKey),'Complete')  
					When 'Complete' then 'Review Complete' 
			  Else 'Review Incomplete'
			  End AS ReviewStatus
FROM            dbo.ActionStatus 
				LEFT JOIN dbo.vwRequestsNeedingManualData 
					ON dbo.ActionStatus.RecordKey = dbo.vwRequestsNeedingManualData.RecordKey 
				LEFT JOIN dbo.vwRequestsNeedingReview 
					ON dbo.ActionStatus.RecordKey = dbo.vwRequestsNeedingReview.RecordKey
WHERE         (dbo.ActionStatus.RecordsFlaggedDate IS NOT NULL) AND (dbo.ActionStatus.ValidationDate IS NOT NULL)
```

