# Job: MERCHANDISING - Process - WM to Merch Shipments Alloc Adj - WEB

**Enabled:** No  
**Server:** bedrockdb02  
**Description:** Exports Bearhouse to Web Shipments & Allocation Adjustments from WM to Merchandising

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Process - WM to Merch Shipments Alloc Adj - WEB"]
    JOB --> one_1["Step 1: one [TSQL]"]`n```

## Steps

### Step 1: one
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingProcessWMShipmentsAllocAdjWEB
```


