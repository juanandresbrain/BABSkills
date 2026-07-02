# dbo.CleanExpiredJobs

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.CleanExpiredJobs"]
    dbo_RunningJobs(["dbo.RunningJobs"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.RunningJobs |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[CleanExpiredJobs]
AS
SET NOCOUNT OFF
DELETE FROM RunningJobs WHERE DATEADD(s, Timeout, StartDate) < GETDATE()
```

