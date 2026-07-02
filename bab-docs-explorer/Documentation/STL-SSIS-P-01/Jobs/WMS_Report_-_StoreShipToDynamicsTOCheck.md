# Job: WMS_Report - StoreShipToDynamicsTOCheck

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** Email Corperate Applications and Distro Bear teams a report that lists store shipments that have not attempted to push through the API to Dynamics;

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WMS_Report - StoreShipToDynamicsTOCheck"]
    JOB --> spReportStoreShipToDynamicsTOCheck_1["Step 1: spReportStoreShipToDynamicsTOCheck [TSQL]"]`n```

## Steps

### Step 1: spReportStoreShipToDynamicsTOCheck
**Subsystem:** TSQL  

```sql
EXEC WMS.spReportStoreShipToDynamicsTOCheck
```


