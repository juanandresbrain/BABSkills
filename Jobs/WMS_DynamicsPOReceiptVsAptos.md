# Job: WMS_DynamicsPOReceiptVsAptos

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WMS_DynamicsPOReceiptVsAptos"]
    JOB --> WMS_DynamicsPOReceiptVsAptos_1["Step 1: WMS_DynamicsPOReceiptVsAptos [SSIS]"]`n```

## Steps

### Step 1: WMS_DynamicsPOReceiptVsAptos
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WMS\WMS_DynamicsPOReceiptVsAptos\WMS_DynamicsPOReceiptVsAptos.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10150 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


