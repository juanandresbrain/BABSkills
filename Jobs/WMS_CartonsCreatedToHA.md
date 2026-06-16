# Job: WMS_CartonsCreatedToHA

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WMS_CartonsCreatedToHA"]
    JOB --> WMS_CartonsCreatedToHA_1["Step 1: WMS_CartonsCreatedToHA [SSIS]"]`n```

## Steps

### Step 1: WMS_CartonsCreatedToHA
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WMS\WMS_CartonsCreatedToHA\WMS_CartonsCreatedToHA.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10072 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


