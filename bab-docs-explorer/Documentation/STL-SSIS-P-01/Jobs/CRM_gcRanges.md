# Job: CRM_gcRanges

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["CRM_gcRanges"]
    JOB --> daily_1["Step 1: daily [SSIS]"]`n```

## Steps

### Step 1: daily
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\CRM\CRM_gcRanges\CRM_gcRanges.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /Par "\"DWStaging_ServerName\"";papamart /Par "\"DW_ServerName\"";papamart /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


