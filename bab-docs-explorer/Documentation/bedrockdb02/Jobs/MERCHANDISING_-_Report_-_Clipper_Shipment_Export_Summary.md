# Job: MERCHANDISING - Report - Clipper Shipment Export Summary

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Sends email with summary of exported distros to Clipper

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Report - Clipper Shipment Export Summary"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingReportWarehouseStoreShipmentDailySummary
```


