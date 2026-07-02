# Job: zRetired - DISTRO EXPORT - DYNAMICS AND MERCH

**Enabled:** No  
**Server:** bedrockdb02  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired - DISTRO EXPORT - DYNAMICS AND MERCH"]
    JOB --> STL_SSIS_P_01____ERP_TransfersAndSalesOrderDistros_1["Step 1: STL-SSIS-P-01 -- ERP_TransfersAndSalesOrderDistros [TSQL]"]`n```

## Steps

### Step 1: STL-SSIS-P-01 -- ERP_TransfersAndSalesOrderDistros
**Subsystem:** TSQL  

```sql
EXEC [STL-SSIS-P-01].msdb.dbo.sp_start_job @job_name='ERP_TransfersAndSalesOrderDistros'
```


