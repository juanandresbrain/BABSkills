# dbo.spMissingTransQtyAlertBACK20240216

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMissingTransQtyAlertBACK20240216"]
    audit_status(["audit_status"]) --> SP
    notification_history(["notification_history"]) --> SP
    dbo_sp_send_dbmail(["dbo.sp_send_dbmail"]) --> SP
    transaction_missing(["transaction_missing"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| audit_status |
| notification_history |
| dbo.sp_send_dbmail |
| transaction_missing |

## Stored Procedure Code

```sql
--DROP PROC [dbo].[spMissingTransQtyAlert]
--GO

create PROC [dbo].[spMissingTransQtyAlertBACK20240216]
-- =============================================================================================================
-- Name: [dbo].[spMissingTransQtyAlert]
--
-- Description:	Sends email and text alert if there are too many Missing Transactions in Sales Audit
--
-- Input:	@filelocation	varchar(100)	path to drop files
--			@rowcount		int				total number of records to process
--
-- Output: N/A
--
-- Dependencies: 
--
-- Revision History
--		Name:			Date:			Comments:
--		Paul Beckman	02/23/2015		Created SP
--		Paul Beckman	07/27/2015		Updated from POSDBSSA to BEDROCKDB01
--		Paul Beckman	08/31/2016		Updated profile_name from 'POSadmin' to 'SAAdmin'
--		Paul Beckman	01/17/2017		Updated Alert email body to HTML
--		Paul Beckman	02/17/2017		Changed @alertrecipients from POSAlert to SAAlert
--		Paul Beckman	02/13/2018		Removed old non-HTML code for email body
--		Paul Beckman	10/17/2019		Updated to use notification_history table
--		Paul Beckman	01/02/2020		Changed SAAlert@buildabear.com to EnterpriseSystemsAlerts@buildabear.com
--		Paul Beckman	02/05/2020		Updated email profile to 'EntSysSupport'
--
-- exec spMissingTransQtyAlert
-- =============================================================================================================
AS

declare @sql varchar(8000)
declare @recipients varchar(4000)
declare @alertrecipients varchar(4000)
declare @Subject varchar(60)
declare @query varchar(8000)
declare @copy_recipients varchar(8000)
declare @text nvarchar(max)

--set @recipients = 'posadmin@buildabear.com'
--set @recipients = 'poll@buildabear.com;POSAlert@buildabear.com'
--set @alertrecipients = 'poll@buildabear.com;EntSysSupport@buildabear.com' --temp exclude EnterpriseSystemsAlerts@buildabear.com LT 11/29/22
set @alertrecipients = 'EnterpriseSystemsAlerts@buildabear.com;EntSysSupport@buildabear.com;BIAdmin@buildabear.com;benb@buildabear.com;brandonh@buildabear.com;enjolia@buildabear.com;bradw@buildabear.com;juanp@buildabear.com'
--set @copy_recipients = 'paulb@buildabear.com'

IF (Object_ID('tempdb..##misstransqty') IS NOT NULL) DROP TABLE ##misstransqty
SELECT CONVERT (VARCHAR(5),audit_status.store_no) AS Store,CONVERT (VARCHAR(3),audit_status.register_no) AS WS,CONVERT(VARCHAR(11), audit_status.sales_date, 101) AS Sales_Date,CONVERT (VARCHAR(14),from_transaction_no) AS from_Trans_No,CONVERT (VARCHAR(12),to_transaction_no) AS to_Trans_No,CONVERT (VARCHAR(7),(to_transaction_no+1) - from_transaction_no) AS Total_Trans
INTO ##misstransqty
FROM audit_status,transaction_missing
WHERE audit_status.missing_qty > 0
AND audit_status.missing_qty < 20000
AND verified = 0
and sa_reject_qty = 0
and if_reject_qty = 0
and audit_status.register_no not in (21,22,23,24,1000)
AND audit_status.store_no = transaction_missing.store_no
AND audit_status.register_no = transaction_missing.register_no
AND audit_status.sales_date = transaction_missing.sales_date
ORDER BY audit_status.store_no

if (select count(*) from ##misstransqty) > 50
begin 
	set @text = 
				'<font face =arial size = 2 color="Red">' +
				'There are too many missing Transactions from Sales Audit.  This could be due to a failed import batch.<br>' +
				'<br>' +
				'<table border="1">' + 
				'<font face =arial size = 2>' +
				'<tr bgcolor=#D5D5F7><th>Store</th><th>Wksn</th><th>Sales Date</th><th>from Trans No</th><th>to Trans No</th><th>Total Trans</th></tr>' +
				CAST ( ( SELECT [td/@align]='center',
								td = Store, '',
								[td/@align]='center',
								td = WS, '',
								td = Sales_Date, '',
								td = from_Trans_No, '',
								td = to_Trans_No, '',
								td = Total_Trans, ''
					  FROM ##misstransqty
					  FOR xml path ('tr'), type
				) AS NVARCHAR(MAX) ) +
				'</table>' +
				'<br>' +
				'Please take action to resolve this issue.  Aptos may need to be involved.<br>' +
				'<font face =arial size = 1 color="#C0C0C0">' +
				'<br><br><br><br>' +
				'Server:  BEDROCKDB01 <br>' +
				'Job Name:  MissingTransQtyAlert <br>' +
				'Stored Proc:  BEDROCKDB01.auditworks.dbo.spMissingTransQtyAlert <br>' +
				'Created by:  Paul Beckman <br>' +
				'Team Ownership:  Enterprise Systems <br>'

set @Subject = 'WARNING - Too many Missing Transactions in SA'
	exec msdb.dbo.sp_send_dbmail  
		@profile_name = 'EntSysSupport',
		@recipients = @alertrecipients,
		--@copy_recipients = @copy_recipients,
		@subject=@Subject, 
		@body = @text,
		@body_format = 'HTML'

	INSERT INTO notification_history
	(stored_proc_name,
	record_logged_datetime,
	issues_found,
	action_required,
	notification_sent,
	email_type,
	email_to,
	email_cc,
	email_subject,
	comment
	)
	VALUES (
	'spMissingTransQtyAlert', --<< Stored Proc name
	GETDATE(),
	'Yes', --<< Issues found - Yes / No
	'Yes', --<< Action required - Yes / No
	'Yes', --<< Notification sent - Yes / No
	'Warning', --<< Email type - Notification Only / Alert / Warning
	@recipients, --<< Email TO
	NULL, --<< Email CC
	@Subject, --<< Email Subject
	'There are too many missing Transactions from Sales Audit.  This could be due to a failed import batch.' --<< Comment
	)
end
```

