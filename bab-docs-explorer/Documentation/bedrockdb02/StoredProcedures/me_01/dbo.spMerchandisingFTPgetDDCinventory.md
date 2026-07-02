# dbo.spMerchandisingFTPgetDDCinventory

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMerchandisingFTPgetDDCinventory"]
    dbo_ftpDELLoginventory(["dbo.ftpDELLoginventory"]) --> SP
    dbo_ftpDIRLoginventory(["dbo.ftpDIRLoginventory"]) --> SP
    dbo_ftpGETLoginventory(["dbo.ftpGETLoginventory"]) --> SP
    dbo_ftpPUTLoginventory(["dbo.ftpPUTLoginventory"]) --> SP
    dbo_sp_send_dbmail(["dbo.sp_send_dbmail"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ftpDELLoginventory |
| dbo.ftpDIRLoginventory |
| dbo.ftpGETLoginventory |
| dbo.ftpPUTLoginventory |
| dbo.sp_send_dbmail |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spMerchandisingFTPgetDDCinventory]
as

-- =====================================================================================================
-- Name: spMerchandisingFTPgetDDCinventory
--
-- Description:	FTP's to DDC server to retrieve inventory files.
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
		
set @ftpDIR = 'ftp -d -s:\\kermode\FileRepository\MERCHANDISING\WC_Distro\INVENTORY\FTP\SCRIPTS\ftpDIR.txt' 
set @ftpGET = 'ftp -d -s:\\kermode\FileRepository\MERCHANDISING\WC_Distro\INVENTORY\FTP\SCRIPTS\ftpGET.txt' 
set @ftpPUT = 'ftp -d -s:\\kermode\FileRepository\MERCHANDISING\WC_Distro\INVENTORY\FTP\SCRIPTS\ftpPUT.txt' 
set @ftpDEL = 'ftp -d -s:\\kermode\FileRepository\MERCHANDISING\WC_Distro\INVENTORY\FTP\SCRIPTS\ftpDEL.txt'

--create temp tables for ftp logs
IF (Object_ID('me_01..ftpDIRLoginventory') IS NOT NULL) DROP TABLE ftpDIRLoginventory
create table ftpDIRLoginventory
(ftpLog varchar(4000))

IF (Object_ID('me_01..ftpGETLoginventory') IS NOT NULL) DROP TABLE ftpGETLoginventory
create table ftpGETLoginventory
(ftpLog varchar(4000))

IF (Object_ID('me_01..ftpPUTLoginventory') IS NOT NULL) DROP TABLE ftpPUTLoginventory
create table ftpPUTLoginventory
(ftpLog varchar(4000))

IF (Object_ID('me_01..ftpDELLoginventory') IS NOT NULL) DROP TABLE ftpDELLoginventory
create table ftpDELLoginventory
(ftpLog varchar(4000))

--execute sql/ftp
----connect to ftp server, if connection unsuccessful, send email
insert ftpDIRLoginventory exec master..xp_cmdshell @ftpDIR
if (select count(*) from ftpDIRLoginventory where ftplog like '%Welcome%') < 1
	begin

		set @Log_query = 'select * from me_01.dbo.ftpDIRLoginventory'
		set @Log_filename = 'ftpDIRLog.txt'
		set @Log_file_location = '\\kermode\FileRepository\MERCHANDISING\WC_Distro\INVENTORY\FTP\LOGS\'
		set @Log_bcp = 'bcp "' + @Log_query + '" queryout "' + @Log_file_location + @Log_filename + '" -t, -T -c -Sbedrockdb02'

		exec master..xp_cmdshell @Log_bcp
			
		set @body =	'An attempt to connect to the DDC FTP server failed.' 
					+ char(10) + char(13) + 
					'See the attached log for details.'
					+ char(10) + char(13) + 
					+ char(10) + char(13) + 
					'This process is managed by me_01.dbo.spMerchandisingFTPgetDDCinventory'

		EXEC msdb.dbo.sp_send_dbmail
		@profile_name = 'MerchAdmin',
		@recipients = 'merchadmin@buildabear.com',
		@subject = 'FTP Failure: Connection Failed',
		@body = @body,
		@file_attachments = '\\kermode\FileRepository\MERCHANDISING\WC_Distro\INVENTORY\FTP\LOGS\ftpDIRLog.txt',
		@importance = 'HIGH'
	
	end
--if inventory file is present, continue
if (select count(*) from ftpDIRLoginventory where ftplog like '%Inventory%.txt%') > 0 

	BEGIN

		insert ftpGETLoginventory exec master..xp_cmdshell @ftpGET
		if (select count(*) from ftpGETLoginventory where ftplog like '%Transfer OK%') < 1
			begin
			
				set @Log_query = 'select * from me_01.dbo.ftpGETLoginventory'
				set @Log_filename = 'ftpGETLog.txt'
				set @Log_file_location = '\\kermode\FileRepository\MERCHANDISING\WC_Distro\INVENTORY\FTP\LOGS\'
				set @Log_bcp = 'bcp "' + @Log_query + '" queryout "' + @Log_file_location + @Log_filename + '" -t, -T -c -Sbedrockdb02'

				exec master..xp_cmdshell @Log_bcp
										
				set @body =	'An attempt to FTP a inventory file from DDC to BAB failed.' 
							+ char(10) + char(13) + 
							'See the attached log for details.'
							+ char(10) + char(13) + 
							+ char(10) + char(13) + 
							'This process is managed by bedrockdb02.me_01.dbo.spMerchandisingFTPgetDDCinventory'
		
				EXEC msdb.dbo.sp_send_dbmail
				@profile_name = 'MerchAdmin',
				@recipients = 'merchadmin@buildabear.com',
				@subject = 'FTP Failure: inventory file from DDC to BAB',
				@body = @body,
				@file_attachments = '\\kermode\FileRepository\MERCHANDISING\WC_Distro\INVENTORY\FTP\LOGS\ftpGETLog.txt',
				@importance = 'HIGH'
						
			end

		insert ftpPUTLoginventory exec master..xp_cmdshell @ftpPUT
		if (select count(*) from ftpPUTLoginventory where ftplog like '%Transfer OK%') < 1
			begin
				set @Log_query = 'select * from me_01.dbo.ftpPUTLoginventory'
				set @Log_filename = 'ftpPUTLog.txt'
				set @Log_file_location = '\\kermode\FileRepository\MERCHANDISING\WC_Distro\INVENTORY\FTP\LOGS\'
				set @Log_bcp = 'bcp "' + @Log_query + '" queryout "' + @Log_file_location + @Log_filename + '" -t, -T -c -Sbedrockdb02'

				exec master..xp_cmdshell @Log_bcp
										
				set @body =	'An attempt to FTP a inventory file from BAB to DDC DONE folder failed.' 
							+ char(10) + char(13) + 
							'See the attached log for details.'
							+ char(10) + char(13) + 
							+ char(10) + char(13) + 
							'This process is managed by bedrockdb02.me_01.dbo.spMerchandisingFTPgetDDCinventory'
		
				EXEC msdb.dbo.sp_send_dbmail
				@profile_name = 'MerchAdmin',
				@recipients = 'merchadmin@buildabear.com',
				@subject = 'FTP Failure: inventory file from BAB to DDC DONE folder',
				@body = @body,
				@file_attachments = '\\kermode\FileRepository\MERCHANDISING\WC_Distro\INVENTORY\FTP\LOGS\ftpPUTLog.txt',
				@importance = 'HIGH'
			end

		insert ftpDELLoginventory exec master..xp_cmdshell @ftpDEL
		if (select count(*) from ftpDELLoginventory where ftplog like '%File deleted successfully%') < 1
			begin
				set @Log_query = 'select * from me_01.dbo.ftpDELLoginventory'
				set @Log_filename = 'ftpDELLog.txt'
				set @Log_file_location = '\\kermode\FileRepository\MERCHANDISING\WC_Distro\INVENTORY\FTP\LOGS\'
				set @Log_bcp = 'bcp "' + @Log_query + '" queryout "' + @Log_file_location + @Log_filename + '" -t, -T -c -Sbedrockdb02'

				exec master..xp_cmdshell @Log_bcp
										
				set @body =	'An attempt to DELETE a inventory file on the DDC server failed.' 
							+ char(10) + char(13) + 
							'See the attached log for details.'
							+ char(10) + char(13) + 
							+ char(10) + char(13) + 
							'This process is managed by bedrockdb02.me_01.dbo.spMerchandisingFTPgetDDCinventory'
		
				EXEC msdb.dbo.sp_send_dbmail
				@profile_name = 'MerchAdmin',
				@recipients = 'merchadmin@buildabear.com',
				@subject = 'FTP Failure: Delete inventory file DDC server',
				@body = @body,
				@file_attachments = '\\kermode\FileRepository\MERCHANDISING\WC_Distro\INVENTORY\FTP\LOGS\ftpDELLog.txt',
				@importance = 'HIGH'
			end


END
```

