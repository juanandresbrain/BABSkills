# Job: MERCHANDISING - Report - Canceled Distributions

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Sends email to report canceled distributions

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Report - Canceled Distributions"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingReportCanceledDistros
```


