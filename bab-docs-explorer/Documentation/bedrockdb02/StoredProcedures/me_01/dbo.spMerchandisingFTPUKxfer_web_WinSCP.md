# dbo.spMerchandisingFTPUKxfer_web_WinSCP

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMerchandisingFTPUKxfer_web_WinSCP"]
    dbo_SFTP_upload_UK_xfer_web(["dbo.SFTP_upload_UK_xfer_web"]) --> SP
    dbo_sp_send_dbmail(["dbo.sp_send_dbmail"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.SFTP_upload_UK_xfer_web |
| dbo.sp_send_dbmail |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spMerchandisingFTPUKxfer_web_WinSCP] -- Stored Proc name
as
-- =====================================================================================================
-- Name: spMerchandisingFTPUKxfer_web_WinSCP
--
-- Description:	Uploads UK Transfer ASN files to Clipper Warehouse (2013) SFTP site.
--
-- Revision History
--		Name:			Date:			Comments:
--		Tim Callahan	08/16/2017		Created proc as part of Clipper Upgrade, previously did not provide ASN files 

-- =====================================================================================================

set nocount on

--DELETE PREVIOUS LOG FILES
IF (Object_ID('tempdb..#DEL') IS NOT NULL) DROP TABLE #DEL
create table #DEL(output varchar(1000))
insert #DEL exec master..xp_cmdshell 'dir \\kermode\FileRepository\MERCHANDISING\UK_Distro\FTP\WinSCP\Logs\Outbound\xferWebUpload.log /B'
insert #DEL exec master..xp_cmdshell 'dir \\kermode\FileRepository\MERCHANDISING\UK_Distro\FTP\WinSCP\Logs\Outbound\SFTP_xfer_web_upload_UK_MonitorLog.txt /B'
delete from #DEL where output is null or output = 'File Not Found'


IF (select count(*) from #DEL where output = 'xferWebUpload.log') > 0
	begin
		exec master..xp_cmdshell 'del \\kermode\FileRepository\MERCHANDISING\UK_Distro\FTP\WinSCP\Logs\Outbound\xferWebUpload.log'
	end
IF (select count(*) from #DEL where output = 'SFTP_xfer_web_upload_UK_MonitorLog.txt') > 0
	begin
		exec master..xp_cmdshell 'del \\kermode\FileRepository\MERCHANDISING\UK_Distro\FTP\WinSCP\Logs\Outbound\SFTP_xfer_web_upload_UK_MonitorLog.txt'
	end


--CHECK FOR FILES TO UPLOAD
-------------do a DIR command and store the results in a temp table
IF (Object_ID('tempdb..#DIR') IS NOT NULL) DROP TABLE #DIR
create table #DIR (output varchar(1000))
insert #DIR exec master..xp_cmdshell 'dir \\kermode\FileRepository\MERCHANDISING\UK_Distro\OUTBOUND\ASN_XFER_Web\*.csv /B'
delete from #DIR where output is null or output = 'File Not Found'

------------query temp table to see if there are CSV files
if (select count(*) from #DIR) > 0

BEGIN
			-----ftp upload
					declare 
							@winSCP varchar(1000),
							@ini varchar(1000),
							@script varchar(1000),
							@log varchar(1000),
							@SFTP varchar(4000),

							@Log_query varchar(1000),
							@Log_filename varchar(100),
							@Log_file_location varchar(100),
							@Log_bcp varchar(1000),
							@body varchar(4000),

							@Log_query2 varchar(1000),
							@Log_filename2 varchar(100),
							@Log_file_location2 varchar(100),
							@Log_bcp2 varchar(1000),
							@body2 varchar(4000)
							
					select 
							@winSCP = '"\\stl-ssis-p-01\C$\Program Files (x86)\WinSCP\winscp.com"',
							@ini = ' /ini=\\kermode\FileRepository\MERCHANDISING\UK_Distro\FTP\WinSCP\WINSCP.ini', 
							@script = ' /script=\\kermode\FileRepository\MERCHANDISING\UK_Distro\FTP\WinSCP\Scripts\Asns\Web\xferWebUpload.txt',
							@log = ' /log=\\kermode\FileRepository\MERCHANDISING\UK_Distro\FTP\WinSCP\Logs\Outbound\xferWebUpload.log',
							@SFTP = concat(@winSCP, @ini, @script, @log)

					--create temp tables for ftp logs
					IF (Object_ID('me_01..SFTP_upload_UK_xfer_web') IS NOT NULL) DROP TABLE SFTP_upload_UK_xfer_web
					create table SFTP_upload_UK_xfer_web
					(ftpLog varchar(4000))

					--execute sql/ftp
					----connect to ftp server
							insert SFTP_upload_UK_xfer_web exec master..xp_cmdshell @SFTP 
								-- This executes the SFTP as well as inserts the SQL log of what happpenend in the XP Command Shell, aka it's not injecting the WinSCP log into the table. 

								-- select * from SFTP_upload_UK_xfer_web -- Just for SP troubleshooting 

					-- Send Log of XP_cmdshell Each time export occurs, still send seperate alert if appears to fail
					-- This step may ultimately be disabled once we are comfortbale with the new SFTP process, this was put in place when we had routine issues with uploading via FTP   						
				
									set @Log_query = 'select * from bedrockdb02.me_01.dbo.SFTP_upload_UK_xfer_web'
									set @Log_filename = 'SFTP_xfer_web_upload_UK_MonitorLog.txt'
									set @Log_file_location = '\\kermode\FileRepository\MERCHANDISING\UK_Distro\FTP\WinSCP\Logs\Outbound\'
									set @Log_bcp = 'bcp "' + @Log_query + '" queryout "' + @Log_file_location + @Log_filename + '" -t, -T -c -Sbedrockdb02'
																		
									exec master..xp_cmdshell @Log_bcp


									set @body = 'Attached is the SQL log from the most recent SFTP transmission to Clipper Warehouse.'
										+ char(10) + char(13) +
										'This may be useful for troubleshooting missing files sent to Clipper.'
										+ char(10) + char(13) +
										'You may also find the latest log here \\kermode\FileRepository\MERCHANDISING\UK_Distro\FTP\WinSCP\Logs\Outbound\'

									EXEC bedrockdb02.msdb.dbo.sp_send_dbmail
									@profile_name = 'MerchAdmin',
									@recipients = 'MerchAdmin@buildabear.com', -- Change to MerchAdmin when ready to go live
									@subject = 'BAB to Clipper - Web Transfer ASN Upload SFTP Log',
									@body= @body, 
									@file_attachments = '\\kermode\FileRepository\MERCHANDISING\UK_Distro\FTP\WinSCP\Logs\Outbound\SFTP_xfer_web_upload_UK_MonitorLog.txt'


					--if connection unsuccessful, send email
							if (select count(*) from SFTP_upload_UK_xfer_web where ftplog like 'UK_WEB_XFER_ASN_%.csv%100[%]') < 1
								begin																	
									set @Log_query2 = 'select * from bedrockdb02.me_01.dbo.SFTP_upload_UK_xfer_web'
									set @Log_filename2 = 'SFTP_upload_UK_xfer_web_Log.txt'
									set @Log_file_location2 = '\\kermode\FileRepository\MERCHANDISING\UK_Distro\FTP\WinSCP\Logs\Outbound\'
									set @Log_bcp2 = 'bcp "' + @Log_query2 + '" queryout "' + @Log_file_location2 + @Log_filename2 + '" -t, -T -c -Sbedrockdb02'

									exec master..xp_cmdshell @Log_bcp2
															
									set @body2 =	'An attempt to FTP a UK Web Transfer ASN to Clipper failed.' 
												+ char(10) + char(13) + 
												'See the attached logs for details.'
												+ char(10) + char(13) + 
												+ char(10) + char(13) + 
												'This process is managed by bedrockdb02.me_01.dbo.spMerchandisingFTPUKxfer_web_WinSCP'
							
									EXEC bedrockdb02.msdb.dbo.sp_send_dbmail
									@profile_name = 'MerchAdmin',
									@recipients = 'MerchAdmin@buildabear.com', -- Change to MerchAdmin when ready to go live
									@subject = 'FTP Failure: UK Web Transfer ASN File Upload from BAB to Clipper',
									@body = @body2,
									@file_attachments = '\\kermode\FileRepository\MERCHANDISING\UK_Distro\FTP\WinSCP\Logs\Outbound\SFTP_upload_UK_xfer_web_Log.txt;\\kermode\FileRepository\MERCHANDISING\UK_Distro\FTP\WinSCP\Logs\Outbound\xferWebUpload.log',
									@importance = 'HIGH'

								end
							else
								begin
									EXEC master..xp_cmdshell 'move \\kermode\FileRepository\MERCHANDISING\UK_Distro\OUTBOUND\ASN_XFER_Web\* \\kermode\FileRepository\MERCHANDISING\UK_Distro\OUTBOUND\ASN_XFER_Web\Done'
								end

END
```

