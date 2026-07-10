# Job: zRetired_05_AuditDailyWHProduction

**Enabled:** No  
**Server:** papamart  
**Description:** No description available.  

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_05_AuditDailyWHProduction"]
    JOB --> S1["Step 1: exec spWCAudit_LogDailyWHProduction [TSQL]"]
```

## Steps

### Step 1: exec spWCAudit_LogDailyWHProduction
**Subsystem:** TSQL  

```sql
exec spWCAudit_DailyWHProduction
```

