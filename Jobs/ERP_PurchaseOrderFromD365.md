# Job: ERP_PurchaseOrderFromD365

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["ERP_PurchaseOrderFromD365"]
    JOB --> WMS_DynamicsPurchaseOrderExtract_1["Step 1: WMS_DynamicsPurchaseOrderExtract [SSIS]"]`n    JOB --> ERP_PurchaseOrderFromD365_2["Step 2: ERP_PurchaseOrderFromD365 [SSIS]"]`n```

## Steps

### Step 1: WMS_DynamicsPurchaseOrderExtract
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WMS\WMS_DynamicsPurchaseOrderExtract\WMS_DynamicsPurchaseOrderExtract.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10103 /Par "\"DaysToGoBack(Int32)\"";10 /Par "\"DaysToInclude(Int32)\"";10 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 2: ERP_PurchaseOrderFromD365
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\ERP_PurchaseOrderFromD365\ERP_PurchaseOrderFromD365.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 11 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /SET "\"\Package.Variables[User::Entity]\"";1100 /CALLERINFO SQLAGENT /REPORTING E
```


