# dbo.spMerchandisingOutputWMshipments

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMerchandisingOutputWMshipments"]
    dbo_tmpDetailWM(["dbo.tmpDetailWM"]) --> SP
    dbo_tmpHeaderWM(["dbo.tmpHeaderWM"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tmpDetailWM |
| dbo.tmpHeaderWM |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spMerchandisingOutputWMshipments]

as

-- =====================================================================================================
-- Name: spMerchandisingOutputWMshipments
--
-- Description:	Outputs WM store shipments to Merch Pipeline
--				 
-- Revision History
--		Name:			Date:			Comments:
--		Dan Tweedie		04/30/2015		created proc
-- =====================================================================================================

set nocount on

declare @headers int,
		@document_no varchar(100),
		@date_shipped varchar(12),
		@erd varchar(12),
		@location varchar(4),
		@rec_type varchar(100),
		@distro varchar(6),
		@carton varchar(20),
		@upc varchar(12),
		@qty int,
		@cartons int


select @headers = count(*) from tmpHeaderWM
while @headers > 0 
begin
	select 
		   @document_no = max(document_no),
		   @date_shipped = date_shipped,
		   @erd = expected_receipt_date,
		   @location = location_code,
		   @rec_type = left(external_system_name, 20)
	from tmpHeaderWM
	group by date_shipped, expected_receipt_date, location_code, external_system_name
	order by 1

	print 'H' + '	' + 'A' + '	' +	@document_no + '	' + @date_shipped + '	' + '	' + @erd + '	' + @location + '	' + '0980' + '	' + 'S' + '	' + '	' + '	' + '	' + @rec_type + '	' + '0'

	select @cartons = count(carton_nbr) from tmpDetailWM where document_no = @document_no

	while @cartons > 0
		begin
			select top 1
				   @distro = distribution_no,
				   @carton = carton_nbr,
				   @upc = upc_no,
				   @qty = sent_units
			from tmpDetailWM
			where document_no = @document_no

			print 'D' + '	' + 'A' + '	' +	@document_no + '	' + @distro + '	' + @carton + '	' + @upc + '	' + '	' + '	' + '	' + '	' + convert(varchar, @qty)  + '	' + '0980'
			
			delete from tmpDetailWM where carton_nbr = @carton and upc_no = @upc and distribution_no = @distro
			
			select @cartons = count(carton_nbr) from tmpDetailWM where document_no = @document_no
			
			if @cartons < 1
				break
			else
				continue	
		end
	
	delete from tmpHeaderWM where document_no = @document_no
	select @headers = count(*) from tmpHeaderWM
	
	if @headers < 1
		break
	else
		continue
end
```

