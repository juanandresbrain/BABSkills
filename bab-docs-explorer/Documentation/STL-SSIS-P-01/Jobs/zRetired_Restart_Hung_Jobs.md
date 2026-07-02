# Job: zRetired_Restart Hung Jobs

**Enabled:** No  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_Restart Hung Jobs"]
    JOB --> spRestartHungSQLAgentJobs_1["Step 1: spRestartHungSQLAgentJobs [TSQL]"]`n```

## Steps

### Step 1: spRestartHungSQLAgentJobs
**Subsystem:** TSQL  

```sql
exec spRestartHungSQLAgentJobs 
```


