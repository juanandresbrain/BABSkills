# Job: MERCHANDISING - Process - Costco UDA

**Enabled:** No  
**Server:** bedrockdb02  
**Description:** Creates UDA file based on Costco shipments shipped today in WM

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Process - Costco UDA"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingOutputCostcoUDA
```


