# dbo.spMerchandisingOutputFedExReceipts

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMerchandisingOutputFedExReceipts"]
    dbo_FedExReceiptsArchive(["dbo.FedExReceiptsArchive"]) --> SP
    dbo_location(["dbo.location"]) --> SP
    dbo_store_shipment(["dbo.store_shipment"]) --> SP
    dbo_store_shipment_detail(["dbo.store_shipment_detail"]) --> SP
    dbo_tmpFedExCBR(["dbo.tmpFedExCBR"]) --> SP
    dbo_tmpFedExReceipts(["dbo.tmpFedExReceipts"]) --> SP
    WMS_ShipmentConfirmAptos(["WMS.ShipmentConfirmAptos"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.FedExReceiptsArchive |
| dbo.location |
| dbo.store_shipment |
| dbo.store_shipment_detail |
| dbo.tmpFedExCBR |
| dbo.tmpFedExReceipts |
| WMS.ShipmentConfirmAptos |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spMerchandisingOutputFedExReceipts]
as

-- =====================================================================================================
-- Name: spMerchandisingOutputFedExReceipts
--
-- Description:	Imports FedEx receipt file from FedEx, outputs carton batch receipt file to pipeapp01
--				
--
-- Input:	Imports FedEx receipt file from \\wmetl01\Informatica\TgtFiles\FEDEX
--
-- Output: CBR file output to \\pipeapp01\Company01\Text File to IM Import Tables  - Batch Carton
--         Emails exceptions
-- Dependencies: NA
--				 
-- Revision History
--		Name:			Date:			Comments:
--		Dan Tweedie		03/07/2012		created proc
--		Dan Tweedie		01/16/2014		Added lookup to WM if the location number isn't in the FedEx data
--		Dan Tweedie		02/24/2014		Added lookup to WM if carton number isn't in FedEx data, will match by tracking number
--		Dan Tweedie		04/08/2014		Modified the code to allow for lookups to WM, streamlined it
--		Dan Tweedie		11/03/2014		Added a check for received cartons previously archived but not found in the batch carton import table
--		Dan Tweedie		07/24/2015		The FedEx FTP was changed from wmetl01 to kermode, so code was changed to match this
--		Lizzy Timm		03/05/2020		Added logic to prevent creation of empty pipeline files and replaced references to WMDB01 with stl-ssis-p-01
-- =====================================================================================================
set nocount on

----PART ONE - IMPORT FEDEX RECEIPT FILES

set nocount on
IF (Object_ID('tempdb..#files') IS NOT NULL) DROP TABLE #files
create table #files (output varchar(1000))
--insert #files exec master..xp_cmdshell 'dir \\wmetl01\Informatica\TgtFiles\FEDEX\*.txt /B'
insert #files exec master..xp_cmdshell 'dir \\kermode\filerepository\MERCHANDISING\FEDEX\UploadFromFedEx\*.txt /B'
delete from #files where output is null or output = 'File Not Found'

if (select count(*) from #files) > 0

------------------------------------------------
BEGIN
		IF (Object_ID('me_01..tmpFedExReceipts') IS NOT NULL) DROP TABLE tmpFedExReceipts
		create table tmpFedExReceipts
		(tracking varchar(50),
		 carton_no varchar(50),
		 location varchar(50),
		 delivery_date varchar(50),
		 delivery_time varchar(50),
		 [signature] varchar(50))

		
		declare @files int,
				@filename varchar(52),
				@filepath1 varchar(1000),
				@filepath2 varchar(1000),
				@filepath3 varchar(1000),
				@filepath4 varchar(1000),
				@bulkinsert varchar(4000),
				@del varchar(1000),
				@copy varchar(1000),
				@move1 varchar(1000),
				@move2 varchar(1000)

		--select @filepath1 = '\\wmetl01\Informatica\TgtFiles\FEDEX\'
		select @filepath1 = '\\kermode\filerepository\MERCHANDISING\FEDEX\UploadFromFedEx\'
		select @filepath2 = '\\kermode\Filerepository\MERCHANDISING\FEDEX\'
		--select @filepath3 = '\\wmetl01\Informatica\TgtFiles\FEDEX\DONE\'
		select @filepath3 = '\\kermode\filerepository\MERCHANDISING\FEDEX\UploadFromFedEx\DONE'
		select @filepath4 = '\\kermode\FileRepository\MERCHANDISING\FEDEX\DONE\'
		
		select @files = count(*) from #files

		while @files > 0
			begin

				select @filename = max(output) from #files
				
				select @copy = 'copy ' + @filepath1 + @filename + ' ' + @filepath2
				exec master..xp_cmdshell @copy
				
				select @bulkinsert = 'bulk insert tmpFedExReceipts from ''' + @filepath2 + @filename + ''' with (FIRSTROW = 2, FIELDTERMINATOR = ''	'', ROWTERMINATOR = ''\n'', FORMATFILE = ''\\kermode\FileRepository\MERCHANDISING\FEDEX\FormatFile\FF_.fmt'')'
				exec (@bulkinsert)
				
				select @move1 = 'move ' + @filepath1 + @filename + ' ' + @filepath3
				exec master..xp_cmdshell @move1
								
				select @move2 = 'move ' + @filepath2 + @filename + ' ' + @filepath4
				exec master..xp_cmdshell @move2
												
				delete from #files where output = @filename
				select @files = count(*) from #files
								
				if @files < 1
					break
				else
					continue
			end

-------------------------------------
--archive receipt data for future reference ---this includes all receipt data in the file, not just bab locations
insert FedExReceiptsArchive
select * 
from tmpFedExReceipts
where len(delivery_date) > 0 
-------------------------------------
	if(select count(*) from tmpFedExReceipts) > 0

	begin
	
		--IF (Object_ID('me_01..tmpFedExCBR') IS NOT NULL) DROP TABLE tmpFedExCBR
		-----get carton information from Merch if carton information is not missing from FedEx
		--select	distinct 
		--		'BC' BC,
		--		'A' A,
		--		fx.carton_no,
		--		substring(fx.location,24,4) location,
		--		'099060199' code 
		--into tmpFedExCBR
		--from tmpFedExReceipts fx
		--join store_shipment_detail ssd (nolock) on ssd.carton_no = fx.carton_no
		--join location l (nolock) on l.location_code = substring(fx.location,24,4)
		--UNION ALL
		-----get carton and location information from WM if the location information is missing from FedEx
		--select distinct
		--	   'BC' BC,
		--	   'A' A,
		--	   ch.carton_nbr carton_no, 
		--	   ph.shipto location,
		--	   '099060199' code
		--from wmdb01.wmprod.dbo.carton_hdr ch
		--join wmdb01.wmprod.dbo.pkt_hdr ph on ch.pkt_ctrl_nbr = ph.pkt_ctrl_nbr
		--join tmpFedExReceipts fx on ch.trkg_nbr = fx.tracking 
		--where ph.ord_type is null
		--and len(fx.location) = 0
		--UNION ALL
		-----get carton information from WM if the carton information is missing from FedEx
		--select	distinct 
		--		'BC' BC,
		--		'A' A,
		--		ssd.carton_no,
		--		substring(fx.location,24,4) location,
		--		'099060199' code 
		--from tmpFedExReceipts fx
		--join store_shipment_detail ssd (nolock) on ssd.carton_no = fx.carton_no
		--join location l (nolock) on l.location_code = substring(fx.location,24,4)
		--join wmdb01.wmprod.dbo.carton_hdr ch on fx.tracking = ch.trkg_nbr
		--join wmdb01.wmprod.dbo.pkt_hdr ph on ch.pkt_ctrl_nbr = ph.pkt_ctrl_nbr
		--where ph.ord_type is null
		--and len(fx.carton_no) = 0
		--union all --add 11/03/2014
		----get cartons that were previously archived but not posted to Merch
		--select	distinct 
		--		'BC' BC,
		--		'A' A,
		--		ssd.carton_no,
		--		l.location_code location,
		--		'099060199' code 
		--from FedExReceiptsArchive fa (nolock)
		--join store_shipment_detail ssd (nolock) on fa.carton_no = ssd.carton_no
		--join store_shipment ss (nolock) on ssd.store_shipment_id = ss.store_shipment_id
		--join location l (nolocK) on ss.location_id = l.location_id
		--left join c_imp_batch_carton ibc (nolock) on fa.carton_no = ibc.carton_no
		--left join tmpFedExReceipts fr (nolock) on fa.carton_no = fr.carton_no
		--where ibc.carton_no is null --not found in the carton import table
		--and fr.carton_no is null --not in the fedex receipt temp table that is part of this procedure
		--and ssd.units_received = 0
		--and ss.document_status = 3
		--order by 4,3

		/* IF (Object_ID('me_01..tmpFedExCBR') IS NOT NULL) DROP TABLE tmpFedExCBR
		select distinct
			'BC' BC,
			'A' A,
			ssd.carton_no,
			l.location_code location,
			'099060199' code 
		into tmpFedExCBR
		from store_shipment ss with (nolock)
		join store_shipment_detail ssd with (nolock) on ss.store_shipment_id = ssd.store_shipment_id
		join location l with (nolock) on ss.location_id = l.location_id
		join FedExReceiptsArchive f on ssd.carton_no = f.carton_no
		where ss.document_status = 3
		union
		select distinct
			'BC' BC,
			'A' A,
			ssd.carton_no,
			l.location_code location,
			'099060199' code 
		from store_shipment ss with (nolock)
		join store_shipment_detail ssd with (nolock) on ss.store_shipment_id = ssd.store_shipment_id
		join location l with (nolock) on ss.location_id = l.location_id
		join wmdb01.wmprod.dbo.carton_hdr ch on ssd.carton_no = ch.carton_nbr
		join FedExReceiptsArchive f on ch.trkg_nbr = f.tracking
		where ss.document_status = 3 */ -- 03/05/2020, old WM

		IF (Object_ID('me_01..tmpFedExCBR') IS NOT NULL) DROP TABLE tmpFedExCBR
		select distinct
			'BC' BC,
			'A' A,
			ssd.carton_no,
			l.location_code location,
			'099060199' code 
		into tmpFedExCBR
		from store_shipment ss with (nolock)
		join store_shipment_detail ssd with (nolock) on ss.store_shipment_id = ssd.store_shipment_id
		join location l with (nolock) on ss.location_id = l.location_id
		join FedExReceiptsArchive f on ssd.carton_no = f.carton_no
		where ss.document_status = 3
		union
		select distinct
			'BC' BC,
			'A' A,
			ssd.carton_no,
			l.location_code location,
			'099060199' code 
		from store_shipment ss with (nolock)
		join store_shipment_detail ssd with (nolock) on ss.store_shipment_id = ssd.store_shipment_id
		join location l with (nolock) on ss.location_id = l.location_id
		JOIN [stl-ssis-p-01].IntegrationStaging.WMS.ShipmentConfirmAptos sc	ON ssd.carton_no = sc.containerid
		join FedExReceiptsArchive f on sc.ContainerManifestID  = f.tracking
		where ss.document_status = 3

			-------------------------------
			---output CBR file to pipeapp01
	if(select count(*) from tmpFedExCBR) > 0 -- 03/05/2020, added to prevent empty pipeline files
		BEGIN
			declare @query varchar(1000),
					@date varchar(200),
					@file_name varchar(100),
					@file_location varchar(1000),
					@server varchar(20),
					@database varchar(20),
					@bcp varchar(1000)

			set @date = convert(varchar, datepart(yyyy, getdate())) + convert(varchar, datepart(mm, getdate())) + convert(varchar, datepart(dd, getdate())) + convert(varchar, datepart(hh, getdate())) + convert(varchar, datepart(mi, getdate())) + convert(varchar, datepart(ss, getdate()))
			set @query = 'set nocount on select * from me_01.dbo.tmpFedExCBR'
			set @file_location = '\\pipeapp01\Company01\Text File to IM Import Tables  - Batch Carton\'
			set @file_name = 'STSIMCTN.FEDEX.' + @date + '.GO'
			set @server = 'bedrockdb02'
			set @database = 'me_01'
			set @bcp = 'bcp "' + @query + '" queryout "' + @file_location + @file_name + '"  -T -c -S' + @server 
			exec master..xp_cmdshell @bcp
		end
	END
END
```

