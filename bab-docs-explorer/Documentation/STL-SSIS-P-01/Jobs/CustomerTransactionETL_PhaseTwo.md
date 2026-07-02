# Job: CustomerTransactionETL_PhaseTwo

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["CustomerTransactionETL_PhaseTwo"]
    JOB --> CRMCustomerTransactionMetrics_1["Step 1: CRMCustomerTransactionMetrics [SSIS]"]`n    JOB --> Start_Job____CRM_UKcompareValidation_2["Step 2: Start Job -> CRM_UKcompareValidation [TSQL]"]`n    JOB --> Start_Job____CRM_SalesForceDataExtensionExport_3["Step 3: Start Job -> CRM_SalesForceDataExtensionExport [TSQL]"]`n    JOB --> CRM_BirthdayPartyExclusion_4["Step 4: CRM_BirthdayPartyExclusion [SSIS]"]`n    JOB --> JobCompletionNotice_5["Step 5: JobCompletionNotice [TSQL]"]`n```

## Steps

### Step 1: CRMCustomerTransactionMetrics
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\CRM\CRMCustomerTransactionMetrics___\CRMCustomerTransactionMetrics___.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10136 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 2: Start Job -> CRM_UKcompareValidation
**Subsystem:** TSQL  

```sql
EXEC sp_start_job @job_name='CRM_UKcompareValidation'
```

### Step 3: Start Job -> CRM_SalesForceDataExtensionExport
**Subsystem:** TSQL  

```sql
EXEC sp_start_job @job_name='CRM_SalesForceDataExtensionExport'
```

### Step 4: CRM_BirthdayPartyExclusion
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\CRM\PartyDailyBirthdayExclusions\PartyDailyBirthdayExclusions.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 5: JobCompletionNotice
**Subsystem:** TSQL  

```sql
exec spEmailSQLAgentJobCompletion   @ProcessName = 'CRM to DW Customer-Transaction ETL (phase two)',   @SQLAgent = 'CustomerTransactionETL_PhaseTwo',  @Recipients = 'biadmin@buildabear.com'
```


