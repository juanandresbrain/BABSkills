# dbo.spMerchandisingSelectMissingStoreShipmentWC

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMerchandisingSelectMissingStoreShipmentWC"]
    dbo_dist_detail(["dbo.dist_detail"]) --> SP
    dbo_distribution(["dbo.distribution"]) --> SP
    dbo_distribution_ship_day(["dbo.distribution_ship_day"]) --> SP
    dbo_location(["dbo.location"]) --> SP
    dbo_sku(["dbo.sku"]) --> SP
    dbo_sp_send_dbmail(["dbo.sp_send_dbmail"]) --> SP
    dbo_store_shipment(["dbo.store_shipment"]) --> SP
    dbo_store_shipment_detail(["dbo.store_shipment_detail"]) --> SP
    dbo_style(["dbo.style"]) --> SP
    wms_DynamicsTo3PLOrderExport(["wms.DynamicsTo3PLOrderExport"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.dist_detail |
| dbo.distribution |
| dbo.distribution_ship_day |
| dbo.location |
| dbo.sku |
| dbo.sp_send_dbmail |
| dbo.store_shipment |
| dbo.store_shipment_detail |
| dbo.style |
| wms.DynamicsTo3PLOrderExport |

## Stored Procedure Code

```sql
CREATE procEDURE [dbo].[spMerchandisingSelectMissingStoreShipmentWC]
AS
SET NOCOUNT ON

-- =====================================================================================================
-- Name: spMerchandisingSelectMissingStoreShipmentWC
--
-- Description: 
--
-- Input:	
--
-- Output: 
--
-- Dependencies: 
--				 
-- Revision History
--		Name:			Date:			Comments: This Proc is replaces existing DTS pkg on Beehive called Validation_Missing_Store_Shipment_WC_V1
--		Dan Tweedie 	    03/05/2015		Created proc.
--		Tim Callahan		08/16/2016		Added Field to SSE Table, Cancelled, for shipments cancelled after export, this way we still have record. 	
--		Tim Callahan		06/08/2018		Modified the join to the ship table, removed date constraint and also added layer to omit SSE records before 01/01/2018
--											Also remarked out part about joining to IB audit trail, seems unncessary 
--		Lizzy Timm			08/20/2020		Added logic to exclude a shipment received by 960 but placed on hold by BAB
--		Tim Callahan		08/04/2022		Updated Data Source due to changes related to 3PW Integationg with Dynamics
-- =====================================================================================================


IF (Object_ID('tempdb..#work_Validation_Missing_Store_Shipment_Report_WC') IS NOT NULL) DROP TABLE #work_Validation_Missing_Store_Shipment_Report_WC
SELECT
cast(sse.document_number AS DECIMAL(20, 0)) AS document_number
,cast(sse.ExportDate as date) as release_date
,sse.distribution_number
,sse.sourceid as warehouse
,sse.style_code 
,sse.destid as location_code
	,dsd.ship_day_1 AS ship_day
	,sse.rec_type
INTO #work_Validation_Missing_Store_Shipment_Report_WC
FROM [stl-ssis-p-01].[IntegrationStaging].wms.DynamicsTo3PLOrderExport sse
--LEFT JOIN store_shipment ss ON ss.document_no = sse.document_number
LEFT JOIN store_shipment ss ON ss.document_no = cast(cast(sse.document_number AS DECIMAL(10, 0)) AS VARCHAR)
LEFT JOIN store_shipment_detail ssd ON ssd.store_shipment_id = ss.store_shipment_id
LEFT JOIN style s ON s.style_id = ssd.style_id AND sse.style_code = s.style_code
LEFT JOIN location l ON l.location_id = ss.location_id AND sse.destid = l.location_code
INNER JOIN distribution d ON d.distribution_number = sse.distribution_number
INNER JOIN distribution_ship_day dsd ON sse.destid = dsd.location_code AND dsd.ship_day_1 = upper(datename(dw, getdate()))
WHERE ss.document_no IS  NULL
AND l.location_code IS NULL
AND s.style_code IS NULL
AND sse.sourceid = '0960'
AND cast(sse.ExportDate as date) < cast(convert(VARCHAR, getdate(), 101) AS DATETIME)	
AND d.distribution_status NOT IN (8,9)
AND sse.release_date > '08-01-2022' -- Temp Add on 7/25/2018
ORDER BY sse.destid

IF (Object_ID('tempdb..##MAHITEMP18_CSV') IS NOT NULL) DROP TABLE ##MAHITEMP18_CSV
SELECT kt.document_number
	,kt.release_date
	,kt.distribution_number
	,kt.warehouse
	,kt.style_code
	,kt.location_code
	,kt.ship_day
	,kt.rec_type
INTO ##MAHITEMP18_CSV
FROM #work_Validation_Missing_Store_Shipment_Report_WC kt
INNER JOIN distribution d(NOLOCK) ON kt.distribution_number = d.distribution_number
INNER JOIN style s(NOLOCK) ON kt.style_code = s.style_code
INNER JOIN sku sk(NOLOCK) ON s.style_id = sk.style_id
INNER JOIN dist_detail dd(NOLOCK) ON d.distribution_id = dd.distribution_id AND sk.sku_id = dd.sku_id
INNER JOIN location l(NOLOCK) ON dd.location_id = l.location_id AND kt.location_code = l.location_code
WHERE dd.quantity <> 0
ORDER BY 1,5

if (select count(*) from ##MAHITEMP18_CSV) > 0

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

	SELECT @1query_text = 'set nocount on select * from ##MAHITEMP18_CSV'

	SET @1query = @1query_text
	SET @1file_location = '\\kermode\FileRepository\MERCHANDISING\DBCompare\'
	SET @1file_name = 'WC_missing_store_shipments.csv'
	SET @1server = 'bedrockdb02'
	SET @1database = 'me_01'
	SET @1sqlcmd = 'sqlcmd -S' + @1server + ' -d' + @1database + ' -Q' + '"' + @1query + '"' + ' -o' + '"' + @1file_location + @1file_name + '"' + ' -s"," -w1000 -W'

	EXEC master..xp_cmdshell @1sqlcmd

	EXEC msdb.dbo.sp_send_dbmail 
		@profile_name = 'MerchAdmin',
		@recipients='EntSysSupport@buildabear.com;santiagob@buildabear.com',
		@blind_copy_recipients = 'TimC@buildabear.com', 
		@file_attachments = '\\kermode\FileRepository\MERCHANDISING\DBCompare\WC_missing_store_shipments.csv',
		@body = 'Here is a report of Store Shipments that were sent to the WC Warehouse but have not been fed back into Merchandising.  This automated report was generate by BEDROCKDB02.me_01.dbo.spMerchandisingSelectMissingStoreShipmentWC called from the SQL agent job MERCHANDISING - Report - Missing Store Shipments - WC.',
		@subject = 'Missing Store Shipments WC'

END
```

