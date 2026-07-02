# Job: zRetire___ERP_MasterDataETL

**Enabled:** No  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetire___ERP_MasterDataETL"]
    JOB --> ERP_MasterDataETL___Entity_1100_1["Step 1: ERP_MasterDataETL - Entity 1100 [SSIS]"]`n    JOB --> ERP_MasterDataETL___Entity_1200_2["Step 2: ERP_MasterDataETL - Entity 1200 [SSIS]"]`n    JOB --> ERP_MasterDataETL___Entity_1700_3["Step 3: ERP_MasterDataETL - Entity 1700 [SSIS]"]`n    JOB --> ERP_MasterDataETL___Entity_2110_4["Step 4: ERP_MasterDataETL - Entity 2110 [SSIS]"]`n    JOB --> ERP_MasterDataETL___Entity_2300_5["Step 5: ERP_MasterDataETL - Entity 2300 [SSIS]"]`n    JOB --> ERP_MasterDataETL___Entity_3001_6["Step 6: ERP_MasterDataETL - Entity 3001 [SSIS]"]`n```

## Steps

### Step 1: ERP_MasterDataETL - Entity 1100
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\ERP_MasterDataETL\ERP_MasterData.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 14 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /SET "\"\Package.Variables[User::Entity]\"";1100 /CALLERINFO SQLAGENT /REPORTING E
```

### Step 2: ERP_MasterDataETL - Entity 1200
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\ERP_MasterDataETL\ERP_MasterData.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 14 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /SET "\"\Package.Variables[User::Entity]\"";1200 /CALLERINFO SQLAGENT /REPORTING E
```

### Step 3: ERP_MasterDataETL - Entity 1700
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\ERP_MasterDataETL\ERP_MasterData.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 14 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /SET "\"\Package.Variables[User::Entity]\"";1700 /CALLERINFO SQLAGENT /REPORTING E
```

### Step 4: ERP_MasterDataETL - Entity 2110
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\ERP_MasterDataETL\ERP_MasterData.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 14 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /SET "\"\Package.Variables[User::Entity]\"";2110 /CALLERINFO SQLAGENT /REPORTING E
```

### Step 5: ERP_MasterDataETL - Entity 2300
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\ERP_MasterDataETL\ERP_MasterData.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 14 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /SET "\"\Package.Variables[User::Entity]\"";2300 /CALLERINFO SQLAGENT /REPORTING E
```

### Step 6: ERP_MasterDataETL - Entity 3001
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\ERP_MasterDataETL\ERP_MasterData.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 14 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /SET "\"\Package.Variables[User::Entity]\"";3001 /CALLERINFO SQLAGENT /REPORTING E
```


