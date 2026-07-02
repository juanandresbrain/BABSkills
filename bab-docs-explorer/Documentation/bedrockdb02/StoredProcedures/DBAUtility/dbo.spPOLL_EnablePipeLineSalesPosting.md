# dbo.spPOLL_EnablePipeLineSalesPosting

**Database:** DBAUtility  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spPOLL_EnablePipeLineSalesPosting"]
    dbo_spPOLL_StatusPipeLineSalesPosting(["dbo.spPOLL_StatusPipeLineSalesPosting"]) --> SP
    dbo_xp_cmdshell(["dbo.xp_cmdshell"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.spPOLL_StatusPipeLineSalesPosting |
| dbo.xp_cmdshell |

## Stored Procedure Code

```sql
create PROCEDURE [dbo].[spPOLL_EnablePipeLineSalesPosting]
AS
DECLARE @sql VARCHAR(1000)
SET @sql = 'OSQL -E -Q "EXEC msdb.dbo.sp_update_job @job_name = ''MERCHANDISING - Process - Pipeline Sales Posting'', @enabled  = 1"' 

--print @sql
EXEC master.dbo.xp_cmdshell @sql
EXEC [spPOLL_StatusPipeLineSalesPosting]
```

