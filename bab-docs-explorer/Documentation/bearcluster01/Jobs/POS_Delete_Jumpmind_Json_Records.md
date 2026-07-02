# Job: POS Delete Jumpmind Json Records

**Enabled:** Yes  
**Server:** bearcluster01  
**Description:** Delete Jumpmind Json Records older than 90 days

## Architecture Diagram

```mermaid
flowchart LR
    JOB["POS Delete Jumpmind Json Records"]
    JOB --> EXEC_spDeleteJumpmindJsonRecords_1["Step 1: EXEC spDeleteJumpmindJsonRecords [TSQL]"]`n```

## Steps

### Step 1: EXEC spDeleteJumpmindJsonRecords
**Subsystem:** TSQL  

```sql
EXEC ApplicationResources.dbo.spDeleteJumpmindJsonRecords
```


