# dbo.vwCurrentForgetMeStatus

**Database:** BABWForgetMe_Restore  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwCurrentForgetMeStatus"]
    dbo_ActionRequest(["dbo.ActionRequest"]) --> VIEW
    dbo_ActionStatus(["dbo.ActionStatus"]) --> VIEW
    dbo_ValidationResponse(["dbo.ValidationResponse"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ActionRequest |
| dbo.ActionStatus |
| dbo.ValidationResponse |

## View Code

```sql
CREATE VIEW [dbo].[vwCurrentForgetMeStatus]
AS
SELECT        TOP (100) PERCENT a.RecordKey, a.EmailAddress, a.InsertDate, a.ValidationDate, a.CompletionDate, a.RecordsFlaggedDate, r.ActionRequestName, v.ResponseName, r.ActionRequestID
FROM            dbo.ActionStatus AS a LEFT OUTER JOIN
                         dbo.ActionRequest AS r ON a.ActionRequestID = r.ActionRequestID LEFT OUTER JOIN
                         dbo.ValidationResponse AS v ON a.ValidationResponseID = v.ResponseID
ORDER BY a.InsertDate DESC
```

