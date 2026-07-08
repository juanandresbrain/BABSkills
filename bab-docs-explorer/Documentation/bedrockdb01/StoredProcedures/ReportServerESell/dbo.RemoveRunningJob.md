# dbo.RemoveRunningJob

**Database:** ReportServerESell  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.RemoveRunningJob"]
    RunningJobs(["RunningJobs"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| RunningJobs |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[RemoveRunningJob]
@JobID as nvarchar(32)
AS
SET NOCOUNT OFF
DELETE FROM RunningJobs WHERE JobID = @JobID
```

