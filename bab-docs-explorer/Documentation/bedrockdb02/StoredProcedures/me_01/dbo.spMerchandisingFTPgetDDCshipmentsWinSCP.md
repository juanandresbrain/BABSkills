# dbo.spMerchandisingFTPgetDDCshipmentsWinSCP

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMerchandisingFTPgetDDCshipmentsWinSCP"]
    dbo_ftpWC_GETShipments(["dbo.ftpWC_GETShipments"]) --> SP
    dbo_ftpWC_GETShipmentsDIR(["dbo.ftpWC_GETShipmentsDIR"]) --> SP
    dbo_sp_send_dbmail(["dbo.sp_send_dbmail"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ftpWC_GETShipments |
| dbo.ftpWC_GETShipmentsDIR |
| dbo.sp_send_dbmail |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spMerchandisingFTPgetDDCshipmentsWinSCP]

as

-- =====================================================================================================
-- Name: spMerchandisingFTPgetDDCshipmentsWinSCP
--
--
-- Revision History
--		Name:			Date:			Comments:
--		Dan Tweedie		2020-06-23		Created proc
-- =====================================================================================================
	
set nocount on


--==================================================================================================================================================
--DELETE PREVIOUS LOG FILES
IF (Object_ID('tempdb..#DEL4') IS NOT NULL) DROP TABLE #DEL4
create table #DEL4(output varchar(1000))
	insert #DEL4 exec master..xp_cmdshell 'dir \\kermode\FileRepository\MERCHANDISING\WC_Distro\FTP\WinSCP\Logs\Inbound\WCShipmentsDownload.log /B'
	insert #DEL4 exec master..xp_cmdshell 'dir \\kermode\FileRepository\MERCHANDISING\WC_Distro\FTP\WinSCP\Logs\Inbound\ftpWC_GETShipmentsLog.txt /B'
	insert #DEL4 exec master..xp_cmdshell 'dir \\kermode\FileRepository\MERCHANDISING\WC_Distro\FTP\WinSCP\Logs\Inbound\WCShipmentsDIR.log /B'
	insert #DEL4 exec master..xp_cmdshell 'dir \\kermode\FileRepository\MERCHANDISING\WC_Distro\FTP\WinSCP\Logs\Inbound\ftpWC_GETShipmentsDIRLog.txt /B'
delete from #DEL4 where output is null or output = 'File Not Found'

IF (select count(*) from #DEL4 where output = 'WCShipmentsDownload.log') > 0
	begin
		exec master..xp_cmdshell 'del \\kermode\FileRepository\MERCHANDISING\WC_Distro\FTP\WinSCP\Logs\Inbound\WCShipmentsDownload.log'
	end
IF (select count(*) from #DEL4 where output = 'ftpWC_GETShipmentsLog.txt') > 0
	begin
		exec master..xp_cmdshell 'del \\kermode\FileRepository\MERCHANDISING\WC_Distro\FTP\WinSCP\Logs\Inbound\ftpWC_GETShipmentsLog.txt'
	end	
IF (select count(*) from #DEL4 where output = 'WCShipmentsDIR.log') > 0
	begin
		exec master..xp_cmdshell 'del \\kermode\FileRepository\MERCHANDISING\WC_Distro\FTP\WinSCP\Logs\Inbound\WCShipmentsDIR.log'
	end	
IF (select count(*) from #DEL4 where output = 'ftpWC_GETShipmentsDIRLog.txt') > 0
	begin
		exec master..xp_cmdshell 'del \\kermode\FileRepository\MERCHANDISING\WC_Distro\FTP\WinSCP\Logs\Inbound\ftpWC_GETShipmentsDIRLog.txt'
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
		--@ini = ' /ini=\\kermode\FileRepository\MERCHANDISING\WC_Distro\FTP\WinSCP\WINSCP.ini',
		@script = ' /script=\\kermode\FileRepository\MERCHANDISING\WC_Distro\FTP\WinSCP\Scripts\Shipments\ShipmentsDIR.txt',
		@log = ' /log=\\kermode\FileRepository\MERCHANDISING\WC_Distro\FTP\WinSCP\Logs\Inbound\WCShipmentsDIR.log',
		@FTP = concat(@winSCP, /*@ini,*/ @script, @log)

IF (Object_ID('me_01..ftpWC_GETShipmentsDIR') IS NOT NULL) DROP TABLE ftpWC_GETShipmentsDIR
create table ftpWC_GETShipmentsDIR
(ftpLog varchar(4000))

insert ftpWC_GETShipmentsDIR exec master..xp_cmdshell @FTP

if (select count(*) from ftpWC_GETShipmentsDIR where ftpLog like '%.dat') > 0


--==================================================================================================================================================
------DOWNLOAD SHIPMENTS FILE
--==================================================================================================================================================
		BEGIN
				select 
						@script = ' /script=\\kermode\FileRepository\MERCHANDISING\WC_Distro\FTP\WinSCP\Scripts\Shipments\Shipments.txt',
						@log = ' /log=\\kermode\FileRepository\MERCHANDISING\WC_Distro\FTP\WinSCP\Logs\Inbound\WCShipmentsDownload.log',
						@FTP = concat(@winSCP, /*@ini,*/ @script, @log)

				--create temp tables for ftp logs
				IF (Object_ID('me_01..ftpWC_GETShipments') IS NOT NULL) DROP TABLE ftpWC_GETShipments
				create table ftpWC_GETShipments
				(ftpLog varchar(4000))

				--execute sql/ftp
				----connect to ftp server, if connection unsuccessful, send email
						insert ftpWC_GETShipments exec master..xp_cmdshell @FTP
						if (select count(*) from ftpWC_GETShipments where ftplog like '%.dat%[100%]') < 1
							begin
								set @Log_query = 'select * from bedrockdb02.me_01.dbo.ftpWC_GETShipments'
								set @Log_filename = 'ftpWC_GETShipmentsLog.txt'
								set @Log_file_location = '\\kermode\FileRepository\MERCHANDISING\WC_Distro\FTP\WinSCP\Logs\Inbound\'
								set @Log_bcp = 'bcp "' + @Log_query + '" queryout "' + @Log_file_location + @Log_filename + '" -t, -T -c -Sbedrockdb02'

								exec master..xp_cmdshell @Log_bcp
															
								set @body =	'An attempt to FTP download from DDC failed.' 
											+ char(10) + char(13) + 
											'See the attached logs for details.'
											+ char(10) + char(13) + 
											+ char(10) + char(13) + 
											'This process is managed by bedrockdb02.me_01.dbo.spMerchandisingFtpWC_GetShipmentFilesWinSCP'
							
								EXEC bedrockdb02.msdb.dbo.sp_send_dbmail
								@profile_name = 'MerchAdmin',
								@recipients = 'EntSysSupport@buildabear.com',
								@subject = 'FTP Failure: WC Shipment File Download from DDC',
								@body = @body,
								@file_attachments = '\\kermode\FileRepository\MERCHANDISING\WC_Distro\FTP\WinSCP\Logs\Inbound\ftpWC_GETShipmentsLog.txt;\\kermode\FileRepository\MERCHANDISING\WC_Distro\FTP\WinSCP\Logs\Inbound\WCShipmentsDownload.log',
								@importance = 'HIGH'
							end


		END
--==================================================================================================================================================
```

