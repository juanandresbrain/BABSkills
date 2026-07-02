# Job: CRM_TransactionKeyStoryRanking

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** Job is not scheduled but is called from CRM_SalesForceDataExtensionExport

## Architecture Diagram

```mermaid
flowchart LR
    JOB["CRM_TransactionKeyStoryRanking"]
    JOB --> spCRMTransactionSequenceKeyStoryRanking_1["Step 1: spCRMTransactionSequenceKeyStoryRanking [TSQL]"]`n    JOB --> Start_Job___AzureProcessing_CRMTransactionKeyStoryRanking_2["Step 2: Start Job - AzureProcessing_CRMTransactionKeyStoryRanking [TSQL]"]`n    JOB --> Job_Completion_Notification_3["Step 3: Job Completion Notification [TSQL]"]`n```

## Steps

### Step 1: spCRMTransactionSequenceKeyStoryRanking
**Subsystem:** TSQL  

```sql
exec papamart.dwstaging.dbo.spCRMTransactionSequenceKeyStoryRanking @daystoGoBack=66  --need to add a step to process the table in azure
```

### Step 2: Start Job - AzureProcessing_CRMTransactionKeyStoryRanking
**Subsystem:** TSQL  

```sql
EXEC [stl-ssis-p-02].msdb.dbo.sp_start_job @job_name='AzureProcessing_CRMTransactionKeyStoryRanking'
```

### Step 3: Job Completion Notification
**Subsystem:** TSQL  

```sql
exec spEmailSQLAgentJobCompletion   @ProcessName = 'CRM Transaction KeyStory Ranking for Power BI',   @SQLAgent = 'CRM_TransactionKeyStoryRanking',  @Recipients = 'biadmin@buildabear.com'
```


