# Job: EasyMetricsExtract_LaborHours

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** Generates Labor Hour Report Files for upload to Easy Metrics Amazon S3 Location. Dependent on daily UKG Load

## Architecture Diagram

```mermaid
flowchart LR
    JOB["EasyMetricsExtract_LaborHours"]
    JOB --> SSIS___EasyMetricsExtract_LaborHours_1["Step 1: SSIS - EasyMetricsExtract_LaborHours [SSIS]"]`n```

## Steps

### Step 1: SSIS - EasyMetricsExtract_LaborHours
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WMS\EasyMetricsExtract_LaborHours\EasyMetricsExtract_LaborHours.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10170 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


