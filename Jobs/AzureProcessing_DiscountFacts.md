# Job: AzureProcessing_DiscountFacts

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["AzureProcessing_DiscountFacts"]
    JOB --> run_1["Step 1: run [TSQL]"]`n```

## Steps

### Step 1: run
**Subsystem:** TSQL  

```sql
EXEC [stl-ssis-p-02].msdb.dbo.sp_start_job @job_name='AzureProcessing_DiscountFacts'
```


