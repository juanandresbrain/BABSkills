# Job: SalesAuditToDW

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** Job will load sales into DW and will process the Cube (runs ProcessCubeMeasures SSIS as dw..transaction_facts is loaded)

## Architecture Diagram

```mermaid
flowchart LR
    JOB["SalesAuditToDW"]
    JOB --> Job_Start_Notice_1["Step 1: Job Start Notice [TSQL]"]`n    JOB --> SalesAuditToDWStaging_2["Step 2: SalesAuditToDWStaging [SSIS]"]`n    JOB --> Start_Job___AzureProcessing_TransactionFacts_3["Step 3: Start Job - AzureProcessing_TransactionFacts [TSQL]"]`n    JOB --> spPopulateBearDimFromTDF_4["Step 4: spPopulateBearDimFromTDF [TSQL]"]`n    JOB --> Send_out_Audit_Transaction_Daily_Check_Report_if_any_daily_summary_amount_is_0_5["Step 5: Send out Audit Transaction Daily Check Report if any daily summary amount is 0 [TSQL]"]`n    JOB --> DiscountResultsETL_6["Step 6: DiscountResultsETL [SSIS]"]`n    JOB --> Trigger_AW_Balancing_By_Day_Report_7["Step 7: Trigger AW Balancing By Day Report [TSQL]"]`n    JOB --> trigger_Azure_PostGres_DiscountFacts_8["Step 8: trigger Azure PostGres DiscountFacts [TSQL]"]`n    JOB --> Trigger_Historical_Load__Tues_Fri__9["Step 9: Trigger Historical Load (Tues-Fri) [TSQL]"]`n    JOB --> Job_Completion_Notice_10["Step 10: Job Completion Notice [TSQL]"]`n```

## Steps

### Step 1: Job Start Notice
**Subsystem:** TSQL  

```sql
exec spEmailSQLAgentJobStart   @ProcessName = 'Sales Audit to Data Warehouse - Daily Load',   @SQLAgent = 'SalesAuditToDWStaging',  @Recipients = 'biadmin@buildabear.com'
```

### Step 2: SalesAuditToDWStaging
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\DW\SalesAuditToDWStaging\SalesAuditToDWStaging.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10119 /Par "\"DaysToGoBack(Int32)\"";30 /Par "\"DaysToInclude(Int32)\"";30 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";3 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 3: Start Job - AzureProcessing_TransactionFacts
**Subsystem:** TSQL  

```sql
EXEC [stl-ssis-p-02].msdb.dbo.sp_start_job @job_name='AzureProcessing_TransactionFacts'
```

### Step 4: spPopulateBearDimFromTDF
**Subsystem:** TSQL  

```sql
EXEC PAPAMART.dw.[dbo].[spPopulateBearDimFromTDF]
```

### Step 5: Send out Audit Transaction Daily Check Report if any daily summary amount is 0
**Subsystem:** TSQL  

```sql
EXEC papamart.dwstaging.DW_Monitor.spAuditTransactionLoadStatus 60    DECLARE @EmptyRowCount INT  SELECT @EmptyRowCount = erc.EmptyRowCount  FROM (SELECT COUNT(*) AS EmptyRowCount FROM papamart.dwstaging.DW_Monitor.AuditTransactionLoadStatus WITH(NOLOCK) WHERE TransactionCount = 0   UNION SELECT COUNT(*) AS EmptyRowCount FROM papamart.dwstaging.DW_Monitor.AuditTransactionLoadStatus WITH(NOLOCK) WHERE TransactionDetailFactCount = 0   UNION SELECT COUNT(*) AS EmptyRowCount FROM papamart.dwstaging.DW_Monitor.AuditTransactionLoadStatus WITH(NOLOCK) WHERE TenderFactCount = 0   UNION SELECT COUNT(*) AS EmptyRowCount FROM papamart.dwstaging.DW_Monitor.AuditTransactionLoadStatus WITH(NOLOCK) WHERE DiscountFactCount = 0   UNION SELECT COUNT(*) AS EmptyRowCount FROM papamart.dwstaging.DW_Monitor.AuditTransactionLoadStatus WITH(NOLOCK) WHERE GiftcardActivatedCount = 0   UNION SELECT COUNT(*) AS EmptyRowCount FROM papamart.dwstaging.DW_Monitor.AuditTransactionLoadStatus WITH(NOLOCK) WHERE GiftcardRedeemedCount = 0  ) erc    IF @EmptyRowCount > 0 EXEC [stl-sql-p-04\sql2008R2].msdb.dbo.sp_start_job @job_name='13B2B3D0-D7E5-4D1A-A630-EA8D8A4CCF00'  
```

### Step 6: DiscountResultsETL
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\DW\DiscountResultsETL\DiscountResultsETL.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10123 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 7: Trigger AW Balancing By Day Report
**Subsystem:** TSQL  

```sql
EXEC [stl-sql-p-04\sql2008r2].msdb.dbo.sp_start_job @job_name='D00A380C-4AF2-47F5-913C-C71EE8CF5925'
```

### Step 8: trigger Azure PostGres DiscountFacts
**Subsystem:** TSQL  

```sql
EXEC sp_start_job @job_name='AzureProcessing_DiscountFacts'
```

### Step 9: Trigger Historical Load (Tues-Fri)
**Subsystem:** TSQL  

```sql
declare    @Day int    select    @Day=datepart(dw, getdate())    if @Day in (2,3,4,5,6) --Mon-Fri  and datepart(hh, getdate()) <8 --won't run after 8am     Begin    EXEC sp_start_job @job_name='SalesAuditToDW_HistoricalLoad'   end    
```

### Step 10: Job Completion Notice
**Subsystem:** TSQL  

```sql
exec spEmailSQLAgentJobCompletion   @ProcessName = 'Sales Audit to Data Warehouse',   @SQLAgent = 'SalesAuditToDWStaging',  @Recipients = 'biadmin@buildabear.com'
```


