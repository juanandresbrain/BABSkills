# dbo.spMerchandisingEmailWMTPMDirectoryErrors

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMerchandisingEmailWMTPMDirectoryErrors"]
    dbo_sp_send_dbmail(["dbo.sp_send_dbmail"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.sp_send_dbmail |

## Stored Procedure Code

```sql
CREATE procedure [dbo].[spMerchandisingEmailWMTPMDirectoryErrors]
as
set nocount on
-- =====================================================================================================
-- Name: spMerchandisingEmailWMTPMDirectoryErrors
--
-- Description: Export to merch_report
--
-- Input:	
--
-- Output: 
--
-- Dependencies: 
--				 
-- Revision History
--		Name:			Date:			Comments: This Proc is replaces existing DTS pkg on Beehive called Validation_WM_TPM_Driectories_Errors
--		Dan Tweedie 	    03/06/2015		Created proc.	
--		Lizzy Timm							Updated proc to exclude WM checks as it is no longer needed with the WM upgrade.
-- =====================================================================================================
DECLARE @cmd VARCHAR(500)
	,@path VARCHAR(200)

SET @path = '\\Wmtpmdb\e$\TPMInterfaces\Host_TPM_Order\90_TPM_Order_Errors'
SET @cmd = 'master..xp_cmdshell ''dir ' + @path + '\*.xml /X /B'''

IF (Object_ID('tempdb..#filelist1') IS NOT NULL) DROP TABLE #filelist1
CREATE TABLE #filelist1 (NAME VARCHAR(100) NULL)

INSERT #filelist1
EXEC (@cmd)

if (SELECT count(*) FROM #filelist1 WHERE NAME LIKE '%.xml') > 0

	begin
		EXEC msdb.dbo.sp_send_dbmail 
			@profile_name = 'MerchAdmin',
			@recipients='EntSysSupport@buildabear.com',
			@body = '"There are rejected files in this directory: \\Wmtpmdb\e$\TPMInterfaces\Host_TPM_Order\90_TPM_Order_Errors"',
			@subject = '"TPM File Directory Check - PROBLEM"'
	end 

IF (Object_ID('tempdb..#filelist2') IS NOT NULL) DROP TABLE #filelist2
CREATE TABLE #filelist2 (NAME VARCHAR(100) NULL)

SET @path = '\\Wmtpmdb\e$\TPMInterfaces\Host_TPM_Org\90_TPM_Org_Errors'
SET @cmd = 'master..xp_cmdshell ''dir ' + @path + '\*.xml /X /B'''

INSERT #filelist2
EXEC (@cmd)

if (SELECT count(*) FROM #filelist2 WHERE NAME LIKE '%.xml') > 0

	begin
		EXEC msdb.dbo.sp_send_dbmail 
			@profile_name = 'MerchAdmin',
			@recipients = 'EntSysSupport@buildabear.com',
			@body = '"There are rejected files in this directory: \\Wmtpmdb\e$\TPMInterfaces\Host_TPM_Org\90_TPM_Org_Errors"',
			@subject = '"TPM File Directory Check - PROBLEM"'
	end

IF (Object_ID('tempdb..#filelist3') IS NOT NULL) DROP TABLE #filelist3
CREATE TABLE #filelist3 (NAME VARCHAR(100) NULL)

-- Begin comment out for WM upgrade cutover

SET @path = '\\wminteg01\d$\Interfaces\ItemMaster\Failure'
SET @cmd = 'master..xp_cmdshell ''dir ' + @path + '\*.xml /X /B'''

INSERT #filelist3
EXEC (@cmd)

if (SELECT count(*) FROM #filelist3 WHERE NAME LIKE '%.xml') > 0
	begin
		EXEC msdb.dbo.sp_send_dbmail 
			@profile_name = 'MerchAdmin',
			@recipients = 'EntSysSupport@buildabear.com',
			@body = '"There are rejected files in this directory: \\wminteg01\d$\Interfaces\ItemMaster\Failure"',
			@subject = '"WM File Directory Check - PROBLEM"'
	end
----------------------------------------------------------------------- 4
IF (Object_ID('tempdb..#filelist4') IS NOT NULL) DROP TABLE #filelist4
CREATE TABLE #filelist4 (NAME VARCHAR(100) NULL)

SET @path = '\\wminteg01\d$\Interfaces\StoreDistro\Failure'
SET @cmd = 'master..xp_cmdshell ''dir ' + @path + '\*.xml /X /B'''

INSERT #filelist4
EXEC (@cmd)

if (SELECT count(*) FROM #filelist4 WHERE NAME LIKE '%.xml') > 0
	begin
		EXEC msdb.dbo.sp_send_dbmail 
			@profile_name = 'MerchAdmin',
			@recipients = 'EntSysSupport@buildabear.com',
			@body = '"There are rejected files in this directory: \\wminteg01\d$\Interfaces\StoreDistro\Failure"',
			@subject = '"WM File Directory Check - PROBLEM"'
	end
-------------------------------------------------------------------------- 5 
IF (Object_ID('tempdb..#filelist5') IS NOT NULL) DROP TABLE #filelist5
CREATE TABLE #filelist5 (NAME VARCHAR(100) NULL)

SET @path = '\\wminteg01\d$\Interfaces\StoreMaster\Failure'
SET @cmd = 'master..xp_cmdshell ''dir ' + @path + '\*.xml /X /B'''

INSERT #filelist5
EXEC (@cmd)

if (SELECT count(*) FROM #filelist5 WHERE NAME LIKE '%.xml') > 0
	begin
		EXEC msdb.dbo.sp_send_dbmail 
			@profile_name = 'MerchAdmin',
			@recipients='EntSysSupport@buildabear.com ',
			@body = '"There are rejected files in this directory: \\wminteg01\d$\Interfaces\StoreMaster\Failure"',
			@subject = '"WM File Directory Check - PROBLEM"'
	end
-------------------------------------------------------------------------- 6
IF (Object_ID('tempdb..#filelist6') IS NOT NULL) DROP TABLE #filelist6
CREATE TABLE #filelist6 (NAME VARCHAR(100) NULL)

SET @path = '\\wminteg01\d$\Interfaces\VendorMaster\Failure'
SET @cmd = 'master..xp_cmdshell ''dir ' + @path + '\*.xml /X /B'''

INSERT #filelist6
EXEC (@cmd)

if (SELECT count(*) FROM #filelist6 WHERE NAME LIKE '%.xml') > 0
	begin
		EXEC msdb.dbo.sp_send_dbmail 
			@profile_name = 'MerchAdmin',
			@recipients='EntSysSupport@buildabear.com ',
			@body = '"There are rejected files in this directory: \\wminteg01\d$\Interfaces\VendorMaster\Failure"',
			@subject = '"WM File Directory Check - PROBLEM"'
	end
------------------------------------------------ 7 
IF (Object_ID('tempdb..#filelist7') IS NOT NULL) DROP TABLE #filelist7
CREATE TABLE #filelist7 (NAME VARCHAR(100) NULL)

SET @path = '\\wminteg01\d$\Interfaces\XRef\Failure'
SET @cmd = 'master..xp_cmdshell ''dir ' + @path + '\*.xml /X /B'''

INSERT #filelist7
EXEC (@cmd)

if (SELECT count(*) FROM #filelist7 WHERE NAME LIKE '%.xml') > 0
	begin
		EXEC msdb.dbo.sp_send_dbmail 
			@profile_name = 'MerchAdmin',
			@recipients='EntSysSupport@buildabear.com',
			@body = '"There are rejected files in this directory: \\wminteg01\d$\Interfaces\XRef\Failure"',
			@subject = '"WM File Directory Check - PROBLEM"'
	end

-- End comment out for WM upgrade cutover
```

