# Job: WEB - CouponExports

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WEB - CouponExports"]
    JOB --> Execute_SSIS_Package_1["Step 1: Execute SSIS Package [SSIS]"]`n```

## Steps

### Step 1: Execute SSIS Package
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\WebCoupons\ExportWebCouponsPackage.dtsx\"" /SERVER "\"STL-SSIS-P-01\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


