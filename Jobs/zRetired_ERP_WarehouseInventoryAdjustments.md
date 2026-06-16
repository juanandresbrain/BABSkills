# Job: zRetired__ERP_WarehouseInventoryAdjustments

**Enabled:** No  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired__ERP_WarehouseInventoryAdjustments"]
    JOB --> 1100_1["Step 1: 1100 [SSIS]"]`n    JOB --> 2110_2["Step 2: 2110 [SSIS]"]`n    JOB --> 3001_3["Step 3: 3001 [SSIS]"]`n    JOB --> 1200_4["Step 4: 1200 [SSIS]"]`n```

## Steps

### Step 1: 1100
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\ERP_WarehouseInventoryAdjustments\ERP_WarehouseInventoryAdjustments.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 21 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /SET "\"\Package.Variables[User::Entity]\"";1100 /CALLERINFO SQLAGENT /REPORTING E
```

### Step 2: 2110
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\ERP_WarehouseInventoryAdjustments\ERP_WarehouseInventoryAdjustments.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 21 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /SET "\"\Package.Variables[User::Entity]\"";2110 /CALLERINFO SQLAGENT /REPORTING E
```

### Step 3: 3001
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\ERP_WarehouseInventoryAdjustments\ERP_WarehouseInventoryAdjustments.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 21 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /SET "\"\Package.Variables[User::Entity]\"";3001 /CALLERINFO SQLAGENT /REPORTING E
```

### Step 4: 1200
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\ERP_WarehouseInventoryAdjustments\ERP_WarehouseInventoryAdjustments.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 21 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /SET "\"\Package.Variables[User::Entity]\"";1200 /CALLERINFO SQLAGENT /REPORTING E
```


