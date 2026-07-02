# WMS.spOutputWMSShipment

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["WMS.spOutputWMSShipment"]
    WMS_tmpWMSShipmentImport(["WMS.tmpWMSShipmentImport"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| WMS.tmpWMSShipmentImport |

## Stored Procedure Code

```sql
CREATE proc [WMS].[spOutputWMSShipment]

-- =====================================================================================================
-- Name: spMerchandisingOutputWMSShipment
--
-- Description:	Outputs shipment file for Pipeline, based on imported shipment data from Dynamics WMS
--					modeled after bedrockdb02.me_01.dbo.spMerchandisingOutputUKShipment
--
--
-- Revision History
--		Name:			Date:			Comments:
--		Dan Tweedie		2019-07-30		Created proc.	
-- =====================================================================================================

as

set nocount on

declare @headers int,
		@document_no varchar(10),
		@date_shipped varchar(12),
		@erd varchar(12),
		@location varchar(4),
		@rec_type varchar(100),
		@distro varchar(7),
		@carton varchar(20),
		@upc varchar(12),
		@qty int,
		@cartons int

		
				
select @headers = count(distinct shipment) from WMS.tmpWMSShipmentImport where sent_qty > 0
while @headers > 0 
begin
	select 
		   @document_no = max(shipment),
		   @date_shipped = ship_date,
		   @erd = erd_date,
		   @location = location_code,
		   @rec_type = left(external_system_name, 20)
	from WMS.tmpWMSShipmentImport
	where sent_qty > 0
	group by ship_date, erd_date, location_code, left(external_system_name, 20)
	order by 1

	print 'H' + '	' + 'A' + '	' +	@document_no + '	' + @date_shipped + '	' + '	' + @erd + '	' + @location + '	' + '0980' + '	' + 'S' + '	' + '	' + '	' + '	' + @rec_type + '	' + '0'

	select @cartons = count(carton_nbr) from WMS.tmpWMSShipmentImport where shipment = @document_no and sent_qty  > 0

	while @cartons > 0
		begin
			select top 1
				   @distro = distribution_number,
				   @carton = carton_nbr,
				   @upc = style_code,
				   @qty = sent_qty
			from WMS.tmpWMSShipmentImport
			where shipment = @document_no
			and sent_qty> 0

			print 'D' + '	' + 'A' + '	' +	@document_no + '	' + @distro + '	' + @carton + '	' + @upc + '	' + '	' + '	' + '	' + '	' + convert(varchar, @qty)  + '	' + '0980'
			
			delete from WMS.tmpWMSShipmentImport where carton_nbr = @carton and style_code = @upc and distribution_number = @distro
			
			select @cartons = count(carton_nbr) from WMS.tmpWMSShipmentImport where shipment = @document_no and sent_qty > 0
			
			if @cartons < 1
				break
			else
				continue	
		end
	
	delete from WMS.tmpWMSShipmentImport where shipment = @document_no
	select @headers = count(distinct shipment) from WMS.tmpWMSShipmentImport where sent_qty > 0
	
	if @headers < 1
		break
	else
		continue
end
```

