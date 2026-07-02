# dbo.spMerchandisingFtpUKSKU_bak

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMerchandisingFtpUKSKU_bak"]
    dbo_ftpPUT_SKU(["dbo.ftpPUT_SKU"]) --> SP
    dbo_sp_send_dbmail(["dbo.sp_send_dbmail"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ftpPUT_SKU |
| dbo.sp_send_dbmail |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spMerchandisingFtpUKSKU]

as

-- =====================================================================================================
-- Name: spMerchandisingFtpUKSKU
--
-- Description:	Outputs CSV file for UK Item Master
--
-- Revision History
--		Name:			Date:			Comments:
--		Dan Tweedie		03/31/2015		Created proc
--		Keith Lee		9/7/2017		Updated proc to look and send .xml files for item master
-- =====================================================================================================
	
set nocount on

--check the directory to see if there are distro CSV files ready to import
-------------do a DIR command and store the results in a temp table
IF (Object_ID('tempdb..#DIR') IS NOT NULL) DROP TABLE #DIR
create table #DIR (output varchar(1000))
--insert #DIR exec master..xp_cmdshell 'dir \\kermode\FileRepository\MERCHANDISING\UK_Distro\OUTBOUND\ItemMaster\*.csv /B' -- old
insert #DIR exec master..xp_cmdshell 'dir \\kermode\FileRepository\MERCHANDISING\UK_Distro\OUTBOUND\ItemMaster\*.xml /B'  -- change for go live 9/11/2017
delete from #DIR where output is null or output = 'File Not Found'

------------query temp table to see if there are XML files
if (select count(*) from #DIR) > 0

BEGIN
			-----ftp upload
					declare @ftpPUT varchar(1000),
							@Log_query varchar(1000),
							@Log_filename varchar(100),
							@Log_file_location varchar(100),
							@Log_bcp varchar(1000),
							@body varchar(4000)
							
					set @ftpPUT = 'ftp -d -s:\\kermode\FileRepository\MERCHANDISING\uk_distro\OUTBOUND\FTP\ftpPUT_SKU.txt' 

					--create temp tables for ftp logs
					IF (Object_ID('me_01..ftpPUT_SKU') IS NOT NULL) DROP TABLE ftpPUT_SKU
					create table ftpPUT_SKU
					(ftpLog varchar(4000))

					--execute sql/ftp
					----connect to ftp server, if connection unsuccessful, send email
							insert ftpPUT_SKU exec master..xp_cmdshell @ftpPUT
							if (select count(*) from ftpPUT_SKU where ftplog like '%Port command successful%') < 1
								begin
									set @Log_query = 'select * from bedrockdb02.me_01.dbo.ftpPUT_SKU'
									set @Log_filename = 'ftpPUT_SKULog.txt'
									set @Log_file_location = '\\kermode\FileRepository\MERCHANDISING\uk_distro\OUTBOUND\FTP\LOGS\'
									set @Log_bcp = 'bcp "' + @Log_query + '" queryout "' + @Log_file_location + @Log_filename + '" -t, -T -c -Sbedrockdb02'

									exec master..xp_cmdshell @Log_bcp
															
									set @body =	'An attempt to FTP a UK SKU file from Clipper failed.' 
												+ char(10) + char(13) + 
												'See the attached log for details.'
												+ char(10) + char(13) + 
												+ char(10) + char(13) + 
												'This process is managed by bedrockdb02.me_01.dbo.spMerchandisingFtpUKSKU'
							
									EXEC bedrockdb02.msdb.dbo.sp_send_dbmail
									@profile_name = 'MerchAdmin',
									@recipients = 'merchadmin@buildabear.com',
									@subject = 'FTP Failure: UK SKU File Upload from BAB to Clipper',
									@body = @body,
									@file_attachments = '\\kermode\FileRepository\MERCHANDISING\uk_distro\OUTBOUND\FTP\LOGS\ftpPUT_SKULog.txt',
									@importance = 'HIGH'
								end
							else
								begin
									EXEC master..xp_cmdshell 'move \\kermode\FileRepository\MERCHANDISING\UK_Distro\OUTBOUND\ItemMaster\* \\kermode\FileRepository\MERCHANDISING\UK_Distro\OUTBOUND\ItemMaster\done'
								end

END
```

