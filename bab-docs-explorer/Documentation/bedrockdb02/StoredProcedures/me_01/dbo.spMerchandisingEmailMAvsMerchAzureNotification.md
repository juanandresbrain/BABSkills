# dbo.spMerchandisingEmailMAvsMerchAzureNotification

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMerchandisingEmailMAvsMerchAzureNotification"]
    dbo_sp_send_dbmail(["dbo.sp_send_dbmail"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.sp_send_dbmail |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spMerchandisingEmailMAvsMerchAzureNotification] 
	
--========================================================================================================================
--	2020-09-30	Ian Wallace  - Created proc 
--========================================================================================================================

as

set nocount on

declare 
	@subj varchar(100),
	@recip varchar(1000),
	@cc varchar(100),
	@body nvarchar(max),
	@priority varchar(6)

set @Subj = 'Azure MA data to SilverDeltaLake process notification'
--set @recip = 'ianw@buildabear.com'
--set @recip = 'ianw@buildabear.com'
set @recip = 'BIadmin@buildabear.com;Jeffk@buildabear.com'
--@copy_recipients = 'ianw@buildabear.com'
select @priority = 'Normal'

select @body = 
'MA data extracts to SilverDeltaLake have completed. <br> ' +
    '<br><br>' +
    '<br>
    <font face =arial size = 1><B>This report was run from Azure Synapse pi_ma_weekly_views_master pipeline</B></font>
    <br>
    <br>
<font face =arial size = 1><i>The information in this message may be privileged, “confidential” and protected from disclosure and/or intended only for the addressee(s) named above. ' +
'If the reader of this message is not the intended recipient, or an employee or agent responsible for delivering this message to the intended recipient, ' +
'you are hereby notified that any dissemination, distribution or copying of the communication is strictly prohibited.  If you have received this communication in error, ' + 
'please notify us immediately by replying to the message and deleting it from your computer.  Thank you beary much.</i></font>'


		exec msdb.dbo.sp_send_dbmail
			@profile_name = 'MerchAdmin',
			@recipients = @recip,
			@body = @body,
			@subject = @subj,
			@importance = @priority,
			@body_format = 'HTML'
```

