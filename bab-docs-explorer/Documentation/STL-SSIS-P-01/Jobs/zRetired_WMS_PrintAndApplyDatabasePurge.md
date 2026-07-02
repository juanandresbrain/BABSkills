# Job: zRetired_WMS_PrintAndApplyDatabasePurge

**Enabled:** No  
**Server:** STL-SSIS-P-01  
**Description:** Purges carton records older than 30 days in the print and apply database.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_WMS_PrintAndApplyDatabasePurge"]
    JOB --> SSIS____WMS_PrintAndApplyDatabasePurge_1["Step 1: SSIS  - WMS_PrintAndApplyDatabasePurge [SSIS]"]`n```

## Steps

### Step 1: SSIS  - WMS_PrintAndApplyDatabasePurge
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WMS\WMS_PrintAndApplyDatabasePurge\WMS_PrintAndApplyDatabasePurge.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10126 /Par "\"DaysToGoBack(Int32)\"";21 /Par "\"DaysToInclude(Int32)\"";21 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";1 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


