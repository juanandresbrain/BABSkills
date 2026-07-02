# dbo.spMerchandisingFTPgetUKfiles_WinSCP

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMerchandisingFTPgetUKfiles_WinSCP"]
    dbo_sftpGETLogUKWhse(["dbo.sftpGETLogUKWhse"]) --> SP
    dbo_sp_send_dbmail(["dbo.sp_send_dbmail"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.sftpGETLogUKWhse |
| dbo.sp_send_dbmail |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spMerchandisingFTPgetUKfiles_WinSCP]
as
-- =====================================================================================================
-- Name: spMerchandisingFTPgetUKfiles_WinSCP
--
-- Description:	FTP's to UK Clipper server to retrieve Whse files.
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
--		Tim Callahan	01/24/2017		Created proc.	
--		Tim Callahan	02/09/2017		Implemented Proc into Prod after testing with Clipper IT 
--		Tim Callahan	08/04/2022		As related to JIRA Task BIB419 - There are reports that "Clipper loads file to the FTP address but we are unable to see them." 
--										To provide evidence thought it would be best to not delete the sftp_UK_GET.log upon each run so we can look back when there are file discrepency discussions 
--		Lizzy Timm		04/01/2025		Updated email failure criteria to only send during the main pull at 4
-- =====================================================================================================
set nocount on

-- Delete Previous Log Files
IF (Object_ID('tempdb..#DEL') IS NOT NULL) DROP TABLE #DEL
create table #DEL(output varchar(1000))
--insert #DEL exec master..xp_cmdshell 'dir \\kermode\FileRepository\MERCHANDISING\UK_Distro\FTP\WinSCP\Logs\Inbound\sftp_UK_GET.log /B' -- Remarked out on 8/4/2022
insert #DEL exec master..xp_cmdshell 'dir \\kermode\FileRepository\MERCHANDISING\UK_Distro\FTP\WinSCP\Logs\Inbound\sftpGETLog.txt /B'
delete from #DEL where output is null or output = 'File Not Found'


--IF (select count(*) from #DEL where output = 'sftp_UK_GET.log') > 0
--	begin
--		exec master..xp_cmdshell 'del \\kermode\FileRepository\MERCHANDISING\UK_Distro\FTP\WinSCP\Logs\Inbound\sftp_UK_GET.log' -- Remarked out on 8/4/2022
--	end
IF (select count(*) from #DEL where output = 'sftpGETLog.txt') > 0
	begin
		exec master..xp_cmdshell 'del \\kermode\FileRepository\MERCHANDISING\UK_Distro\FTP\WinSCP\Logs\Inbound\sftpGETLog.txt'
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
							@ini = ' /ini=\\kermode\FileRepository\MERCHANDISING\UK_Distro\FTP\WinSCP\WINSCP.ini',
							@script = ' /script=\\kermode\FileRepository\MERCHANDISING\UK_Distro\FTP\WinSCP\Scripts\Get\sftpGET.txt',
							@log = ' /log=\\kermode\FileRepository\MERCHANDISING\UK_Distro\FTP\WinSCP\Logs\Inbound\sftp_UK_GET.log',
							@SFTP = concat(@winSCP, @ini, @script, @log)

--create temp tables for ftp logs

IF (Object_ID('me_01..sftpGETLogUKWhse') IS NOT NULL) DROP TABLE sftpGETLogUKWhse
create table sftpGETLogUKWhse
(ftpLog varchar(4000))

--execute sql/ftp
----connect to ftp server, if connection unsuccessful, send email
insert sftpGETLogUKWhse exec master..xp_cmdshell @SFTP

	--select * from sftpGETLogUKWhse -- Troubleshooting Purposes 

		if (select count(*) from sftpGETLogUKWhse where ftplog like '%.txt%' or ftplog like '%.dat%' ) < 1
		  AND DATEPART(hh, getdate()) = 4 

			begin
				declare 
					@Log_query varchar(1000),
					@Log_filename varchar(100),
					@Log_file_location varchar(100),
					@Log_bcp varchar(1000),
					@body varchar(4000)

			
				set @Log_query = 'select * from BEDROCKDB02.me_01.dbo.sftpGETLogUKWhse'
				set @Log_filename = 'sftpGETLog.txt'
				set @Log_file_location = '\\kermode\FileRepository\MERCHANDISING\UK_Distro\FTP\WinSCP\Logs\Inbound\'
				set @Log_bcp = 'bcp "' + @Log_query + '" queryout "' + @Log_file_location + @Log_filename + '" -t, -T -c -SBEDROCKDB02'

				exec master..xp_cmdshell @Log_bcp
										
				set @body =	'An attempt to SFTP Whse files from Clipper - UK to BAB appears to have failed. Please investigate.' 
							+ char(10) + char(13) + 
							'See the attached log for details.'
							+ char(10) + char(13) + 
							+ char(10) + char(13) + 
							'This process is managed by spMerchandisingFTPgetUKfiles_WinSCP'
		
				EXEC BEDROCKDB02.msdb.dbo.sp_send_dbmail
				@profile_name = 'MerchAdmin',
				@recipients = 'EntSysSupport@buildabear.com;LizzyT@buildabear.com;',
				@subject = 'SFTP Failure: Download Supply Chain Files from Clipper - UK to BAB',
				@body = @body,
				@file_attachments = '\\kermode\FileRepository\MERCHANDISING\UK_Distro\FTP\WinSCP\Logs\Inbound\sftpGETLog.txt',
				@importance = 'HIGH'
						
			end
			
------
	--move files to the interface directories
	declare @moveInventory varchar(1000),
		    @moveShipment varchar(1000),
			@moveReceipt varchar(1000),
			@moveStockAdj varchar(1000)

	select @moveInventory = 'move \\kermode\FileRepository\MERCHANDISING\UK_Distro\FTP\WinSCP\Hold\inventory*.txt \\kermode\FileRepository\MERCHANDISING\UK_Distro\INVENTORY'
	select @moveshipment = 'move \\kermode\FileRepository\MERCHANDISING\UK_Distro\FTP\WinSCP\Hold\distribution*.txt \\kermode\FileRepository\MERCHANDISING\UK_Distro\SHIPMENTS'
	select @movereceipt = 'move \\kermode\FileRepository\MERCHANDISING\UK_Distro\FTP\WinSCP\Hold\recv*.dat \\kermode\FileRepository\MERCHANDISING\UK_Distro\RECEIPTS'
	select @movestockadj = 'move \\kermode\FileRepository\MERCHANDISING\UK_Distro\FTP\WinSCP\Hold\stockadjustment*.txt \\kermode\FileRepository\MERCHANDISING\UK_Distro\STOCKADJ'

	exec master..xp_cmdshell @moveInventory
	exec master..xp_cmdshell @moveshipment
	exec master..xp_cmdshell @movereceipt
	exec master..xp_cmdshell @movestockadj
-------------------------------------------------------------------------------------------------------------------------------------
	---now do a final dir command and send email report to confirm that files were retrieved.
	IF (Object_ID('tempdb..##dirInventory') IS NOT NULL) DROP TABLE ##dirInventory
	create table ##dirInventory(files varchar(4000))
	
	IF (Object_ID('tempdb..##dirShipment') IS NOT NULL) DROP TABLE ##dirShipment
	create table ##dirShipment(files varchar(4000))

	IF (Object_ID('tempdb..##dirReceipt') IS NOT NULL) DROP TABLE ##dirReceipt
	create table ##dirReceipt(files varchar(4000))

	IF (Object_ID('tempdb..##dirStockAdj') IS NOT NULL) DROP TABLE ##dirStockAdj
	create table ##dirStockAdj(files varchar(4000))
	
	declare @dirInventory varchar(1000),
			@dirShipment varchar(1000),
			@dirReceipt varchar(1000),
			@dirStockAdj varchar(1000)

	select @dirInventory = 'dir \\kermode\FileRepository\MERCHANDISING\UK_Distro\INVENTORY /B'
	select @dirShipment = 'dir \\kermode\FileRepository\MERCHANDISING\UK_Distro\SHIPMENTS /B'
	select @dirReceipt = 'dir \\kermode\FileRepository\MERCHANDISING\UK_Distro\RECEIPTS /B'
	select @dirStockAdj = 'dir \\kermode\FileRepository\MERCHANDISING\UK_Distro\STOCKADJ /B'

	insert ##dirInventory
	exec master..xp_cmdshell @dirInventory

	insert ##dirShipment
	exec master..xp_cmdshell @dirshipment
	
	insert ##dirReceipt
	exec master..xp_cmdshell @dirreceipt
	
	insert ##dirStockAdj
	exec master..xp_cmdshell @dirstockadj

/*	declare @inv int,
			@shpmt int,
			@rcpt int,
			@adj int,
			@text nvarchar(max)

	select @inv = count(*) from ##dirInventory where files like '%.txt'
	select @shpmt = count(*) from ##dirShipment where files like '%.txt'
	select @rcpt = count(*) from ##dirReceipt where files like '%.dat'
	select @adj = count(*) from ##dirStockAdj where files like '%.txt'

	set @text = '<font face =arial size = 2>' + 
			'Clipper File Count Summary<br>' +
			'(files retrieved from the Clipper UK server and successfully located to our interface directories on \\kermode\FileRepository\MERCHANDISING\UK_Distro)' + 
			'<br><br>' +
			'<table border="1">' +
			'<tr><th>SHIPMENT</th><th>RECEIPT</th><th>ADJUSTMENT</th><th>INVENTORY</th></tr>' +
			CAST ( ( SELECT td = @shpmt,'',
							td = @rcpt, '',
							td = @adj, '',
							td = @inv, ''
					  FOR XML PATH('tr'), TYPE 
			) AS NVARCHAR(MAX) ) +
			'</font></table></font></p></p>
			<br>
			<font face =arial size = 1>This report was run from bedrockdb02.me_01.dbo.spMerchandisingFTPgetUKfiles_WinSCP.</font>
			<br>
			<br>'

	exec msdb.dbo.sp_send_dbmail
		@profile_name = 'merchadmin',
		@recipients = 'MerchAdmin@buildabear.com', -- Change to MerchAdmin once in production
		@body = @text,
		@subject = 'Clipper UK File Summary',
		@body_format = 'HTML'
*/
```

