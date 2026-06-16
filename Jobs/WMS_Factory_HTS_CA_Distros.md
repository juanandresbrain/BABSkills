# Job: WMS_Factory_HTS_CA_Distros

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WMS_Factory_HTS_CA_Distros"]
    JOB --> WMS_Factory_HTS_CA_Distros_1["Step 1: WMS_Factory_HTS_CA_Distros [SSIS]"]`n```

## Steps

### Step 1: WMS_Factory_HTS_CA_Distros
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WMS\WMS_Factory_HTS_CA_Distros\WMS_Factory_HTS_CA_Distros.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10092 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


