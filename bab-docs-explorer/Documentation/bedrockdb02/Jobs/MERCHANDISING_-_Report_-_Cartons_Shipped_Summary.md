# Job: MERCHANDISING - Report - Cartons Shipped Summary

**Enabled:** No  
**Server:** bedrockdb02  
**Description:** Sends email w/report to the Logistics team. Will run on Sunday, so gathers data from previous week.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Report - Cartons Shipped Summary"]
    JOB --> one_1["Step 1: one [TSQL]"]`n```

## Steps

### Step 1: one
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingReportCartonsShippedSummary
```


