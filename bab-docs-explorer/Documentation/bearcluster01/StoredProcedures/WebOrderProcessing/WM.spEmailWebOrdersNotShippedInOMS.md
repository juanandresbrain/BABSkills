# WM.spEmailWebOrdersNotShippedInOMS

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["WM.spEmailWebOrdersNotShippedInOMS"]
    dbo_sp_send_dbmail(["dbo.sp_send_dbmail"]) --> SP
    WM_OrdersNotShippedInOMS(["WM.OrdersNotShippedInOMS"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.sp_send_dbmail |
| WM.OrdersNotShippedInOMS |

## Stored Procedure Code

```sql
CREATE proc [WM].[spEmailWebOrdersNotShippedInOMS]

as 

------------------------------------------------------------------------------------------------------------------------------------------------------------
-- Dan Tweedie - 2017-09-14 - Runs at end of SSIS package WebIntegrationValidations, which stages Orders shipped in WM but not in OMS etl tables
--							- Send Email to WebAlerts
------------------------------------------------------------------------------------------------------------------------------------------------------------

set nocount on

declare @count int

select @count = count(*) from WM.OrdersNotShippedInOMS

if @count > 0

begin

	declare 
		@text nvarchar(max),
		@subj varchar(100),
		@recip varchar(1000)
		

	select @recip = 'WebAlerts@buildabear.com'
	select @subj = 'Web Orders NOT SHIPPED in OMS'

	set @text = '
	<font face =arial><H3>US Web Orders Which Are Shipped in WM but NOT in OMS. <br>Total Orders: ' + cast(@count as varchar) + '</H3>' +
		'<table border="1">' +
		'<tr>
		<th>OrderNumber</th>
		<th>ShipDate</th>
		<th>ErrorMessage</th>
		<th>LogDateTime</th>
		<th>Logged Attempts</th>
		</tr>' +
		'<font face =arial size = 2>' +
		CAST ( ( SELECT td = OrderNum,'',
						td = ShipDate, '',
						td = isnull(ErrorMessage, 'n/a'), '',
						td = isnull(LogDateTime, cast(cast(ShipDate as date) as datetime)), '',
						td = isnull(Attempts, 0), ''
				 from WM.OrdersNotShippedInOMS
				 order by ShipDate, OrderNum
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

