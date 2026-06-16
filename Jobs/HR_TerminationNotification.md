# Job: HR_TerminationNotification

**Enabled:** No  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["HR_TerminationNotification"]
    JOB --> HR_TerminationNotification_SSIS_1["Step 1: HR_TerminationNotification SSIS [SSIS]"]`n    JOB --> HR_UltiproTermSamaccount_2["Step 2: HR_UltiproTermSamaccount [SSIS]"]`n    JOB --> HR_UltiproAddPhoneExt_3["Step 3: HR_UltiproAddPhoneExt [SSIS]"]`n    JOB --> Active_with_Expiration_email_4["Step 4: Active with Expiration email [TSQL]"]`n    JOB --> Duplicate_name_email_5["Step 5: Duplicate name email [TSQL]"]`n```

## Steps

### Step 1: HR_TerminationNotification SSIS
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\HR\HR_TerminationNotification\HR_TerminationNotification.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10042 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 2: HR_UltiproTermSamaccount
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\HR\HR_UltiproTermSamaccount\Package.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 3: HR_UltiproAddPhoneExt
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\HR\HR_UltiproADphoneExt\Package.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 4: Active with Expiration email
**Subsystem:** TSQL  

```sql
exec  PAPAMART.dw.dbo.spEmailUltiProToActiveDirectoryActiveExpired 
```

### Step 5: Duplicate name email
**Subsystem:** TSQL  

```sql
EXEC PAPAMART.dw.dbo.spEmailUltiProToActiveDirectoryDuplicateNames
```


