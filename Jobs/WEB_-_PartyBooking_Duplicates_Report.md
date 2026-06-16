# Job: WEB - PartyBooking Duplicates Report

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WEB - PartyBooking Duplicates Report"]
    JOB --> PartyDupes_SSIS_1["Step 1: PartyDupes-SSIS [SSIS]"]`n```

## Steps

### Step 1: PartyDupes-SSIS
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\PartyReports\PartyDupes.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


