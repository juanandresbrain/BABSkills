# dbo.UpdateRunningJob

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.UpdateRunningJob"]
    dbo_RunningJobs(["dbo.RunningJobs"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.RunningJobs |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[UpdateRunningJob]
@JobID as nvarchar(32),
@JobStatus as smallint
AS
SET NOCOUNT OFF
UPDATE RunningJobs SET JobStatus = @JobStatus WHERE JobID = @JobID
```

