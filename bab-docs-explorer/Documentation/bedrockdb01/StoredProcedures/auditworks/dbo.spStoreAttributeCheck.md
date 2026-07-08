# dbo.spStoreAttributeCheck

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spStoreAttributeCheck"]
    ATRBT_VAL_A(["ATRBT_VAL_A"]) --> SP
    POLLING_STORES(["POLLING_STORES"]) --> SP
    notification_history(["notification_history"]) --> SP
    dbo_sp_send_dbmail(["dbo.sp_send_dbmail"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| ATRBT_VAL_A |
| POLLING_STORES |
| notification_history |
| dbo.sp_send_dbmail |

## Stored Procedure Code

```sql
--DROP PROC [dbo].[spStoreAttributeCheck]
--GO

CREATE PROC [dbo].[spStoreAttributeCheck]
-- =============================================================================================================
-- Name: [dbo].[spStoreAttributeCheck]
--
-- Description:	Checks for stores missing BANKACCT attribute assignment & notifies via email accordingly
--				This attribute affects how the "ACCOUNTDISPLAYVALUE" column is reported in the 
--				Daily Media export file for ERP.
--
--
-- Output: N/A
--
-- Dependencies: 
--
-- Revision History
--		Name:			Date:			Comments:
--		Paul Beckman	01/11/2018		Created SP
--		Paul Beckman	01/18/2018		Modified store check by excluding stores with a closed date
--		Paul Beckman	01/23/2018		Modified store check by excluding stores with open date <= today+6
--		Paul Beckman	07/01/2018		Added check based on STORE_BRAND
--		Paul Beckman	11/13/2018		Updated to account for other attributes being assigned to a store in SA
--		Paul Beckman	03/22/2019		Added LisaM@buildabear.com to email notification
--		Paul Beckman	04/08/2019		Replaced ronw@buildabear.com with DawnGo@buildabear.com
--		Paul Beckman	10/18/2019		Updated to use notification_history table
--		Paul Beckman	02/05/2020		Updated email profile to 'EntSysSupport'
--		
--
-- exec spStoreAttributeCheck
-- =============================================================================================================
AS
SET NOCOUNT ON


--####################################################

IF (Object_ID('tempdb..##StoresMissingAttrList') IS NOT NULL) DROP TABLE ##StoresMissingAttrList

SELECT a.STORE_NUM
INTO ##StoresMissingAttrList
FROM POLLING_STORES a
WHERE a.STORE_NUM NOT IN (SELECT a.STORE_NUM FROM POLLING_STORES a
LEFT JOIN ATRBT_VAL_A b ON a.STORE_NUM = b.ASGND_OBJ_NUM
WHERE b.ATRBT_CODE = 'BANKACCT'
)
AND a.CLOSED_DATE IS NULL
AND a.STORE_BRAND IN ('Workshop')
AND a.OPEN_DATE <= DATEADD(day,+6,GETDATE())
ORDER BY a.STORE_NUM


--####################################################

IF (SELECT COUNT(*) FROM ##StoresMissingAttrList) = 0
GOTO FINISH

begin

DECLARE @sql VARCHAR(8000)
DECLARE @recipients VARCHAR(4000)
DECLARE @copy_recipients VARCHAR(4000)
DECLARE @Subject VARCHAR(80)
DECLARE @query VARCHAR(8000)
declare @text nvarchar(max)

--SET @recipients = 'paulb@buildabear.com'
SET @recipients = 'ScottP@buildabear.com;LisaM@buildabear.com;DawnGo@buildabear.com'
SET @copy_recipients = 'EntSysSupport@buildabear.com;erics@buildabear.com'

SET @text = 
		'<font face =arial size = 2 color="Red">' +
		N'<H3>** ACTION REQUIRED **</H3>' +
		'<br>' +
		'The following stores are missing a "BANKACCT" attribute setup in CRDM under Store setup and need to be added. <br>' +
		'This attribute affects how the "ACCOUNTDISPLAYVALUE" column is reported in the Daily Media export file for ERP. <br>' +
		'<br>' +
		'<table border="1">' + 
		'<font face =arial size = 2 color="Black">' +
		'<tr bgcolor=#D5D5F7><th>Store Num</th></tr>' +
		CAST ( ( SELECT [td/@align]='center',
						td = STORE_NUM, ''
				FROM ##StoresMissingAttrList
				FOR xml path ('tr'), type
		) AS NVARCHAR(MAX) ) +
		'</table>' +
		'<font face =arial size = 1 color="#C0C0C0">' +
		'<br><br><br><br>' +
		'Server:  BEDROCKDB01 <br>' +
		'Job Name:  Store_Setup_Checks <br>' +
		'Stored Proc:  BEDROCKDB01.auditworks.dbo.spStoreAttributeCheck <br>' +
		'Created by:  Paul Beckman <br>' +
		'Team Ownership:  Enterprise Systems <br>'

SET @Subject = 'ALERT - Store "BANKACCT" attribute missing in CRDM'
	EXEC msdb.dbo.sp_send_dbmail  
		@profile_name = 'EntSysSupport',
		@recipients = @recipients,
		@copy_recipients = @copy_recipients,
		@subject = @Subject, 
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
	'spStoreAttributeCheck', --<< Stored Proc name
	GETDATE(),
	'Yes', --<< Issues found - Yes / No
	'Yes', --<< Action required - Yes / No
	'Yes', --<< Notification sent - Yes / No
	'Alert', --<< Email type - Notification Only / Alert / Warning
	@recipients, --<< Email TO
	@copy_recipients, --<< Email CC
	@Subject, --<< Email Subject
	'Stores are missing a BANKACCT attribute setup in CRDM under Store setup and need to be added' --<< Comment
	)
END

--####################################################
FINISH:
```

