# Job: MERCHANDISING - Report - UK MHU Shrink

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Captures a monthly snapshot of shrink adjustments from UK stores, which come to Merch by way of the MHU (merchandise heads up)

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Report - UK MHU Shrink"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingOutputUKstoreMHUshrink
```


