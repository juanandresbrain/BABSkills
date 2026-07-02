# Job: zRetired_WMS_Validation_AptosPOvsTPM

**Enabled:** No  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_WMS_Validation_AptosPOvsTPM"]
    JOB --> WMS_Validation_AptosPOvsTPM_1["Step 1: WMS_Validation_AptosPOvsTPM [SSIS]"]`n```

## Steps

### Step 1: WMS_Validation_AptosPOvsTPM
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WMS\WMS_Validation_AptosPOvsTPM\WMS_Validation_AptosPOvsTPM.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10078 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


