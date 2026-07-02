# Job: MERCHANDISING - Process - DDC PO Export

**Enabled:** No  
**Server:** bedrockdb02  
**Description:** exports po data to west coast warehouse - Disabled on 10/11/2016 because DDC advised they no longer use this data.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Process - DDC PO Export"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingOutputPOData
```


