# WMS.spMerchandisingFTPUKDistro_WinSCP

**Database:** IntegrationStaging  

## Architecture Diagram

```mermaid
flowchart LR
    SP["WMS.spMerchandisingFTPUKDistro_WinSCP"]
    dbo_SFTP_upload_UK_Distro(["dbo.SFTP_upload_UK_Distro"]) --> SP
    dbo_sp_send_dbmail(["dbo.sp_send_dbmail"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.SFTP_upload_UK_Distro |
| dbo.sp_send_dbmail |

## Stored Procedure Code

```sql
CREATE proc [WMS].[spMerchandisingFTPUKDistro_WinSCP]

as
-- =====================================================================================================
-- Name: spMerchandisingFTPUKDistro_WinSCP
--
-- Description:	Uploads UK distro files to Clipper warehouse system
--
-- Revision History
--		Name:			Date:			Comments:
--		Tim Callahan	01/23/2017		Created proc as Clipper requested we move from FTP to SFTP which requires using an application to FTP rather than native FTP in Windows. 
--		Tim Callahan	02/02/2017		Implemented into Production
--		Lizzy Timm		11/16/2022		Commented out email success logs to MerchAdmin
--		Tim Callahan	2025-01-30		Ported over from Bedrockdb02 as part of Aptos Decommission
-- =====================================================================================================
	
set nocount on

--DELETE PREVIOUS LOG FILES
IF (Object_ID('tempdb..#DEL') IS NOT NULL) DROP TABLE #DEL
create table #DEL(output varchar(1000))
insert #DEL exec master..xp_cmdshell 'dir \\stl-ssis-p-01\IntegrationStaging\3PW\UK_Distro\FTP\WinSCP\Logs\Outbound\DistroUpload.log /B'
insert #DEL exec master..xp_cmdshell 'dir \\stl-ssis-p-01\IntegrationStaging\3PW\UK_Distro\FTP\WinSCP\Logs\Outbound\SFTP_upload_UK_MonitorLog.txt /B'
delete from #DEL where output is null or output = 'File Not Found'


