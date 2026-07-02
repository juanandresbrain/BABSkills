# WMS.spMerchandisingProcessCNStoreShipments

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["WMS.spMerchandisingProcessCNStoreShipments"]
    WMS_ERP_DynamicsShipmentStage_CN(["WMS.ERP_DynamicsShipmentStage_CN"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| WMS.ERP_DynamicsShipmentStage_CN |

## Stored Procedure Code

```sql
CREATE proc [WMS].[spMerchandisingProcessCNStoreShipments]


as 
-- =====================================================================================================
-- Name: spMerchandisingProcessCNStoreShipments
--
-- Description:	Imports shipment records from Shanghai warehouse, generates shipment and allocation adjustment files for Merchandising Pipeline
--
-- Revision History
--		Name:			Date:			Comments:
--		Dan Tweedie		01/25/2016		created proc
--		Dan Tweedie		05/15/2016		Corrected style_code in file input table, so it has the 6 leading zero's
--		Keith Lee		05/18/2016		Changed code so that allocated adjustment file would use shipped_qty and not varience_qty
--		Keith Lee		06/1/2016		Changed code since Kerry Logistics is providing a space in the carton number field so changed to use len.  Also removed -1 code when calculating the allocated units.
--		Tim Callahan	06/26/2017		The change made on 5/18/2016 was still not properly creating alloc adjustment, see date stamp notes below 
--		Dan Tweedie		2018-07-03		Added Stage Data For Dynamics
--		Tim Callahan	07-03-2018		Extended the max character of #file_input from 6 to 12 to accomodated D365 distro data 
--										Added logic to remove D365 distros from being include in Merchandising Pipeline files
--		Dan Tweedie		2019-01-22		Updated insert statement for stage to Dynamics
--		Tim Callahan	2025-02-03		Ported over from Bedrockdb02 as part of Aptos Decommission
-- =====================================================================================================

set nocount on

----PART ONE - IMPORT SHIPMENT FILES

IF (Object_ID('tempdb..#files') IS NOT NULL) DROP TABLE #files
create table #files (output varchar(1000))
insert #files exec master..xp_cmdshell 'dir \\stl-ssis-p-01\IntegrationStaging\3PW\CN_Distro\INBOUND\SHIPMENTS\*.csv /B'
delete from #files where output is null or output = 'File Not Found'

if (select count(*) from #files) > 0

BEGIN
		IF (Object_ID('tempdb..#file_input') IS NOT NULL) DROP TABLE #file_input
			create table #file_input
			(fromLocation varchar(4),
			 document_no varchar(10),
			 location_code varchar(10),
			 date_shipped varchar(10),
			 distribution_no varchar(12),
			 distribution_line int,
			 style_code varchar(12),
			 ordered_qty int,
			 shipped_qty int,
			 variance_qty int,
			 carton_no varchar(20))
		
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


		select @filepath = '\\stl-ssis-p-01\IntegrationStaging\3PW\CN_Distro\INBOUND\SHIPMENTS\'
		select @files = count(*) from #files

		while @files > 0
			begin

				select @filename = max(output) from #files
				select @bulkinsert = 'bulk insert #file_input from ''' + @filepath + @filename + ''' with (FIELDTERMINATOR = '','', ROWTERMINATOR = ''\n'')'
				exec (@bulkinsert)
				
				select @move = 'move ' + @filepath + @filename + ' \\stl-ssis-p-01\IntegrationStaging\3PW\CN_Distro\INBOUND\SHIPMENTS\Done'

				exec master..xp_cmdshell @move
								
				delete from #files where output = @filename
				select @files = count(*) from #files
								
				if @files < 1
					break
				else
					continue
			end

		
			----STAGE SHIPMENTS FOR DYNAMICS
			insert WMS.ERP_DynamicsShipmentStage_CN
			select 
			 fromLocation
			,document_no
			,location_code
			,date_shipped
			,distribution_no
			,distribution_line
			,style_code
			,ordered_qty
			,shipped_qty
			,variance_qty
			,carton_no
			,null as rec_type
			,null as external_system_name
			,getdate() as insert_date
			from #file_input
			where len(carton_no) > 1
			and carton_no is not null
			and carton_no not in (select carton_no from WMS.ERP_DynamicsShipmentStage_CN where carton_no is NOT NULL)
			
End
```

