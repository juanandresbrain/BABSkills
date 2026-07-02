# Job: MERCHANDISING - Report - UK Cartons Summary

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Sends CSV email to Distro team to report weekly cartons shipped from UK Warehouse

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Report - UK Cartons Summary"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingSelectUKCartonSummary
```


