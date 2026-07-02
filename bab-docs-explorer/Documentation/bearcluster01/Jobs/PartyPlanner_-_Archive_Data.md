# Job: PartyPlanner - Archive Data

**Enabled:** Yes  
**Server:** bearcluster01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["PartyPlanner - Archive Data"]
    JOB --> Execute_Data_Archival_Stored_Proc_1["Step 1: Execute Data Archival Stored Proc [TSQL]"]`n```

## Steps

### Step 1: Execute Data Archival Stored Proc
**Subsystem:** TSQL  

```sql
EXEC [dbo].[sp_ArchiveEventData] 
```


