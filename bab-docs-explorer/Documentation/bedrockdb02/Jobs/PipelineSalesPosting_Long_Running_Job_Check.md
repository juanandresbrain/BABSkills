# Job: PipelineSalesPosting Long Running Job Check

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Checking to see if PIPELINE JOBS RUN LONGER THAN 2 HOURS SENDS EMAIL TO ENT SYS ALERTS

## Architecture Diagram

```mermaid
flowchart LR
    JOB["PipelineSalesPosting Long Running Job Check"]
    JOB --> CHECK_FOR_PIPELINE_JOBS_RUNING_LONGER_THAN_2_HOURS_1["Step 1: CHECK FOR PIPELINE JOBS RUNING LONGER THAN 2 HOURS [TSQL]"]`n```

## Steps

### Step 1: CHECK FOR PIPELINE JOBS RUNING LONGER THAN 2 HOURS
**Subsystem:** TSQL  

```sql
EXEC [me_01].[dbo].[PiplelineSalesPostingTimeCheck]
```


