# WEB.spFTPgetUKfiles_Web_WinSCP

**Database:** IntegrationStaging  

## Architecture Diagram

```mermaid
flowchart LR
    SP["WEB.spFTPgetUKfiles_Web_WinSCP"]
    dbo_sftpGETLogUKWhseWeb(["dbo.sftpGETLogUKWhseWeb"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.sftpGETLogUKWhseWeb |

## Stored Procedure Code

```sql
CREATE proc [WEB].[spFTPgetUKfiles_Web_WinSCP]
as
-- =====================================================================================================
-- Name: WEB.spFTPgetUKfiles_Web_WinSCP
--
-- Description:	FTP's to UK GXO server to retrieve Whse files.
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
--		Tim Callahan	09/05/2017		Created proc based of UK Retail Proc
--		Tim Callahan	11/20/2018		Updated proc to account for the PRODBAL file we now receive from Clipper 
--		Lizzy Timm		12/05/2024		Copied proc from BEDROCKDTESTB02.me_01.dbo.spMerchandisingFTPgetUKfiles_Web_WinSCP and replaced "GXO" with "GXO"
--
-- =====================================================================================================
set nocount on

-- Delete Previous Log Files
IF (Object_ID('tempdb..#DEL') IS NOT NULL) DROP TABLE #DEL
create table #DEL(output varchar(1000))
insert #DEL exec master..xp_cmdshell 'dir \\stl-ssis-p-01\IntegrationStaging\3PW\UK_Distro\FTP\WinSCP\Logs\Inbound\sftp_UK_WEB_GET.log /B'
insert #DEL exec master..xp_cmdshell 'dir \\stl-ssis-p-01\IntegrationStaging\3PW\UK_Distro\FTP\WinSCP\Logs\Inbound\sftpGETwebLog.txt /B'
delete from #DEL where output is null or output = 'File Not Found'

