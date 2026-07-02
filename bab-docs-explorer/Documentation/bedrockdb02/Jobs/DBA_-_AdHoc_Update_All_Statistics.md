# Job: DBA - AdHoc Update All Statistics

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["DBA - AdHoc Update All Statistics"]
    JOB --> Execute_SP_Update_Stats_1["Step 1: Execute SP Update Stats [TSQL]"]`n```

## Steps

### Step 1: Execute SP Update Stats
**Subsystem:** TSQL  

```sql
exec sp_updatestats
```


