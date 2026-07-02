# Job: MERCHANDISING - Email - Store Shipment Error

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Sends email/text alert if shipment errors are logged in pipeline error queue

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Email - Store Shipment Error"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingEmailShipmentErrors
```


