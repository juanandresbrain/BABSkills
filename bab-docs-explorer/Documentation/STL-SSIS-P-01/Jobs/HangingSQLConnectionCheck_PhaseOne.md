# Job: HangingSQLConnectionCheck_PhaseOne

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** This is designed to connect to stores to identify the locations which are 'hanging' and not allowing the process to continue.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["HangingSQLConnectionCheck_PhaseOne"]
    JOB --> HangingSQLConnectionCheck_1["Step 1: HangingSQLConnectionCheck [SSIS]"]`n```

## Steps

### Step 1: HangingSQLConnectionCheck
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\ADMIN\HangingSQLConnectionCheck\HangingSQLConnectionCheck.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10121 /Par "\"PhaseCounter(Int32)\"";1 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


