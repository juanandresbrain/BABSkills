# Job: WMS_ShipConfirmToAptos

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WMS_ShipConfirmToAptos"]
    JOB --> WMS_ShipConfirmToAptos_1["Step 1: WMS_ShipConfirmToAptos [SSIS]"]`n```

## Steps

### Step 1: WMS_ShipConfirmToAptos
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WMS\WMS_ShipConfirmToAptos\WMS_ShipConfirmToAptos.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10069 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


