# Job: zRetired_MERCHANDISING - Process - Store Distributions Reports

**Enabled:** No  
**Server:** bedrockdb02  
**Description:** Captures report of distributions created per store, emails each store their specific distribution report.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_MERCHANDISING - Process - Store Distributions Reports"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingSelectStoreDistributions
```


