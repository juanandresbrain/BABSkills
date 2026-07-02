# Job: zRetire - ERP_ItemMasterToWM3PL

**Enabled:** No  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetire - ERP_ItemMasterToWM3PL"]
    JOB --> Entity_1100_1["Step 1: Entity 1100 [SSIS]"]`n```

## Steps

### Step 1: Entity 1100
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\ERP_ItemMasterToWM3PL\ERP_ItemMasterToWM3PL.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 13 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /SET "\"\Package.Variables[User::Entity]\"";1100 /CALLERINFO SQLAGENT /REPORTING E
```


