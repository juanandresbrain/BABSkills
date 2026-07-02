# Job: MERCHANDISING - Report - WM Locked Vs Merch 1000

**Enabled:** No  
**Server:** bedrockdb02  
**Description:** Captures and emails a summary of variances between WM Locked inventory and Merch location 1000

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Report - WM Locked Vs Merch 1000"]
    JOB --> one_1["Step 1: one [TSQL]"]`n```

## Steps

### Step 1: one
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingReportWMLockedVsMerchLocation1000
```


