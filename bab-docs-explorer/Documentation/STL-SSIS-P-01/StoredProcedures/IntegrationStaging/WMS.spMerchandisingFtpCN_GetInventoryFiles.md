# WMS.spMerchandisingFtpCN_GetInventoryFiles

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["WMS.spMerchandisingFtpCN_GetInventoryFiles"]
    dbo_ftpCN_GETInventory(["dbo.ftpCN_GETInventory"]) --> SP
    dbo_ftpCN_GETInventoryDIR(["dbo.ftpCN_GETInventoryDIR"]) --> SP
    dbo_sp_send_dbmail(["dbo.sp_send_dbmail"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ftpCN_GETInventory |
| dbo.ftpCN_GETInventoryDIR |
| dbo.sp_send_dbmail |

## Stored Procedure Code

```sql
CREATE proc [WMS].[spMerchandisingFtpCN_GetInventoryFiles]

as

-- =====================================================================================================
-- Name: spMerchandisingFtpCN_GetInventoryFiles
--
-- Description:	Downloads staged inventory file from Shanghai warehouse system, stages files for import to Merchandising system
--
-- Revision History
--		Name:			Date:			Comments:
--		Dan Tweedie		03/29/2016		Created proc
--		Tim Callahan	2025-01-31		Ported over from Bedrockdb02 as part of Aptos Decommission
-- =====================================================================================================
	
set nocount on


--==================================================================================================================================================
--DELETE PREVIOUS LOG FILES
IF (Object_ID('tempdb..#DEL1') IS NOT NULL) DROP TABLE #DEL1
create table #DEL1(output varchar(1000))
	insert #DEL1 exec master..xp_cmdshell 'dir \\stl-ssis-p-01\IntegrationStaging\3PW\CN_Distro\FTP\WinSCP\Logs\Inbound\CNInventoryDownload.log /B'
	insert #DEL1 exec master..xp_cmdshell 'dir \\stl-ssis-p-01\IntegrationStaging\3PW\CN_Distro\FTP\WinSCP\Logs\Inbound\ftpCN_GETInventoryLog.txt /B'
	insert #DEL1 exec master..xp_cmdshell 'dir \\stl-ssis-p-01\IntegrationStaging\3PW\CN_Distro\FTP\WinSCP\Logs\Inbound\CNInventoryDIR.log /B'
	insert #DEL1 exec master..xp_cmdshell 'dir \\stl-ssis-p-01\IntegrationStaging\3PW\CN_Distro\FTP\WinSCP\Logs\Inbound\ftpCN_GETInventoryDIRLog.txt /B'
delete from #DEL1 where output is null or output = 'File Not Found'

IF (select count(*) from #DEL1 where output = 'CNInventoryDownload.log' ) > 0
	begin
		exec master..xp_cmdshell 'del \\stl-ssis-p-01\IntegrationStaging\3PW\CN_Distro\FTP\WinSCP\Logs\Inbound\CNInventoryDownload.log'
	end	
IF (select count(*) from #DEL1 where output = 'ftpCN_GETInventoryLog.txt' ) > 0
	begin
		exec master..xp_cmdshell 'del \\stl-ssis-p-01\IntegrationStaging\3PW\CN_Distro\FTP\WinSCP\Logs\Inbound\ftpCN_GETInventoryLog.txt'
	end
IF (select count(*) from #DEL1 where output = 'CNInventoryDIR.log' ) > 0
	begin	
		exec master..xp_cmdshell 'del \\stl-ssis-p-01\IntegrationStaging\3PW\CN_Distro\FTP\WinSCP\Logs\Inbound\CNInventoryDIR.log'
	end
IF (select count(*) from #DEL1 where output = 'ftpCN_GETInventoryDIRLog.txt' ) > 0
	begin	
		exec master..xp_cmdshell 'del \\stl-ssis-p-01\IntegrationStaging\3PW\CN_Distro\FTP\WinSCP\Logs\Inbound\ftpCN_GETInventoryDIRLog.txt'
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
		@ini = ' /ini=\\stl-ssis-p-01\IntegrationStaging\3PW\CN_Distro\FTP\WinSCP\WINSCP.ini',
		@script = ' /script=\\stl-ssis-p-01\IntegrationStaging\3PW\CN_Distro\FTP\WinSCP\Scripts\Inventory\InventoryDIR.txt',
		@log = ' /log=\\stl-ssis-p-01\IntegrationStaging\3PW\CN_Distro\FTP\WinSCP\Logs\Inbound\CNInventoryDIR.log',
		@FTP = concat(@winSCP, @ini, @script, @log)

IF (Object_ID('IntegrationStaging..ftpCN_GETInventoryDIR') IS NOT NULL) DROP TABLE ftpCN_GETInventoryDIR
create table ftpCN_GETInventoryDIR
(ftpLog varchar(4000))

insert ftpCN_GETInventoryDIR exec master..xp_cmdshell @FTP

if (select count(*) from ftpCN_GETInventoryDIR where ftpLog like '%.csv') > 0


--==================================================================================================================================================
------DOWNLOAD INVENTORY FILE
--==================================================================================================================================================
		BEGIN
							
				select 

						@script = ' /script=\\stl-ssis-p-01\IntegrationStaging\3PW\CN_Distro\FTP\WinSCP\Scripts\Inventory\Inventory.txt',
						@log = ' /log=\\stl-ssis-p-01\IntegrationStaging\3PW\CN_Distro\FTP\WinSCP\Logs\Inbound\CNInventoryDownload.log',
						@FTP = concat(@winSCP, @ini, @script, @log)

				--create temp tables for ftp logs
				IF (Object_ID('IntegrationStaging..ftpCN_GETInventory') IS NOT NULL) DROP TABLE ftpCN_GETInventory
				create table ftpCN_GETInventory
				(ftpLog varchar(4000))

				--execute sql/ftp
				----connect to ftp server, if connection unsuccessful, send email
						insert ftpCN_GETInventory exec master..xp_cmdshell @FTP
						if (select count(*) from ftpCN_GETInventory where ftplog like '%.csv%[100%]') < 1
							begin
								set @Log_query = 'select * from [stl-ssis-p-01].IntegrationStaging.dbo.ftpCN_GETInventory'
								set @Log_filename = 'ftpCN_GETInventoryLog.txt'
								set @Log_file_location = '\\stl-ssis-p-01\IntegrationStaging\3PW\CN_Distro\FTP\WinSCP\Logs\Inbound\'
								set @Log_bcp = 'bcp "' + @Log_query + '" queryout "' + @Log_file_location + @Log_filename + '" -t, -T -c -S[stl-ssis-p-01]'

								exec master..xp_cmdshell @Log_bcp
															
								set @body =	'An attempt to FTP download from China Whse failed.' 
											+ char(10) + char(13) + 
											'See the attached logs for details.'
											+ char(10) + char(13) + 
											+ char(10) + char(13) + 
											'This process is managed by [stl-ssis-p-01].IntegrationStaging.wms.spMerchandisingFtpCN_GetInventoryFiles'
							
								EXEC [stl-ssis-p-01].msdb.dbo.sp_send_dbmail
								@profile_name = 'BiAdmin',
								@recipients = 'EntSysSupport@buildabear.com',
								@subject = 'FTP Failure: CN Inventory File Download from Ocean East Logistics',
								@body = @body,
								@file_attachments = '\\stl-ssis-p-01\IntegrationStaging\3PW\CN_Distro\FTP\WinSCP\Logs\Inbound\ftpCN_GETInventoryLog.txt;\\stl-ssis-p-01\IntegrationStaging\3PW\CN_Distro\FTP\WinSCP\Logs\Inbound\CNInventoryDownload.log',
								@importance = 'HIGH'
							end


		END
--==================================================================================================================================================
```

