# Job: DBA - Purge SSISLogs

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["DBA - Purge SSISLogs"]
    JOB --> Execute_Stored_Procedure_1["Step 1: Execute Stored Procedure [TSQL]"]`n```

## Steps

### Step 1: Execute Stored Procedure
**Subsystem:** TSQL  

```sql
EXEC [dbo].[spPurgeSSISLogData] 
```


