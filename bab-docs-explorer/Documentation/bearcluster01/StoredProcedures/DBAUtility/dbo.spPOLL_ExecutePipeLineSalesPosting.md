# dbo.spPOLL_ExecutePipeLineSalesPosting

**Database:** DBAUtility  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spPOLL_ExecutePipeLineSalesPosting"]
    dbo_sp_start_job(["dbo.sp_start_job"]) --> SP
    dbo_spPOLL_StatusPipeLineSalesPosting(["dbo.spPOLL_StatusPipeLineSalesPosting"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.sp_start_job |
| dbo.spPOLL_StatusPipeLineSalesPosting |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[spPOLL_ExecutePipeLineSalesPosting]
AS

EXEC msdb.dbo.sp_start_job @job_name = 'MERCHANDISING - Process - Pipeline Sales Posting'

EXEC [spPOLL_StatusPipeLineSalesPosting]
```

