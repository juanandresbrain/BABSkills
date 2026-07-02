# Job: WMS_Report - WholesalePurchaseOrderOnOrderData

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WMS_Report - WholesalePurchaseOrderOnOrderData"]
    JOB --> WMS_WholesalePurchaseOrderOnOrderData_1["Step 1: WMS_WholesalePurchaseOrderOnOrderData [SSIS]"]`n```

## Steps

### Step 1: WMS_WholesalePurchaseOrderOnOrderData
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WMS\WMS_WholesalePurchaseOrderOnOrderData\WMS_WholesalePurchaseOrderOnOrderData.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10075 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


