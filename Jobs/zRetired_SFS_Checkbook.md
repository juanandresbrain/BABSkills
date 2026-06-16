# Job: zRetired_SFS_Checkbook

**Enabled:** No  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_SFS_Checkbook"]
    JOB --> SFS_Checkbook_1["Step 1: SFS_Checkbook [SSIS]"]`n```

## Steps

### Step 1: SFS_Checkbook
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\CRM\SOX_SFSCheckbook\SOX_SFSCheckbook.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10025 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


