# Job: WMS - Manage D365 Wave Messages

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WMS - Manage D365 Wave Messages"]
    JOB --> Manage_D365_Wave_Message_1["Step 1: Manage D365 Wave Message [SSIS]"]`n```

## Steps

### Step 1: Manage D365 Wave Message
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\WebOrderProcessing\ManageD36WaveMessages.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 6 /Par "\"DaysToGoBack(Int32)\"";1 /Par "\"DaysToInclude(Int32)\"";1 /Par "\"messageAgeInMinutes(Int32)\"";180 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";3 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


