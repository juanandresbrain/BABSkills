# Job: WebDemandTrackingETL

**Enabled:** Yes  
**Description:** Runs hourly to capture hourly files from \\stl-sftp-p-01\ecommerce\to-bab\from-Deck\PendingOrders\ for real-time / hourly web order demand tracking for Power BI.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WebDemandTrackingETL"]
    JOB --> WebDemandTrackingETL_1["Step 1: WebDemandTrackingETL [SSIS]"]`n```

## Steps

### Step 1: WebDemandTrackingETL
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WEB\WebDemandTrackingETL\WebDemandTrackingETL.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10139 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


