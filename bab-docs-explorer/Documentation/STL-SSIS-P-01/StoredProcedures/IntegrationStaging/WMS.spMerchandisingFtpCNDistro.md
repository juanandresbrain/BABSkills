# WMS.spMerchandisingFtpCNDistro

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["WMS.spMerchandisingFtpCNDistro"]
    dbo_ftpPUT_Distro(["dbo.ftpPUT_Distro"]) --> SP
    dbo_sp_send_dbmail(["dbo.sp_send_dbmail"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ftpPUT_Distro |
| dbo.sp_send_dbmail |

## Stored Procedure Code

```sql
CREATE proc [WMS].[spMerchandisingFtpCNDistro]

as

-- =====================================================================================================
-- Name: spMerchandisingFtpCNDistro
--
-- Description:	Uploads CN distro files to Shanghai warehouse system
--
-- Revision History
--		Name:			Date:			Comments:
--		Dan Tweedie		03/31/2016		Created proc
--		Tim Callahan	08/08/2022		Updated proc to not delete WinScp log, 
--		Tim Callahan	2025-01-30		Ported over from Bedrockdb02 as part of Aptos Decommission
-- =====================================================================================================
	
set nocount on

--DELETE PREVIOUS LOG FILES
IF (Object_ID('tempdb..#DEL') IS NOT NULL) DROP TABLE #DEL
create table #DEL(output varchar(1000))
--insert #DEL exec master..xp_cmdshell 'dir \\stl-ssis-p-01\IntegrationStaging\3PW\CN_Distro\FTP\WinSCP\Logs\Outbound\DistroUpload.log /B'
insert #DEL exec master..xp_cmdshell 'dir \\stl-ssis-p-01\IntegrationStaging\3PW\CN_Distro\FTP\WinSCP\Logs\Outbound\ftpPUT_DistroLog.txt /B'
delete from #DEL where output is null or output = 'File Not Found'

--IF (select count(*) from #DEL where output = 'DistroUpload.log') > 0
--	begin
--		exec master..xp_cmdshell 'del \\stl-ssis-p-01\IntegrationStaging\3PW\CN_Distro\FTP\WinSCP\Logs\Outbound\DistroUpload.log'
--	end
IF (select count(*) from #DEL where output = 'ftpPUT_DistroLog.txt') > 0
	begin
		exec master..xp_cmdshell 'del \\stl-ssis-p-01\IntegrationStaging\3PW\CN_Distro\FTP\WinSCP\Logs\Outbound\ftpPUT_DistroLog.txt'
	end


--CHECK FOR FILES TO UPLOAD
-------------do a DIR command and store the results in a temp table
IF (Object_ID('tempdb..#DIR') IS NOT NULL) DROP TABLE #DIR
create table #DIR (output varchar(1000))
insert #DIR exec master..xp_cmdshell 'dir \\stl-ssis-p-01\IntegrationStaging\3PW\CN_Distro\OUTBOUND\Distros\*.csv /B'
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
							@FTP varchar(4000),
							@Log_query varchar(1000),
							@Log_filename varchar(100),
							@Log_file_location varchar(100),
							@Log_bcp varchar(1000),
							@body varchar(4000)
							
					select 
							@winSCP = '"\\stl-ssis-p-01\C$\Program Files (x86)\WinSCP\winscp.com"',
							@ini = ' /ini=\\stl-ssis-p-01\IntegrationStaging\3PW\CN_Distro\FTP\WinSCP\WINSCP.ini',
							@script = ' /script=\\stl-ssis-p-01\IntegrationStaging\3PW\CN_Distro\FTP\WinSCP\Scripts\Distros\DistroUpload.txt',
							@log = ' /log=\\stl-ssis-p-01\IntegrationStaging\3PW\CN_Distro\FTP\WinSCP\Logs\Outbound\DistroUpload.log',
							@FTP = concat(@winSCP, @ini, @script, @log)

					--create temp tables for ftp logs
					IF (Object_ID('IntegrationStaging..ftpPUT_Distro') IS NOT NULL) DROP TABLE ftpPUT_Distro
					create table ftpPUT_Distro
					(ftpLog varchar(4000))

					--execute sql/ftp
					----connect to ftp server, if connection unsuccessful, send email
							insert ftpPUT_Distro exec master..xp_cmdshell @FTP
							if (select count(*) from ftpPUT_Distro where ftplog like 'DISTRIBUTION%.csv%100[%]') < 1
								begin
									set @Log_query = 'select * from [stl-ssis-p-01].IntegrationStaging.dbo..ftpPUT_Distro'
									set @Log_filename = 'ftpPUT_DistroLog.txt'
									set @Log_file_location = '\\stl-ssis-p-01\IntegrationStaging\3PW\CN_Distro\FTP\WinSCP\Logs\Outbound\'
									set @Log_bcp = 'bcp "' + @Log_query + '" queryout "' + @Log_file_location + @Log_filename + '" -t, -T -c -Sbedrockdb02'

									exec master..xp_cmdshell @Log_bcp
															
									set @body =	'An attempt to FTP a CN Distro to China Whse failed.' 
												+ char(10) + char(13) + 
												'See the attached logs for details.'
												+ char(10) + char(13) + 
												+ char(10) + char(13) + 
												'This process is managed by [stl-ssis-p-01].IntegrationStaging.wms.spMerchandisingFtpCNDistro'
							
									EXEC [stl-ssis-p-01].msdb.dbo.sp_send_dbmail
									@profile_name = 'BiAdmin',
									@recipients = 'EntSysSupport@buildabear.com',
									@subject = 'FTP Failure: CN Distro File Upload from BAB to China Whse',
									@body = @body,
									@file_attachments = '\\stl-ssis-p-01\IntegrationStaging\3PW\CN_Distro\FTP\WinSCP\Logs\Outbound\ftpPUT_DistroLog.txt;\\stl-ssis-p-01\IntegrationStaging\3PW\CN_Distro\FTP\WinSCP\Logs\Outbound\DistroUpload.log',
									@importance = 'HIGH'
								end
							else
								begin
									EXEC master..xp_cmdshell 'move \\stl-ssis-p-01\IntegrationStaging\3PW\CN_Distro\OUTBOUND\Distros\* \\stl-ssis-p-01\IntegrationStaging\3PW\CN_Distro\OUTBOUND\Distros\done'
								end

END
```

