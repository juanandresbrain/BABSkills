# Job: MERCHANDISING - Report - Trapped Cost in Transit

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Looks for styles which have 0 units in transit and <> 0 cost in transit, sends email

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Report - Trapped Cost in Transit"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchAnalyticsReportTrappedCostInTransit
```


