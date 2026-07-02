# Job: WEB - StoresExports

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WEB - StoresExports"]
    JOB --> ExportStoresPackage_1["Step 1: ExportStoresPackage [SSIS]"]`n```

## Steps

### Step 1: ExportStoresPackage
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\WebStores\ExportStoresPackage.dtsx\"" /SERVER "\"STL-SSIS-P-01\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


