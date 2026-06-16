# Job: EasyMetricsExtract

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["EasyMetricsExtract"]
    JOB --> SSIS___EasyMetricsExtract_1["Step 1: SSIS - EasyMetricsExtract [SSIS]"]`n```

## Steps

### Step 1: SSIS - EasyMetricsExtract
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WMS\EasyMetricsExtract\EasyMetricsExtract.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10163 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


