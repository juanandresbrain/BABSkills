# dbo.vwCurrentForgetMeStatus_V1_1

**Database:** BABWForgetMe  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwCurrentForgetMeStatus_V1_1"]
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
CREATE VIEW [dbo].[vwCurrentForgetMeStatus_V1_1]
AS
SELECT        TOP (100) PERCENT a.RecordKey, a.EmailAddress, a.InsertDate, a.ValidationDate, a.CompletionDate, a.RecordsFlaggedDate, r.ActionRequestName, v.ResponseName, r.ActionRequestID, a.ForgetMeAdminValidationDate
FROM            dbo.ActionStatus AS a LEFT OUTER JOIN
                         dbo.ActionRequest AS r ON a.ActionRequestID = r.ActionRequestID LEFT OUTER JOIN
                         dbo.ValidationResponse AS v ON a.ValidationResponseID = v.ResponseID
ORDER BY a.InsertDate DESC
```

