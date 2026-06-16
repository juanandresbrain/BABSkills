# Job: Party_Facts ETL

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["Party_Facts ETL"]
    JOB --> Execute_Package_1["Step 1: Execute Package [SSIS]"]`n```

## Steps

### Step 1: Execute Package
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\PartyFacts\MergePartyFacts.dtsx\"" /SERVER "\"STL-SSIS-P-01\"" /ENVREFERENCE 10049 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


