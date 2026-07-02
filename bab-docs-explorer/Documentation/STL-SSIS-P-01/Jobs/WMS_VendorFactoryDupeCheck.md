# Job: WMS_VendorFactoryDupeCheck

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WMS_VendorFactoryDupeCheck"]
    JOB --> spEmailVendorsWithSameVendorFactory_1["Step 1: spEmailVendorsWithSameVendorFactory [TSQL]"]`n```

## Steps

### Step 1: spEmailVendorsWithSameVendorFactory
**Subsystem:** TSQL  

```sql
exec wms.spEmailVendorsWithSameVendorFactory
```


