# Job: MERCHANDISING - Report - Unselected Web Orders by Order Type

**Enabled:** No  
**Server:** bedrockdb02  
**Description:** E-mails a Summary\Count of Web Picktickets by Order type, three times a day.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Report - Unselected Web Orders by Order Type"]
    JOB --> Uno___Select_Counts_1["Step 1: Uno - Select Counts [TSQL]"]`n    JOB --> Dos___Email_Count_Summary_2["Step 2: Dos - Email Count Summary [TSQL]"]`n```

## Steps

### Step 1: Uno - Select Counts
**Subsystem:** TSQL  

```sql
exec wmdb01.wmprod.dbo.sp_SelectPktCountsByOrderType
```

### Step 2: Dos - Email Count Summary
**Subsystem:** TSQL  

```sql
if (select count(*) from wmdb01.wmprod.dbo.WebOrdersByOrderType) > 0


Begin

Declare @BODY3 nvarchar(4000);

	set @BODY3 = '<font face = arial size = 2>' + 
			'Below you will find the number of picktickets by order type that are in UNSELECTED status in WM.'+
			'<br>'+
			'<br>'+
			'<br>'+
			'<br>'+		
			'<br>'+
			'<br>'+
				'<table border="1">' +
				'<tr><th>Order_Type</th><th>Number_of_PickTickets</th></tr>' +
				CAST ( ( select td = isnull(m.Order_Type, ''), '',
						td = isnull(m.Number_of_PickTickets, ''),''
						  from wmdb01.wmprod.dbo.WebOrdersByOrderType m
						  FOR XML PATH('tr'), TYPE 
				) AS NVARCHAR(4000) ) +
				'</font></table></font></p></p>
				<br>
				<br>
				<br>'
	

		EXEC bedrockdb02.msdb.dbo.sp_send_dbmail
			@recipients = 'ChrisTh@buildabear.com;WilliamD@buildabear.com;BellaT@buildabear.com;ChristinaL@buildabear.com;ShaunS@buildabear.com;LarryW@buildabear.com', 
			@copy_recipients = 'MerchAdmin@buildabear.com', -- Likely will omit after a few weeks of go live 
			@subject = 'Number of Unselected Web Picktickets By Order Type',
			@body = @BODY3,
			@profile_name = 'MerchAdmin',
			@body_format= HTML

End

if (select count(*) from wmdb01.wmprod.dbo.WebOrdersByOrderType) = 0

Begin


		EXEC bedrockdb02.msdb.dbo.sp_send_dbmail
			@recipients = 'ChrisTh@buildabear.com;WilliamD@buildabear.com;BellaT@buildabear.com;ChristinaL@buildabear.com;ShaunS@buildabear.com;LarryW@buildabear.com', 
			@copy_recipients = 'MerchAdmin@buildabear.com', -- Likely will omit after a few weeks of go live 
			@subject = 'Number of Unselected Web Picktickets By Order Type',
			@body = 'There are currently zero Web Picktickets in Unselected Status in WM',
			@profile_name = 'MerchAdmin',
			@body_format= HTML

End 



```


