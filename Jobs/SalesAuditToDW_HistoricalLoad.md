# Job: SalesAuditToDW_HistoricalLoad

**Enabled:** Yes  
**Description:** Called at end of SalesAuditToDW

## Architecture Diagram

```mermaid
flowchart LR
    JOB["SalesAuditToDW_HistoricalLoad"]
    JOB --> Job_Start_Notice_1["Step 1: Job Start Notice [TSQL]"]`n    JOB --> Determine_Transactions_to_Pull_2["Step 2: Determine Transactions to Pull [TSQL]"]`n    JOB --> SalesAuditToDW_3["Step 3: SalesAuditToDW [SSIS]"]`n    JOB --> Send_Out_Balancing_Report_4["Step 4: Send Out Balancing Report [TSQL]"]`n    JOB --> Job_Completion_Notification_5["Step 5: Job Completion Notification [TSQL]"]`n```

## Steps

### Step 1: Job Start Notice
**Subsystem:** TSQL  

```sql
exec spEmailSQLAgentJobStart   @ProcessName = 'Sales Audit to Data Warehouse - Historical Load',   @SQLAgent = 'SalesAuditToDWStaging',  @Recipients = 'biadmin@buildabear.com'
```

### Step 2: Determine Transactions to Pull
**Subsystem:** TSQL  

```sql
-- Typical is 45 Days   EXEC bedrockdb01.auditworks.dbo.spDW_DetermineTransactionsToPull @numDaysHorizon = 45    
```

### Step 3: SalesAuditToDW
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\DW\SalesAuditToDWStaging\SalesAuditToDWStaging.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10119 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 4: Send Out Balancing Report
**Subsystem:** TSQL  

```sql
EXEC [stl-sql-p-04\sql2008r2].msdb.dbo.sp_start_job @job_name='D00A380C-4AF2-47F5-913C-C71EE8CF5925'
```

### Step 5: Job Completion Notification
**Subsystem:** TSQL  

```sql
exec spEmailSQLAgentJobCompletion   @ProcessName = 'Sales Audit to Data Warehouse - Historical Load',   @SQLAgent = 'SalesAuditToDW_HistoricalLoad',  @Recipients = 'biadmin@buildabear.com'
```


