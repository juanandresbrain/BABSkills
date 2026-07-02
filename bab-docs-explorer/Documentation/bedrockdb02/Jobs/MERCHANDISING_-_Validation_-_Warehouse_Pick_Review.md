# Job: MERCHANDISING - Validation - Warehouse Pick Review

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Checks to see that all is well with the Warehouse Pick Review run each night.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Validation - Warehouse Pick Review"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingWhsePickReviewSummary
```


