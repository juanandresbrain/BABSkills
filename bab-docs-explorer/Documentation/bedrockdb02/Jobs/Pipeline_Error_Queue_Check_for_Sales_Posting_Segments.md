# Job: Pipeline Error Queue Check for Sales Posting Segments

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Checks for errors related to segments:1005, 3100, 5105, 5100, 5100, 5101, 5102, 5103, 5104, 5006, 5010

## Architecture Diagram

```mermaid
flowchart LR
    JOB["Pipeline Error Queue Check for Sales Posting Segments"]
    JOB --> One_1["Step 1: One [TSQL]"]`n```

## Steps

### Step 1: One
**Subsystem:** TSQL  

```sql
EXEC [me_01].[dbo].[spPipelineERRORqueuecheck]
```


