# Job: HR_termDCN

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["HR_termDCN"]
    JOB --> nightly_file_creation_1["Step 1: nightly file creation [SSIS]"]`n```

## Steps

### Step 1: nightly file creation
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\HR\HR_termDcn\DCNterm.dtsx\"" /SERVER "\"STL-SSIS-P-01\"" /ENVREFERENCE 10043 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


