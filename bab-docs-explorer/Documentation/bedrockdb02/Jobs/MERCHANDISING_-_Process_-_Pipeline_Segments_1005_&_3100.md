# Job: MERCHANDISING - Process - Pipeline Segments 1005 & 3100

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Executes Pipleline segments 1005 and 3100

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Process - Pipeline Segments 1005 & 3100"]
    JOB --> PipeApp01Segments_1005___3100_1["Step 1: PipeApp01Segments 1005 & 3100 [TSQL]"]`n```

## Steps

### Step 1: PipeApp01Segments 1005 & 3100
**Subsystem:** TSQL  

```sql
EXEC pipeapp01.master..xp_cmdshell 'PipelineScheduleClient Start 1005 0' -- EDM & PROD to MA

EXEC pipeapp01.master..xp_cmdshell 'PipelineScheduleClient Start 3100 0' -- IM to Infobase - Sales Posting
```


