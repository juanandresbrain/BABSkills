# Job: MERCHANDISING -  Validation - AutoRerun

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Re runs sales posting Job and Validations upon Problem Email from either validation IB to MA

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING -  Validation - AutoRerun"]
    JOB --> Pipeline_Sales_Posting_1["Step 1: Pipeline Sales Posting [TSQL]"]`n    JOB --> Wait_for_30_min_for_pipeline_sales_posting_to_complete_2["Step 2: Wait for 30 min for pipeline sales posting to complete [TSQL]"]`n    JOB --> IB_to_MA_validation_3["Step 3: IB to MA validation [TSQL]"]`n```

## Steps

### Step 1: Pipeline Sales Posting
**Subsystem:** TSQL  

```sql
EXEC msdb.dbo.sp_start_job @job_name = 'MERCHANDISING - Process - Pipeline Sales Posting';
```

### Step 2: Wait for 30 min for pipeline sales posting to complete
**Subsystem:** TSQL  

```sql
WAITFOR DELAY '00:30:00'; -- Wait for 30 min
```

### Step 3: IB to MA validation
**Subsystem:** TSQL  

```sql
EXEC [bedrockdb02].msdb.dbo.sp_start_job @job_name = 'MERCHANDISING - Report - InfoBase-MerchantviewDailyVerification_CA';
```


