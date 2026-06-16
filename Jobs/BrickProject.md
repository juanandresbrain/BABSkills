# Job: BrickProject

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["BrickProject"]
    JOB --> BrickDataNotification_1["Step 1: BrickDataNotification [SSIS]"]`n```

## Steps

### Step 1: BrickDataNotification
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\Brick project\BrickDataNotification\BrickDataNotification.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10059 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


