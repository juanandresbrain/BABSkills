# Job: MERCHANDISING - Process - WC to Merch Store Shipments Alloc Adj

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Processes store shipment data from west coast warehouse

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Process - WC to Merch Store Shipments Alloc Adj"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingProcessWCShipmentsAllocAdj
```


