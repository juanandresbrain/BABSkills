# Job: SalesToDynamics-CRITICAL_JOB_CHECK

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["SalesToDynamics-CRITICAL_JOB_CHECK"]
    JOB --> spSalesToDynamicsWeeklyUpdateJobHistoryEmail_1["Step 1: spSalesToDynamicsWeeklyUpdateJobHistoryEmail [TSQL]"]`n```

## Steps

### Step 1: spSalesToDynamicsWeeklyUpdateJobHistoryEmail
**Subsystem:** TSQL  

```sql
exec spSalesToDynamicsWeeklyUpdateJobHistoryEmail
```


