# dbo.spMerchandisingFTPgetDDCAdjustments

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMerchandisingFTPgetDDCAdjustments"]
    dbo_ftpDELLogAdjustments(["dbo.ftpDELLogAdjustments"]) --> SP
    dbo_ftpDIRLogAdjustments(["dbo.ftpDIRLogAdjustments"]) --> SP
    dbo_ftpGETLogAdjustments(["dbo.ftpGETLogAdjustments"]) --> SP
    dbo_ftpPUTLogAdjustments(["dbo.ftpPUTLogAdjustments"]) --> SP
    dbo_sp_send_dbmail(["dbo.sp_send_dbmail"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ftpDELLogAdjustments |
| dbo.ftpDIRLogAdjustments |
| dbo.ftpGETLogAdjustments |
| dbo.ftpPUTLogAdjustments |
| dbo.sp_send_dbmail |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spMerchandisingFTPgetDDCAdjustments]
as

-- =====================================================================================================
-- Name: spMerchandisingFTPgetDDCAdjustments
--
-- Description:	FTP's to DDC server to retrieve Adjustments files.
--				Captures log, sends email if failure occurs.
--
-- Input:	NA
--
-- Output: log file and emails only if failure occurs
--
-- Dependencies: NA
--				 
-- Revision History
--		Name:			Date:			Comments:
--		Dan Tweedie		10/08/2010		Created proc.	
--		Dan Tweedie		07/14/2015		Pointed to Kermode instead of oursmerchdb01
-- =====================================================================================================


set nocount on

--declare and set ftp variables 
declare @ftpDIR varchar(1000),
		@ftpGET varchar(1000),
		@ftpPUT varchar(1000),
		@ftpDEL varchar(1000),
		@Log_query varchar(1000),
		@Log_filename varchar(100),
		@Log_file_location varchar(100),
		@Log_bcp varchar(1000),
		@body varchar(4000)
		
set @ftpDIR = 'ftp -d -s:\\kermode\FileRepository\MERCHANDISING\WC_Distro\STOCKADJ\FTP\SCRIPTS\ftpDIR.txt' 
set @ftpGET = 'ftp -d -s:\\kermode\FileRepository\MERCHANDISING\WC_Distro\STOCKADJ\FTP\SCRIPTS\ftpGET.txt' 
set @ftpPUT = 'ftp -d -s:\\kermode\FileRepository\MERCHANDISING\WC_Distro\STOCKADJ\FTP\SCRIPTS\ftpPUT.txt' 
set @ftpDEL = 'ftp -d -s:\\kermode\FileRepository\MERCHANDISING\WC_Distro\STOCKADJ\FTP\SCRIPTS\ftpDEL.txt'

--create temp tables for ftp logs
IF (Object_ID('me_01..ftpDIRLogAdjustments') IS NOT NULL) DROP TABLE ftpDIRLogAdjustments
create table ftpDIRLogAdjustments
(ftpLog varchar(4000))

IF (Object_ID('me_01..ftpGETLogAdjustments') IS NOT NULL) DROP TABLE ftpGETLogAdjustments
create table ftpGETLogAdjustments
(ftpLog varchar(4000))

IF (Object_ID('me_01..ftpPUTLogAdjustments') IS NOT NULL) DROP TABLE ftpPUTLogAdjustments
create table ftpPUTLogAdjustments
(ftpLog varchar(4000))

IF (Object_ID('me_01..ftpDELLogAdjustments') IS NOT NULL) DROP TABLE ftpDELLogAdjustments
create table ftpDELLogAdjustments
(ftpLog varchar(4000))

--execute sql/ftp
----connect to ftp server, if connection unsuccessful, send email
insert ftpDIRLogAdjustments exec master..xp_cmdshell @ftpDIR
if (select count(*) from ftpDIRLogAdjustments where ftplog like '%Welcome%') < 1
	begin

		set @Log_query = 'select * from me_01.dbo.ftpDIRLogAdjustments'
		set @Log_filename = 'ftpDIRLog.txt'
		set @Log_file_location = '\\kermode\FileRepository\MERCHANDISING\WC_Distro\STOCKADJ\FTP\LOGS\'
		set @Log_bcp = 'bcp "' + @Log_query + '" queryout "' + @Log_file_location + @Log_filename + '" -t, -T -c -Sbedrockdb02'

		exec master..xp_cmdshell @Log_bcp
			
		set @body =	'An attempt to connect to the DDC FTP server failed.' 
					+ char(10) + char(13) + 
					'See the attached log for details.'
					+ char(10) + char(13) + 
					+ char(10) + char(13) + 
					'This process is managed by me_01.dbo.spMerchandisingFTPgetDDCAdjustments'

		EXEC msdb.dbo.sp_send_dbmail
		@profile_name = 'MerchAdmin',
		@recipients = 'merchadmin@buildabear.com',
		@subject = 'FTP Failure: Connection Failed',
		@body = @body,
		@file_attachments = '\\kermode\FileRepository\MERCHANDISING\WC_Distro\STOCKADJ\FTP\LOGS\ftpDIRLog.txt',
		@importance = 'HIGH'
	
	end
	

--if Adjustments file is present, continue
if (select count(*) from ftpDIRLogAdjustments where ftplog like '%IA%.txt%') > 0 

	BEGIN
	insert ftpGETLogAdjustments exec master..xp_cmdshell @ftpGET

			if (select count(*) from ftpGETLogAdjustments where ftplog like '%Transfer OK%') < 1
			begin
			
				set @Log_query = 'select * from me_01.dbo.ftpGETLogAdjustments'
				set @Log_filename = 'ftpGETLog.txt'
				set @Log_file_location = '\\kermode\FileRepository\MERCHANDISING\WC_Distro\STOCKADJ\FTP\LOGS\'
				set @Log_bcp = 'bcp "' + @Log_query + '" queryout "' + @Log_file_location + @Log_filename + '" -t, -T -c -Sbedrockdb02'

				exec master..xp_cmdshell @Log_bcp
										
				set @body =	'An attempt to FTP a Adjustments file from DDC to BAB failed.' 
							+ char(10) + char(13) + 
							'See the attached log for details.'
							+ char(10) + char(13) + 
							+ char(10) + char(13) + 
							'This process is managed by me_01.dbo.spMerchandisingFTPgetDDCAdjustments'
		
				EXEC msdb.dbo.sp_send_dbmail
				@profile_name = 'MerchAdmin',
				@recipients = 'merchadmin@buildabear.com',
				@subject = 'FTP Failure: Adjustments file from DDC to BAB',
				@body = @body,
				@file_attachments = '\\kermode\FileRepository\MERCHANDISING\WC_Distro\STOCKADJ\FTP\LOGS\ftpGETLog.txt',
				@importance = 'HIGH'
						
			end
			
		insert ftpPUTLogAdjustments exec master..xp_cmdshell @ftpPUT
		if (select count(*) from ftpPUTLogAdjustments where ftplog like '%Transfer OK%') < 1
			begin
				set @Log_query = 'select * from me_01.dbo.ftpPUTLogAdjustments'
				set @Log_filename = 'ftpPUTLog.txt'
				set @Log_file_location = '\\kermode\FileRepository\MERCHANDISING\WC_Distro\STOCKADJ\FTP\LOGS\'
				set @Log_bcp = 'bcp "' + @Log_query + '" queryout "' + @Log_file_location + @Log_filename + '" -t, -T -c -Sbedrockdb02'

				exec master..xp_cmdshell @Log_bcp
										
				set @body =	'An attempt to FTP a Adjustments file from BAB to DDC DONE folder failed.' 
							+ char(10) + char(13) + 
							'See the attached log for details.'
							+ char(10) + char(13) + 
							+ char(10) + char(13) + 
							'This process is managed by me_01.dbo.spMerchandisingFTPgetDDCAdjustments'
		
				EXEC msdb.dbo.sp_send_dbmail
				@profile_name = 'MerchAdmin',
				@recipients = 'merchadmin@buildabear.com',
				@subject = 'FTP Failure: Adjustments file from BAB to DDC DONE folder',
				@body = @body,
				@file_attachments = '\\kermode\FileRepository\MERCHANDISING\WC_Distro\STOCKADJ\FTP\LOGS\ftpPUTLog.txt',
				@importance = 'HIGH'
			end
			
		insert ftpDELLogAdjustments exec master..xp_cmdshell @ftpDEL
	
		if (select count(*) from ftpDELLogAdjustments where ftplog like '%File deleted successfully%') < 1
			begin
				set @Log_query = 'select * from me_01.dbo.ftpDELLogAdjustments'
				set @Log_filename = 'ftpDELLog.txt'
				set @Log_file_location = '\\kermode\FileRepository\MERCHANDISING\WC_Distro\STOCKADJ\FTP\LOGS\'
				set @Log_bcp = 'bcp "' + @Log_query + '" queryout "' + @Log_file_location + @Log_filename + '" -t, -T -c -Sbedrockdb02'

				exec master..xp_cmdshell @Log_bcp
										
				set @body =	'An attempt to DELETE a Adjustments file on the DDC server failed.' 
							+ char(10) + char(13) + 
							'See the attached log for details.'
							+ char(10) + char(13) + 
							+ char(10) + char(13) + 
							'This process is managed by me_01.dbo.spMerchandisingFTPgetDDCAdjustments'
		
				EXEC msdb.dbo.sp_send_dbmail
				@profile_name = 'MerchAdmin',
				@recipients = 'merchadmin@buildabear.com',
				@subject = 'FTP Failure: Delete Adjustments file DDC server',
				@body = @body,
				@file_attachments = '\\kermode\FileRepository\MERCHANDISING\WC_Distro\STOCKADJ\FTP\LOGS\ftpDELLog.txt',
				@importance = 'HIGH'
			end
			

END
```

