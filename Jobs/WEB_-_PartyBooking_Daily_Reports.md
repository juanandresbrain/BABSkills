# Job: WEB - PartyBooking Daily Reports

**Enabled:** Yes  
**Description:** No Description

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WEB - PartyBooking Daily Reports"]
    JOB --> WMS_PartyWebOrdersShippedDetailExtract_1["Step 1: WMS_PartyWebOrdersShippedDetailExtract [SSIS]"]`n    JOB --> PartyReports_SSIS_2["Step 2: PartyReports-SSIS [SSIS]"]`n```

## Steps

### Step 1: WMS_PartyWebOrdersShippedDetailExtract
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WMS\WMS_PartyWebOrdersShippedDetailExtract\WMS_PartyWebOrdersShippedDetailExtract.dtsx\"" /SERVER "\"STL-SSIS-P-01\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 2: PartyReports-SSIS
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\PartyReports\PartyReports.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10035 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";3 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


