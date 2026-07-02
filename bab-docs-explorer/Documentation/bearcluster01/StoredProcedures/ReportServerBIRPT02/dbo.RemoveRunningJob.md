# dbo.RemoveRunningJob

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.RemoveRunningJob"]
    dbo_RunningJobs(["dbo.RunningJobs"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.RunningJobs |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[RemoveRunningJob]
@JobID as nvarchar(32)
AS
SET NOCOUNT OFF
DELETE FROM RunningJobs WHERE JobID = @JobID
```

