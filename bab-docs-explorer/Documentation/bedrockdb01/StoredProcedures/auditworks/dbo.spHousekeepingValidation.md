# dbo.spHousekeepingValidation

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spHousekeepingValidation"]
    dbo_if_transaction_header(["dbo.if_transaction_header"]) --> SP
    dbo_if_transaction_line(["dbo.if_transaction_line"]) --> SP
    notification_history(["notification_history"]) --> SP
    process_log(["process_log"]) --> SP
    dbo_process_log(["dbo.process_log"]) --> SP
    dbo_sp_send_dbmail(["dbo.sp_send_dbmail"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.if_transaction_header |
| dbo.if_transaction_line |
| notification_history |
| process_log |
| dbo.process_log |
| dbo.sp_send_dbmail |

## Stored Procedure Code

```sql
--DROP PROC [dbo].[spHousekeepingValidation]
--GO

CREATE PROC [dbo].[spHousekeepingValidation]
-- =============================================================================================================
-- Name: [dbo].[spHousekeepingValidation]
--
-- Description:	Shows that SA Housekeeping has run successfully and shows the table record counts
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
--		Paul Beckman	10/18/2010		Created SP
--		Paul Beckman	07/19/2015		Updated from POSDBSSA to BEDROCKDB01
--		Paul Beckman	12/11/2015		Updated select for email to show process_status_flag as Completed or FAILED
--		Paul Beckman	08/31/2016		Updated profile_name from 'POSadmin' to 'SAAdmin'
--		Paul Beckman	01/10/2017		Updated email body to HTML
--		Paul Beckman	10/03/2019		Updated recipient with 'EntSysSupport'
--		Paul Beckman	10/18/2019		Updated to use notification_history table
--		Paul Beckman	11/29/2019		Added section to log record to notification_history if threshold is OK
--		Paul Beckman	02/05/2020		Updated email profile to 'EntSysSupport'
--
-- exec spHousekeepingValidation
-- =============================================================================================================
AS
SET NOCOUNT ON

declare @sql varchar(8000)
declare @recipients varchar(4000)
declare @Subject varchar(60)
declare @query varchar(8000)
declare @text nvarchar(max)

set @recipients = 'EntSysSupport@buildabear.com'
--set @recipients = 'paulb@buildabear.com'

--#########################################################

if (select sum(transaction_count) from process_log where process_no = 41 and process_start_time > CONVERT(varchar,DATEADD(DAY,-3,GETDATE()),111)) = 0

begin
	set @text = 
				'<font face =arial size = 3 color="Red">' +
				N'<H3>** ACTION REQUIRED **</H3>' +
				'There have been ZERO transactions deleted from auditworks db if_transaction tables.<br>' + 
				'There should NEVER be more than 3 days gone by without cleanup.<br>' +
				'<br>' +
				'<table border="1">' +
				'<font face = arial size = 2>' +
				'<tr bgcolor=#D5D5F7><th>Process Start Time</th><th>Trans Count</th><th>prosess status</th></tr>' +
				CAST ( ( SELECT td = convert (varchar(24),process_start_time), '',
								[td/@align]='right',
								td = FORMAT(transaction_count,'#,###'), '',
								[td/@align]='center',
								td = CASE WHEN process_status_flag = 2 THEN 'Completed' ELSE 'FAILED' END
					  FROM auditworks.dbo.process_log
					  WHERE process_no = 41
					  AND process_start_time > CONVERT(varchar,DATEADD(DAY,-6,GETDATE()),111)
					  ORDER BY process_start_time
					  FOR xml path ('tr'), type
				) AS NVARCHAR(MAX) ) +
				'</table>' +
				'<br><br>' +
				'<font face =arial size = 2>' +
				'Record count in "if_transaction_header" table... <br>' +
				'<table border="1">' + 
				'<font face =arial size = 2>' +
				'<tr bgcolor=#D5D5F7><th>IF Header Record Count</th></tr>' +
				CAST ( ( SELECT [td/@align]='right',
								td = FORMAT(COUNT(if_entry_no),'#,###')
					  FROM auditworks.dbo.if_transaction_header (nolock)
					  FOR xml path ('tr'), type
				) AS NVARCHAR(MAX) ) +
				'</table>' +
				'<br><br>' +
				'<font face =arial size = 2>' +
				'Record count in "if_transaction_line" table... <br>' +
				'<table border="1">' + 
				'<font face =arial size = 2>' +
				'<tr bgcolor=#D5D5F7><th>IF Line Record Count</th></tr>' +
				CAST ( ( SELECT [td/@align]='right',
								td = FORMAT(COUNT(if_entry_no),'#,###')
					  FROM auditworks.dbo.if_transaction_line (nolock)
					  FOR xml path ('tr'), type
				) AS NVARCHAR(MAX) ) +
				'</table>' +
				'<br>' +
				'<font face =arial size = 2>' +
				'These needs to be investigated and resolved ASAP.  It is likely that Epicor will need to be involved.<br>' +
				'<br>' +
				'SA app > Services Administration > Job Scheduler > SAAPP01 - SA > Housekeeping Server and is named "Housekeeping Job"<br>' +
				'<font face =arial size = 1 color="#C0C0C0">' +
				'<br><br><br><br>' +
				'Server:  BEDROCKDB01 <br>' +
				'Job Name:  Housekeeping_Validation <br>' +
				'Stored Proc:  BEDROCKDB01.auditworks.dbo.spHousekeepingValidation <br>' +
				'Created by:  Paul Beckman <br>' +
				'Team Ownership:  Enterprise Systems <br>'

	set @Subject = 'WARNING - Auditworks HouseKeeping Process error'

	exec msdb.dbo.sp_send_dbmail  
		@profile_name = 'EntSysSupport',
		@recipients = @recipients,
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
	'spHousekeepingValidation', --<< Stored Proc name
	GETDATE(),
	'Yes', --<< Issues found - Yes / No
	'Yes', --<< Action required - Yes / No
	'Yes', --<< Notification sent - Yes / No
	'Warning', --<< Email type - Notification Only / Alert / Warning
	@recipients, --<< Email TO
	NULL, --<< Email CC
	@Subject, --<< Email Subject
	'There have been ZERO transactions deleted from auditworks db if_transaction tables in past 3 days' --<< Comment
	)

end


--#########################################################

if (select sum(transaction_count) from process_log where process_no = 41 and process_start_time > CONVERT(varchar,DATEADD(DAY,-1,GETDATE()),111)) = 0

begin
	set @text = 
				'<font face =arial size = 3 color="Red">' +
				'There have been ZERO transactions deleted from auditworks db if_transaction tables.<br>' +
				'<br>' +
				'<table border="1">' +
				'<font face = arial size = 2>' +
				'<tr bgcolor=#D5D5F7><th>Process Start Time</th><th>Trans Count</th><th>prosess status</th></tr>' +
				CAST ( ( SELECT td = convert (varchar(24),process_start_time), '',
								[td/@align]='right',
								td = FORMAT(transaction_count,'#,###'), '',
								[td/@align]='center',
								td = CASE WHEN process_status_flag = 2 THEN 'Completed' ELSE 'FAILED' END
					  FROM auditworks.dbo.process_log
					  WHERE process_no = 41
					  AND process_start_time > CONVERT(varchar,DATEADD(DAY,-6,GETDATE()),111)
					  ORDER BY process_start_time
					  FOR xml path ('tr'), type
				) AS NVARCHAR(MAX) ) +
				'</table>' +
				'<br><br>' +
				'<font face =arial size = 2>' +
				'Record count in "if_transaction_header" table... <br>' +
				'<table border="1">' + 
				'<font face =arial size = 2>' +
				'<tr bgcolor=#D5D5F7><th>IF Header Record Count</th></tr>' +
				CAST ( ( SELECT [td/@align]='right',
								td = FORMAT(COUNT(if_entry_no),'#,###')
					  FROM auditworks.dbo.if_transaction_header (nolock)
					  FOR xml path ('tr'), type
				) AS NVARCHAR(MAX) ) +
				'</table>' +
				'<br><br>' +
				'<font face =arial size = 2>' +
				'Record count in "if_transaction_line" table... <br>' +
				'<table border="1">' + 
				'<font face =arial size = 2>' +
				'<tr bgcolor=#D5D5F7><th>IF Line Record Count</th></tr>' +
				CAST ( ( SELECT [td/@align]='right',
								td = FORMAT(COUNT(if_entry_no),'#,###')
					  FROM auditworks.dbo.if_transaction_line (nolock)
					  FOR xml path ('tr'), type
				) AS NVARCHAR(MAX) ) +
				'</table>' +
				'<br>' +
				'<font face =arial size = 2>' +
				'SA app > Services Administration > Job Scheduler > SAAPP01 - SA > Housekeeping Server and is named "Housekeeping Job"<br>' +
				'<font face =arial size = 1 color="#C0C0C0">' +
				'<br><br><br><br>' +
				'Server:  BEDROCKDB01 <br>' +
				'Job Name:  Housekeeping_Validation <br>' +
				'Stored Proc:  BEDROCKDB01.auditworks.dbo.spHousekeepingValidation <br>' +
				'Created by:  Paul Beckman <br>' +
				'Team Ownership:  Enterprise Systems <br>'

	set @Subject = 'ALERT - Auditworks HouseKeeping Process error'

	exec msdb.dbo.sp_send_dbmail  
		@profile_name = 'EntSysSupport',
		@recipients = @recipients,
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
	'spHousekeepingValidation', --<< Stored Proc name
	GETDATE(),
	'Yes', --<< Issues found - Yes / No
	'No', --<< Action required - Yes / No
	'Yes', --<< Notification sent - Yes / No
	'Alert', --<< Email type - Notification Only / Alert / Warning
	@recipients, --<< Email TO
	NULL, --<< Email CC
	@Subject, --<< Email Subject
	'There have been ZERO transactions deleted from auditworks db if_transaction tables' --<< Comment
	)

end

--#########################################################


if (select sum(transaction_count) from process_log where process_no = 41 and process_start_time > CONVERT(varchar,DATEADD(DAY,-0,GETDATE()),111)) > 0

begin
	INSERT INTO notification_history
	(stored_proc_name,
	record_logged_datetime,
	issues_found,
	action_required,
	notification_sent,
	comment
	)
	VALUES (
	'spHousekeepingValidation', --<< Stored Proc name
	GETDATE(),
	'No', --<< Issues found - Yes / No
	'No', --<< Action required - Yes / No
	'No', --<< Notification sent - Yes / No
	'Housekeeping ran successfully today and deleted transactions from auditworks db if_transaction tables' --<< Comment
	)

end

--set @text = 
--				'<font face =arial size = 2>' +
--				'Transaction cleanup counts from if_transaction_header in Sales Audit... <br>' + 
--				'<br>' +
--				'<table border="1">' +
--				'<font face = arial size = 2>' +
--				'<tr bgcolor=#D5D5F7><th>Process Start Time</th><th>Trans Count</th><th>Process Status</th></tr>' +
--				CAST ( ( SELECT td = convert (varchar(24),process_start_time), '',
--								[td/@align]='right',
--								td = FORMAT(transaction_count,'#,###'), '',
--								[td/@align]='center',
--								td = CASE WHEN process_status_flag = 2 THEN 'Completed' ELSE 'FAILED' END
--					  FROM auditworks.dbo.process_log
--					  WHERE process_no = 41
--					  AND process_start_time > CONVERT(varchar,DATEADD(DAY,-6,GETDATE()),111)
--					  ORDER BY process_start_time
--					  FOR xml path ('tr'), type
--				) AS NVARCHAR(MAX) ) +
--				'</table>' +
--				'<br><br>' +
--				'<font face =arial size = 2>' +
--				'Record count in "if_transaction_header" table... <br>' +
--				'<table border="1">' + 
--				'<font face =arial size = 2>' +
--				'<tr bgcolor=#D5D5F7><th>IF Header Record Count</th></tr>' +
--				CAST ( ( SELECT [td/@align]='right',
--								td = FORMAT(COUNT(if_entry_no),'#,###')
--					  FROM auditworks.dbo.if_transaction_header (nolock)
--					  FOR xml path ('tr'), type
--				) AS NVARCHAR(MAX) ) +
--				'</table>' +
--				'<br><br>' +
--				'<font face =arial size = 2>' +
--				'Record count in "if_transaction_line" table... <br>' +
--				'<table border="1">' + 
--				'<font face =arial size = 2>' +
--				'<tr bgcolor=#D5D5F7><th>IF Line Record Count</th></tr>' +
--				CAST ( ( SELECT [td/@align]='right',
--								td = FORMAT(COUNT(if_entry_no),'#,###')
--					  FROM auditworks.dbo.if_transaction_line (nolock)
--					  FOR xml path ('tr'), type
--				) AS NVARCHAR(MAX) ) +
--				'</table>' +
--				'<font face =arial size = 1 color="#C0C0C0">' +
--				'<br><br><br><br>' +
--				'Server:  BEDROCKDB01 <br>' +
--				'Job Name:  Housekeeping_Validation <br>' +
--				'Stored Proc:  BEDROCKDB01.auditworks.dbo.spHousekeepingValidation <br>' +
--				'Created by:  Paul Beckman <br>' +
--				'Team Ownership:  Enterprise Systems Support <br>'

--set @Subject = 'Auditworks Daily HouseKeeping Process Check'
--	exec msdb.dbo.sp_send_dbmail  
--		@profile_name = 'EntSysSupport',
--		@recipients = @recipients,
--		@subject=@Subject, 
--		@body = @text,
--		@body_format = 'HTML'


dbo,spGiftCardAnalysis,
-------------This is it!-----------------------------------------------------------
CREATE
--CREATE 
PROCEDURE [dbo].[spGiftCardAnalysis] 

@GiftCardBeginRange numeric(28,0) = null, 
@GiftCardEndRange numeric(28,0) = null, 
@ActivationStartDate datetime,
@ActivationEndDate datetime,
@RedemptionStartDate datetime,
@RedemptionEndDate datetime,
@GiftCardType varchar(50)

AS
-- =====================================================================================================
-- Name: spGiftCardAnalysis
--
-- Description:	
--
-- Input:	
--			Date ranges
--
-- Output: Resultset with the following columns:
--			redemption history
--
-- Dependencies: None
--
-- Revision History
--		Name:			Date:			Comments:
--		?				08/24/2010		Initial version source control
--		dave			08/30/2010		added isnumeric to shortcircuit the case statements numeric cast
--
--
-- exec spGiftCardAnalysis 6058200000000000, 6058294485889000,'2010-08-01', '2010-08-22', '2010-08-01', '2010-08-22', 'fake' --this procedure does not seem to be working
-- =====================================================================================================

SET NOCOUNT ON
/*--********************************************--********************************************--********************************************
										NON-AV TRANSACTIONS
--********************************************--********************************************--********************************************/

IF (Object_ID('tempdb..##non_av_activations') IS NOT NULL) DROP TABLE  ##non_av_activations
SELECT  CardType = 
case 
	when isnumeric(tl.reference_no) = 0 then 'Unclassified'
	when @GiftCardBeginRange is not null and isnumeric(tl.reference_no) = 1 and 
     cast(tl.reference_no as numeric(28,0)) between @GiftCardBeginRange and @GiftCardEndRange then @GiftCardType
 --    when @GiftCardActivationValue is not null then @GiftCardType 
else 'Unclassified' end
, th.store_no, th.register_no, th.transaction_no, th.transaction_date, d.date_key, d.fiscal_year,
d.fiscal_quarter,d.fiscal_period, d.fiscal_week, th.transaction_void_flag,th.tender_total, tl.line_void_flag,
tl.gross_line_amount, tl.line_object, tl.line_action,th.transaction_id, tl.reference_no  
  INTO ##non_av_activations  
 FROM auditworks..transaction_header th with (nolock)  join  auditworks..transaction_line tl with (nolock) on 
th.transaction_id = tl.transaction_id join
 dbo.date_dim d with (nolock) on 
th.transaction_date = d.actual_date
where 
 th.transaction_void_flag = 0
  and tl.line_void_flag <> 1 
   and th.transaction_date between @ActivationStartDate and @ActivationEndDate
   and 
   (( line_object = 404  -- Gift Card Activations
     and line_action = 1 )
     or  
	 (line_object = 633  -- Gift Card Activations
     and line_action = 12))


create index ix_g##non_av_activations_compositekey on ##non_av_activations (transaction_id,date_key,store_no,CardType)

--create index ix_g##non_av_activations_CardType on ##non_av_activations (CardType)
-- --go 

IF (Object_ID('tempdb..##non_av_redemptions') IS NOT NULL) DROP TABLE  ##non_av_redemptions

SELECT  CardType = 
case 
	when isnumeric(tl.reference_no) = 0 then 'Unclassified'
	when @GiftCardBeginRange is not null and isnumeric(tl.reference_no) = 1 and 
     cast(tl.reference_no as numeric(28,0)) between @GiftCardBeginRange and @GiftCardEndRange then @GiftCardType
 --    when @GiftCardActivationValue is not null then @GiftCardType 
else 'Unclassified' end
, th.store_no, th.register_no, th.transaction_no, th.transaction_date, d.date_key, d.fiscal_year,
d.fiscal_quarter,d.fiscal_period, d.fiscal_week, th.transaction_void_flag,th.tender_total, tl.line_void_flag,
tl.gross_line_amount, tl.line_object, tl.line_action,th.transaction_id, tl.reference_no  
  INTO ##non_av_redemptions  
 FROM auditworks..transaction_header th with (nolock)  join  auditworks..transaction_line tl with (nolock) on 
th.transaction_id = tl.transaction_id join
 dbo.date_dim d with (nolock) on 
th.transaction_date = d.actual_date
where 
   th.transaction_void_flag = 0
  and tl.line_void_flag <> 1 
  and th.transaction_date between @RedemptionStartDate and @RedemptionEndDate 
  and 
   (
( tl.line_object = 404  and tl.line_action = 2  ) -- Gift Card Redemptions
            or  
	 (tl.line_object = 633  and tl.line_action = 25 )-- Gift Card redemptions
     )


--create index ix_g##non_av_SameTrans_CardType on ##non_av_SameTrans (CardType)

IF (Object_ID('tempdb..##non_av_CardTypeTransactions') IS NOT NULL) DROP TABLE  ##non_av_CardTypeTransactions --##non_av_transactions1

--##non_av_SameTrans

select * into ##non_av_CardTypeTransactions
from ##non_av_activations with (nolock)
where CardType = @GiftCardType
union 
select * from ##non_av_redemptions  with (nolock) 
where CardType = @GiftCardType


create index ix_g##non_av_CardTypeTransactions_compositekey on ##non_av_CardTypeTransactions (transaction_id,date_key,store_no,CardType)
--##non_av_SameTrans

IF (Object_ID('tempdb..##non_av_SameTrans') IS NOT NULL) DROP TABLE  ##non_av_SameTrans

select t2.* 
into ##non_av_SameTrans
from ##non_av_CardTypeTransactions t1 with (nolock) 
join ##non_av_activations t2 with (nolock) on 
t1.transaction_id = t2.transaction_id and
t1.date_key = t2.date_key and
t1.store_no = t2.store_no 
where 
t1.CardType = @GiftCardType and 
t2.CardType <> @GiftCardType 
union all 
select t2.* 
--into ##non_av_transactions2
from ##non_av_CardTypeTransactions t1 with (nolock) 
join ##non_av_redemptions t2 with (nolock) on 
t1.transaction_id = t2.transaction_id and
t1.date_key = t2.date_key and
t1.store_no = t2.store_no 
where 
t1.CardType = @GiftCardType and 
t2.CardType <> @GiftCardType 


IF (Object_ID('tempdb..##non_av_transactions') IS NOT NULL) DROP TABLE  ##non_av_transactions

select * 
into ##non_av_transactions
from ##non_av_CardTypeTransactions with (nolock) 
union
select * from ##non_av_SameTrans with (nolock) 

/*--********************************************--********************************************--********************************************
										AV TRANSACTIONS
--********************************************--********************************************--********************************************/

IF (Object_ID('tempdb..##av_activations') IS NOT NULL) DROP TABLE  ##av_activations

SELECT  CardType = 
case 
	when isnumeric(tl.reference_no) = 0 then 'Unclassified'
	when @GiftCardBeginRange is not null and isnumeric(tl.reference_no) = 1 and 
     cast(tl.reference_no as numeric(28,0)) between @GiftCardBeginRange and @GiftCardEndRange then @GiftCardType
 --    when @GiftCardActivationValue is not null then @GiftCardType 
else 'Unclassified' end
, th.store_no, th.register_no, th.transaction_no, th.transaction_date, d.date_key, d.fiscal_year,
d.fiscal_quarter,d.fiscal_period, d.fiscal_week, th.transaction_void_flag,th.tender_total,tl.line_void_flag,
 tl.gross_line_amount, tl.line_object,tl.line_action,th.av_transaction_id transaction_id,tl.reference_no
  INTO ##av_activations 
 FROM  auditworks..av_transaction_header th with (nolock) join auditworks..av_transaction_line tl with (nolock) on 
 th.av_transaction_id = tl.av_transaction_id join
 dbo.date_dim d with (nolock) on 
th.transaction_date = d.actual_date 
where 
  th.transaction_void_flag = 0
  and tl.line_void_flag <> 1 
   and th.transaction_date between @ActivationStartDate and @ActivationEndDate
   and 
   (( line_object = 404  -- Gift Card Activations
     and line_action = 1 )
     or  
	 (line_object = 633  -- Gift Card Activations
     and line_action = 12))

create index ix_g##av_activations_compositekey on ##av_activations (transaction_id,date_key,store_no,CardType)

--create index ix_g##av_activations_CardType on ##av_activations (CardType)


IF (Object_ID('tempdb..##av_redemptions') IS NOT NULL) DROP TABLE ##av_redemptions 

SELECT  CardType = 
case 
	when isnumeric(tl.reference_no) = 0 then 'Unclassified'
	when @GiftCardBeginRange is not null and isnumeric(tl.reference_no) = 1 and 
     cast(tl.reference_no as numeric(28,0)) between @GiftCardBeginRange and @GiftCardEndRange then @GiftCardType
 --    when @GiftCardActivationValue is not null then @GiftCardType 
else 'Unclassified' end
, th.store_no, th.register_no, th.transaction_no, th.transaction_date, d.date_key, d.fiscal_year,
d.fiscal_quarter,d.fiscal_period, d.fiscal_week, th.transaction_void_flag,th.tender_total,tl.line_void_flag,
 tl.gross_line_amount, tl.line_object,tl.line_action,th.av_transaction_id transaction_id,tl.reference_no
  INTO ##av_redemptions  
 FROM  auditworks..av_transaction_header th with (nolock) join auditworks..av_transaction_line tl with (nolock) on 
 th.av_transaction_id = tl.av_transaction_id join
 dbo.date_dim d with (nolock) on 
th.transaction_date = d.actual_date 
where 
   th.transaction_void_flag = 0
  and tl.line_void_flag <> 1 
  and th.transaction_date between @RedemptionStartDate and @RedemptionEndDate 
  and 
   (
( tl.line_object = 404  and tl.line_action = 2  ) -- Gift Card Activations
            or  
	 (tl.line_object = 633  and tl.line_action = 25 )-- Gift Card redemptions
     )

-- create index ix_g##av_SameTrans_CardType on ##av_SameTrans (CardType)


IF (Object_ID('tempdb..##av_CardTypeTransactions') IS NOT NULL) DROP TABLE ##av_CardTypeTransactions 

select * into ##av_CardTypeTransactions
from ##av_activations with (nolock)
where CardType = @GiftCardType
union 
select * from ##av_redemptions  with (nolock) 
where CardType = @GiftCardType


create index ix_g##av_CardTypeTransactions_compositekey on ##av_CardTypeTransactions (transaction_id,date_key,store_no,CardType)


IF (Object_ID('tempdb..##av_SameTrans') IS NOT NULL) DROP TABLE  ##av_SameTrans

select t2.* 
into ##av_SameTrans
from ##av_CardTypeTransactions t1 with (nolock) 
join ##av_activations t2 with (nolock) on 
t1.transaction_id = t2.transaction_id and
t1.date_key = t2.date_key and
t1.store_no = t2.store_no 
where 
t1.CardType = @GiftCardType and 
t2.CardType <> @GiftCardType 
union all 
select t2.* 
--into ##av_transactions2
from ##av_CardTypeTransactions t1 with (nolock) 
join ##av_redemptions t2 with (nolock) on 
t1.transaction_id = t2.transaction_id and
t1.date_key = t2.date_key and
t1.store_no = t2.store_no 
where 
t1.CardType = @GiftCardType and 
t2.CardType <> @GiftCardType 


IF (Object_ID('tempdb..##av_transactions') IS NOT NULL) DROP TABLE  ##av_transactions

select * 
into ##av_transactions
from ##av_CardTypeTransactions with (nolock) 
union
select * from ##av_SameTrans with (nolock) 

IF (Object_ID('tempdb..##all_transactions') IS NOT NULL) DROP TABLE  ##all_transactions

select * into ##all_transactions
from ##non_av_transactions  
union
select * from ##av_transactions

--select * from ##all_transactions

--******************wip***************************************************************************************
IF (Object_ID('tempdb..##all_activations') IS NOT NULL) DROP TABLE  ##all_activations

select * into ##all_activations
from ##all_transactions   
where 
(line_object = 404 and line_action = 1)  
 or
(line_object = 633 and line_action = 12) 


IF (Object_ID('tempdb..##all_redemptions') IS NOT NULL) DROP TABLE  ##all_redemptions

select * into ##all_redemptions
from ##all_transactions   
where 
(line_object = 404 and line_action = 2)  
 or
(line_object = 633 and line_action = 25) 

--select * from ##AllGiftCard_Activations

--******************Output stats***************************************************************************************

/*
--Q1: How many gift cards of the types were activated? 
*/

--select top 1 * from ##all_transactions

select 'Store Total Activations' as ReportName, cast(store_no as varchar(50)) store_no, CardType,
 count(distinct reference_no) TotalGiftCardsActivated ,count(distinct transaction_id) TransactionCount
from ##all_activations with (nolock)
-- and r.store_no = 991 -- 277
where CardType = @GiftCardType
--and store_no = 2003 
group by store_no,  CardType 
order by store_no ,CardType
-- --go 


/*
--Q2: How many gift cards of the types were redeemed? 
*/

--select top 1 * from ##all_redemptions

select 'Store Total Redemptions' as ReportName, cast(store_no as varchar(50)) store_no, CardType,
 count(distinct reference_no) TotalGiftCardsRedeemed ,count(distinct transaction_id) TransactionCount
from ##all_redemptions with (nolock)
-- and r.store_no = 991 -- 277
where CardType = @GiftCardType
--and store_no = 2003 
group by store_no,  CardType 
order by store_no ,CardType
-- --go 


/*
--Q3: How many gift cards were activated and Redeemed on the same day? 
--Same activation and redemption day Store Totals
*/


----Q3a) Same activation and redemption day Store Totals/Summary

select 'Store Total Same Day Redemption' as ReportName, cast(r.store_no as varchar(50)) store_no, r.CardType,  
count(distinct r.reference_no) SameDayRedemptionGiftCardCount,
count(distinct r.transaction_id) SameDayRedemptionTransCount
from 
##all_activations a with (nolock) join 
##all_redemptions r with (nolock)
on 
 r.reference_no = a.reference_no  and 
 r.date_key = a.date_key 
--where a.store_no = 2003 
group by r.store_no, r.CardType
--go


----Q3b) Details of Activations (Same day activation and redemption)
select 'Activation Details'  as ReportName,
cast(a.store_no as varchar(50)) store_no
, a.transaction_date
,cast(a.register_no as varchar(50)) register_no
,cast(a.transaction_no as varchar(50)) transaction_no
,cast(a.transaction_id as varchar(50)) transaction_id
,a.CardType
,a.reference_no
,a.gross_line_amount
,a.tender_total
,cast(a.fiscal_year as varchar(4)) fiscal_year
,cast(a.fiscal_quarter as varchar(2)) fiscal_quarter
,cast(a.fiscal_period as varchar(2)) fiscal_period
,cast(a.fiscal_week as varchar(2)) fiscal_week
,cast(a.line_object as varchar(8)) line_object
,cast(a.line_action as varchar(8)) line_action
from 
##all_activations a with (nolock) join 
##all_redemptions r with (nolock) on 
 a.reference_no = r.reference_no   
 and a.date_key = r.date_key
--where a.store_no = 2003 
group by a.CardType, a.store_no, a.register_no, a.transaction_no, a.transaction_date, a.fiscal_year,
a.fiscal_quarter, a.fiscal_period, a.fiscal_week, a.transaction_void_flag, a.tender_total, a.line_void_flag,
a.gross_line_amount, a.line_object, a.line_action,a.transaction_id, a.reference_no 
order by a.reference_no


----Q3c) Details of Redemptions (Same day activation and redemption)

select 'Redemption Details' as ReportName,
cast(r.store_no as varchar(50)) store_no
, r.transaction_date
,cast(r.register_no as varchar(50)) register_no
,cast(r.transaction_no as varchar(50)) transaction_no
,cast(r.transaction_id as varchar(50)) transaction_id
,r.CardType
,r.reference_no
,r.gross_line_amount
,r.tender_total
,cast(r.fiscal_year as varchar(4)) fiscal_year
,cast(r.fiscal_quarter as varchar(2)) fiscal_quarter
,cast(r.fiscal_period as varchar(2)) fiscal_period
,cast(r.fiscal_week as varchar(2)) fiscal_week
,cast(r.line_object as varchar(8)) line_object
,cast(r.line_action as varchar(8)) line_action
from 
##all_activations a with (nolock) join 
##all_redemptions r with (nolock) on 
 a.reference_no = r.reference_no   
 and a.date_key = r.date_key
-- where r.store_no = 2003 
group by r.CardType, r.store_no, r.register_no, r.transaction_no, r.transaction_date, r.fiscal_year,
r.fiscal_quarter, r.fiscal_period, r.fiscal_week, r.transaction_void_flag, r.tender_total, r.line_void_flag,
r.gross_line_amount, r.line_object, r.line_action,r.transaction_id, r.reference_no 
order by r.reference_no



--Q4: Multiple Redemptions on single transaction


--Q4a) Multiple Redemptions on same transaction - Store Totals/Summary

select 'Trans with Multiple Redems Store Totals' as ReportName,
cast(store_no as varchar(50)) store_no, 
count(distinct r.transaction_id) MultipleRedemptions_TransCount, count(distinct r.reference_no) GiftCardsRedemeed
from 
##all_redemptions r 
where 
-- r.store_no = 2003 and
 transaction_id in 
(select transaction_id 
from ##all_redemptions  with (nolock) where
transaction_id in 
(select transaction_id from ##all_redemptions with (nolock) where CardType = @GiftCardType )
group by transaction_id having count(distinct reference_no) > 1)
group by store_no
--go

----Q4b) Multiple Redemptions on same transaction - Transaction_ID Totals/Summary

select 'Trans with Multiple Redems' as ReportName,
cast(r.store_no as varchar(50)) store_no
,cast(r.transaction_no as varchar(50)) transaction_no
,cast(r.transaction_id as varchar(50)) transaction_id
, count(distinct r.reference_no) GiftCardsRedemeed,
 sum(r.gross_line_amount) total_gross_line_amount,r.tender_total
from 
##all_redemptions r 
where 
-- r.store_no = 2003 and
 transaction_id in 
(select transaction_id 
from ##all_redemptions  with (nolock) where
transaction_id in 
(select transaction_id from ##all_redemptions with (nolock) where CardType = @GiftCardType) 
group by transaction_id having count(distinct reference_no) > 1)
group by store_no,r.transaction_id,r.transaction_no,r.tender_total
--go


----Q4c) Multiple Redemptions on same transaction - Details

select 'Multiple Redems Trans Details' as ReportName,
cast(r.store_no as varchar(50)) store_no
, r.transaction_date
,cast(r.register_no as varchar(50)) register_no
,cast(r.transaction_no as varchar(50)) transaction_no
,cast(r.transaction_id as varchar(50)) transaction_id
,r.CardType
,r.reference_no
,r.gross_line_amount
,r.tender_total
,cast(r.fiscal_year as varchar(4)) fiscal_year
,cast(r.fiscal_quarter as varchar(2)) fiscal_quarter
,cast(r.fiscal_period as varchar(2)) fiscal_period
,cast(r.fiscal_week as varchar(2)) fiscal_week
,cast(r.line_object as varchar(8)) line_object
,cast(r.line_action as varchar(8)) line_action
from 
##all_redemptions r 
where 
-- r.store_no = 2003 and
 transaction_id in 
(select transaction_id --,count(distinct reference_no) NoOfGiftCards
from ##all_redemptions  with (nolock) where
transaction_id in 
(select transaction_id from ##all_redemptions  with (nolock) where CardType  = @GiftCardType)
group by transaction_id having count(distinct reference_no) > 1)
group by r.CardType, r.store_no, r.register_no, r.transaction_no, r.transaction_date, r.fiscal_year,
r.fiscal_quarter, r.fiscal_period, r.fiscal_week, r.transaction_void_flag, r.tender_total, r.line_void_flag,
r.gross_line_amount, r.line_object, r.line_action,r.transaction_id, r.reference_no 
order by r.store_no,r.transaction_no, r.reference_no



----Q5a) Sales Details of transactions with Activations 
select 'Activation Sales Details by Transaction'  as ReportName,
cast(a.store_no as varchar(50)) store_no
, a.transaction_date
,cast(a.register_no as varchar(50)) register_no
,cast(a.transaction_no as varchar(50)) transaction_no
,cast(a.transaction_id as varchar(50)) transaction_id
,count(distinct a.reference_no) NoOfGCActivated
,sum(a.gross_line_amount) TtlAmtGCActivated
,a.tender_total
,a.tender_total - sum(a.gross_line_amount) [gaap_sale (TenderTotal - TtlAmtGCActivated)]
,cast(a.fiscal_year as varchar(4)) fiscal_year
,cast(a.fiscal_quarter as varchar(2)) fiscal_quarter
,cast(a.fiscal_period as varchar(2)) fiscal_period
,cast(a.fiscal_week as varchar(2)) fiscal_week
,cast(a.line_object as varchar(8)) line_object
,cast(a.line_action as varchar(8)) line_action
from 
##all_activations a with (nolock) 
group by  
a.store_no, a.register_no, a.transaction_no, a.transaction_date, a.fiscal_year,a.tender_total,
a.fiscal_quarter, a.fiscal_period, a.fiscal_week, a.transaction_void_flag, a.tender_total, a.line_void_flag,
a.line_object, a.line_action,a.transaction_id 
order by a.store_no,a.transaction_date, a.transaction_no


----Q5b) Sales Details of transactions with redemptions 
select 'Redemption Sales Details by Transaction'  as ReportName,
cast(r.store_no as varchar(50)) store_no
, r.transaction_date
,cast(r.register_no as varchar(50)) register_no
,cast(r.transaction_no as varchar(50)) transaction_no
,cast(r.transaction_id as varchar(50)) transaction_id
,count(distinct r.reference_no) NoOfGCRedeemed
,sum(r.gross_line_amount) TtlAmtGCRedeemed
,r.tender_total
,r.tender_total - sum(r.gross_line_amount) [GC_lift (TenderTotal - TtlAmtGCRedeemed)]
,cast(r.fiscal_year as varchar(4)) fiscal_year
,cast(r.fiscal_quarter as varchar(2)) fiscal_quarter
,cast(r.fiscal_period as varchar(2)) fiscal_period
,cast(r.fiscal_week as varchar(2)) fiscal_week
,cast(r.line_object as varchar(8)) line_object
,cast(r.line_action as varchar(8)) line_action
from 
 ##all_redemptions r with (nolock)  
group by 
r.store_no, r.register_no, r.transaction_no, r.transaction_date, r.fiscal_year,r.tender_total,
r.fiscal_quarter, r.fiscal_period, r.fiscal_week, r.transaction_void_flag, r.tender_total, r.line_void_flag,
r.line_object, r.line_action,r.transaction_id 
order by r.store_no,r.transaction_date, r.transaction_no


SET ANSI_NULLS OFF
--go
SET --QUOTED_IDENTIFIER OFF
--go
```

