# Job: MERCHANDISING - Validation - Merch/MA Styles vs ES

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Validation - Merch/MA Styles vs ES"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingEmailMerchVsESStyles
```