IF (select count(*) from #DEL where output = 'sftp_UK_WEB_GET.log') > 0
	begin
		exec master..xp_cmdshell 'del \\stl-ssis-p-01\IntegrationStaging\3PW\UK_Distro\FTP\WinSCP\Logs\Inbound\sftp_UK_WEB_GET.log'
	end
IF (select count(*) from #DEL where output = 'sftpGETwebLog.txt') > 0
	begin
		exec master..xp_cmdshell 'del \\stl-ssis-p-01\IntegrationStaging\3PW\UK_Distro\FTP\WinSCP\Logs\Inbound\sftpGETwebLog.txt'
	end

--declare and set ftp variables 
					declare 
							@winSCP varchar(1000),
							@ini varchar(1000),
							@script varchar(1000),
							@log varchar(1000),
							@SFTP varchar(4000)										
						
					select
							@winSCP = '"\\stl-ssis-p-01\C$\Program Files (x86)\WinSCP\winscp.com"',
							--@ini = ' /ini=\\stl-ssis-p-01\IntegrationStaging\3PW\UK_Distro\FTP\WinSCP\WINSCP.ini',
							@script = ' /script=\\stl-ssis-p-01\IntegrationStaging\3PW\UK_Distro\FTP\WinSCP\Scripts\Get\sftpGETweb.txt',
							@log = ' /log=\\stl-ssis-p-01\IntegrationStaging\3PW\UK_Distro\FTP\WinSCP\Logs\Inbound\sftp_UK_WEB_GET.log',
							@SFTP = concat(@winSCP, @ini, @script, @log)

--create temp tables for ftp logs

IF (Object_ID('IntegrationStaging..sftpGETLogUKWhseWeb') IS NOT NULL) DROP TABLE sftpGETLogUKWhseWeb
create table sftpGETLogUKWhseWeb
(ftpLog varchar(4000))

--execute sql/ftp
----connect to ftp server, if connection unsuccessful, send email
insert sftpGETLogUKWhseWeb exec master..xp_cmdshell @SFTP

	--select * from sftpGETLogUKWhseWeb -- Troubleshooting Purposes 

		--if (select count(*) from sftpGETLogUKWhseWeb where ftplog like '%.txt%' or ftplog like '%.dat%' ) < 1
		--	begin
		--		declare 
		--			@Log_query varchar(1000),
		--			@Log_filename varchar(100),
		--			@Log_file_location varchar(100),
		--			@Log_bcp varchar(1000),
		--			@body varchar(4000)

			
		--		set @Log_query = 'select * from me_01.dbo.sftpGETLogUKWhseWeb'
		--		set @Log_filename = 'sftpGETwebLog.txt'
		--		set @Log_file_location = '\\stl-ssis-p-01\IntegrationStaging\3PW\UK_Distro\FTP\WinSCP\Logs\Inbound\'
		--		set @Log_bcp = 'bcp "' + @Log_query + '" queryout "' + @Log_file_location + @Log_filename + '" -t, -T -c -S"stl-ssis-p-01"'

		--		exec master..xp_cmdshell @Log_bcp
										
		--		set @body =	'An attempt to SFTP Whse files from GXO - UK Web to BAB TEST appears to have failed. Please investigate.' 
		--					+ char(10) + char(13) + 
		--					'See the attached log for details.'
		--					+ char(10) + char(13) + 
		--					+ char(10) + char(13) + 
		--					'This process is managed by spMerchandisingFTPgetUKfiles_Web_WinSCP'
		
		--		EXEC [stl-ssis-p-01].msdb.dbo.sp_send_dbmail
		--		@profile_name = 'BIAdmin',
		--		@recipients = 'EntSysSupport@buildabear.com;', 
		--		@subject = 'SFTP Failure: Download Supply Chain Files from GXO Webstore - UK to BAB',
		--		@body = @body,
		--		@file_attachments = '\\stl-ssis-p-01\IntegrationStaging\3PW\UK_Distro\FTP\WinSCP\Logs\Inbound\sftpGETwebLog.txt',
		--		@importance = 'HIGH'
						
		--	end
			
------
	--move files to the interface directories
	declare @moveInventory varchar(1000),
		    @moveCBR varchar(1000),
			@moveReceipt varchar(1000),
			@moveStockAdj varchar(1000),
			@moveProdBal varchar(1000)

	select @moveInventory = 'move \\stl-ssis-p-01\IntegrationStaging\3PW\UK_Distro\FTP\WinSCP\Hold\Web\INVENTORY_WEB_*.txt \\stl-ssis-p-01\IntegrationStaging\3PW\UK_Distro\INVENTORY\Web'
	select @moveCBR = 'move \\stl-ssis-p-01\IntegrationStaging\3PW\UK_Distro\FTP\WinSCP\Hold\Web\STSIMCTN.UKWEB.*.txt \\stl-ssis-p-01\IntegrationStaging\3PW\UK_Distro\WebCBR'
	select @movereceipt = 'move \\stl-ssis-p-01\IntegrationStaging\3PW\UK_Distro\FTP\WinSCP\Hold\Web\recv*.dat \\stl-ssis-p-01\IntegrationStaging\3PW\UK_Distro\RECEIPTS'
	select @movestockadj = 'move \\stl-ssis-p-01\IntegrationStaging\3PW\UK_Distro\FTP\WinSCP\Hold\Web\STOCKADJUSTMENT_WEB_*.txt \\stl-ssis-p-01\IntegrationStaging\3PW\UK_Distro\STOCKADJ\Web'
	select @moveProdBal = 'move \\stl-ssis-p-01\IntegrationStaging\3PW\UK_Distro\FTP\WinSCP\Hold\Web\PRODBAL_WEB_*.txt \\stl-ssis-p-01\IntegrationStaging\3PW\UK_Distro\PRODBAL\WEB'

	exec master..xp_cmdshell @moveInventory
	exec master..xp_cmdshell @moveCBR
	exec master..xp_cmdshell @movereceipt
	exec master..xp_cmdshell @movestockadj
	exec master..xp_cmdshell @moveProdBal
-------------------------------------------------------------------------------------------------------------------------------------
	---now do a final dir command and send email report to confirm that files were retrieved.
	IF (Object_ID('tempdb..##dirInventory') IS NOT NULL) DROP TABLE ##dirInventory
	create table ##dirInventory(files varchar(4000))
	
	IF (Object_ID('tempdb..##dirCBR') IS NOT NULL) DROP TABLE ##dirCBR
	create table ##dirCBR(files varchar(4000))

	IF (Object_ID('tempdb..##dirReceipt') IS NOT NULL) DROP TABLE ##dirReceipt
	create table ##dirReceipt(files varchar(4000))

	IF (Object_ID('tempdb..##dirStockAdj') IS NOT NULL) DROP TABLE ##dirStockAdj
	create table ##dirStockAdj(files varchar(4000))

	IF (Object_ID('tempdb..##dirProdBal') IS NOT NULL) DROP TABLE ##dirProdBal
	create table ##dirProdBal(files varchar(4000))
	
	declare @dirInventory varchar(1000),
			@dirCBR varchar(1000),
			@dirReceipt varchar(1000),
			@dirStockAdj varchar(1000),
			@dirProdBal varchar(1000)

	select @dirInventory = 'dir \\stl-ssis-p-01\IntegrationStaging\3PW\UK_Distro\INVENTORY\Web /B'
	select @dirCBR = 'dir \\stl-ssis-p-01\IntegrationStaging\3PW\UK_Distro\WebCBR /B'
	select @dirReceipt = 'dir \\stl-ssis-p-01\IntegrationStaging\3PW\UK_Distro\RECEIPTS\ /B'
	select @dirStockAdj = 'dir \\stl-ssis-p-01\IntegrationStaging\3PW\UK_Distro\STOCKADJ\Web /B'
	select @dirProdBal = 'dir \\stl-ssis-p-01\IntegrationStaging\3PW\UK_Distro\PRODBAL\WEB /B'

	insert ##dirInventory
	exec master..xp_cmdshell @dirInventory

	insert ##dirCBR
	exec master..xp_cmdshell @dirCBR
	
	insert ##dirReceipt
	exec master..xp_cmdshell @dirreceipt
	
	insert ##dirStockAdj
	exec master..xp_cmdshell @dirstockadj

	insert ##dirProdBal
	exec master..xp_cmdshell @dirProdBal



WEB,spFTPOmniture,create proc WEB.spFTPOmniture

as

-- =====================================================================================================
-- Name: spFTPOmniture
--
-- Revision History
--		Name:			Date:			Comments:
--		Dan Tweedie		2018-04-04		Created proc
-- =====================================================================================================
	
set nocount on

--DELETE PREVIOUS LOG FILES
IF (Object_ID('tempdb..#DEL') IS NOT NULL) DROP TABLE #DEL
create table #DEL(output varchar(1000))
insert #DEL exec master..xp_cmdshell 'dir \\kermode\Filerepository\omsorders\babw-UK\log\Upload.log /B'
insert #DEL exec master..xp_cmdshell 'dir \\kermode\Filerepository\omsorders\babw-UK\log\FTPLog_UKWeb.txt /B'

delete from #DEL where output is null or output = 'File Not Found'

IF (select count(*) from #DEL where output = 'Upload.log') > 0
	begin
		exec master..xp_cmdshell 'del \\kermode\Filerepository\omsorders\babw-UK\log\Upload.log'
	end
IF (select count(*) from #DEL where output = 'FTPLog_UKWeb.txt') > 0
	begin
		exec master..xp_cmdshell 'del \\kermode\Filerepository\omsorders\babw-UK\log\FTPLog_UKWeb.txt'
	end

--CHECK FOR FILES TO UPLOAD
-------------do a DIR command and store the results in a temp table
IF (Object_ID('tempdb..#DIR') IS NOT NULL) DROP TABLE #DIR
create table #DIR (output varchar(1000))
insert #DIR exec master..xp_cmdshell 'dir \\kermode\Filerepository\omsorders\babw-UK\Temp\*.xml /B'
delete from #DIR where output is null or output = 'File Not Found'
--or substring(output, 16, 10) in (
--									select substring(ftpLog,64,10) 
--									from WEB.UKFTPTransmissionLogDump 
--									where ftplog like '%OMSInBoundOrder%'
--									and right(ftpLog,4) = '100%'
--								)


------------query temp table to see if there are CSV files
if (select count(*) from #DIR) > 0

--create table WEB.UKFTPLog 
--(UKFileName varchar(1000), UploadDateTime datetime, Success int)


BEGIN
insert WEB.UKFTPLog 
select output as UKFilename, getdate(), NULL 
from #DIR

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
							@ini = ' /ini=\\stl-ssis-p-01\Integrationstaging\wm\Production\WinSCP.ini',
							@script = ' /script=\\stl-ssis-p-01\Integrationstaging\wm\Production\winscp.txt',
							@log = ' /log=\\kermode\Filerepository\omsorders\babw-UK\log\Upload.log',
							@FTP = concat(@winSCP, @ini, @script, @log)

					--create temp tables for ftp logs
					IF (Object_ID('IntegrationStaging.WEB.tmpFTPukWeb') IS NOT NULL) DROP TABLE WEB.tmpFTPukWeb
					create table WEB.tmpFTPukWeb
					(ftpLog varchar(4000))

					--execute sql/ftp
					----connect to ftp server, if connection unsuccessful, send email
							insert WEB.tmpFTPukWeb exec master..xp_cmdshell @FTP --create table  (ftpLog varchar(4000), LogDateTime datetime)
							insert WEB.UKFTPTransmissionLogDump 
							select ftpLog, getdate() from WEB.tmpFTPukWeb 

							if (select count(*) from WEB.tmpFTPukWeb where ftplog like '%.xml%100[%]') < 1
								begin
									set @Log_query = 'select * from IntegrationStaging.WEB.tmpFTPukWeb'
									set @Log_filename = 'FTPLog_UKWeb.txt'
									set @Log_file_location = '\\kermode\Filerepository\omsorders\babw-UK\log\'
									set @Log_bcp = 'bcp "' + @Log_query + '" queryout "' + @Log_file_location + @Log_filename + '" -t, -T -c -Sstl-ssis-p-01'

									exec master..xp_cmdshell @Log_bcp
									
									------------------------------------------------------------------------------------------------------------------------
									EXEC master..xp_cmdshell 'move \\kermode\Filerepository\omsorders\babw-UK\Temp\* \\kermode\Filerepository\omsorders\babw-UK\FAILED\'
									update WEB.UKFTPLog  set Success = 0 where Success is NULL
								end
							else
								begin
			
									EXEC master..xp_cmdshell 'del \\kermode\Filerepository\omsorders\babw-UK\Temp\*.xml'
									update WEB.UKFTPLog  set Success = 1 where Success is NULL
								end

END



WEB,spFTPukORDERS,CREATE proc [WEB].[spFTPukORDERS]

as

-- =====================================================================================================
-- Name: spFTPukORDERS
--
-- Description:	Uploads web orders to UK 
--
-- Revision History
--		Name:			Date:			Comments:
--		Dan Tweedie		2017-09-25		Created proc
--		Dan Tweedie		2018-12-03		updated proc to exclude order files from uploading to uk if they are for Transactions that have canceled items
--		Dan Tweedie		2020-12-16		Updated proc to exclude non 2013 orders
-- =====================================================================================================
	
set nocount on

--DELETE PREVIOUS LOG FILES
IF (Object_ID('tempdb..#DEL') IS NOT NULL) DROP TABLE #DEL
create table #DEL(output varchar(1000))
insert #DEL exec master..xp_cmdshell 'dir \\kermode\Filerepository\omsorders\babw-UK\log\Upload.log /B'
insert #DEL exec master..xp_cmdshell 'dir \\kermode\Filerepository\omsorders\babw-UK\log\FTPLog_UKWeb.txt /B'

delete from #DEL where output is null or output = 'File Not Found'

IF (select count(*) from #DEL where output = 'Upload.log') > 0
	begin
		exec master..xp_cmdshell 'del \\kermode\Filerepository\omsorders\babw-UK\log\Upload.log'
	end
IF (select count(*) from #DEL where output = 'FTPLog_UKWeb.txt') > 0
	begin
		exec master..xp_cmdshell 'del \\kermode\Filerepository\omsorders\babw-UK\log\FTPLog_UKWeb.txt'
	end

--CHECK FOR FILES TO UPLOAD
-------------do a DIR command and store the results in a temp table
IF (Object_ID('tempdb..#DIR') IS NOT NULL) DROP TABLE #DIR
create table #DIR (output varchar(1000))
insert #DIR exec master..xp_cmdshell 'dir \\kermode\Filerepository\omsorders\babw-UK\Temp\*.xml /B'
delete from #DIR where output is null or output = 'File Not Found'

--===========================================================================================================================
--===========================================================================================================================
---------------BEGIN ORDERS WITH CANCELS----------------------------------------------
------------NEW CODE ADDED 2018-12-03 TO EXCLUDE ORDERS FROM GOING TO UK IF WE KNOW THE ORDER HAS CANCELED ITEMS
IF (Object_ID('tempdb..#FilesToExclude') IS NOT NULL) DROP TABLE #FilesToExclude
;
WITH
TransactionsWithCancels as
	(
		select 
			distinct o.TransactionID
		from [Bearcluster01.sql.buildabear.com].WebOrderProcessing.wm.Orders O  
		inner join [Bearcluster01.sql.buildabear.com].WebOrderProcessing.wm.Orderstatus s on o.Orderid = s.OrderID and s.currentstatus = 1
		inner join [Bearcluster01.sql.buildabear.com].WebOrderProcessing.wm.ItemStatus S2 on O.orderid = s2.OrderID and s2.currentstatus = 1      
		where s2.status = 'IV' and s.status = 'Complete' and Isnull(pickticketflag,0) = 0
		and sourcesite = 'BABW-UK'
	),
OrdersToExclude as
	(
		select 
			w.OrderNum
		from [Bearcluster01.sql.buildabear.com].WebOrderProcessing.wm.orders w
		join TransactionsWithCancels oc on w.TransactionID = oc.TransactionID 
		where substring(w.OrderNum, 9,1) = '_'
		UNION
		select 
			w.OrderNum
		from [Bearcluster01.sql.buildabear.com].WebOrderProcessing.wm.orders w
		where 
			case 
				when isnull(w.PickupStore,'') = ''
					then case 
						when w.SourceSite = 'BABW-US' then '0013'
						when w.SourceSite = 'BABW-UK' then '2013'
					end
				else w.PickupStore 
			end <> '2013'
		and substring(w.OrderNum, 9,1) = '_'
	),
StagedFiles as
	(
		select 
			substring(d.output, 16,10) as OrderNumber, 
			d.output as StagedFileName
		from #dir d  ---NEED TO FIND ORDERS / FILES WITH TRANSACTION ID IN ORDERSWITHCANCELS CTE, MOVE TO DIFFERENT FOLDER
		where substring(d.output, 16,10) in (select OrderNum from OrdersToExclude)
	)
select * 
into #FilesToExclude
from StagedFiles 

if (select count(*) from #FilesToExclude) > 0

BEGIN

		declare 
			@FileCount int,
			@FileName varchar(100),
			@Move varchar(1000)

		select @FileCount = count(*) from #FilesToExclude

		while @FileCount > 0
			begin
				select @FileCount = count(*) from #FilesToExclude

				select 
					@FileName = max(StagedFileName) 
				from #FilesToExclude

				select @Move = 'move \\kermode\Filerepository\omsorders\babw-UK\Temp\' + @FileName + ' \\kermode\Filerepository\OMSOrders\BABW-UK\Temp\OrdersWithCancels\'

				EXEC master..xp_cmdshell @Move 

				delete from #FilesToExclude
				where StagedFileName = @FileName

				if (select count(*) from #FilesToExclude) = 0
					break
				else
					continue
			end
END
---------------------------------------------- END ORDERS WITH CANCELS----------------------------------------------------


--===========================================================================================================================
--===========================================================================================================================


------------query temp table to see if there are CSV files
if (select count(*) from #DIR) > 0

--create table WEB.UKFTPLog 
--(UKFileName varchar(1000), UploadDateTime datetime, Success int)


BEGIN
insert WEB.UKFTPLog 
select output as UKFilename, getdate(), NULL 
from #DIR

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
							@ini = ' /ini=\\stl-ssis-p-01\Integrationstaging\wm\Production\WinSCP.ini',
							@script = ' /script=\\stl-ssis-p-01\Integrationstaging\wm\Production\winscp.txt',
							@log = ' /log=\\kermode\Filerepository\omsorders\babw-UK\log\Upload.log',
							@FTP = concat(@winSCP, @ini, @script, @log)

					--create temp tables for ftp logs
					IF (Object_ID('IntegrationStaging.WEB.tmpFTPukWeb') IS NOT NULL) DROP TABLE WEB.tmpFTPukWeb
					create table WEB.tmpFTPukWeb
					(ftpLog varchar(4000))

					--execute sql/ftp
					----connect to ftp server, if connection unsuccessful, send email
							insert WEB.tmpFTPukWeb exec master..xp_cmdshell @FTP --create table  (ftpLog varchar(4000), LogDateTime datetime)
							insert WEB.UKFTPTransmissionLogDump 
							select ftpLog, getdate() from WEB.tmpFTPukWeb 

							if (select count(*) from WEB.tmpFTPukWeb where ftplog like '%.xml%100[%]') < 1
								begin
									set @Log_query = 'select * from IntegrationStaging.WEB.tmpFTPukWeb'
									set @Log_filename = 'FTPLog_UKWeb.txt'
									set @Log_file_location = '\\kermode\Filerepository\omsorders\babw-UK\log\'
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
									EXEC master..xp_cmdshell 'move \\kermode\Filerepository\omsorders\babw-UK\Temp\* \\kermode\Filerepository\omsorders\babw-UK\FAILED\'
									update WEB.UKFTPLog  set Success = 0 where Success is NULL
								end
							else
								begin
									--EXEC master..xp_cmdshell 'move \\kermode\Filerepository\omsorders\babw-UK\Temp\* \\kermode\Filerepository\omsorders\babw-UK\Success\'
									EXEC master..xp_cmdshell 'del \\kermode\Filerepository\omsorders\babw-UK\Temp\*.xml'
									update WEB.UKFTPLog  set Success = 1 where Success is NULL
								end

END
```

