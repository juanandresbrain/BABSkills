# Job: MERCHANDISING - Process - WM to Merch Shipments Alloc Adj

**Enabled:** No  
**Server:** bedrockdb02  
**Description:** Creates WM shipment and allocation adjustment pipeline files

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Process - WM to Merch Shipments Alloc Adj"]
    JOB --> 1___Export_Shipments_Alloc_Adj_1["Step 1: 1 - Export Shipments Alloc Adj [TSQL]"]`n```

## Steps

### Step 1: 1 - Export Shipments Alloc Adj
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingProcessWMShipmentsAllocAdj
```


