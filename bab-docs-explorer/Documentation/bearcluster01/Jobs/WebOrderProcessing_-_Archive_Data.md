# Job: WebOrderProcessing - Archive Data

**Enabled:** Yes  
**Server:** bearcluster01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WebOrderProcessing - Archive Data"]
    JOB --> execute_archival_stored_proc_1["Step 1: execute archival stored proc [TSQL]"]`n```

## Steps

### Step 1: execute archival stored proc
**Subsystem:** TSQL  

```sql
EXEC [WM].[spArchiveItemStatusData]
```


