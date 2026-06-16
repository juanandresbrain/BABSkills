# Job: WMS_VendorMasterTo3PL

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WMS_VendorMasterTo3PL"]
    JOB --> WMS_VendorMasterTo3PL_1["Step 1: WMS_VendorMasterTo3PL [SSIS]"]`n```

## Steps

### Step 1: WMS_VendorMasterTo3PL
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WMS\WMS_VendorMasterTo3PL\WMS_VendorMasterTo3PL.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10110 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


