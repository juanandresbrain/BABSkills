# dbo.spMerchandisingOutputCNshipments

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMerchandisingOutputCNshipments"]
    dbo_tmpDetailCN(["dbo.tmpDetailCN"]) --> SP
    dbo_tmpHeaderCN(["dbo.tmpHeaderCN"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tmpDetailCN |
| dbo.tmpHeaderCN |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spMerchandisingOutputCNshipments]
as
-- =====================================================================================================
-- Name: spMerchandisingOutputCNshipments
--
-- Description:	selects shipment records, presented in a format that is readable by the Merchandising Pipeline.
--				 
-- Revision History
--		Name:			Date:			Comments:
--		Dan Tweedie		01/25/2016		created proc
-- =====================================================================================================


set nocount on

declare @headers int,
		@document_no varchar(10),
		@date_shipped varchar(12),
		@erd varchar(12),
		@location varchar(4),
		@rec_type varchar(100),
		@distro varchar(6),
		@carton varchar(20),
		@upc varchar(12),
		@qty int,
		@cartons int,
		@fromLocation varchar(4)


select @headers = count(*) from tmpHeaderCN
while @headers > 0 
begin
	select 
		   @fromLocation = fromLocation,
		   @document_no = max(document_no),
		   @date_shipped = date_shipped,
		   @erd = expected_receipt_date,
		   @location = location_code,
		   @rec_type = left(external_system_name, 20)
	from tmpHeaderCN
	group by fromLocation, date_shipped, expected_receipt_date, location_code, external_system_name
	order by 1

	print 'H' + '	' + 'A' + '	' +	@document_no + '	' + @date_shipped + '	' + '	' + @erd + '	' + @location + '	' + @fromLocation + '	' + 'S' + '	' + '	' + '	' + '	' + @rec_type + '	' + '0'

	select @cartons = count(carton_no) from tmpDetailCN where document_no = @document_no

	while @cartons > 0
		begin
			select top 1
				   @distro = distribution_no,
				   @carton = carton_no,
				   @upc = upc_no,
				   @qty = sent_units
			from tmpDetailCN
			where document_no = @document_no

			print 'D' + '	' + 'A' + '	' +	@document_no + '	' + @distro + '	' + @carton + '	' +  @upc + '	' + '	' + '	' + '	' + '	' + convert(varchar, @qty)  + '	' + @fromLocation
			
			delete from tmpDetailCN where carton_no = @carton and upc_no = @upc and distribution_no = @distro
			
			select @cartons = count(carton_no) from tmpDetailCN where document_no = @document_no
			
			if @cartons < 1
				break
			else
				continue	
		end
	
	delete from tmpHeaderCN where document_no = @document_no
	select @headers = count(*) from tmpHeaderCN
	
	if @headers < 1
		break
	else
		continue
end
```

