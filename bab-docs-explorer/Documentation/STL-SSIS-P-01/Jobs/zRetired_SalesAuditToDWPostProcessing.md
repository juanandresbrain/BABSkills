# Job: zRetired_SalesAuditToDWPostProcessing

**Enabled:** No  
**Server:** STL-SSIS-P-01  
**Description:** Job is called from SalesAuditToDWStaging

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_SalesAuditToDWPostProcessing"]
    JOB --> spTransactionSummaryBuild_1["Step 1: spTransactionSummaryBuild [TSQL]"]`n    JOB --> spMetricsBuild_2["Step 2: spMetricsBuild [TSQL]"]`n    JOB --> spMetricFacts_DupeCheck_3["Step 3: spMetricFacts_DupeCheck [TSQL]"]`n    JOB --> spTransSummaryFacts_DupeCheck_4["Step 4: spTransSummaryFacts_DupeCheck [TSQL]"]`n    JOB --> spUpdate_Metric_Facts_5["Step 5: spUpdate_Metric_Facts [TSQL]"]`n    JOB --> Job_Completion_Notice_6["Step 6: Job Completion Notice [TSQL]"]`n```

## Steps

### Step 1: spTransactionSummaryBuild
**Subsystem:** TSQL  

```sql
DECLARE @startDate datetime  DECLARE @EndDate datetime    --SET @startDate = dbo.fnDateOnly(DATEADD(DAY, -15, GETDATE()))  --SET @EndDate = dbo.fnDateOnly(DATEADD(DAY, -1, GETDATE()))    --SET @startDate = '5/26/2013'  --SET @EndDate = '7/2/2013'      SELECT   @startDate = MIN(ath.Transaction_Date),   @EndDate = MAX(Transaction_Date)  FROM papamart.dwstaging.dbo.aw_Transaction_Header ath WITH (NOLOCK)    EXEC papamart.dw.dbo.spTransactionSummaryBuild   @startDate = @startDate,   @EndDate = @EndDate
```

### Step 2: spMetricsBuild
**Subsystem:** TSQL  

```sql
EXEC PAPAMART.dw.dbo.spMetricsBuild
```

### Step 3: spMetricFacts_DupeCheck
**Subsystem:** TSQL  

```sql
EXEC PAPAMART.dw.dbo.spMetricFacts_DupeCheck
```

### Step 4: spTransSummaryFacts_DupeCheck
**Subsystem:** TSQL  

```sql
EXEC PAPAMART.dw.dbo.spTransSummaryFacts_DupeCheck
```

### Step 5: spUpdate_Metric_Facts
**Subsystem:** TSQL  

```sql
--== Call the procedure for Updating LY values  --=================================================================*/  DECLARE @RCode int  DECLARE @StartDateLY datetime  DECLARE @EndDateLY datetime    Set @EndDateLY = (select CAST(CONVERT(char(8),dateadd(dd,45,getdate()),1) as datetime))  Set @StartDateLY = (select dateadd(dd, -90, @EndDateLY))    EXEC @RCode = PAPAMART.dw.dbo.spUpdate_Metric_Facts @StartDateLY, @EndDateLY    /*==========================================================================*/
```

### Step 6: Job Completion Notice
**Subsystem:** TSQL  

```sql
exec spEmailSQLAgentJobCompletion   @ProcessName = 'Sales Audit to Data Warehouse - Post-Processing',   @SQLAgent = 'SalesAuditToDWStagingPostProcessing',  @Recipients = 'biadmin@buildabear.com'
```


