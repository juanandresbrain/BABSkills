# dbo.CleanExpiredJobs

**Database:** ReportServerESell  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.CleanExpiredJobs"]
    RunningJobs(["RunningJobs"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| RunningJobs |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[CleanExpiredJobs]
AS
SET NOCOUNT OFF
DELETE FROM RunningJobs WHERE DATEADD(s, Timeout, StartDate) < GETDATE()
```

