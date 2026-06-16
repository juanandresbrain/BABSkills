# Job: zREtired_CRM_CustomerCreateFromWebSale

**Enabled:** No  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zREtired_CRM_CustomerCreateFromWebSale"]
    JOB --> CRM_CustomerCreateFromWebSale_1["Step 1: CRM_CustomerCreateFromWebSale [SSIS]"]`n```

## Steps

### Step 1: CRM_CustomerCreateFromWebSale
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\CRM\CRM_CustomerCreateFromWebSale\CRM_CustomerCreateFromWebSale.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10056 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


