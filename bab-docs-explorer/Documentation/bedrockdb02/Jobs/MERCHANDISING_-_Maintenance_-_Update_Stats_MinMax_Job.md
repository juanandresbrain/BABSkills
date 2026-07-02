# Job: MERCHANDISING - Maintenance - Update Stats MinMax Job

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Calls me_01.dbo.sp_MinMaxMaintenance which updates statistics for the tables used by the Min/Max job.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Maintenance - Update Stats MinMax Job"]
    JOB --> Uno_1["Step 1: Uno [TSQL]"]`n```

## Steps

### Step 1: Uno
**Subsystem:** TSQL  

```sql
EXEC [me_01].[dbo].[sp_MinMaxMaintenance]
```


