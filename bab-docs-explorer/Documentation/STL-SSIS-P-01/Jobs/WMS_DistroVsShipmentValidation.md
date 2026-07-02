# Job: WMS_DistroVsShipmentValidation

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WMS_DistroVsShipmentValidation"]
    JOB --> WMS_DistroVsShipmentValidation_1["Step 1: WMS_DistroVsShipmentValidation [SSIS]"]`n```

## Steps

### Step 1: WMS_DistroVsShipmentValidation
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WMS\WMS_DistroVsShipmentValidation\WMS_DistroVsShipmentValidation.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10077 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


