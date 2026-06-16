# Job: WEB - PartyBooking Monthly Reports

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WEB - PartyBooking Monthly Reports"]
    JOB --> PartyMonthly_SSIS_1["Step 1: PartyMonthly-SSIS [SSIS]"]`n```

## Steps

### Step 1: PartyMonthly-SSIS
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\PartyReports\PartyMonthly.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


