# Job: MERCHANDISING - Process - CN to Merch - Inventory Adjustments

**Enabled:** No  
**Server:** bedrockdb02  
**Description:** No description available. Disabled Job on 11/29/2018 because of Data Integrity Issues with Kerry Logistics. - TC

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Process - CN to Merch - Inventory Adjustments"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec spMerchandisingImportCNInvAdj
```


