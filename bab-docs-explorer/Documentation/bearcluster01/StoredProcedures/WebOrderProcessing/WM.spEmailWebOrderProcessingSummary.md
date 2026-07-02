# WM.spEmailWebOrderProcessingSummary

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["WM.spEmailWebOrderProcessingSummary"]
    dbo_sp_send_dbmail(["dbo.sp_send_dbmail"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.sp_send_dbmail |

## Stored Procedure Code

```sql
CREATE proc [WM].[spEmailWebOrderProcessingSummary]
	@WMCreated int,
	@WMShipped int,
	@UKCreated int,
	@UKShipped int

as 

-------------------------------
-- Dan Tweedie - 2017-12-04
-------------------------------



begin

	declare 
		@text nvarchar(max),
		@subj varchar(100),
		@recip varchar(1000)

	select @recip = 'webalerts@buildabear.com'
	--select @recip = 'WebAlerts@buildabear.com;TimC@buildabear.com'
	select @subj = 'Web Orders Summary: Created and Shipped Today'

	set @text = 
	'<font face =arial>' + 
	'US Orders Created in WM: ' + cast(@WMCreated as varchar) + '<br>' +
	'US Orders Shipped in WM ' + cast(@WMShipped as varchar) + '<br><br>' +
	'UK Orders Uploaded: ' + cast(@UKCreated as varchar) + '<br>' +
	'UK Orders Shipped: ' + cast(@UKShipped as varchar) +
	'</font>'


	exec msdb.dbo.sp_send_dbmail
	@profile_name = 'BIAdmin',
	@recipients = @recip,
	@body = @text,
	@subject = @subj,
	@body_format = 'HTML'
	
end


WM,spEmailWebOrdersNotInFileLog,CREATE proc [WM].[spEmailWebOrdersNotInFileLog]

as 

------------------------------------------------------------------------------------------------------------------------------------------------------------
-- Dan Tweedie - 2018-03-12 - Created proc, called from ssis
------------------------------------------------------------------------------------------------------------------------------------------------------------

set nocount on

declare @count int

select @count = count(*) from WM.OrdersNotInImportFileLog

If @count > 0

begin

	declare 
		@text nvarchar(max),
		@subj varchar(100),
		@recip varchar(1000)

	select @recip = 'WebAlerts@buildabear.com'
	select @subj = 'Web Orders NOT in XML File Import Log'

	set @text = '
	<font face =arial><H3>Orders From Deck Which are NOT in our XML File log. Do we have/need these??<br>Total Orders: ' + cast(@count as varchar) + '</H3>' +
		'<table border="1">' +
		'<tr>
		<th>OrderNumber</th>
		<th>OrderDateUTC</th>
		</tr>' +
		'<font face =arial size = 2>' +
		CAST ( ( SELECT td = OrderNumber,'',
						td = OrderDateUTC,''
				 from WM.OrdersNotInImportFileLog
				 order by OrderDateUTC, OrderNumber
				  FOR XML PATH('tr'), TYPE 
		) AS NVARCHAR(MAX) ) +
		'</font></table></font></p></p>
		<br>
		<br>
		<br>'


	exec msdb.dbo.sp_send_dbmail
	@profile_name = 'BIAdmin',
	@recipients = @recip,
	@body = @text,
	@subject = @subj,
	@body_format = 'HTML'
	

end
```

