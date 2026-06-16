# Job: CRM_DB_Stats_Archive

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["CRM_DB_Stats_Archive"]
    JOB --> daily_check_1["Step 1: daily check [SSIS]"]`n```

## Steps

### Step 1: daily check
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\CRM\CRMdbStatsArchive\CRMdbStatsArchive.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /Par CRMfileStagePath;"\"\\stl-ssis-p-01\IntegrationStaging\CRM\DBstatsArchive\\"" /Par "\"DW_ServerName\"";papamart /Par "\"IntegrationStaging_ServerName\"";"\"STL-SSIS-P-01\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


