# WMS.spMerchandisingProcessUKStoreShipments

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["WMS.spMerchandisingProcessUKStoreShipments"]
    WMS_ERP_DynamicsShipmentStage_UK(["WMS.ERP_DynamicsShipmentStage_UK"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| WMS.ERP_DynamicsShipmentStage_UK |

## Stored Procedure Code

```sql
create proc [WMS].[spMerchandisingProcessUKStoreShipments]

as 

-- =====================================================================================================
-- Name: spMerchandisingProcessUKStoreShipments
--
-- Description:	Bulk insert Store Shipment file from UK warehouse, stages data, calls another proc to output the pipeline file
--
-- Input: NA
--
-- Output: Resultset formatted to meet Epicor requirements for Shipments.
--
-- Revision History
--		Name:			Date:			Comments:
--		Dan Tweedie		09/06/2013		Created proc.
--		Dan Tweedie		05/27/2014		Modified rec type lookup to get from store_shipment_export instead of distribution
--		Dan Tweedie		06/26/2014		Modified code to include carton number in rec type query to allow for proper join with ERD query, to prevent extra lines returned
--		Dan Tweedie		07/18/2014		For allocation adjustment staging query, 
--										changed to max instead of sum to ensure we don't over report the shipped qty 
--										if the warehouse reports multiples lines of the same carton number & UPC 
--										(this should only be on one line, but they have accidentally over reported in the past and had multiple lines with the same data
--		Dan Tweedie		04/15/2015		Updated allocation adjustment queries so the value is determined by subtracting shipped qty from allocated qty
--		Dan Tweedie		05/1/2015		Break/Fix - Allocation adjustment = allocated - variance qty, only create adjustment if <> 0
--		Tim Callahan	12/11/2015		Called Pipeline Segments After Shipment and Allocation Adjustment Files are Generated
--		Tim Callahan	05/23/2017		Remarked Out BreakFix from 5/1/2015 , Added Where Clause for Carton Numbers of 00000000000000000000, indicates units were not shipped 
--		Tim Callahan	06/13/2017		Added code to account for if Allocator\Distro team cancels distribution lines in Merch
--										This could create a negative allocation which would cause the entire batch for that distribution to fail to import via pipeline segment 65000
--		Dan Tweedie		2018-07-03		Added stage data for Dynamics
--		Tim Callahan	07-03-2018		Added Code to remove D365 transfers from #file_input table after D365 capture otherwise this data would fail in Merch\Pipeline
--		Tim Callahan	12-01-2018		Changed location_code max length to 6 for D3FO Sales Order Location Processing
--		Dan Tweedie		2019-01-22		Updated insert statement for stage to Dynamics
--		Tim Callahan	2022-07-31		Added Insert Ddate for stage to Dynamics 
--		Tim Callahan	2025-02-03		Ported over from Bedrockdb02 as part of Aptos Decommission
--										Also Renamed from spMerchandisingSelectUKStoreShipments to keep similar naming structure between 3PLS
-- =====================================================================================================

set nocount on

--check the directory to see if there are distro CSV files ready to import
-------------do a DIR command and store the results in a temp table
IF (Object_ID('tempdb..#DIR') IS NOT NULL) DROP TABLE #DIR
create table #DIR (output varchar(1000))
insert #DIR exec master..xp_cmdshell 'dir \\stl-ssis-p-01\IntegrationStaging\3PW\uk_distro\shipments\*.txt /B'
delete from #DIR where output is null or output = 'File Not Found'

------------query temp table to see if there are CSV files
if (select count(*) from #DIR) > 0
---find files with spaces in the name, rename to remove the spaces

BEGIN

		if (object_id('tempdb..#UKSHIPMENT') is not null) drop table #UKSHIPMENT
		create table #UKSHIPMENT
		(shipment varchar(52),
		location_code varchar(6),
		ship_date smalldatetime,
		distribution_number varchar(52),
		distribution_line int,
		style_code varchar(6),
		req_qty int,
		sent_qty int,
		variance_qty int,
		carton_nbr varchar(25))


			
		declare @files int,
				@filename varchar(100),
				@filepath varchar(100),
				@bulkinsert varchar(4000),
				@bulkinsertArchive varchar(4000),
				@del varchar(100),
				@move varchar(1000),
				@query varchar(1000),
				@file_name varchar(100),
				@file_location varchar(100),
				@server varchar(20),
				@database varchar(20),
				@bcp varchar(1000),
				@timestamp varchar(52),
				@rename varchar(1000),
				@nameage varchar(104),
				@documentNumber varchar(9)

		select @filepath = '\\stl-ssis-p-01\IntegrationStaging\3PW\uk_distro\shipments\'
		select @files = count(*) from #dir
		
	
---------Bulk Insert Loop
		while @files > 0
			begin
			    select @timestamp = cast(datepart(yyyy, getdate()) as varchar) + cast(datepart(mm, getdate()) as varchar) + cast(datepart(dd, getdate()) as varchar) + cast(datepart(hh, getdate()) as varchar) + cast(datepart(mi, getdate()) as varchar) + cast(datepart(ss, getdate()) as varchar)
				select @filename = max(output) from #dir
								
				select @bulkinsert = 'set language ''British'' bulk insert #UKSHIPMENT from ''' + @filepath + @filename + ''' with (FIELDTERMINATOR = '','', ROWTERMINATOR = ''\n'')'
				exec (@bulkinsert)
				
				select @rename = 'ren ' + @filepath + @filename + ' ' + @filename + '.' + @timestamp + '.txt'
				exec master..xp_cmdshell @rename
				
				select @move = 'move ' + @filepath + @filename + '.' + @timestamp + '.txt' + ' \\stl-ssis-p-01\IntegrationStaging\3PW\uk_distro\shipments\Done\'
		        exec master..xp_cmdshell @move
				
				delete from #dir where output = @filename
				select @files = count(*) from #dir
								
				if @files < 1
					break
				else
					continue
			end
			

	------------STAGE FOR DYNAMICS

		
		insert [WMS].[ERP_DynamicsShipmentStage_UK]
		select
			Shipment,
			location_code, 
			ship_date,
			distribution_number,
			distribution_line,
			style_code,
			req_qty,
			sent_qty,
			variance_qty,
			carton_nbr,
			NULL as rec_type,
			NULL as external_system_name,
			NULL as erd_date, 					 
			GETDATE()
		from #UKSHIPMENT
		where carton_nbr is not null
		and len(carton_nbr) > 1
		and carton_nbr not in (select carton_nbr from [WMS].[ERP_DynamicsShipmentStage_UK] where carton_nbr is not null) -- From Aptos Proce - Easily Exclude from duplicate data inserting

End
```

