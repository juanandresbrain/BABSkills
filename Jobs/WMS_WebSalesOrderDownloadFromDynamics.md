# Job: WMS_WebSalesOrderDownloadFromDynamics

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WMS_WebSalesOrderDownloadFromDynamics"]
    JOB --> WMS_WebSalesOrderDownloadFromDynamics_1["Step 1: WMS_WebSalesOrderDownloadFromDynamics [SSIS]"]`n    JOB --> WMS_DuplicateWebOrderDetection_2["Step 2: WMS_DuplicateWebOrderDetection [SSIS]"]`n    JOB --> Run_SSRS_WMS_DuplicateWebOrderDetection_3["Step 3: Run SSRS WMS_DuplicateWebOrderDetection [TSQL]"]`n```

## Steps

### Step 1: WMS_WebSalesOrderDownloadFromDynamics
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WMS\WMS_WebSalesOrderDownloadFromDynamics\WMS_WebSalesOrderDownloadFromDynamics.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10079 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 2: WMS_DuplicateWebOrderDetection
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WMS\WMS_DuplicateWebOrderDetection\WMS_DuplicateWebOrderDetection.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10137 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 3: Run SSRS WMS_DuplicateWebOrderDetection
**Subsystem:** TSQL  

```sql
if (select count (*) from wms.DuplicateWebOrderDetection) > 0  Begin     exec [clb-sql-p-01].msdb.dbo.sp_start_job @JOB_name = 'B2F410BF-DA53-4F1F-802F-F0A60B112E4F'     End    else Print 'Nothing to See here'
```


