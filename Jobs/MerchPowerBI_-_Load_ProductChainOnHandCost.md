# Job: MerchPowerBI - Load ProductChainOnHandCost

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MerchPowerBI - Load ProductChainOnHandCost"]
    JOB --> Load_ProductChainOnHandCost_1["Step 1: Load ProductChainOnHandCost [TSQL]"]`n```

## Steps

### Step 1: Load ProductChainOnHandCost
**Subsystem:** TSQL  

```sql
EXEC papamart.msdb.dbo.sp_start_job @job_name='Load ProductChainOnHandCost'
```


