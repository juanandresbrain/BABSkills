# Job: WMS_DynamicsContainer

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WMS_DynamicsContainer"]
    JOB --> WMS_DynamicsContainer_1["Step 1: WMS_DynamicsContainer [SSIS]"]`n```

## Steps

### Step 1: WMS_DynamicsContainer
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WMS\WMS_DynamicsContainer\WMS_DynamicsContainer.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10107 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


