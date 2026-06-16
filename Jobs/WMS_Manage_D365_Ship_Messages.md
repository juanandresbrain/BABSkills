# Job: WMS_Manage D365 Ship Messages

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WMS_Manage D365 Ship Messages"]
    JOB --> Manage_D365_Ship_Messages_1["Step 1: Manage D365 Ship Messages [SSIS]"]`n    JOB --> WEB_ManageD365ShipMessages_2["Step 2: WEB_ManageD365ShipMessages [SSIS]"]`n```

## Steps

### Step 1: Manage D365 Ship Messages
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\WebOrderProcessing\ManageD365ShipMessages.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 6 /Par "\"DaysToGoBack(Int32)\"";1 /Par "\"DaysToInclude(Int32)\"";1 /Par "\"messageAgeInMinutes(Int32)\"";180 /Par "\"operationTimeout(UInt32)\"";1800 /Par "\"sbBatchSize(Int32)\"";100 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 2: WEB_ManageD365ShipMessages
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\WEB_ManageD365ShipMessages\WEB_ManageD365ShipMessages.dtsx\"" /SERVER "\"STL-SSIS-P-01\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


