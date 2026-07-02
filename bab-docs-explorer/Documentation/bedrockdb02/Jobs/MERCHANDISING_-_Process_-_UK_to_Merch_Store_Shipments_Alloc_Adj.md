# Job: MERCHANDISING - Process - UK to Merch Store Shipments Alloc Adj

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Generates shipment and allocation adjustment file and posts to pipeline, based on a shipment file provided by UK Warehouse

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Process - UK to Merch Store Shipments Alloc Adj"]
    JOB --> UNO_1["Step 1: UNO [TSQL]"]`n```

## Steps

### Step 1: UNO
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingSelectUKStoreShipments
```


