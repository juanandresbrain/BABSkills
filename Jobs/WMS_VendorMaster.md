# Job: WMS_VendorMaster

**Enabled:** Yes  
**Description:** Step 2 added 9/14/2021 : This is used to pull data from Dynamics in order to load VendorInvoiceDim in DataWarehouse

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WMS_VendorMaster"]
    JOB --> WMS_VendorMaster_1["Step 1: WMS_VendorMaster [SSIS]"]`n    JOB --> WMS_VendorDataExtract_2["Step 2: WMS_VendorDataExtract [SSIS]"]`n```

## Steps

### Step 1: WMS_VendorMaster
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WMS\WMS_VendorMaster\WMS_VendorMaster.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10083 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 2: WMS_VendorDataExtract
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WMS\WMS_VendorDataExtract\WMS_VendorDataExtract.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10122 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


