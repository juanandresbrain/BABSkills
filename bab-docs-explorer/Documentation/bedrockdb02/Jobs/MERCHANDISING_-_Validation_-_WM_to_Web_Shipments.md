# Job: MERCHANDISING - Validation - WM to Web Shipments

**Enabled:** No  
**Server:** bedrockdb02  
**Description:** Compares WM to Merch and sends email if WM shipments to the web have not posted to Merch.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Validation - WM to Web Shipments"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingCompareWMtoWEBShipments
```


