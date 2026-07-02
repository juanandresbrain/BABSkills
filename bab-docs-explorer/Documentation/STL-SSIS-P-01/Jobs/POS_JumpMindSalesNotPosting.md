# Job: POS_JumpMindSalesNotPosting

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["POS_JumpMindSalesNotPosting"]
    JOB --> Sales_Not_Posting_To_Service_Bus_1["Step 1: Sales Not Posting To Service Bus [TSQL]"]`n    JOB --> SalesNotPostingToSalesAudit_2["Step 2: SalesNotPostingToSalesAudit [TSQL]"]`n    JOB --> Sales_Not_Posting_to_DW_JMC_Tables_3["Step 3: Sales Not Posting to DW JMC Tables [TSQL]"]`n```

## Steps

### Step 1: Sales Not Posting To Service Bus
**Subsystem:** TSQL  

```sql
declare    @Count int,   @Subj varchar(1000)    select @Count=count(*)  FROM papamart.[dw].[Azure].[vwPOSCompareJumpMindStageUnpublishedMessages]   where datediff(hh, InsertDate, getdate())>=4    if @Count > 0 and @Count <50    select @Subj = concat('JumpMind POS Sales are NOT Posting to Azure Service Bus. Count= ', cast(@Count as varchar) )    begin    exec msdb.dbo.sp_send_dbmail  @profile_name = 'biadmin',  @recipients = 'BIAdmin@buildabear.com;benb@buildabear.com;brandonh@buildabear.com;enjolia@buildabear.com;bradw@buildabear.com;juanp@buildabear.com',  @body = 'JumpMind POS Sales are NOT Posting to Azure Service Bus - Run papamart.dw.azure.[vwPOSCompareJumpMindStageUnpublishedMessages] to see this',  @subject = @Subj    end    if @Count >= 50  begin    exec msdb.dbo.sp_send_dbmail  @profile_name = 'biadmin',  @recipients = 'BIAdminTextAlert@buildabear.com;benb@buildabear.com;brandonh@buildabear.com;enjolia@buildabear.com;bradw@buildabear.com;juanp@buildabear.com;3143094521@txt.att.net',  @body = 'JumpMind POS Sales are NOT Posting to Azure Service Bus - Run papamart.dw.azure.[vwPOSCompareJumpMindStageUnpublishedMessages] to see this',  @subject = @Subj    end  
```

### Step 2: SalesNotPostingToSalesAudit
**Subsystem:** TSQL  

```sql
declare    @year int,    @period int,   @count int,   @bod varchar(max),   @subj varchar(max),   @email varchar(1000)    select    @year=fiscal_year,    @period=fiscal_period  from papamart.dw.dbo.date_dim dd where datediff(dd, actual_date, getdate())=0    select    @count=count(*)   from papamart.dw.azure.vwPOSCompareJumpMindStageToSalesAudit_V2 s    join papamart.dw.dbo.date_dim dd on cast(s.SalesAuditTransactionDate as date)=cast(dd.actual_date as date)    where      dd.fiscal_year=@year    and dd.fiscal_period=@period     and s.InsertDate <= dateadd(hh, -3, getdate())    and datediff(dd, s.InsertDate, getdate())<=3    select @bod='JumpMind POS Sales (' + cast(@count as varchar) + ' transactions) are NOT Posting to Sales Audit - Run the following to see this from papamart:  declare    @year int,    @period int,   @count int    select    @year=fiscal_year,    @period=fiscal_period  from papamart.dw.dbo.date_dim dd where datediff(dd, actual_date, getdate())=0    select    @count=count(*)   from papamart.dw.azure.vwPOSCompareJumpMindStageToSalesAudit_V2 s    join papamart.dw.dbo.date_dim dd on cast(s.SalesAuditTransactionDate as date)=cast(dd.actual_date as date)    where      dd.fiscal_year=@year    and dd.fiscal_period=@period     and s.InsertDate <= dateadd(hh, -3, getdate())  '    select @subj = 'JumpMind POS Sales (' + cast(@count as varchar) + ' transactions) are NOT Posting to Sales Audit'    if @count >0  begin    select @Email = case        when @Count>100         then 'BIAdminTextAlert@buildabear.com;benb@buildabear.com;brandonh@buildabear.com;enjolia@buildabear.com;bradw@buildabear.com;juanp@buildabear.com'       else 'BIAdmin@buildabear.com;benb@buildabear.com;brandonh@buildabear.com;enjolia@buildabear.com;bradw@buildabear.com;juanp@buildabear.com'      end    exec msdb.dbo.sp_send_dbmail  @profile_name = 'biadmin',  @recipients = @Email,  @body = @bod,  @subject = @subj    end
```

### Step 3: Sales Not Posting to DW JMC Tables
**Subsystem:** TSQL  

```sql
if datepart(hh, getdate()) > 4    Begin    if    (    select datediff(mi, max(InsertDate), getdate())    from  papamart.dw.dbo.JMC_sls_trans with (nolock)   )  >= 60    or    (                                      select datediff(mi, max(InsertDate), getdate())    from  papamart.dw.dbo.JMC_sls_retail_line_item with (nolock)   )  >=60    exec msdb.dbo.sp_send_dbmail  @profile_name = 'biadmin',  @recipients = 'BIAdminTextAlert@buildabear.com',  @body = 'JumpMind POS Sales are NOT Posting to Papamart JMC Reporting tables. It has been at least 1 hour since the last Insert.',  @subject = 'JumpMind POS Sales are NOT Posting to Papamart JMC Reporting tables'    End
```


