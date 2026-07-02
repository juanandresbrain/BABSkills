# Job: WMS_CartonsDetailToHA

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WMS_CartonsDetailToHA"]
    JOB --> WMS_CartonsDetailToHA_1["Step 1: WMS_CartonsDetailToHA [SSIS]"]`n    JOB --> WMS_PreWaveRouting_2["Step 2: WMS_PreWaveRouting [SSIS]"]`n```

## Steps

### Step 1: WMS_CartonsDetailToHA
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WMS\WMS_CartonsDetailToHA\WMS_CartonsDetailToHA.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10071 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";3 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 2: WMS_PreWaveRouting
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WMS\PreWaveRoutingReport\WMS_PreWaveRouting.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10080 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";3 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


