# dbo.spERP_Daily_Banking_Totals_Export

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spERP_Daily_Banking_Totals_Export"]
    dbo_GEOG_ADRS(["dbo.GEOG_ADRS"]) --> SP
    dbo_ORG_CHN(["dbo.ORG_CHN"]) --> SP
    dbo_SV_PRMY_ADDRESS(["dbo.SV_PRMY_ADDRESS"]) --> SP
    media_reconciliation_detail(["media_reconciliation_detail"]) --> SP
    media_reconciliation_status(["media_reconciliation_status"]) --> SP
    notification_history(["notification_history"]) --> SP
    dbo_sp_send_dbmail(["dbo.sp_send_dbmail"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.GEOG_ADRS |
| dbo.ORG_CHN |
| dbo.SV_PRMY_ADDRESS |
| media_reconciliation_detail |
| media_reconciliation_status |
| notification_history |
| dbo.sp_send_dbmail |

## Stored Procedure Code

```sql
CREATE   procedure [dbo].[spERP_Daily_Banking_Totals_Export]
--(
--@TransactionStartDate as int
--,@TransactionEndDate as int
--)
AS
-- =====================================================================================================
-- Name: spERP_Daily_Banking_Totals_Export
--
-- Description:	Tender Totals Media rec banking export from SA for Dynamics 365 ERP
--	
--
-- Input:	
--			
--
-- Output: CSV files.  One for each Country
--			
--
-- Schedule: 
--    Tue 9:00pm run for prior Wed-Thu sales
--    Wed 9:00pm run for prior Fri-Sat sales
--    Thu 9:00pm run for prior Sun-Mon sales
--    Fri 9:00pm run for prior Tue sales			
--
-- Dependencies: None	
--	
--
-- Revision History
--		Name:			Date:			Comments:
--		Paul Beckman		05/10/2018		Initial testing began
--		Paul Beckman		05/16/2018		Created stored proc in BEDROCKDB01.auditworks
--		Paul Beckman		06/26/2018		Added exclusion for records with amount equal to zero
--		Paul Beckman		06/29/2018		Changed 'AcctCode' for IRL from '2110SAUDTCLEAR' to '2110IRLCLEAR'
--		Paul Beckman		07/31/2018		Added data date range text for the email message body
--		Paul Beckman		07/31/2018		Added email recipients DawnGo@buildabear.com and MichaelBeiser@buildabear.com
--		Paul Beckman		08/02/2018		Set file location to the Prod location for processing
--		Paul Beckman		08/05/2019		Adjusted file backup days from 20 to 40
--		Paul Beckman		08/27/2019		Removed IanW@buildabear.com
--		Paul Beckman		10/03/2019		Updated recipient from 'SAAdmin' to 'EntSysSupport'
--		Paul Beckman		10/17/2019		Updated to use notification_history table
--		Paul Beckman		02/05/2020		Updated email profile to 'EntSysSupport'
--		
-- 
-- exec spERP_Daily_Banking_Totals_Export		(  if paramters used:  exec spERP_Daily_Banking_Totals_Export 4, 3  )
-- 
-- =====================================================================================================

--####################################
-- Run day check
--####################################

-->>>>>>   Comment out this IF statement when running manually on Sat, Sun, or Mon   <<<<<<--
IF (SELECT CAST(LEFT(DATENAME(dw,DATEADD(DAY,-0,GETDATE())),3) AS VARCHAR(3))) IN ('Sat','Sun','Mon')
GOTO FINISH


--####################################
-- Temp Tables
--####################################

IF (Object_ID('tempdb..##ERPStoreData') IS NOT NULL) DROP TABLE ##ERPStoreData
IF (Object_ID('tempdb..##ERPCountryList') IS NOT NULL) DROP TABLE ##ERPCountryList
IF (Object_ID('tempdb..##ERPMediaCash') IS NOT NULL) DROP TABLE ##ERPMediaCash
IF (Object_ID('tempdb..##ERPMediaCashAcct') IS NOT NULL) DROP TABLE ##ERPMediaCashAcct
IF (Object_ID('tempdb..##ERPMediaRec') IS NOT NULL) DROP TABLE ##ERPMediaRec
IF (Object_ID('tempdb..##ERPMediaRecSummary') IS NOT NULL) DROP TABLE ##ERPMediaRecSummary
IF (Object_ID('tempdb..##ERPMediaRecHeaders') IS NOT NULL) DROP TABLE ##ERPMediaRecHeaders
IF (Object_ID('tempdb..##ERPMediaRecOutput') IS NOT NULL) DROP TABLE ##ERPMediaRecOutput


--####################################
-- Declare script variables
--####################################

DECLARE @SQL VARCHAR(8000)
DECLARE @CMD VARCHAR(4000)
DECLARE @FileDate VARCHAR(14)
DECLARE @FileName VARCHAR(40)
DECLARE @FilePath VARCHAR(90)
DECLARE @ERPFilePath VARCHAR(90)
DECLARE @BackupFilePath VARCHAR(90)
DECLARE @TempFilePath VARCHAR(90)
DECLARE @TransactionStartDate AS INT
DECLARE @TransactionEndDate AS INT

DECLARE @ChkFileDrive VARCHAR(5)  
DECLARE @ChkFileCMD VARCHAR(200)
DECLARE @ChkFileCount VARCHAR(5)

DECLARE @Recipients VARCHAR(4000)
DECLARE @Copy_Recipients VARCHAR(4000)
DECLARE @Subject VARCHAR(80)
DECLARE @Query VARCHAR(8000)
DECLARE @Text nvarchar(max)



--####################################
-- Set Date range used by schedule
--####################################

-- Tue run for prior Wed-Thu sales:
IF (SELECT CAST(LEFT(DATENAME(dw,DATEADD(DAY,-0,GETDATE())),3) AS VARCHAR(3))) = 'Tue'
BEGIN
SET @TransactionStartDate = 6
SET @TransactionEndDate = 5
END

-- Wed run for prior Fri-Sat sales:
IF (SELECT CAST(LEFT(DATENAME(dw,DATEADD(DAY,-0,GETDATE())),3) AS VARCHAR(3))) = 'Wed'
BEGIN
SET @TransactionStartDate = 5
SET @TransactionEndDate = 4
END

-- Thu run for prior Sun-Mon sales:
IF (SELECT CAST(LEFT(DATENAME(dw,DATEADD(DAY,-0,GETDATE())),3) AS VARCHAR(3))) = 'Thu'
BEGIN
SET @TransactionStartDate = 4
SET @TransactionEndDate = 3
END

-- Fri run for prior Tue sales:
IF (SELECT CAST(LEFT(DATENAME(dw,DATEADD(DAY,-0,GETDATE())),3) AS VARCHAR(3))) = 'Fri'
BEGIN
SET @TransactionStartDate = 3
SET @TransactionEndDate = 3
END


--####################################
-- Set dates for manual execution
--####################################

-->>>>>>   Set dates then uncomment these two SET statements when running manually   <<<<<<--
--SET @TransactionStartDate = DATEDIFF(DAY, '02/04/2018', GETDATE())  --<< SET START DATE
--SET @TransactionEndDate = DATEDIFF(DAY, '02/04/2018', GETDATE())  --<< SET END DATE


--####################################
-- Build Store and Country info
--####################################

SELECT oc.ORG_CHN_NUM AS StrNum
	,oc.DFLT_CRNCY_CODE AS StrCrncyCode
	,ga.CNTRY_CODE_ISO3 AS StrCountry
	,CASE WHEN ga.CNTRY_CODE_ISO3 = 'USA' THEN '1100SAUDTCLEAR'
		WHEN ga.CNTRY_CODE_ISO3 = 'CAN' THEN '1700SAUDTCLEAR'
		WHEN ga.CNTRY_CODE_ISO3 = 'GBR' THEN '2110SAUDTCLEAR'
		WHEN ga.CNTRY_CODE_ISO3 = 'IRL' THEN '2110IRLCLEAR'
		WHEN ga.CNTRY_CODE_ISO3 = 'DNK' THEN '2300SAUDTCLEAR'
		WHEN ga.CNTRY_CODE_ISO3 = 'CHN' THEN '3001SAUDTCLEAR'
		END AS 'AcctCode'
	,CASE WHEN LEN(oc.ORG_CHN_NUM) <= 3 AND oc.ORG_CHN_NUM NOT IN (470,990,991,995)
		THEN '1' + RIGHT('00' + CONVERT(VARCHAR(3),oc.ORG_CHN_NUM),3)
		WHEN LEN(oc.ORG_CHN_NUM) = 4
		THEN CONVERT(VARCHAR(4),oc.ORG_CHN_NUM)
		END AS 'ERPStrNum'
INTO ##ERPStoreData
FROM auditworks.dbo.ORG_CHN oc  WITH (NOLOCK)
	JOIN	auditworks.dbo.SV_PRMY_ADDRESS spa  WITH (NOLOCK) ON oc.PRTY_ID = spa.PRTY_ID
	JOIN	auditworks.dbo.GEOG_ADRS ga  WITH (NOLOCK) ON spa.ADRS_ID = ga.ADRS_ID
WHERE oc.ORG_CHN_NUM BETWEEN 1 AND 3100
ORDER BY oc.ORG_CHN_NUM

SELECT ROW_NUMBER() OVER(ORDER BY StrCountry ASC) AS CountryID
	,StrCountry
INTO ##ERPCountryList
FROM ##ERPStoreData
WHERE StrCountry IN ('CAN','DNK','GBR','IRL','USA') --<< Add new countries here
GROUP BY StrCountry


--####################################
-- Cash
--####################################

SELECT a.store_no
	,a.transaction_date
	,'9007' line_object
	,SUM(a.rec_amount) AS expected_media_amount
INTO ##ERPMediaCash
FROM media_reconciliation_detail a WITH (NOLOCK)
	,media_reconciliation_status b WITH (NOLOCK)
WHERE a.store_no = b.balancing_entity
AND a.balancing_entity_id = b.balancing_entity_id
AND line_action = 247
AND b.rec_type IN (10,20,21)
AND a.line_object IN (600,601,602,619,625,9007)
AND a.transaction_date BETWEEN CONVERT(VARCHAR,DATEADD(DAY,-@TransactionStartDate,GETDATE()),111) AND CONVERT(VARCHAR,DATEADD(DAY,-@TransactionEndDate,GETDATE()),111)
--AND a.store_no IN (1,2,26,48,59,125,146,158,220,272)
GROUP BY a.store_no
	,a.transaction_date
ORDER BY a.store_no

SELECT a.*
	,b.StrCountry
	,b.StrCrncyCode
	,b.AcctCode
	,b.ERPStrNum
INTO ##ERPMediaRec
FROM ##ERPMediaCash a
	JOIN ##ERPStoreData b WITH (NOLOCK)
		ON a.store_no = b.StrNum


--####################################
-- Add Summary Totals
--####################################

INSERT INTO ##ERPMediaRec
SELECT '9999'
	,transaction_date
	,line_object
	,SUM(expected_media_amount)
	,StrCountry
	,StrCrncyCode
	,AcctCode
	,'9999'
FROM ##ERPMediaRec
GROUP BY line_object
	,transaction_date
	,StrCountry
	,StrCrncyCode
	,AcctCode


--####################################
-- Set variables
--####################################

SET @FileDate = (SELECT CONVERT(VARCHAR(8), GETDATE(), 112) + REPLACE(CONVERT(VARCHAR(8),GETDATE(), 108),':',''))

SET @FilePath = '\\saapp01\Financials\ERP'  --<< File path
SET @TempFilePath = '\\saapp01\Financials\ERP\Work'
SET @BackupFilePath = '\\saapp01\Financials\ERP\Backup'

--SET @ERPFilePath = '\\saapp01\Financials\ERP\Test'  --<< TEST build path
--SET @ERPFilePath = '\\ShareBear1\Shared\Accounting\ERP_Daily'  --<< PRE-PROD ERP file destination path
--SET @ERPFilePath = '\\stl-dynsnc-t-01\GeneralJournal\Test2\1100'  --<< TEST ERP file destination path
SET @ERPFilePath = '\\stl-dynsnc-p-01\oData\CashBankStatements'  --<< PROD ERP file destination path

--SET @Recipients = 'paulb@buildabear.com'
SET @Recipients = 'DawnGo@buildabear.com;MichaelBeiser@buildabear.com'
--SET @Copy_Recipients = 'SAAdmin@buildabear.com'


--####################################
-- Create Headers file
--####################################

SELECT 
	'As Of' AS 'As Of'
	,'Currency' AS 'Currency'
	,'BankID Type' AS 'BankID Type'
	,'BankID' AS 'BankID'
	,'Account' AS 'Account'
	,'Data Type' AS 'Data Type'
	,'BAI Code' AS 'BAI Code'
	,'Description' AS 'Description'
	,'Amount' AS 'Amount'
	,'Balance/Value Date' AS 'Balance/Value Date'
	,'Customer Reference' AS 'Customer Reference'
	,'Immediate Availability' AS 'Immediate Availability'
	,'1 Day Float' AS '1 Day Float'
	,'2+ DayFloat' AS '2+ DayFloat'
	,'Bank Reference' AS 'Bank Reference'
	,'# of Items' AS '# of Items'
	,'Text' AS 'Text'
INTO ##ERPMediaRecHeaders

SET @SQL = 'SELECT * FROM ##ERPMediaRecHeaders'

SELECT  @CMD = 'bcp "' + @SQL + '" queryout "' + @TempFilePath + '\SA_ERP_BANK_HEADERS.csv" -T -c -t,'
    SELECT  @CMD
    exec master..xp_cmdshell @CMD

--####################################
-- Create file for each country
--   loops through each country code
--   to create results & file output
--####################################

DECLARE @cntrycode VARCHAR(3)
DECLARE cntrycode CURSOR FOR  
SELECT StrCountry
FROM ##ERPCountryList 
ORDER BY CountryID  
  
--open cursor  
OPEN cntrycode  
  
FETCH next  
 FROM cntrycode  
 INTO @cntrycode  

WHILE @@fetch_status = 0  

BEGIN

IF (Object_ID('tempdb..##ERPMediaRecOutput') IS NOT NULL) DROP TABLE ##ERPMediaRecOutput

SELECT CONVERT(VARCHAR(10), GETDATE(), 101) AS 'As Of'
	,StrCrncyCode AS 'Currency'
	,'ABA' AS 'BankID Type'
	,'123456789' AS 'BankID'
	,AcctCode AS 'Account'
	,CASE WHEN ERPStrNum = '9999' THEN 'Debits'
		ELSE 'Credits'
		END AS 'Data Type'
	,CASE WHEN ERPStrNum = '9999' THEN '699'
		ELSE '399'
		END AS 'BAI Code'
	,CASE WHEN ERPStrNum = '9999' THEN 'Disbursement'
		ELSE 'Deposit'
		END AS 'Description'
	,CONVERT(DECIMAL(10,2),expected_media_amount) AS 'Amount'
	,NULL AS 'Balance/Value Date'
	,ERPStrNum AS 'Customer Reference'
	,NULL AS 'Immediate Availability'
	,NULL AS '1 Day Float'
	,NULL AS '2+ DayFloat'
	,CONVERT(VARCHAR(8), transaction_date, 112) + ERPStrNum AS 'Bank Reference'
	,NULL AS '# of Items'
	,CONVERT(VARCHAR(8), transaction_date, 112) + ERPStrNum AS 'Text'
INTO ##ERPMediaRecOutput
FROM ##ERPMediaRec WITH (NOLOCK)
WHERE StrCountry = @cntrycode
AND expected_media_amount != 0
ORDER BY transaction_date
	,ERPStrNum
	

SET @FileName = '\ERP_DAILY_SA_BANK_' + @cntrycode + '_' + @FileDate

SET @SQL = 'SELECT * FROM ##ERPMediaRecOutput'

SELECT  @CMD = 'bcp "' + @SQL + '" queryout "' + @TempFilePath + '\SA_ERP_BANK_RESULTS_' + @cntrycode + '.csv" -T -c -t,'
    select  @CMD
    exec master..xp_cmdshell @CMD

SET @CMD = 'type ' + @TempFilePath + '\SA_ERP_BANK_HEADERS.csv > ' + @FilePath + @FileName + '.dat'
    select  @CMD
    exec master..xp_cmdshell @CMD

SET @CMD = 'type ' + @TempFilePath + '\SA_ERP_BANK_RESULTS_' + @cntrycode + '.csv >> ' + @FilePath + @FileName + '.dat'
    select  @CMD
    exec master..xp_cmdshell @CMD
	
FETCH next  
 FROM cntrycode  
 INTO @cntrycode  
END  
  
CLOSE cntrycode
DEALLOCATE cntrycode


--####################################
-- File copy and rename to ERP
--####################################

SET @CMD = 'xcopy /y /v /f /r  ' + @FilePath + '\*.dat ' + @ERPFilePath
    select  @CMD
    exec master..xp_cmdshell @CMD

WAITFOR DELAY '00:00:05'

SET @CMD = 'rename ' + @ERPFilePath + '\*.dat *.csv'
    select  @CMD
    exec master..xp_cmdshell @CMD

SET @CMD = 'rename ' + @FilePath + '\*.dat *.csv'
    select  @CMD
    exec master..xp_cmdshell @CMD


--####################################
-- File cleanup
--####################################

SET @CMD = 'del /Q ' + @TempFilePath + '\SA_ERP_BANK_*.csv'
    select  @CMD
    exec master..xp_cmdshell @CMD

SET @CMD = 'move /Y ' + @FilePath + '\*.csv ' + @BackupFilePath
    select  @CMD
    exec master..xp_cmdshell @CMD

WAITFOR DELAY '00:00:05'


--####################################
-- File check and email completion
--####################################

IF (Object_ID('tempdb..#filecheck') IS NOT NULL) DROP TABLE #filecheck
CREATE TABLE #filecheck (dirtext VARCHAR(50))

SET @ChkFileDrive = 'v:'  
SET @ChkFileCMD = 'net use ' + @ChkFileDrive + ' /d'  
EXEC master..xp_cmdshell @ChkFileCMD  
SET @ChkFileCMD = 'net use ' + @ChkFileDrive + ' \\saapp01\Financials\ERP\Backup'  
EXEC master..xp_cmdshell @ChkFileCMD  
SET @ChkFileCMD = 'dir /B ' + @ChkFileDrive + '\ERP_DAILY_SA_BANK_*_' + @FileDate + '.csv'  
INSERT INTO #filecheck (dirtext)
EXEC master..xp_cmdshell @ChkFileCMD 
DELETE FROM #filecheck WHERE dirtext IS NULL OR dirtext = 'File Not Found'

SET @CMD = 'forfiles /p ' + @ChkFileDrive + ' /s /m *.csv /D -40 /C "cmd /c del @path"'
    select  @CMD
    exec master..xp_cmdshell @CMD

SET @ChkFileCMD = 'net use ' + @ChkFileDrive + ' /d'
EXEC master..xp_cmdshell @ChkFileCMD

SET @ChkFileCount = (SELECT COUNT(*) FROM #filecheck)

IF (SELECT COUNT(*) FROM #filecheck) != (SELECT COUNT(*) FROM ##ERPCountryList)
GOTO ERROREMAIL

SET @Text = 
		'<font face =arial size = 2>' +
		'Daily SA export files have been created for ERP import to D365 for Bank Settlement. <br>' +
		'Data date range: ' + CONVERT(VARCHAR,DATEADD(DAY,-@TransactionStartDate,GETDATE()),101) + ' - ' + CONVERT(VARCHAR,DATEADD(DAY,-@TransactionEndDate,GETDATE()),101) + '<br>' +
		'<br>' +
		'(' + @ChkFileCount + ') Files found in ' + @BackupFilePath + '... <br>' +
		'<br>' +
		'<table border="1">' + 
		'<font face =arial size = 2>' +
		'<tr bgcolor=#D5D5F7><th>ERP Daily SA file name</th></tr>' +
		CAST ( ( SELECT [td/@align]='left',
						td = dirtext, ''
				FROM #filecheck
				FOR xml path ('tr'), type
		) AS NVARCHAR(MAX) ) +
		'</table>' +
		'<font face =arial size = 2>' +
		'<br>' +
		'The files listed above have been copied to ' + @ERPFilePath + ' for processing into D365. <br>' +
		'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Files are moved to Archive folder if processed successfully. <br>' +
		'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Files are moved to Error folder if processing fails. <br>' +
		'<font face =arial size = 1 color="#C0C0C0">' +
		'<br><br><br><br>' +
		'Server:  BEDROCKDB01 <br>' +
		'Job Name:  ERP_Daily_Files_Export <br>' +
		'Stored Proc:  BEDROCKDB01.auditworks.dbo.spERP_Daily_Banking_Totals_Export <br>' +
		'Created by:  Paul Beckman <br>' +
		'Team Ownership:  Enterprise Systems <br>'

SET @Subject = 'ERP Daily Export files created (Bank)'
	EXEC msdb.dbo.sp_send_dbmail  
	@profile_name = 'EntSysSupport',
	@recipients = @Recipients,
	@copy_recipients = @Copy_Recipients,
	@subject = @Subject, 
	@body = @Text,
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
	'spERP_Daily_Banking_Totals_Export', --<< Stored Proc name
	GETDATE(),
	'No', --<< Issues found - Yes / No
	'No', --<< Action required - Yes / No
	'Yes', --<< Notification sent - Yes / No
	'Notification Only', --<< Email type - Notification Only / Alert / Warning
	@Recipients, --<< Email TO
	NULL, --<< Email CC
	@Subject, --<< Email Subject
	'Daily SA export files have been created for ERP import to D365 for Bank Settlement' --<< Comment
	)

GOTO FINISH

ERROREMAIL:

SET @Recipients = 'EntSysSupport@buildabear.com'
SET @Copy_Recipients = 'DawnGo@buildabear.com;MichaelBeiser@buildabear.com'
IF (SELECT COUNT(*) FROM #filecheck) = 0
BEGIN
SET @Text = 
		'<font face =arial size = 2 color="Red">' +
		'** ACTION REQUIRED **  <br>' +
		'<br>' +
		'Daily SA export files Missing for ERP import to D365 for Bank Settlement. <br>' +
		'Data date range: ' + CONVERT(VARCHAR,DATEADD(DAY,-@TransactionStartDate,GETDATE()),101) + ' - ' + CONVERT(VARCHAR,DATEADD(DAY,-@TransactionEndDate,GETDATE()),101) + '<br>' +
		'<br>' +
		'Please check on status of SQL job execution. <br>' +
		'<br>' +
		'(' + @ChkFileCount + ') ERP_DAILY_SA_BANK_*_' + @FileDate + '.csv Files found in ' + @BackupFilePath + '... <br>' +
		'<font face =arial size = 1 color="#C0C0C0">' +
		'<br><br><br><br>' +
		'Server:  BEDROCKDB01 <br>' +
		'Job Name:  ERP_Daily_Files_Export <br>' +
		'Stored Proc:  BEDROCKDB01.auditworks.dbo.spERP_Daily_Banking_Totals_Export <br>' +
		'Created by:  Paul Beckman <br>' +
		'Team Ownership:  Enterprise Systems <br>'

SET @Subject = 'WARNING - Missing all (' + CONVERT(VARCHAR(1),(SELECT COUNT(*) FROM ##ERPCountryList)-@ChkFileCount) + ') ERP Daily Export files (Bank)'
	EXEC msdb.dbo.sp_send_dbmail  
	@profile_name = 'EntSysSupport',
	@recipients = @Recipients,
	@copy_recipients = @Copy_Recipients,
	@subject = @Subject, 
	@body = @Text,
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
	'spERP_Daily_Banking_Totals_Export', --<< Stored Proc name
	GETDATE(),
	'Yes', --<< Issues found - Yes / No
	'Yes', --<< Action required - Yes / No
	'Yes', --<< Notification sent - Yes / No
	'Warning', --<< Email type - Notification Only / Alert / Warning
	@Recipients, --<< Email TO
	@Copy_Recipients, --<< Email CC
	@Subject, --<< Email Subject
	'All Daily SA export files Missing for ERP import to D365 for Bank Settlement' --<< Comment
	)
END
ELSE
BEGIN
SET @Text = 
		'<font face =arial size = 2 color="Red">' +
		'** ACTION REQUIRED **  <br>' +
		'<br>' +
		'Daily SA export files Missing for ERP import to D365 for Bank Settlement. <br>' +
		'Data date range: ' + CONVERT(VARCHAR,DATEADD(DAY,-@TransactionStartDate,GETDATE()),101) + ' - ' + CONVERT(VARCHAR,DATEADD(DAY,-@TransactionEndDate,GETDATE()),101) + '<br>' +
		'<br>' +
		'Please check on status of SQL job execution. <br>' +
		'<br>' +
		'(' + @ChkFileCount + ') ERP_DAILY_SA_BANK_*_' + @FileDate + '.csv Files found in ' + @BackupFilePath + '... <br>' +
		'<br>' +
		'<table border="1">' + 
		'<font face =arial size = 2>' +
		'<tr bgcolor=#D5D5F7><th>ERP Daily SA file name</th></tr>' +
		CAST ( ( SELECT [td/@align]='left',
						td = dirtext, ''
				FROM #filecheck
				FOR xml path ('tr'), type
		) AS NVARCHAR(MAX) ) +
		'</table>' +
		'<font face =arial size = 1 color="#C0C0C0">' +
		'<br><br><br><br>' +
		'Server:  BEDROCKDB01 <br>' +
		'Job Name:  ERP_Daily_Files_Export <br>' +
		'Stored Proc:  BEDROCKDB01.auditworks.dbo.spERP_Daily_Banking_Totals_Export <br>' +
		'Created by:  Paul Beckman <br>' +
		'Team Ownership:  Enterprise Systems <br>'

SET @Subject = 'ALERT - Missing (' + CONVERT(VARCHAR(1),(SELECT COUNT(*) FROM ##ERPCountryList)-@ChkFileCount) + ') ERP Daily Export files (Bank)'
	EXEC msdb.dbo.sp_send_dbmail  
	@profile_name = 'EntSysSupport',
	@recipients = @Recipients,
	@copy_recipients = @Copy_Recipients,
	@subject=@Subject, 
	@body = @Text,
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
	'spERP_Daily_Banking_Totals_Export', --<< Stored Proc name
	GETDATE(),
	'Yes', --<< Issues found - Yes / No
	'Yes', --<< Action required - Yes / No
	'Yes', --<< Notification sent - Yes / No
	'Alert', --<< Email type - Notification Only / Alert / Warning
	@Recipients, --<< Email TO
	@Copy_Recipients, --<< Email CC
	@Subject, --<< Email Subject
	'Some Daily SA export files Missing for ERP import to D365 for Bank Settlement' --<< Comment
	)
END



FINISH:
--####################################
-- Temp Table Cleanup
--####################################

IF (Object_ID('tempdb..##ERPStoreData') IS NOT NULL) DROP TABLE ##ERPStoreData
IF (Object_ID('tempdb..##ERPCountryList') IS NOT NULL) DROP TABLE ##ERPCountryList
IF (Object_ID('tempdb..##ERPMediaCash') IS NOT NULL) DROP TABLE ##ERPMediaCash
IF (Object_ID('tempdb..##ERPMediaCashAcct') IS NOT NULL) DROP TABLE ##ERPMediaCashAcct
IF (Object_ID('tempdb..##ERPMediaRec') IS NOT NULL) DROP TABLE ##ERPMediaRec
IF (Object_ID('tempdb..##ERPMediaRecSummary') IS NOT NULL) DROP TABLE ##ERPMediaRecSummary
IF (Object_ID('tempdb..##ERPMediaRecHeaders') IS NOT NULL) DROP TABLE ##ERPMediaRecHeaders
IF (Object_ID('tempdb..##ERPMediaRecOutput') IS NOT NULL) DROP TABLE ##ERPMediaRecOutput
IF (Object_ID('tempdb..#filecheck') IS NOT NULL) DROP TABLE #filecheck


--####################################





/*

SELECT * FROM ##ERPStoreData
WHERE StrCrncyCode = 'CAD'
AND StrCountry = 'USA'

SELECT * FROM ##ERPCountryList

SELECT * FROM ##ERPMediaCash

SELECT * FROM ##ERPMediaCashAcct

SELECT * FROM ##ERPMediaRec ORDER by 1,2
WHERE store_no = 9999

SELECT * FROM ##ERPMediaRecSummary
WHERE PAYMENTREFERENCE = 9999

SELECT * FROM ##ERPMediaRecHeaders

SELECT * FROM ##ERPMediaRecOutput
WHERE PAYMENTREFERENCE = 9999

SELECT * FROM #filecheck


*/
```

