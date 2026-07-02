# WEB.spFTPukWarehouseOrderStatusUpdate

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["WEB.spFTPukWarehouseOrderStatusUpdate"]
    WEB_tmpFTGetWeb(["WEB.tmpFTGetWeb"]) --> SP
    WEB_UKFTPTransmissionLogDump(["WEB.UKFTPTransmissionLogDump"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| WEB.tmpFTGetWeb |
| WEB.UKFTPTransmissionLogDump |

## Stored Procedure Code

```sql
CREATE proc [WEB].[spFTPukWarehouseOrderStatusUpdate]

as

-- =====================================================================================================
-- Name: spFTPukWarehouseOrderStatusUpdate
--
-- Description:	Downloads web Warehouse Order Status Updates
--
-- Revision History
--		Name:			Date:			Comments:
--		Ben Barud		2025-07-08		Created proc
-- =====================================================================================================
	
set nocount on

--DELETE PREVIOUS LOG FILES
IF (Object_ID('tempdb..#DEL') IS NOT NULL) DROP TABLE #DEL
create table #DEL(output varchar(1000))
insert #DEL exec master..xp_cmdshell 'dir \\kermode\FileRepository\WarehouseOrderStatusUpdates\log\Download.log /B'
insert #DEL exec master..xp_cmdshell 'dir \\kermode\FileRepository\WarehouseOrderStatusUpdates\log\FTPLog_UKWeb.txt /B'

delete from #DEL where output is null or output = 'File Not Found'

IF (select count(*) from #DEL where output = 'Download.log') > 0
	begin
		exec master..xp_cmdshell 'del \\kermode\FileRepository\WarehouseOrderStatusUpdates\log\Download.log'
	end
IF (select count(*) from #DEL where output = 'FTPLog_UKWeb.txt') > 0
	begin
		exec master..xp_cmdshell 'del \\kermode\FileRepository\WarehouseOrderStatusUpdates\log\FTPLog_UKWeb.txt'
	end


			-----ftp download
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
							@ini = ' /ini=\\stl-ssis-p-01\Integrationstaging\wm\Production\WinSCP.ini',
							@script = ' /script=\\stl-ssis-p-01\Integrationstaging\wm\Production\WinSCPGET.txt',
							@log = ' /log=\\kermode\FileRepository\WarehouseOrderStatusUpdates\log\Download.log',
							@FTP = concat(@winSCP, @ini, @script, @log)

					--create temp tables for ftp logs
					IF (Object_ID('IntegrationStaging.WEB.tmpFTGetWeb') IS NOT NULL) DROP TABLE WEB.tmpFTGetWeb
					create table WEB.tmpFTGetWeb
					(ftpLog varchar(4000))

					--execute sql/ftp
					----connect to ftp server, if connection unsuccessful, send email
							insert WEB.tmpFTGetWeb exec master..xp_cmdshell @FTP --create table  (ftpLog varchar(4000), LogDateTime datetime)
							insert WEB.UKFTPTransmissionLogDump 
							select ftpLog, getdate() from WEB.tmpFTGetWeb 

							if (select count(*) from WEB.tmpFTGetWeb where ftplog like '%.xml%100[%]') < 1
								begin
									set @Log_query = 'select * from IntegrationStaging.WEB.tmpFTGetWeb'
									set @Log_filename = 'FTPLog_UKWeb.txt'
									set @Log_file_location = '\\kermode\FileRepository\WarehouseOrderStatusUpdates\log\'
									set @Log_bcp = 'bcp "' + @Log_query + '" queryout "' + @Log_file_location + @Log_filename + '" -t, -T -c -Sstl-ssis-p-01'

									exec master..xp_cmdshell @Log_bcp
									
									-----commented out becuase we have validations and processes to check the Failed folder and restage and upload again and notify if not sent					
									--set @body =	'An attempt to FTP a UK Web Order failed.' 
									--			+ char(10) + char(13) + 
									--			'See the attached logs for details.'
									--			+ char(10) + char(13) + 
									--			+ char(10) + char(13) + 
									--			'This process is managed by stl-ssip-p-01.IntegrationStaging.WEB.spFTPukORDERS'
							
									--EXEC msdb.dbo.sp_send_dbmail
									--@profile_name = 'BIAdmin',
									--@recipients = 'WebAlerts@buildabear.com',
									--@subject = 'FTP Failure: UK Web Order Upload',
									--@body = @body,
									--@file_attachments = '\\kermode\Filerepository\omsorders\babw-UK\log\FTPLog_UKWeb.txt;\\kermode\Filerepository\omsorders\babw-UK\log\Upload.log',
									--@importance = 'HIGH'
									------------------------------------------------------------------------------------------------------------------------
								END
```

