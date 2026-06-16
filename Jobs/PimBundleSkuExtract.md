# Job: PimBundleSkuExtract

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["PimBundleSkuExtract"]
    JOB --> SSIS___PimBundleSkuExtract_1["Step 1: SSIS - PimBundleSkuExtract [SSIS]"]`n```

## Steps

### Step 1: SSIS - PimBundleSkuExtract
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\PimBundleSkuExtract\PimBundleSkuExtract.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10179 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";3 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


