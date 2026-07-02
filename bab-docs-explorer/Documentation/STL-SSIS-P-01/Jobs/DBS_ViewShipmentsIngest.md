# Job: DBS_ViewShipmentsIngest

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["DBS_ViewShipmentsIngest"]
    JOB --> DBS_ViewShipmentsIngest_1["Step 1: DBS_ViewShipmentsIngest [SSIS]"]`n```

## Steps

### Step 1: DBS_ViewShipmentsIngest
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\Azure\DBS_ViewShipmentsIngest\DBS_ViewShipmentsIngest.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10180 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


