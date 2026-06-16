# Job: zRetired_CoSell Analysis Data Driven Subscription Check

**Enabled:** No  
**Description:** This was migrated from [STL-SQL-P-04\SQL2008R2]

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_CoSell Analysis Data Driven Subscription Check"]
    JOB --> Step_One_1["Step 1: Step One [TSQL]"]`n```

## Steps

### Step 1: Step One
**Subsystem:** TSQL  

```sql
/********** Configuration Section START  **************/  /********** Configuration Section START  **************/  /********** Configuration Section START  **************/  DECLARE @ExecDate AS INT   , @EmailRecipients AS VARCHAR(255)   , @EmailCopyRecipients AS VARCHAR(500)   , @EmailSubject AS VARCHAR(255)   , @EmailMessageBody AS VARCHAR(1000)   , @EmailBodyFormat AS VARCHAR(10)   , @EmailImportance AS VARCHAR(10)   , @JobID AS UNIQUEIDENTIFIER   , @ProcessStatus AS VARCHAR(20)   , @EmailProfile AS VARCHAR(20)    SET @ExecDate = YEAR(GETDATE()) * 10000 + MONTH(GETDATE()) * 100 + DAY(GETDATE())  SET @EmailRecipients ='KateH@buildabear.com;ChadV@buildabear.com;JennK@buildabear.com;LaceyM@buildabear.com;AnnG@buildabear.com'  SET @EmailCopyRecipients = 'BIAdmin@buildabear.com'  SET @EmailSubject = 'CoSell Analysis Reports Generation Status'  SET @EmailBodyFormat = 'HTML'  SET @JobID = '9698CABD-1B5C-421A-97EF-655808FAA13F'  SET @EmailImportance = 'Normal'  SET @EmailProfile = 'BIAdmin'  ;  --/*******************  Debugging  *****************/  --/*******************  Debugging  *****************/  --/*******************  Debugging  *****************/  --SET @ExecDate = 20141127  --SET @EmailRecipients ='kevinsh@buildabear.com'  --SET @EmailCopyRecipients = ''  --SET @EmailImportance = 'Normal'  --/*******************  Debugging  *****************/  --/*******************  Debugging  *****************/  --/*******************  Debugging  *****************/    -- Check data driven subscription status  SELECT @ProcessStatus = CASE        WHEN subs.LastStatus LIKE '%0 errors%'         THEN 'Success'        ELSE 'Failed'       END   --, subs.LastStatus   --, subs.LastRunTime   --, c.Name AS ReportName   --, c.[Path] AS ReportPath   --, sch.ScheduleID AS SQLAgent_Job_Name  FROM [STL-SQL-P-04\SQL2008R2].ReportServer_birpt01.dbo.Schedule sch WITH(NOLOCK)   INNER JOIN [STL-SQL-P-04\SQL2008R2].ReportServer_birpt01.dbo.ReportSchedule rsch WITH(NOLOCK)    ON rsch.ScheduleID = sch.ScheduleID    INNER JOIN [STL-SQL-P-04\SQL2008R2].ReportServer_birpt01.dbo.Subscriptions subs WITH(NOLOCK)    ON rsch.SubscriptionID = subs.SubscriptionID    INNER JOIN [STL-SQL-P-04\SQL2008R2].ReportServer_birpt01.dbo.[Catalog] c WITH (NOLOCK)    ON subs.Report_OID = c.ItemID   WHERE sch.ScheduleID = @JobID   AND ((YEAR(subs.LastRunTime) * 10000) + (MONTH(subs.LastRunTime) * 100) + DAY(subs.LastRunTime)) = @ExecDate    -- if report job hasn't run on the checking date and time, report it as failed  IF @ProcessStatus IS NULL SET @ProcessStatus = 'Failed'  IF @ProcessStatus = 'Failed' SET @EmailImportance = 'High'    SET @EmailMessageBody = 'Process Status: ' + @ProcessStatus       + '<br><br>Report Location: <a href="\\sharebear1\groups\Planning\StyleSummaryReports\CoSellAnalysis">\\sharebear1\groups\Planning\StyleSummaryReports\CoSellAnalysis</a>'        + '<br><br>Current Date and Time: ' + CAST(GETDATE() AS VARCHAR(50))    EXEC msdb.dbo.sp_send_dbmail    @recipients = @EmailRecipients   ,@copy_recipients = @EmailCopyRecipients   , @subject = @EmailSubject   , @body = @EmailMessageBody   , @body_format = @EmailBodyFormat    , @importance = @EmailImportance   , @profile_name = @EmailProfile
```


