# Job: MERCHANDISING - Report - WM Cartons Not In Merch

**Enabled:** No  
**Server:** bedrockdb02  
**Description:** Checks for WM cartons shipped that are not in Merch, sends alert

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Report - WM Cartons Not In Merch"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingSelectWMtoMerchCartonValidation
```


