# Job: ForgetMe

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["ForgetMe"]
    JOB --> Load_Admin_Review_Records_1["Step 1: Load Admin Review Records [SSIS]"]`n    JOB --> LoadPII_2["Step 2: LoadPII [SSIS]"]`n    JOB --> LoadOutputData_3["Step 3: LoadOutputData [SSIS]"]`n    JOB --> Cleanse_PII_4["Step 4: Cleanse PII [SSIS]"]`n```

## Steps

### Step 1: Load Admin Review Records
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\ForgetMe\RetrieveData\LoadAdminReviewRecords.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 22 /Par "\"CRM_ServerName\"";"\"stl-crmdb-p-01\"" /Par "\"DaysToGoBack(Int32)\"";1 /Par "\"DaysToInclude(Int32)\"";1 /Par "\"WebOrderProcessing_ServerName\"";"\"bearcluster01.sql.buildabear.com\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 2: LoadPII
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\ForgetMe\RetrieveData\LoadPIIRecords.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 22 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 3: LoadOutputData
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\ForgetMe\RetrieveData\LoadRetrieveMe.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 22 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 4: Cleanse PII
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\ForgetMe\RetrieveData\CleansePIIRecords.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 22 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


