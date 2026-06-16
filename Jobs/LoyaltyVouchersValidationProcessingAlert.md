# Job: LoyaltyVouchersValidationProcessingAlert

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["LoyaltyVouchersValidationProcessingAlert"]
    JOB --> Check_for_Today_and_Send_Alert_1["Step 1: Check for Today and Send Alert [TSQL]"]`n```

## Steps

### Step 1: Check for Today and Send Alert
**Subsystem:** TSQL  

```sql
select    cast(InsertDate as date) InsertDate,   datepart(hh, InsertDate) InsertHour,   count(distinct SerializedNumber) as DailyCount  into #DailyCount  from papamart.dw.dbo.SerializedVoucher  where datediff(dd, InsertDate, getdate())<=7  and title = 'RWD'  group by cast(InsertDate as date),datepart(hh, InsertDate)    declare    @7DayAvg int,   @Today int,   @Tolerance int,   @Bod nvarchar(max)    select @7DayAvg=avg(DailyCount)   from #DailyCount  where InsertDate<cast(getdate() as date)  and InsertHour<= datepart(hh, getdate())    select @Today=sum(DailyCount)  from #DailyCount   where InsertDate=cast(getdate() as date)    select @Tolerance=@7DayAvg * .25    if (@Today<@Tolerance)    begin    select @Bod = 'We have processded ' + cast(@Today as varchar) + ' vouchers today, while our 7 day average ( by this hour ) is ' + cast(@7DayAvg as varchar) + '. Please investigate and confirm there is not a data processing issue.'      EXEC msdb.dbo.sp_send_dbmail    @profile_name = 'BIAdmin',    @recipients ='BIAdminTextAlert@buildabear.com;3146072459@txt.att.net;6513732147@vtext.com;stevel@buildabear.com;jaimeb@builabear.com',    @subject= 'Salesforce Vouchers May Not Be Staging to Azure. Please Investigate and Confirm',    @body = @Bod     --3146072459@txt.att.net --ATT  --Steve Legrand    --6513732147@vtext.com --VERIZON --Jamie Barth   end
```


