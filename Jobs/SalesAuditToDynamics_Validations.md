# Job: SalesAuditToDynamics_Validations

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["SalesAuditToDynamics_Validations"]
    JOB --> SSIS___Validation_DynamicsSalesData_1["Step 1: SSIS - Validation_DynamicsSalesData [SSIS]"]`n```

## Steps

### Step 1: SSIS - Validation_DynamicsSalesData
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WMS\Validation_DynamicsSalesData\Validation_DynamicsSalesData.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10177 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


