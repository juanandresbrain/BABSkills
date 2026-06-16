# WMS.spMerchandisingFTPgetDDCinventoryWinSCP

**Database:** IntegrationStaging  

## Architecture Diagram

```mermaid
flowchart LR
    SP["WMS.spMerchandisingFTPgetDDCinventoryWinSCP"]
    dbo_ftpWC_GETInventory(["dbo.ftpWC_GETInventory"]) --> SP
    dbo_ftpWC_GETInventoryDIR(["dbo.ftpWC_GETInventoryDIR"]) --> SP
    dbo_sp_send_dbmail(["dbo.sp_send_dbmail"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ftpWC_GETInventory |
| dbo.ftpWC_GETInventoryDIR |
| dbo.sp_send_dbmail |

## Stored Procedure Code

```sql
CREATE proc [WMS].[spMerchandisingFTPgetDDCinventoryWinSCP]

as

-- =====================================================================================================
-- Name: spMerchandisingFTPgetDDCinventoryWinSCP
--
--
-- Revision History
--		Name:			Date:			Comments:
--		Dan Tweedie		2020-06-23		Created proc
--		Tim Callahan	2025-01-31		Ported over from Bedrockdb02 as part of Aptos Decommission
-- =====================================================================================================
	
set nocount on


--==================================================================================================================================================
--DELETE PREVIOUS LOG FILES
IF (Object_ID('tempdb..#DEL1') IS NOT NULL) DROP TABLE #DEL1
create table #DEL1(output varchar(1000))
	insert #DEL1 exec master..xp_cmdshell 'dir \\stl-ssis-p-01\IntegrationStaging\3PW\WC_Distro\FTP\WinSCP\Logs\Inbound\WCInventoryDownload.log /B'
	insert #DEL1 exec master..xp_cmdshell 'dir \\stl-ssis-p-01\IntegrationStaging\3PW\WC_Distro\FTP\WinSCP\Logs\Inbound\ftpWC_GETInventoryLog.txt /B'
	insert #DEL1 exec master..xp_cmdshell 'dir \\stl-ssis-p-01\IntegrationStaging\3PW\WC_Distro\FTP\WinSCP\Logs\Inbound\WCInventoryDIR.log /B'
	insert #DEL1 exec master..xp_cmdshell 'dir \\stl-ssis-p-01\IntegrationStaging\3PW\WC_Distro\FTP\WinSCP\Logs\Inbound\ftpWC_GETInventoryDIRLog.txt /B'
delete from #DEL1 where output is null or output = 'File Not Found'

