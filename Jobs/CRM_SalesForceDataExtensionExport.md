# Job: CRM_SalesForceDataExtensionExport

**Enabled:** Yes  
**Description:** Job is disabled and called from CustomerTransactionETL

## Architecture Diagram

```mermaid
flowchart LR
    JOB["CRM_SalesForceDataExtensionExport"]
    JOB --> data_extension_file_exports_1["Step 1: data extension file exports [SSIS]"]`n    JOB --> EmailFactRevCalc_2["Step 2: EmailFactRevCalc [SSIS]"]`n    JOB --> Start_Job_CRM_TransactionKeyStoryRanking_3["Step 3: Start Job CRM_TransactionKeyStoryRanking [TSQL]"]`n    JOB --> Wait_4["Step 4: Wait [TSQL]"]`n    JOB --> Start_Job___AzureProcessing_CRMCustomerMasterData_5["Step 5: Start Job - AzureProcessing_CRMCustomerMasterData [TSQL]"]`n    JOB --> Job_Completion_Notice_6["Step 6: Job Completion Notice [TSQL]"]`n```

## Steps

### Step 1: data extension file exports
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\CRM\CRMSalesForceDataExtensionFileCreate\CRMSalesForceDataExtensionFileCreate.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /Par "\"SMTP_SmtpServer\"";"\"exstlhyb.buildabear.com\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 2: EmailFactRevCalc
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\CRM\EmailFactRevCalc\EmailFactRevCalc.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 3: Start Job CRM_TransactionKeyStoryRanking
**Subsystem:** TSQL  

```sql
EXEC sp_start_job @job_name='CRM_TransactionKeyStoryRanking'
```

### Step 4: Wait
**Subsystem:** TSQL  

```sql
waitfor delay '00:30:00' --wait to allow for CRMTransactionKeyStoryRanking to finish
```

### Step 5: Start Job - AzureProcessing_CRMCustomerMasterData
**Subsystem:** TSQL  

```sql
EXEC [stl-ssis-p-02].msdb.dbo.sp_start_job @job_name='AzureProcessing_CRMCustomerMasterData'
```

### Step 6: Job Completion Notice
**Subsystem:** TSQL  

```sql
exec spEmailSQLAgentJobCompletion   @ProcessName = 'CRM to DW Customer ETL (phase three), Master Data Extensions + Email Recalcs',   @SQLAgent = 'CRM_SalesForceDataExtensionReport',  @Recipients = 'biadmin@buildabear.com'
```


