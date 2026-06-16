# Job: WEB-Prod - US - Set Shipped

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WEB-Prod - US - Set Shipped"]
    JOB --> Set_Shipped_1["Step 1: Set Shipped [SSIS]"]`n```

## Steps

### Step 1: Set Shipped
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\WebOrderProcessing\setShipped.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 6 /Par "\"messageAgeInHours(Int32)\"";120 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


