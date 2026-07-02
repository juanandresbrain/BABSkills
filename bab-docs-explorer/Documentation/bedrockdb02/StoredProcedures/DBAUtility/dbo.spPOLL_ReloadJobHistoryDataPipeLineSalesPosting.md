# dbo.spPOLL_ReloadJobHistoryDataPipeLineSalesPosting

**Database:** DBAUtility  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spPOLL_ReloadJobHistoryDataPipeLineSalesPosting"]
    dbo_sp_start_job(["dbo.sp_start_job"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.sp_start_job |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[spPOLL_ReloadJobHistoryDataPipeLineSalesPosting] 
	
AS

SET NOCOUNT ON

EXECUTE msdb..sp_start_job @job_id='95EFDC6D-D1D9-4CA1-ADB5-9D499BAD9109'  --Poll - Reload Job Status Data
```

