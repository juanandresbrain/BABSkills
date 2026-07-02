# Job: zRetired_StoreForcePosSalesExport_Every30Minutes

**Enabled:** No  
**Server:** STL-SSIS-P-01  
**Description:** When setting DaysToGoBack and DaysToInclude, if you are only needing today, set both to 0. This job uses this config.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_StoreForcePosSalesExport_Every30Minutes"]
    JOB --> Stop_Daily_Job_if_Running_1["Step 1: Stop Daily Job if Running [TSQL]"]`n    JOB --> HR_StoreForcePosSalesExtractSSIS_2["Step 2: HR_StoreForcePosSalesExtractSSIS [SSIS]"]`n    JOB --> Start_Job___FlashGaapSales_3["Step 3: Start Job - FlashGaapSales [TSQL]"]`n    JOB --> Start_Job___HangingSQLConnectionCheck_MasterController_4["Step 4: Start Job - HangingSQLConnectionCheck_MasterController [TSQL]"]`n    JOB --> Job_Completion_Notification_5["Step 5: Job Completion Notification [TSQL]"]`n```

## Steps

### Step 1: Stop Daily Job if Running
**Subsystem:** TSQL  

```sql
declare @run int  select @run = 1    exec spSQLAGentStopLongRunningJob   @Job= 'StoreForcePosSalesExport_OncePerDay',   @Runtime = @run,   @Rec = 'dant@buildabear.com'
```

### Step 2: HR_StoreForcePosSalesExtractSSIS
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\StoreForce\HR_StoreForcePosSalesExtract\HR_StoreForcePosSalesExtract.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10041 /Par "\"DaysToGoBack(Int32)\"";0 /Par "\"DaysToInclude(Int32)\"";0 /Par StoreForcePOSSalesExtractRunType;NormalRun /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 3: Start Job - FlashGaapSales
**Subsystem:** TSQL  

```sql
if (select datepart(mi, getdate()) ) < 19 --only runs when the Storeforce job runs at the top of the hour, not when it runs at :20 past  or (select datepart(mi, getdate()) ) > 50  begin   EXEC kermode.msdb.dbo.sp_start_job @job_name='FlashGaapSalesByHour'  end
```

### Step 4: Start Job - HangingSQLConnectionCheck_MasterController
**Subsystem:** TSQL  

```sql
if datepart(mi, getdate()) between 16 and 35 or datepart(mi, getdate()) >=46  or datepart(mi, getdate()) <= 5     EXEC msdb.dbo.sp_start_job @job_name='HangingSQLConnectionCheck_MasterController'
```

### Step 5: Job Completion Notification
**Subsystem:** TSQL  

```sql
declare   @US numeric(30,2),   @UK numeric(30,2),   @Date datetime  select    @UK=sum(case when isnull(StoreCode,0)>=2000 then isnull(SaleValue,0) else 0 end) ,   @US=sum(case when isnull(StoreCode,0)<2000 then isnull(SaleValue,0) else 0 end) ,   @Date=max(UpdateDate)  from papamart.dw.dbo.HR_StoreForcePosSalesFact with (nolock)  where (datepart(hh, getdate())>=2 and datediff(dd, DateRaw, getdate())=0)  or (datepart(hh, getdate())<2 and datediff(dd, DateRaw, getdate()-1)=0)    declare   @Statement varchar(4000),   @subj varchar(1000)    select @subj='Process Completion Notice -- Storeforce - Last Updated - ' + cast(@Date as varchar)     select    @Statement = '   <font face=arial size=2> '  +   'The Storeforce Process Has Completed.' +      '<br><br><b>Last Update:</b> ' + cast(@Date as varchar) +    '<br><b>US Sales:</b> ' + cast(@US as varchar) +    '<br><b>UK Sales:</b> ' + cast(@UK as varchar) +       '</font>'            exec msdb.dbo.sp_send_dbmail   @profile_name = 'BIAdmin',      @recipients = 'BIAdmin@buildabear.com',      @body = @Statement,   @subject =@subj ,   @body_format = 'HTML'
```


