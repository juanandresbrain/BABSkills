# Job: SalesAuditToDW PreStageTrigger

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["SalesAuditToDW PreStageTrigger"]
    JOB --> StoreSalesCheck_1["Step 1: StoreSalesCheck [SSIS]"]`n    JOB --> Check_for_StoreSalesCheck_Variances___Fail_Job_if_Conditions_Found_2["Step 2: Check for StoreSalesCheck Variances - Fail Job if Conditions Found [TSQL]"]`n    JOB --> SQL___DW___spPOSNotifyLoadStart_3["Step 3: SQL - DW - spPOSNotifyLoadStart [TSQL]"]`n    JOB --> SQL___AW___pUpdateStatisticsForVATLoad_4["Step 4: SQL - AW - pUpdateStatisticsForVATLoad [TSQL]"]`n    JOB --> SQL___AW___spDW_DetermineTransactionsToPull_5["Step 5: SQL - AW - spDW_DetermineTransactionsToPull [TSQL]"]`n    JOB --> SQL___DW___usp_FlashGAAPSales_6["Step 6: SQL - DW - usp_FlashGAAPSales [TSQL]"]`n    JOB --> spStoreSalesCheck_EmailAlerts_NotifyBusiness_7["Step 7: spStoreSalesCheck_EmailAlerts_NotifyBusiness [TSQL]"]`n    JOB --> SQL_Agent_Job___SalesAuditToDW_8["Step 8: SQL Agent Job - SalesAuditToDW [TSQL]"]`n```

## Steps

### Step 1: StoreSalesCheck
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\DW\StoreSalesCheck\StoreSalesCheck.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10099 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 2: Check for StoreSalesCheck Variances - Fail Job if Conditions Found
**Subsystem:** TSQL  

```sql
---FIRST TRY    exec bedrockdb01.auditworks.dbo.spStoresNoSalesDMT @DaysBack = 1    declare    @zero int,   @TriggerCount int    select @zero=case when count(*) >= 20 then 1 else 0 end    from bedrockdb01.auditworks.dbo.tmpStoresZeroSalesDMT    select @TriggerCount = count(*) + @zero   from IntegrationStaging.dbo.vwStoreSalesCheck_FinalStats  where    StoreCount>=20  or WebStoresMissing25Pct>1  or NonWebStoresMissing25Pct>=10  --or PercentPosted <=60      if @TriggerCount>0   begin    waitfor delay '00:15:00'    EXEC sp_start_job @job_name='StoreSalesCheck'    waitfor delay '00:10:00'      --SECOND TRY    exec bedrockdb01.auditworks.dbo.spStoresNoSalesDMT @DaysBack = 1        select @zero=case when count(*) >= 20 then 1 else 0 end      from bedrockdb01.auditworks.dbo.tmpStoresZeroSalesDMT        select @TriggerCount = count(*) + @zero    from IntegrationStaging.dbo.vwStoreSalesCheck_FinalStats    where      StoreCount>=20    or WebStoresMissing25Pct>1    or NonWebStoresMissing25Pct>=10    --or PercentPosted <=60      if @TriggerCount>0     begin      waitfor delay '00:15:00'      EXEC sp_start_job @job_name='StoreSalesCheck'      waitfor delay '00:10:00'        --THIRD TRY      exec bedrockdb01.auditworks.dbo.spStoresNoSalesDMT @DaysBack = 1          select @zero=case when count(*) >= 20 then 1 else 0 end        from bedrockdb01.auditworks.dbo.tmpStoresZeroSalesDMT          select @TriggerCount = count(*) + @zero      from IntegrationStaging.dbo.vwStoreSalesCheck_FinalStats      where        StoreCount>=20      or WebStoresMissing25Pct>1      or NonWebStoresMissing25Pct>=10      --or PercentPosted <=60        if @TriggerCount>0       begin        RAISERROR ('StoreSalesCheck Trigger Count > 0 -- Run StoreSalesCheck and Try Again - ', 18,1);        end     end   end  
```

### Step 3: SQL - DW - spPOSNotifyLoadStart
**Subsystem:** TSQL  

```sql
exec PAPAMART.dw.dbo.spPOSNotifyLoadStart
```

### Step 4: SQL - AW - pUpdateStatisticsForVATLoad
**Subsystem:** TSQL  

```sql
exec bedrockdb01.auditworks.dbo.spUpdateStatisticsForVATLoad
```

### Step 5: SQL - AW - spDW_DetermineTransactionsToPull
**Subsystem:** TSQL  

```sql
declare    @Day int,    @DayRun int    select    @Day=datepart(dw, getdate()),   @DayRun=case when @Day in (7) then 1 when @Day in (1) then 2 when @Day in (2) then 3 else 1 end    EXEC bedrockdb01.auditworks.dbo.spDW_DetermineTransactionsToPull @numDaysHorizon =@DayRun
```

### Step 6: SQL - DW - usp_FlashGAAPSales
**Subsystem:** TSQL  

```sql
exec PAPAMART.dw.dbo.usp_FlashGAAPSales
```

### Step 7: spStoreSalesCheck_EmailAlerts_NotifyBusiness
**Subsystem:** TSQL  

```sql
exec spStoreSalesCheck_EmailAlerts_NotifyBusiness
```

### Step 8: SQL Agent Job - SalesAuditToDW
**Subsystem:** TSQL  

```sql
EXEC sp_start_job @job_name='SalesAuditToDW'
```


