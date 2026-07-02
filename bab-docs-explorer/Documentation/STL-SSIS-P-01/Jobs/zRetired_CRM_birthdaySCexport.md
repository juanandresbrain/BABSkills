# Job: zRetired_CRM_birthdaySCexport

**Enabled:** No  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_CRM_birthdaySCexport"]
    JOB --> daily_1["Step 1: daily [SSIS]"]`n    JOB --> start_trigger_2["Step 2: start trigger [TSQL]"]`n```

## Steps

### Step 1: daily
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\CRM\CRM_birthdaySCexport\CRM_birthdaySCexport.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 2: start trigger
**Subsystem:** TSQL  

```sql
EXEC [stl-ssis-p-02].msdb.dbo.sp_start_job @job_name='CRM_trigger_bday_export'
```