IF (select count(*) from #DEL where output = 'DistroUpload.log') > 0
	begin
		exec master..xp_cmdshell 'del \\stl-ssis-p-01\IntegrationStaging\3PW\UK_Distro\FTP\WinSCP\Logs\Outbound\DistroUpload.log'
	end
IF (select count(*) from #DEL where output = 'SFTP_upload_UK_MonitorLog.txt') > 0
	begin
		exec master..xp_cmdshell 'del \\stl-ssis-p-01\IntegrationStaging\3PW\UK_Distro\FTP\WinSCP\Logs\Outbound\SFTP_upload_UK_MonitorLog.txt'
	end


--CHECK FOR FILES TO UPLOAD
-------------do a DIR command and store the results in a temp table
IF (Object_ID('tempdb..#DIR') IS NOT NULL) DROP TABLE #DIR
create table #DIR (output varchar(1000))
insert #DIR exec master..xp_cmdshell 'dir \\stl-ssis-p-01\IntegrationStaging\3PW\UK_Distro\OUTBOUND\*.csv /B'
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
							@ini = ' /ini=\\stl-ssis-p-01\IntegrationStaging\3PW\UK_Distro\FTP\WinSCP\WINSCP.ini',
							@script = ' /script=\\stl-ssis-p-01\IntegrationStaging\3PW\UK_Distro\FTP\WinSCP\Scripts\Distros\DistroUpload.txt',
							@log = ' /log=\\stl-ssis-p-01\IntegrationStaging\3PW\UK_Distro\FTP\WinSCP\Logs\Outbound\DistroUpload.log',
							@SFTP = concat(@winSCP, @ini, @script, @log)

					--create temp tables for ftp logs
					IF (Object_ID('IntegrationStaging..SFTP_upload_UK_Distro') IS NOT NULL) DROP TABLE SFTP_upload_UK_Distro
					create table SFTP_upload_UK_Distro
					(ftpLog varchar(4000))

					--execute sql/ftp
					----connect to ftp server
							insert SFTP_upload_UK_Distro exec master..xp_cmdshell @SFTP 
								-- This executes the SFTP as well as inserts the SQL log of what happpenend in the XP Command Shell, aka it's not injecting the WinSCP log into the table. 

								-- select * from SFTP_upload_UK_Distro -- Just for SP troubleshooting 

					-- Send Log of XP_cmdshell Each time export occurs, still send seperate alert if appears to fail
					-- This step may ultimately be disabled once we are comfortbale with the new SFTP process, this was put in place when we had routine issues with uploading via FTP   						
				
									--set @Log_query = 'select * from [stl-ssis-p-01].IntegrationStaging.dbo.SFTP_upload_UK_Distro'
									--set @Log_filename = 'SFTP_upload_UK_MonitorLog.txt'
									--set @Log_file_location = '\\stl-ssis-p-01\IntegrationStaging\3PW\UK_Distro\FTP\WinSCP\Logs\Outbound\'
									--set @Log_bcp = 'bcp "' + @Log_query + '" queryout "' + @Log_file_location + @Log_filename + '" -t, -T -c -S[stl-ssis-p-01]'
																		
									--exec master..xp_cmdshell @Log_bcp

									/*
									set @body = 'Attached is the SQL log from the most recent SFTP transmission to Clipper Warehouse.'
										+ char(10) + char(13) +
										'This may be useful for troubleshooting missing files sent to Clipper.'
										+ char(10) + char(13) +
										'You may also find the latest log here \\stl-ssis-p-01\IntegrationStaging\3PW\UK_Distro\FTP\WinSCP\Logs\Outbound\'

									EXEC bedrockdb02.msdb.dbo.sp_send_dbmail
									@profile_name = 'MerchAdmin',
									@recipients = 'MerchAdmin@buildabear.com', -- Change to MerchAdmin when ready to go live
									@subject = 'BAB to Clipper - Distro Upload SFTP Log',
									@body= @body, 
									@file_attachments = '\\stl-ssis-p-01\IntegrationStaging\3PW\UK_Distro\FTP\WinSCP\Logs\Outbound\SFTP_upload_UK_MonitorLog.txt'
									*/

					--if connection unsuccessful, send email
							if (select count(*) from SFTP_upload_UK_Distro where ftplog like 'DISTRIBUTION%.csv%100[%]') < 1
								begin																	
									set @Log_query2 = 'select * from [stl-ssis-p-01].IntegrationStaging.dbo.SFTP_upload_UK_Distro'
									set @Log_filename2 = 'SFTP_upload_UK_DistroLog.txt'
									set @Log_file_location2 = '\\stl-ssis-p-01\IntegrationStaging\3PW\UK_Distro\FTP\WinSCP\Logs\Outbound\'
									set @Log_bcp2 = 'bcp "' + @Log_query2 + '" queryout "' + @Log_file_location2 + @Log_filename2 + '" -t, -T -c -Sbedrockdb02'

									exec master..xp_cmdshell @Log_bcp2
															
									set @body2 =	'An attempt to FTP a UK Distro to Clipper failed.' 
												+ char(10) + char(13) + 
												'See the attached logs for details.'
												+ char(10) + char(13) + 
												+ char(10) + char(13) + 
												'This process is managed by [stl-ssis-p-01].IntegrationStaging.wms.spMerchandisingFTPUKDistro_WinSCP'
							
									EXEC [stl-ssis-p-01].msdb.dbo.sp_send_dbmail
									@profile_name = 'BiAdmin',
									@recipients = 'EntSysSupport@buildabear.com', -- Change to EntSysSupport@buildabear.com when ready to go live
									@subject = 'FTP Failure: UK Distro File Upload from BAB to Clipper',
									@body = @body2,
									@file_attachments = '\\stl-ssis-p-01\IntegrationStaging\3PW\UK_Distro\FTP\WinSCP\Logs\Outbound\SFTP_upload_UK_DistroLog.txt;\\stl-ssis-p-01\IntegrationStaging\3PW\UK_Distro\FTP\WinSCP\Logs\Outbound\DistroUpload.log',
									@importance = 'HIGH'

								end
							else
								begin
									EXEC master..xp_cmdshell 'move \\stl-ssis-p-01\IntegrationStaging\3PW\UK_Distro\OUTBOUND\* \\stl-ssis-p-01\IntegrationStaging\3PW\UK_Distro\OUTBOUND\done'
								end

END
```

