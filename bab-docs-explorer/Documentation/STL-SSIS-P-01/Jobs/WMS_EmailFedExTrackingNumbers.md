# Job: WMS_EmailFedExTrackingNumbers

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WMS_EmailFedExTrackingNumbers"]
    JOB --> spEmailFedExTracking_1["Step 1: spEmailFedExTracking [TSQL]"]`n```

## Steps

### Step 1: spEmailFedExTracking
**Subsystem:** TSQL  

```sql
if    (    select count(*)     from wms.ShipmentConfirmAptos with (nolock)     where Warehouse='9980'     and AptosDistributionNumber > 0    and isnull(ContainerManifestID,'') <> ''    and datediff(dd, dateadd(hh, -6, ShipConfirmDatetime), getdate()) = 0    ) > 0    begin      exec WMS.spEmailFedExTracking  end
```


