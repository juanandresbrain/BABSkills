# Job: WMS_ProductDataExtract

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WMS_ProductDataExtract"]
    JOB --> WMS_ProductDataExtract_1["Step 1: WMS_ProductDataExtract [SSIS]"]`n```

## Steps

### Step 1: WMS_ProductDataExtract
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WMS\WMS_ProductDataExtract\WMS_ProductDataExtract.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10062 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";3 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


