# dbo.spMerchandisingOutputUKShipment

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMerchandisingOutputUKShipment"]
    dbo_tmpUKShipmentImport(["dbo.tmpUKShipmentImport"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tmpUKShipmentImport |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spMerchandisingOutputUKShipment]

-- =====================================================================================================
-- Name: spMerchandisingOutputUKShipment
--
-- Description:	Outputs shipment file for Pipeline, based on imported file from UK warehouse
--
-- Input: NA
--
-- Output: Resultset formatted to meet Epicor requirements for Shipment.
--
-- Revision History
--		Name:			Date:			Comments:
--		Dan Tweedie		09/06/2013		Created proc.	
--		Dan Tweedie		01/15/2013		Updated code to ensure the header count and subsequent query is only of distinct shipment numbers with qty shipped,
--		Lizzy Timm		05/08/2025		Lengthened @distro varchar(6) fro varchar(7)  to accommodate longer distribution numbers
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

				
select @headers = count(distinct shipment) from tmpUKShipmentImport where sent_qty * -1 > 0
while @headers > 0 
begin
	select 
		   @document_no = max(shipment),
		   @date_shipped = ship_date,
		   @erd = erd_date,
		   @location = location_code,
		   @rec_type = left(external_system_name, 20)
	from tmpUKShipmentImport
	where sent_qty * -1 > 0
	group by ship_date, erd_date, location_code, left(external_system_name, 20)
	order by 1

	print 'H' + '	' + 'A' + '	' +	@document_no + '	' + @date_shipped + '	' + '	' + @erd + '	' + @location + '	' + '2970' + '	' + 'S' + '	' + '	' + '	' + '	' + @rec_type + '	' + '0'

	select @cartons = count(carton_nbr) from tmpUKShipmentImport where shipment = @document_no and sent_qty * -1 > 0

	while @cartons > 0
		begin
			select top 1
				   @distro = distribution_number,
				   @carton = carton_nbr,
				   @upc = style_code,
				   @qty = (sent_qty * -1)
			from tmpUKShipmentImport
			where shipment = @document_no
			and sent_qty * -1 > 0

			print 'D' + '	' + 'A' + '	' +	@document_no + '	' + @distro + '	' + @carton + '	' + @upc + '	' + '	' + '	' + '	' + '	' + convert(varchar, @qty)  + '	' + '2970'
			
			delete from tmpUKShipmentImport where carton_nbr = @carton and style_code = @upc and distribution_number = @distro
			
			select @cartons = count(carton_nbr) from tmpUKShipmentImport where shipment = @document_no and sent_qty * -1 > 0
			
			if @cartons < 1
				break
			else
				continue	
		end
	
	delete from tmpUKShipmentImport where shipment = @document_no
	select @headers = count(distinct shipment) from tmpUKShipmentImport where sent_qty * -1 > 0
	
	if @headers < 1
		break
	else
		continue
end
```

