# WMS.spMerchandisingProcessWCStoreShipments

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["WMS.spMerchandisingProcessWCStoreShipments"]
    wms_ERP_DynamicsShipmentStage_WC(["wms.ERP_DynamicsShipmentStage_WC"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| wms.ERP_DynamicsShipmentStage_WC |

## Stored Procedure Code

```sql
CREATE proc [WMS].[spMerchandisingProcessWCStoreShipments]

as 
-- =====================================================================================================
-- Name: spMerchandisingProcessWCShipmentsAllocAdj
--
-- Description:	Imports shipment records from west coast warehouse, generates shipment and allocation adjustment files for Merchandising Pipeline
--				
--
-- Input:	Imports shipment files from \\stl-ssis-p-01\IntegrationStaging\3PW\WC_Distro\SHIPMENTS
--
-- Output: outputs shipment files to \\pipeapp01\Company01\Text File to IM Import Tables - Import Store Shipment\
--		   outputs allocation adjustment files to \\pipeapp01\Company01\Text File to AR Import Tables - Allocation Adjustment\
-- Dependencies: NA
--				 
-- Revision History
--		Name:			Date:			Comments:
--		Dan Tweedie		03/15/2012		created proc
--		Dan Tweedie		07/14/2015		Pointed to Kermode instead of Oursmerchdb01
--		Tim Callahan	11/14/2017		Removed call of Segment 65000 segment to prevent conflicts with the Pipeline Sales Posting Segments
--										If an allocation adjustment is generated from this data it will post at 7:30 a.m. when Distro Export job begins runnin
--		Tim Callahan	06/28/2018		Added Code to remove D365 transfers from #file_input table after D365 capture otherwise this data would fail in Merch\Pipeline
--										Also updated #file_input table to accept 12 characters in the distribution number field 
--		Dan Tweedie		2018-07-03		Added Stage Data For Dynamics
--		Dan Tweedie		2019-01-22		Updated insert statement for stage to Dynamics
--		Tim Callahan	04/24/2019		Updated Proc to pull left 4 Location Code Characters as this caused issues with allocation adjustment file creation step
--		Tim Callahan	2022-07-31		Updated Proc to Handle an InsertDate and Null License Plate field, a license plate will be provided in near future. 
--		Tim Callahan	2023-04-03		Updated Proc to Handle License Plate Field which DDC should be providing beginnning the evening of 2023-04-03
--		Tim Callahan	2025-02-03		Ported over from Bedrockdb02 as part of Aptos Decommission
-- =====================================================================================================

set nocount on

----PART ONE - IMPORT SHIPMENT FILES

IF (Object_ID('tempdb..#files') IS NOT NULL) DROP TABLE #files
create table #files (output varchar(1000))
insert #files exec master..xp_cmdshell 'dir \\stl-ssis-p-01\IntegrationStaging\3PW\WC_Distro\SHIPMENTS\*.dat /B'
delete from #files where output is null or output = 'File Not Found'

if (select count(*) from #files) > 0

BEGIN
		IF (Object_ID('tempdb..#file_input') IS NOT NULL) DROP TABLE #file_input
			create table #file_input
			(document_no varchar(10),
			 BOL varchar(30),
			 location_code varchar(1000),
			 rec_type varchar(4),
			 ship_date varchar(8),
			 style_code varchar(6),
			 ordered_qty int,
			 shipped_qty int,
			 carton_no varchar(20),
			 distribution_no varchar(12),
			 distribution_line int, 
			 license_plate varchar (100) -- Added 2023-04-03
			 )
		
		declare @files int,
				@filename varchar(52),
				@filepath varchar(100),
				@bulkinsert varchar(4000),
				@del varchar(1000),
				@move varchar(1000),
				@query varchar(1000),
				@file_name varchar(100),
				@file_location varchar(1000),
				@server varchar(20),
				@database varchar(20),
				@bcp varchar(1000)


		select @filepath = '\\stl-ssis-p-01\IntegrationStaging\3PW\WC_Distro\SHIPMENTS\'
		select @files = count(*) from #files

		while @files > 0
			begin

				select @filename = max(output) from #files
				select @bulkinsert = 'bulk insert #file_input from ''' + @filepath + @filename + ''' with (FIELDTERMINATOR = ''	'', ROWTERMINATOR = ''\n'')'
				exec (@bulkinsert)
				
				select @move = 'move ' + @filepath + @filename + ' \\stl-ssis-p-01\IntegrationStaging\3PW\WC_Distro\SHIPMENTS\Done'

				exec master..xp_cmdshell @move
								
				delete from #files where output = @filename
				select @files = count(*) from #files
								
				if @files < 1
					break
				else
					continue
			end

			
-----------STAGE SHIPMENTS FOR DYNAMICS
			insert wms.ERP_DynamicsShipmentStage_WC
			select *, 
			--null , -- Added 7/31/2022, eventually a License Plate field will be available in the WC data file  -- Remarked out on 2023-04-03 per Retail Inventory Go Live 
			GETDATE() -- Added 7/31/2022
			
			from #file_input
			where carton_no is not null
			and len(carton_no) > 1
			and carton_no not in (select carton_no from WMS.ERP_DynamicsShipmentStage_WC where carton_no is NOT NULL)
---------------------------------------
			
End
```

