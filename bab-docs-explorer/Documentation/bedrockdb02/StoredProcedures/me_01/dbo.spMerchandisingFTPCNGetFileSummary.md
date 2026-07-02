# dbo.spMerchandisingFTPCNGetFileSummary

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMerchandisingFTPCNGetFileSummary"]
    dbo_sp_send_dbmail(["dbo.sp_send_dbmail"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.sp_send_dbmail |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spMerchandisingFTPCNGetFileSummary]

as

set nocount on

-- =====================================================================================================
-- Name: spMerchandisingFTPCNGetFileSummary
--
-- Description:	Captures and emails summary of files downloaded from Shanghai DC 
--
-- Revision History
--		Name:			Date:			Comments:
--		Dan Tweedie		03/29/2016		Created proc
--		Tim Callahan	06/14/2021		Updated 3rd Party Warehouse name
-- =====================================================================================================


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

select @dirInventory = 'dir \\kermode\FileRepository\MERCHANDISING\CN_Distro\INBOUND\INVENTORY /B'
select @dirShipment = 'dir \\kermode\FileRepository\MERCHANDISING\CN_Distro\INBOUND\SHIPMENTS /B'
select @dirReceipt = 'dir \\kermode\FileRepository\MERCHANDISING\CN_Distro\INBOUND\RECEIPTS /B'
select @dirStockAdj = 'dir \\kermode\FileRepository\MERCHANDISING\CN_Distro\INBOUND\STOCKADJ /B'

insert ##dirInventory
exec master..xp_cmdshell @dirInventory

insert ##dirShipment
exec master..xp_cmdshell @dirshipment
	
insert ##dirReceipt
exec master..xp_cmdshell @dirreceipt
	
insert ##dirStockAdj
exec master..xp_cmdshell @dirstockadj

--/* 
declare @inv int,
		@shpmt int,
		@rcpt int,
		@adj int,
		@text nvarchar(max)

select @inv = count(*) from ##dirInventory where files like '%.csv'
select @shpmt = count(*) from ##dirShipment where files like '%.csv'
select @rcpt = count(*) from ##dirReceipt where files like '%.csv'
select @adj = count(*) from ##dirStockAdj where files like '%.csv'

set @text = '<font face =arial size = 2>' + 
		'Shanghai DC File Count Summary<br>' +
		'(files retrieved from the Ocean East Logistics server and successfully located to our interface directories on \\kermode\FileRepository\MERCHANDISING\CN_Distro\INBOUND\..)' + 
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
		<font face =arial size = 1>This report was run from bedrockdb02.me_01.dbo.spMerchandisingFTPCNGetFileSummary.</font>
		<br>
		<br>'

exec msdb.dbo.sp_send_dbmail
	@profile_name = 'merchadmin',
	@recipients = 'TimC@buildabear.com',
	@body = @text,
	@subject = 'China Warehouse File Summary',
	@body_format = 'HTML'
--*/
```