IF (select count(*) from #DEL1 where output = 'WCInventoryDownload.log' ) > 0
	begin
		exec master..xp_cmdshell 'del \\stl-ssis-p-01\IntegrationStaging\3PW\WC_Distro\FTP\WinSCP\Logs\Inbound\WCInventoryDownload.log'
	end	
IF (select count(*) from #DEL1 where output = 'ftpWC_GETInventoryLog.txt' ) > 0
	begin
		exec master..xp_cmdshell 'del \\stl-ssis-p-01\IntegrationStaging\3PW\WC_Distro\FTP\WinSCP\Logs\Inbound\ftpWC_GETInventoryLog.txt'
	end
IF (select count(*) from #DEL1 where output = 'WCInventoryDIR.log' ) > 0
	begin	
		exec master..xp_cmdshell 'del \\stl-ssis-p-01\IntegrationStaging\3PW\WC_Distro\FTP\WinSCP\Logs\Inbound\WCInventoryDIR.log'
	end
IF (select count(*) from #DEL1 where output = 'ftpWC_GETInventoryDIRLog.txt' ) > 0
	begin	
		exec master..xp_cmdshell 'del \\stl-ssis-p-01\IntegrationStaging\3PW\WC_Distro\FTP\WinSCP\Logs\Inbound\ftpWC_GETInventoryDIRLog.txt'
	end
	
--==================================================================================================================================================
------CHECK FOR EXISTENCE OF INVENTORY FILE
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
		--@ini = ' /ini=\\stl-ssis-p-01\IntegrationStaging\3PW\WC_Distro\FTP\WinSCP\WINSCP.ini',
		@script = ' /script=\\stl-ssis-p-01\IntegrationStaging\3PW\WC_Distro\FTP\WinSCP\Scripts\Inventory\InventoryDIR.txt',
		@log = ' /log=\\stl-ssis-p-01\IntegrationStaging\3PW\WC_Distro\FTP\WinSCP\Logs\Inbound\WCInventoryDIR.log',
		@FTP = concat(@winSCP,/* @ini,*/ @script, @log)

IF (Object_ID('IntegrationStaging..ftpWC_GETInventoryDIR') IS NOT NULL) DROP TABLE ftpWC_GETInventoryDIR
create table ftpWC_GETInventoryDIR
(ftpLog varchar(4000))

insert ftpWC_GETInventoryDIR exec master..xp_cmdshell @FTP

if (select count(*) from ftpWC_GETInventoryDIR where ftpLog like '%.txt') > 0


--==================================================================================================================================================
------DOWNLOAD INVENTORY FILE
--==================================================================================================================================================
		BEGIN
							
				select 

						@script = ' /script=\\stl-ssis-p-01\IntegrationStaging\3PW\WC_Distro\FTP\WinSCP\Scripts\Inventory\Inventory.txt',
						@log = ' /log=\\stl-ssis-p-01\IntegrationStaging\3PW\WC_Distro\FTP\WinSCP\Logs\Inbound\WCInventoryDownload.log',
						@FTP = concat(@winSCP, /*@ini,*/ @script, @log)

				--create temp tables for ftp logs
				IF (Object_ID('IntegrationStaging..ftpWC_GETInventory') IS NOT NULL) DROP TABLE ftpWC_GETInventory
				create table ftpWC_GETInventory
				(ftpLog varchar(4000))

				--execute sql/ftp
				----connect to ftp server, if connection unsuccessful, send email
						insert ftpWC_GETInventory exec master..xp_cmdshell @FTP
						if (select count(*) from ftpWC_GETInventory where ftplog like '%.txt%[100%]') < 1
							begin
								set @Log_query = 'select * from [stl-ssis-p-01].IntegrationStaging.dbo.ftpWC_GETInventory'
								set @Log_filename = 'ftpWC_GETInventoryLog.txt'
								set @Log_file_location = '\\stl-ssis-p-01\IntegrationStaging\3PW\WC_Distro\FTP\WinSCP\Logs\Inbound\'
								set @Log_bcp = 'bcp "' + @Log_query + '" queryout "' + @Log_file_location + @Log_filename + '" -t, -T -c -Sbedrockdb02'

								exec master..xp_cmdshell @Log_bcp
															
								set @body =	'An attempt to FTP download from DDC failed.' 
											+ char(10) + char(13) + 
											'See the attached logs for details.'
											+ char(10) + char(13) + 
											+ char(10) + char(13) + 
											'This process is managed by [stl-ssis-p-01].IntegrationStaging.wms.spMerchandisingFtpWC_GetInventoryFilesWinSCP'
							
								EXEC [stl-ssis-p-01].msdb.dbo.sp_send_dbmail
								@profile_name = 'BiAdmin',
								@recipients = 'EntSysSupport@buildabear.com',
								@subject = 'FTP Failure: WC Inventory File Download from DDC',
								@body = @body,
								@file_attachments = '\\stl-ssis-p-01\IntegrationStaging\3PW\WC_Distro\FTP\WinSCP\Logs\Inbound\ftpWC_GETInventoryLog.txt;\\stl-ssis-p-01\IntegrationStaging\3PW\WC_Distro\FTP\WinSCP\Logs\Inbound\WCInventoryDownload.log',
								@importance = 'HIGH'
							end


		END
--==================================================================================================================================================
```

