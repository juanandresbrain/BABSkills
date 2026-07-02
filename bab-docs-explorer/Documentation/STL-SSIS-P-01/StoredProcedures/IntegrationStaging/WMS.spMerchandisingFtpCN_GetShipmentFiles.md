# WMS.spMerchandisingFtpCN_GetShipmentFiles

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["WMS.spMerchandisingFtpCN_GetShipmentFiles"]
    dbo_ftpCN_GETShipments(["dbo.ftpCN_GETShipments"]) --> SP
    dbo_ftpCN_GETShipmentsDIR(["dbo.ftpCN_GETShipmentsDIR"]) --> SP
    dbo_sp_send_dbmail(["dbo.sp_send_dbmail"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ftpCN_GETShipments |
| dbo.ftpCN_GETShipmentsDIR |
| dbo.sp_send_dbmail |

## Stored Procedure Code

```sql
CREATE proc [WMS].[spMerchandisingFtpCN_GetShipmentFiles]

as

-- =====================================================================================================
-- Name: spMerchandisingFtpCN_GetShipmentFiles
--
-- Description:	Downloads staged Shipment file from Shanghai warehouse system, stages files for import to Merchandising system
--
-- Revision History
--		Name:			Date:			Comments:
--		Dan Tweedie		03/29/2016		Created proc
--		Tim Callahan	2025-01-31		Ported over from Bedrockdb02 as part of Aptos Decommission
-- =====================================================================================================
	
set nocount on


--==================================================================================================================================================
--DELETE PREVIOUS LOG FILES
IF (Object_ID('tempdb..#DEL4') IS NOT NULL) DROP TABLE #DEL4
create table #DEL4(output varchar(1000))
	insert #DEL4 exec master..xp_cmdshell 'dir \\stl-ssis-p-01\IntegrationStaging\3PW\CN_Distro\FTP\WinSCP\Logs\Inbound\CNShipmentsDownload.log /B'
	insert #DEL4 exec master..xp_cmdshell 'dir \\stl-ssis-p-01\IntegrationStaging\3PW\CN_Distro\FTP\WinSCP\Logs\Inbound\ftpCN_GETShipmentsLog.txt /B'
	insert #DEL4 exec master..xp_cmdshell 'dir \\stl-ssis-p-01\IntegrationStaging\3PW\CN_Distro\FTP\WinSCP\Logs\Inbound\CNShipmentsDIR.log /B'
	insert #DEL4 exec master..xp_cmdshell 'dir \\stl-ssis-p-01\IntegrationStaging\3PW\CN_Distro\FTP\WinSCP\Logs\Inbound\ftpCN_GETShipmentsDIRLog.txt /B'
delete from #DEL4 where output is null or output = 'File Not Found'

IF (select count(*) from #DEL4 where output = 'CNShipmentsDownload.log') > 0
	begin
		exec master..xp_cmdshell 'del \\stl-ssis-p-01\IntegrationStaging\3PW\CN_Distro\FTP\WinSCP\Logs\Inbound\CNShipmentsDownload.log'
	end
IF (select count(*) from #DEL4 where output = 'ftpCN_GETShipmentsLog.txt') > 0
	begin
		exec master..xp_cmdshell 'del \\stl-ssis-p-01\IntegrationStaging\3PW\CN_Distro\FTP\WinSCP\Logs\Inbound\ftpCN_GETShipmentsLog.txt'
	end	
IF (select count(*) from #DEL4 where output = 'CNShipmentsDIR.log') > 0
	begin
		exec master..xp_cmdshell 'del \\stl-ssis-p-01\IntegrationStaging\3PW\CN_Distro\FTP\WinSCP\Logs\Inbound\CNShipmentsDIR.log'
	end	
IF (select count(*) from #DEL4 where output = 'ftpCN_GETShipmentsDIRLog.txt') > 0
	begin
		exec master..xp_cmdshell 'del \\stl-ssis-p-01\IntegrationStaging\3PW\CN_Distro\FTP\WinSCP\Logs\Inbound\ftpCN_GETShipmentsDIRLog.txt'
	end

--==================================================================================================================================================
------CHECK FOR EXISTENCE OF SHIPMENTS FILE
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
		@script = ' /script=\\stl-ssis-p-01\IntegrationStaging\3PW\CN_Distro\FTP\WinSCP\Scripts\Shipments\ShipmentsDIR.txt',
		@log = ' /log=\\stl-ssis-p-01\IntegrationStaging\3PW\CN_Distro\FTP\WinSCP\Logs\Inbound\CNShipmentsDIR.log',
		@FTP = concat(@winSCP, @ini, @script, @log)

IF (Object_ID('IntegrationStaging..ftpCN_GETShipmentsDIR') IS NOT NULL) DROP TABLE ftpCN_GETShipmentsDIR
create table ftpCN_GETShipmentsDIR
(ftpLog varchar(4000))

insert ftpCN_GETShipmentsDIR exec master..xp_cmdshell @FTP

if (select count(*) from ftpCN_GETShipmentsDIR where ftpLog like '%.csv') > 0


--==================================================================================================================================================
------DOWNLOAD SHIPMENTS FILE
--==================================================================================================================================================
		BEGIN
				select 
						@script = ' /script=\\stl-ssis-p-01\IntegrationStaging\3PW\CN_Distro\FTP\WinSCP\Scripts\Shipments\Shipments.txt',
						@log = ' /log=\\stl-ssis-p-01\IntegrationStaging\3PW\CN_Distro\FTP\WinSCP\Logs\Inbound\CNShipmentsDownload.log',
						@FTP = concat(@winSCP, @ini, @script, @log)

				--create temp tables for ftp logs
				IF (Object_ID('IntegrationStaging..ftpCN_GETShipments') IS NOT NULL) DROP TABLE ftpCN_GETShipments
				create table ftpCN_GETShipments
				(ftpLog varchar(4000))

				--execute sql/ftp
				----connect to ftp server, if connection unsuccessful, send email
						insert ftpCN_GETShipments exec master..xp_cmdshell @FTP
						if (select count(*) from ftpCN_GETShipments where ftplog like '%.csv%[100%]') < 1
							begin
								set @Log_query = 'select * from [stl-ssis-p-01].IntegrationStaging.dbo.ftpCN_GETShipments'
								set @Log_filename = 'ftpCN_GETShipmentsLog.txt'
								set @Log_file_location = '\\stl-ssis-p-01\IntegrationStaging\3PW\CN_Distro\FTP\WinSCP\Logs\Inbound\'
								set @Log_bcp = 'bcp "' + @Log_query + '" queryout "' + @Log_file_location + @Log_filename + '" -t, -T -c -S[stl-ssis-p-01]'

								exec master..xp_cmdshell @Log_bcp
															
								set @body =	'An attempt to FTP download from Ocean East Logistics failed.' 
											+ char(10) + char(13) + 
											'See the attached logs for details.'
											+ char(10) + char(13) + 
											+ char(10) + char(13) + 
											'This process is managed by [stl-ssis-p-01].IntegrationStaging.wms.spMerchandisingFtpCN_GetShipmentFiles'
							
								EXEC [stl-ssis-p-01].msdb.dbo.sp_send_dbmail
								@profile_name = 'BiAdmin',
								@recipients = 'EntSysSupport@buildabear.com',
								@subject = 'FTP Failure: CN Shipment File Download from China Whse failed.',
								@body = @body,
								@file_attachments = '\\stl-ssis-p-01\IntegrationStaging\3PW\CN_Distro\FTP\WinSCP\Logs\Inbound\ftpCN_GETShipmentsLog.txt;\\stl-ssis-p-01\IntegrationStaging\3PW\CN_Distro\FTP\WinSCP\Logs\Inbound\CNShipmentsDownload.log',
								@importance = 'HIGH'
							end


		END
--==================================================================================================================================================
```

