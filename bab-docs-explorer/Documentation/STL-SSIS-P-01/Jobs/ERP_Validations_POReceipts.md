# Job: ERP_Validations_POReceipts

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** Only the last step runs (send email), the other steps ingest a file that is no longer valid.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["ERP_Validations_POReceipts"]
    JOB --> Entity_1100_1["Step 1: Entity 1100 [SSIS]"]`n    JOB --> Entity_2110_2["Step 2: Entity 2110 [SSIS]"]`n    JOB --> Entity_3001_3["Step 3: Entity 3001 [SSIS]"]`n    JOB --> SendEmail_4["Step 4: SendEmail [SSIS]"]`n```

## Steps

### Step 1: Entity 1100
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\ERP\ERP_Validation_POReceipts\ERP_Validation_POReceipts.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10029 /Par "\"DaysToGoBack(Int32)\"";7 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /SET "\"\Package.Variables[User::Entity]\"";1100 /SET "\"\Package.Variables[User::SendEmailFlag]\"";0 /CALLERINFO SQLAGENT /REPORTING E
```

### Step 2: Entity 2110
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\ERP\ERP_Validation_POReceipts\ERP_Validation_POReceipts.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10029 /Par "\"DaysToGoBack(Int32)\"";7 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /SET "\"\Package.Variables[User::Entity]\"";2110 /SET "\"\Package.Variables[User::SendEmailFlag]\"";0 /CALLERINFO SQLAGENT /REPORTING E
```

### Step 3: Entity 3001
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\ERP\ERP_Validation_POReceipts\ERP_Validation_POReceipts.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10029 /Par "\"DaysToGoBack(Int32)\"";7 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /SET "\"\Package.Variables[User::Entity]\"";3001 /SET "\"\Package.Variables[User::SendEmailFlag]\"";0 /CALLERINFO SQLAGENT /REPORTING E
```

### Step 4: SendEmail
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\ERP\ERP_Validation_POReceipts\ERP_Validation_POReceipts.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10029 /Par "\"DaysToGoBack(Int32)\"";7 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /SET "\"\Package.Variables[User::SendEmailFlag]\"";1 /CALLERINFO SQLAGENT /REPORTING E
```


