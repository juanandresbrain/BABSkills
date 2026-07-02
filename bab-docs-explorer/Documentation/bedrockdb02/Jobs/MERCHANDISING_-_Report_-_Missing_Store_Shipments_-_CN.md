# Job: MERCHANDISING - Report - Missing Store Shipments - CN

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Sends email for missing CN store shipments

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Report - Missing Store Shipments - CN"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingSelectMissingStoreShipmentCN
```


