# dbo.UpdateRunningJob

**Database:** ReportServerSA  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.UpdateRunningJob"]
    RunningJobs(["RunningJobs"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| RunningJobs |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[UpdateRunningJob]
@JobID as nvarchar(32),
@JobStatus as smallint
AS
SET NOCOUNT OFF
UPDATE RunningJobs SET JobStatus = @JobStatus WHERE JobID = @JobID
```

