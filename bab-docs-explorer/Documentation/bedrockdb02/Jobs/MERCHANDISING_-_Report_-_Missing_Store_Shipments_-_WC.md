# Job: MERCHANDISING - Report - Missing Store Shipments - WC

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** sends email for missing wc store shipments

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Report - Missing Store Shipments - WC"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingSelectMissingStoreShipmentWC
```


