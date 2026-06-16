# Job: zRetired_WEB - DYNAMIC ACTION - CRITICAL JOB CHECK

**Enabled:** No  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_WEB - DYNAMIC ACTION - CRITICAL JOB CHECK"]
    JOB --> spDynamicActionSQLJobHistoryEmail_1["Step 1: spDynamicActionSQLJobHistoryEmail [TSQL]"]`n```

## Steps

### Step 1: spDynamicActionSQLJobHistoryEmail
**Subsystem:** TSQL  

```sql
exec spDynamicActionSQLJobHistoryEmail  
```


