# Job: zRetired_ERP_POReceipts

**Enabled:** No  
**Server:** STL-SSIS-P-01  
**Description:** Retired SQL job on 1/30/2023. Replaced with new SSIS package that uses Dynamics Package API interface. See JIRA BIB-464

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_ERP_POReceipts"]
    JOB --> Entity_1100_1["Step 1: Entity 1100 [SSIS]"]`n    JOB --> Entity_2110_2["Step 2: Entity 2110 [SSIS]"]`n    JOB --> Entity_3001_3["Step 3: Entity 3001 [SSIS]"]`n```

## Steps

### Step 1: Entity 1100
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\ERP_POReceipts\ERP_POReceipts.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 12 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /SET "\"\Package.Variables[User::Entity]\"";1100 /CALLERINFO SQLAGENT /REPORTING E
```

### Step 2: Entity 2110
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\ERP_POReceipts\ERP_POReceipts.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 12 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /SET "\"\Package.Variables[User::Entity]\"";2110 /CALLERINFO SQLAGENT /REPORTING E
```

### Step 3: Entity 3001
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\ERP_POReceipts\ERP_POReceipts.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 12 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /SET "\"\Package.Variables[User::Entity]\"";3001 /CALLERINFO SQLAGENT /REPORTING E
```


