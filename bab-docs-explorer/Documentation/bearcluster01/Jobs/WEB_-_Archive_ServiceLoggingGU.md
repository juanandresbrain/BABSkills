# Job: WEB - Archive ServiceLoggingGU

**Enabled:** Yes  
**Server:** bearcluster01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WEB - Archive ServiceLoggingGU"]
    JOB --> Run_Proc_1["Step 1: Run Proc [TSQL]"]`n```

## Steps

### Step 1: Run Proc
**Subsystem:** TSQL  

```sql
exec sp_ArchiveLoggingData
```


