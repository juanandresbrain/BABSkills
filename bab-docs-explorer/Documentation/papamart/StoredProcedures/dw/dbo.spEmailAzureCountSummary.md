# dbo.spEmailAzureCountSummary

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spEmailAzureCountSummary"]
    dbo_sp_send_dbmail(["dbo.sp_send_dbmail"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.sp_send_dbmail |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spEmailAzureCountSummary] 
@numCust INT,
@numTran INT,
@numDisc INT

as

set nocount on

declare 
	@subj varchar(52),
	@recip varchar(1000),
	@cc varchar(100),
	@body nvarchar(max),
	@priority varchar(6),
	@todaysDate varchar(20)

set @Subj = 'Azure pipeline daily count summary'
--set @recip = 'ianw@buildabear.com'
set @todaysDate = cast(GETDATE() as date)
SET @recip = 'ianw@buildabear.com;dant@buildabear.com;stevel@buildabear.com;jaimeb@buildabear.com'

select @priority = 'NORMAL'



select @body = 
'<font face =arial size = 2><B> </B><br>' +
+ ' <br> ' + ' Distinct count of transactions, discounts and customers added on ' + @todaysDate + ' <br> ' +
'</font>' +
	'<table border="1">' +
		'<tr><th><font face =arial size = 2>customer</font></th>' +
			'<th><font face =arial size = 2>transactions</font></th>' +
			'<th><font face =arial size = 2>discounts</font></th>' +
'<font face =arial size = 2>' +
    CAST ( ( SELECT td = @numCust,'',
                    td =@numTran, '',
					td = @numDisc, ''
              FOR XML PATH('tr'), TYPE 
    ) AS NVARCHAR(MAX) ) +
    '</font></table></font></p></p>
    <br><br>' +
    '<br>
    <font face =arial size = 1><B>This report was run from Azure BABBIADF01 data factory. </B></font>
    <br>
    <br>
<font face =arial size = 1><i>The information in this message may be privileged, “confidential” and protected from disclosure and/or intended only for the addressee(s) named above.  If the reader of this message is not the intended recipient, or an employee or agent responsible for delivering this message to the intended recipient, you are hereby notified that any dissemination, distribution or copying of the communication is strictly prohibited.  If you have received this communication in error, please notify us immediately by replying to the message and deleting it from your computer.  Thank you beary much.</i></font>'







		exec msdb.dbo.sp_send_dbmail
			@profile_name = 'BIAdmin',
			@recipients = @recip,
			@body = @body,
			@subject = @subj,
			@importance = @priority,
			@body_format = 'HTML'
```

