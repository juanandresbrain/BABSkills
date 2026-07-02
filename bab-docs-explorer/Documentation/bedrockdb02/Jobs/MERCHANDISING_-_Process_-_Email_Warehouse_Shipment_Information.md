# Job: MERCHANDISING - Process - Email Warehouse Shipment Information

**Enabled:** No  
**Server:** bedrockdb02  
**Description:** Executes spMerchandisingEmailWarehouseShipmentInformation. captures warehouse shipment data, emails to stores.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Process - Email Warehouse Shipment Information"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingEmailWarehouseShipmentInformation
```


