# Job: MERCHANDISING - Process - CN to Merch - Shipments and Allocation Adjustments

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Process - CN to Merch - Shipments and Allocation Adjustments"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec spMerchandisingProcessCNShipmentsAllocAdj
```


