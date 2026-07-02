# Job: XXXTESTXXX

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["XXXTESTXXX"]
    JOB --> 1_1["Step 1: 1 [SSIS]"]`n```

## Steps

### Step 1: 1
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\ERP_TransfersAndSalesOrderDistros\ERP_TransfersAndSalesOrderDistros.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 19 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /SET "\"\Package.Variables[User::Entity]\"";1100 /CALLERINFO SQLAGENT /REPORTING E
```


