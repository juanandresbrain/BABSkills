# Job: WEB - PartyBooking Weekly Reports

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WEB - PartyBooking Weekly Reports"]
    JOB --> PartyWeekly_SSIS_1["Step 1: PartyWeekly-SSIS [SSIS]"]`n```

## Steps

### Step 1: PartyWeekly-SSIS
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\PartyReports\PartyWeekly.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


