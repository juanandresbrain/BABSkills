# dbo.ListRunningJobs

**Database:** ReportServerSA  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.ListRunningJobs"]
    RunningJobs(["RunningJobs"]) --> SP
    Users(["Users"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| RunningJobs |
| Users |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[ListRunningJobs]
AS
SELECT JobID, StartDate, ComputerName, RequestName, RequestPath, SUSER_SNAME(Users.[Sid]), Users.[UserName], Description, 
    Timeout, JobAction, JobType, JobStatus, Users.[AuthType]
FROM RunningJobs 
INNER JOIN Users 
ON RunningJobs.UserID = Users.UserID
```

