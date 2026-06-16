# Job: ERP_POReceipts

**Enabled:** Yes  
**Description:** Pushes 3PW receipts to Dynamics. Uses Package API Integration as related to JIRA BIB-464.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["ERP_POReceipts"]
    JOB --> 1100___SSIS___ERP_POReceipts_1["Step 1: 1100 - SSIS - ERP_POReceipts [SSIS]"]`n    JOB --> 1200___SSIS___ERP_POReceipts_2["Step 2: 1200 - SSIS - ERP_POReceipts [SSIS]"]`n    JOB --> 2110___SSIS___ERP_POReceipts_3["Step 3: 2110 - SSIS - ERP_POReceipts [SSIS]"]`n    JOB --> 3001___SSIS___ERP_POReceipts_4["Step 4: 3001 - SSIS - ERP_POReceipts [SSIS]"]`n```

## Steps

### Step 1: 1100 - SSIS - ERP_POReceipts
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WMS\ERP_POReceipts\ERP_POReceipts.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10161 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /SET "\"\Package.Variables[User::Entity]\"";1100 /CALLERINFO SQLAGENT /REPORTING E
```

### Step 2: 1200 - SSIS - ERP_POReceipts
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WMS\ERP_POReceipts\ERP_POReceipts.dtsx\"" /SERVER "\"STL-SSIS-P-01\"" /ENVREFERENCE 10161 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /SET "\"\Package.Variables[User::Entity]\"";1200 /CALLERINFO SQLAGENT /REPORTING E
```

### Step 3: 2110 - SSIS - ERP_POReceipts
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WMS\ERP_POReceipts\ERP_POReceipts.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10161 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /SET "\"\Package.Variables[User::Entity]\"";2110 /CALLERINFO SQLAGENT /REPORTING E
```

### Step 4: 3001 - SSIS - ERP_POReceipts
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WMS\ERP_POReceipts\ERP_POReceipts.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10161 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /SET "\"\Package.Variables[User::Entity]\"";3001 /CALLERINFO SQLAGENT /REPORTING E
```


