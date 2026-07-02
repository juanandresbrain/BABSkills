# Job: MERCHANDISING - Report - Missing Store Shipments - UK

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** sends email with missing uk store shipments

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Report - Missing Store Shipments - UK"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingSelectMissingStoreShipmentUK
```


