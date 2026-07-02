# Job: MERCHANDISING - Process - UK Stock Adjustments

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Process - UK Stock Adjustments"]
    JOB --> go_1["Step 1: go [TSQL]"]`n```

## Steps

### Step 1: go
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spUKStockAdjustment
```


