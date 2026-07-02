# dbo.spMerchandisingSelectDDCFiles

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMerchandisingSelectDDCFiles"]
    dbo_tblDDCFiles(["dbo.tblDDCFiles"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tblDDCFiles |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spMerchandisingSelectDDCFiles]
as
-- =====================================================================================================
-- Name: spMerchandisingSelectDDCFiles
--
-- Description:	Captures record of DDC (west coast dc) files to be processed
--
-- Input:	
--
-- Output: 
--
-- Dependencies:
--
-- Revision History
--		Name:			Date:			Comments:
--		Dan Tweedie		10/17/2011		Created proc.	
--		Dan Tweedie		07/14/2015		Pointed to Kermode instead of Oursmerchdb01, added email summary to show file counts
-- =====================================================================================================

set nocount on


--get a DIR listing from each of the DDC file directories
IF (Object_ID('tempdb..#a') IS NOT NULL) DROP TABLE #a
IF (Object_ID('tempdb..#b') IS NOT NULL) DROP TABLE #b
IF (Object_ID('tempdb..#c') IS NOT NULL) DROP TABLE #c
IF (Object_ID('tempdb..#d') IS NOT NULL) DROP TABLE #d

create table #a (output varchar(1000))
create table #b (output varchar(1000))
create table #c (output varchar(1000))
create table #d (output varchar(1000))

insert #a exec master..xp_cmdshell 'dir \\kermode\FileRepository\MERCHANDISING\WC_Distro\SHIPMENTS\*.dat /B'
insert #b exec master..xp_cmdshell 'dir \\kermode\FileRepository\MERCHANDISING\WC_Distro\RECEIPTS\*.dat /B'
insert #c exec master..xp_cmdshell 'dir \\kermode\FileRepository\MERCHANDISING\WC_Distro\STOCKADJ\*.txt /B'
insert #d exec master..xp_cmdshell 'dir \\kermode\FileRepository\MERCHANDISING\WC_Distro\INVENTORY\*.txt /B'

insert tblDDCFiles select output DDCFileName, 'Shipment' DDCFileType, getdate() Capture_Date from #a where output is not null and output not in (select ddcfilename from tblDDCFiles)
insert tblDDCFiles select output DDCFileName, 'Receipt' DDCFileType, getdate() Capture_Date from #b where output is not null and output not in (select ddcfilename from tblDDCFiles)
insert tblDDCFiles select output DDCFileName, 'Adjustment' DDCFileType, getdate() Capture_Date from #c where output is not null and output not in (select ddcfilename from tblDDCFiles)
insert tblDDCFiles select output DDCFileName, 'Inventory' DDCFileType, getdate() Capture_Date from #d where output is not null and output not in (select ddcfilename from tblDDCFiles)

--Email File Count Summary
/*	declare @inv int,
			@shpmt int,
			@rcpt int,
			@adj int,
			@text nvarchar(max)

	select @shpmt = count(*) from #a where output like '%.dat'
	select @rcpt = count(*) from #b where output like '%.dat'
	select @adj = count(*) from #c where output like '%.txt'
	select @inv = count(*) from #d where output like '%.txt'

	set @text = '<font face =arial size = 2>' + 
			'DDC File Count Summary<br>' +
			'(files retrieved from the DDC server and successfully located to our interface directories on \\kermode\FileRepository\MERCHANDISING\WC_Distro)' + 
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
			<font face =arial size = 1>This report was run from bedrockdb02.me_01.dbo.spMerchandisingSelectDDCFiles.</font>
			<br>
			<br>'

	exec msdb.dbo.sp_send_dbmail
		@profile_name = 'merchadmin',
		@recipients = 'merchadmin@buildabear.com',
		@body = @text,
		@subject = 'DDC File Summary',
		@body_format = 'HTML'
*/
```

