# Job: WMS_ASNCreate

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WMS_ASNCreate"]
    JOB --> Reset_ASN_1["Step 1: Reset ASN [TSQL]"]`n    JOB --> WMS_ASNCreate_2["Step 2: WMS_ASNCreate [SSIS]"]`n```

## Steps

### Step 1: Reset ASN
**Subsystem:** TSQL  

```sql
begin   exec wms.ASNToDynamicsResetForAPI  end
```

### Step 2: WMS_ASNCreate
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WMS\WMS_ASNCreate\WMS_ASNCreate.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10065 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


