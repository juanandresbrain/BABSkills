# dbo.spMerchandisingReportWarehouseStoreShipmentDailySummary

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMerchandisingReportWarehouseStoreShipmentDailySummary"]
    dbo_sp_send_dbmail(["dbo.sp_send_dbmail"]) --> SP
    wms_DynamicsTo3PLOrderExport(["wms.DynamicsTo3PLOrderExport"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.sp_send_dbmail |
| wms.DynamicsTo3PLOrderExport |

## Stored Procedure Code

```sql
CREATE procEDURE [dbo].[spMerchandisingReportWarehouseStoreShipmentDailySummary]
AS
SET NOCOUNT ON

-- =====================================================================================================
-- Name: spMerchandisingReportWarehouseStoreShipmentDailySummary
--
--				 
-- Revision History
--		Name:			Date:			Comments: This Proc is replaces existing DTS pkg on Beehive called Report_Warehouse_Store_Shipment_Daily_Summary
--		Dan Tweedie 	    03/04/2015		Created proc.	
--		Tim Callahan		2022-08-02		Updated Proc to point to new source table with integration of 3PW to Dynamics 
-- =====================================================================================================

IF (Object_ID('tempdb..##MAHITEMP10_TXT') IS NOT NULL) DROP TABLE ##MAHITEMP10_TXT
--SELECT cast(document_number AS DECIMAL(20, 0)) AS "Shipment #"
--	,location_code AS "Store"
--	,rec_type AS "REC TYPE"
--	,rec_label AS "REC Label"
--	,count(*) AS "Lines"
--INTO ##MAHITEMP10_TXT
--FROM store_shipment_export
--WHERE warehouse = '2970'
--	AND cast(convert(VARCHAR, release_date, 101) AS DATETIME) = cast(convert(VARCHAR, getdate(), 101) AS DATETIME)
--GROUP BY document_number
--	,location_code
--	,rec_type
--	,rec_label

select 
cast(document_number AS DECIMAL(20, 0)) AS "Shipment #",
destid as "Store" ,
rec_type as "REC TYPE", 
message as "REC Label", 
count (*) as "Lines"
INTO ##MAHITEMP10_TXT
from [stl-ssis-p-01].[IntegrationStaging].wms.DynamicsTo3PLOrderExport -- New Source Table 8/2/2022
where sourceid = '2970'
AND cast(convert(VARCHAR, ExportDate,101) AS DATETIME) = cast(convert(VARCHAR, getdate(), 101) AS DATETIME)
group by document_number, 
destid, 
rec_type, 
message 



if (select count(*) from ##MAHITEMP10_TXT) > 0


BEGIN
	DECLARE @1query VARCHAR(1000)
		,@1file_name VARCHAR(100)
		,@1file_location VARCHAR(100)
		,@1server VARCHAR(20)
		,@1database VARCHAR(20)
		,@1sqlcmd VARCHAR(1000)
		,@1query_text VARCHAR(1000)
		,@1file VARCHAR(1000)
		,@1body VARCHAR(1000)
		,@1subj VARCHAR(1000)

	SELECT @1query_text = 'set nocount on select * from ##MAHITEMP10_TXT'

	SET @1query = @1query_text
	SET @1file_location = '\\kermode\FileRepository\MERCHANDISING\DBCompare\'
	SET @1file_name = 'dts_summary.csv'
	SET @1server = 'bedrockdb02'
	SET @1database = 'me_01'
	SET @1sqlcmd = 'sqlcmd -S' + @1server + ' -d' + @1database + ' -Q' + '"' + @1query + '"' + ' -o' + '"' + @1file_location + @1file_name + '"' + ' -s"," -w1000 -W'

	EXEC master..xp_cmdshell @1sqlcmd
	
	EXEC msdb.dbo.sp_send_dbmail 
		@profile_name = 'MerchAdmin',
		@recipients = 'UKlogistics@buildabear.com',
		--@recipients = 'TimC@buildabear.com',
		@file_attachments = '\\kermode\FileRepository\MERCHANDISING\DBCompare\dts_summary.csv',
		@body = 'The following Store Shipments were exported to Clipper Logistics.',
		@subject = 'Daily Store Shipment Export Summary'
END

if (select count(*) from ##MAHITEMP10_TXT) = 0

BEGIN
	
	EXEC msdb.dbo.sp_send_dbmail 
		@profile_name = 'MerchAdmin',
		@recipients = 'UKlogistics@buildabear.com',
		--@recipients = 'TimC@buildabear.com',
		@body = 'No Store Shipments were exported to Clipper Logistic today.',
		@subject = 'Daily Store Shipment Export Summary'
END
```

