# dbo.spMerchandisingFtpCN_GetInvAdjFiles

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMerchandisingFtpCN_GetInvAdjFiles"]
    dbo_ftpCN_GETInvAdj(["dbo.ftpCN_GETInvAdj"]) --> SP
    dbo_ftpCN_GETInvAdjDIR(["dbo.ftpCN_GETInvAdjDIR"]) --> SP
    dbo_sp_send_dbmail(["dbo.sp_send_dbmail"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ftpCN_GETInvAdj |
| dbo.ftpCN_GETInvAdjDIR |
| dbo.sp_send_dbmail |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spMerchandisingFtpCN_GetInvAdjFiles]

as

-- =====================================================================================================
-- Name: spMerchandisingFtpCN_GetInvAdjFiles
--
-- Description:	Downloads staged inventory adjustment file from Shanghai warehouse system, stages files for import to Merchandising system
--
-- Revision History
--		Name:			Date:			Comments:
--		Dan Tweedie		03/29/2016		Created proc
-- =====================================================================================================
	
set nocount on


--==================================================================================================================================================
--DELETE PREVIOUS LOG FILES
IF (Object_ID('tempdb..#DEL2') IS NOT NULL) DROP TABLE #DEL2
create table #DEL2(output varchar(1000))
	insert #DEL2 exec master..xp_cmdshell 'dir \\kermode\FileRepository\MERCHANDISING\CN_Distro\FTP\WinSCP\Logs\Inbound\CNInvAdjDownload.log /B'
	insert #DEL2 exec master..xp_cmdshell 'dir \\kermode\FileRepository\MERCHANDISING\CN_Distro\FTP\WinSCP\Logs\Inbound\ftpCN_GETInvAdjLog.txt /B'
	insert #DEL2 exec master..xp_cmdshell 'dir \\kermode\FileRepository\MERCHANDISING\CN_Distro\FTP\WinSCP\Logs\Inbound\CNInvAdjDIR.log /B'
	insert #DEL2 exec master..xp_cmdshell 'dir \\kermode\FileRepository\MERCHANDISING\CN_Distro\FTP\WinSCP\Logs\Inbound\ftpCN_GETInvAdjDIRLog.txt /B'
delete from #DEL2 where output is null or output = 'File Not Found'

IF (select count(*) from #DEL2 where output = 'CNInvAdjDownload.log') > 0
	begin
		exec master..xp_cmdshell 'del \\kermode\FileRepository\MERCHANDISING\CN_Distro\FTP\WinSCP\Logs\Inbound\CNInvAdjDownload.log'
	end
IF (select count(*) from #DEL2 where output = 'ftpCN_GETInvAdjLog.txt') > 0
	begin
		exec master..xp_cmdshell 'del \\kermode\FileRepository\MERCHANDISING\CN_Distro\FTP\WinSCP\Logs\Inbound\ftpCN_GETInvAdjLog.txt'
	end
IF (select count(*) from #DEL2 where output = 'CNInvAdjDIR.log') > 0	
	begin
		exec master..xp_cmdshell 'del \\kermode\FileRepository\MERCHANDISING\CN_Distro\FTP\WinSCP\Logs\Inbound\CNInvAdjDIR.log'
	end
IF (select count(*) from #DEL2 where output = 'ftpCN_GETInvAdjDIRLog.txt') > 0	
	begin 
		exec master..xp_cmdshell 'del \\kermode\FileRepository\MERCHANDISING\CN_Distro\FTP\WinSCP\Logs\Inbound\ftpCN_GETInvAdjDIRLog.txt'
	end

--==================================================================================================================================================
------CHECK FOR EXISTENCE OF INV ADJ FILE
--==================================================================================================================================================
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
		@ini = ' /ini=\\kermode\FileRepository\MERCHANDISING\CN_Distro\FTP\WinSCP\WINSCP.ini',
		@script = ' /script=\\kermode\FileRepository\MERCHANDISING\CN_Distro\FTP\WinSCP\Scripts\InvAdj\InvAdjDIR.txt',
		@log = ' /log=\\kermode\FileRepository\MERCHANDISING\CN_Distro\FTP\WinSCP\Logs\Inbound\CNInvAdjDIR.log',
		@FTP = concat(@winSCP, @ini, @script, @log)

IF (Object_ID('me_01..ftpCN_GETInvAdjDIR') IS NOT NULL) DROP TABLE ftpCN_GETInvAdjDIR
create table ftpCN_GETInvAdjDIR
(ftpLog varchar(4000))

insert ftpCN_GETInvAdjDIR exec master..xp_cmdshell @FTP

if (select count(*) from ftpCN_GETInvAdjDIR where ftpLog like '%.csv') > 0



--==================================================================================================================================================
------DOWNLOAD INV ADJ FILE
--==================================================================================================================================================
		BEGIN
							
				select 
						@script = ' /script=\\kermode\FileRepository\MERCHANDISING\CN_Distro\FTP\WinSCP\Scripts\InvAdj\InvAdj.txt',
						@log = ' /log=\\kermode\FileRepository\MERCHANDISING\CN_Distro\FTP\WinSCP\Logs\Inbound\CNInvAdjDownload.log',
						@FTP = concat(@winSCP, @ini, @script, @log)

				--create temp tables for ftp logs
				IF (Object_ID('me_01..ftpCN_GETInvAdj') IS NOT NULL) DROP TABLE ftpCN_GETInvAdj
				create table ftpCN_GETInvAdj
				(ftpLog varchar(4000))

				--execute sql/ftp
				----connect to ftp server, if connection unsuccessful, send email
						insert ftpCN_GETInvAdj exec master..xp_cmdshell @FTP
						if (select count(*) from ftpCN_GETInvAdj where ftplog like '%.csv%[100%]') < 1
							begin
								set @Log_query = 'select * from bedrockdb02.me_01.dbo.ftpCN_GETInvAdj'
								set @Log_filename = 'ftpCN_GETInvAdjLog.txt'
								set @Log_file_location = '\\kermode\FileRepository\MERCHANDISING\CN_Distro\FTP\WinSCP\Logs\Inbound\'
								set @Log_bcp = 'bcp "' + @Log_query + '" queryout "' + @Log_file_location + @Log_filename + '" -t, -T -c -Sbedrockdb02'

								exec master..xp_cmdshell @Log_bcp
															
								set @body =	'An attempt to FTP download from China Whse failed.' 
											+ char(10) + char(13) + 
											'See the attached logs for details.'
											+ char(10) + char(13) + 
											+ char(10) + char(13) + 
											'This process is managed by bedrockdb02.me_01.dbo.spMerchandisingFtpCN_GetInvAdjFiles'
							
								EXEC bedrockdb02.msdb.dbo.sp_send_dbmail
								@profile_name = 'MerchAdmin',
								@recipients = 'EntSysSupport@buildabear.com',
								@subject = 'FTP Failure: CN Inventory Adjustment File Download from Kerry Logistics',
								@body = @body,
								@file_attachments = '\\kermode\FileRepository\MERCHANDISING\CN_Distro\FTP\WinSCP\Logs\Inbound\ftpCN_GETInvAdjLog.txt;\\kermode\FileRepository\MERCHANDISING\CN_Distro\FTP\WinSCP\Logs\Inbound\CNInvAdjDownload.log',
								@importance = 'HIGH'
							end


		END
--==================================================================================================================================================
```

