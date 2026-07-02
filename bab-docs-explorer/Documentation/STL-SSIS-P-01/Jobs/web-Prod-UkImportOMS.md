# Job: web-Prod-UkImportOMS

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["web-Prod-UkImportOMS"]
    JOB --> UKImportOMS_1["Step 1: UKImportOMS [SSIS]"]`n```

## Steps

### Step 1: UKImportOMS
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\WebOrderProcessing\UkImportOMS.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 6 /Par WOPExecutable;"\"\\STL-SSIS-P-01\ETL Executables\WebOrderProcessing\WOP.exe\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


