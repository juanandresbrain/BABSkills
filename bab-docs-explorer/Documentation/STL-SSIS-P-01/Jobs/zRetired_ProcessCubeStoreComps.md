# Job: zRetired_ProcessCubeStoreComps

**Enabled:** No  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_ProcessCubeStoreComps"]
    JOB --> ProcessCubeStoreComps_1["Step 1: ProcessCubeStoreComps [SSIS]"]`n```

## Steps

### Step 1: ProcessCubeStoreComps
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\Cube\ProcessCube\ProcessCube.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10116 /Par "\"ProcessCube_DimensionsOrMeasures\"";StoreComps /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


