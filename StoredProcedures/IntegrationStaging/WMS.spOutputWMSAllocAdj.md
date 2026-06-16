# WMS.spOutputWMSAllocAdj

**Database:** IntegrationStaging  

## Architecture Diagram

```mermaid
flowchart LR
    SP["WMS.spOutputWMSAllocAdj"]
    dbo_tmpAllocationsAdjWMS(["dbo.tmpAllocationsAdjWMS"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tmpAllocationsAdjWMS |

## Stored Procedure Code

```sql
CREATE proc [WMS].[spOutputWMSAllocAdj]
as
-- =====================================================================================================
--	Name: 
--				 
-- Revision History
--		Name:			Date:			Comments:
--		Dan Tweedie		2019-07-30		created proc to format pipeline file for allocation adjustment from staged dynamics wms data
--										--modeled after bedrockdb02.me_01.dbo.spMerchandisingOutputUKAllocAdj
-- =====================================================================================================

set nocount on

declare @headers int,
		@locations int,
		@distro_lines int,
		@document_no varchar(10),
		@distro_line varchar(2),
		@upc varchar(12),
		@location varchar(4),
		@qty varchar(10)

select @headers = count(*) from tmpAllocationsAdjWMS
while @headers > 0 
begin
	select @document_no = max(distribution_number)
	from tmpAllocationsAdjWMS
	
	select @distro_line = max(distribution_line)
	from tmpAllocationsAdjWMS
	where distribution_number = @document_no
	
	print 'H' + '	' + 'C' + '	' +	@document_no + '	' + @distro_line + '	'
	
	select @upc = upc
	from tmpAllocationsAdjWMS
	where distribution_number = @document_no
	and distribution_line = @distro_line
			
	select @locations = count(location_code)
	from tmpAllocationsAdjWMS
	where distribution_number = @document_no
	and distribution_line = @distro_line
	
	while @locations > 0
	begin
	
		select @location = max(location_code)
		from tmpAllocationsAdjWMS
		where distribution_number = @document_no
		and distribution_line = @distro_line
		and upc = @upc
	
		select @qty = sum(adj_qty) --(sum(adj_qty) * -1) --04/15/2015 - Dan T
		from tmpAllocationsAdjWMS
		where distribution_number = @document_no
		and distribution_line = @distro_line
		and upc = @upc
		and location_code = @location
		
		print 'D' + '	' + 'C' + '	' +	@document_no + '	' + @distro_line + '	' + '	' + '	' + '	' + '	' + '	' + @upc + '	' + @location + '	' + @qty + '	'
			
		delete from tmpAllocationsAdjWMS 
		where distribution_number = @document_no
		and distribution_line = @distro_line
		and upc = @upc
		and location_code = @location
			
		select @locations = count(location_code)
		from tmpAllocationsAdjWMS
		where distribution_number = @document_no
		and distribution_line = @distro_line
			
			if @locations < 1
				break
			else
				continue	
	end

select @headers = count(*) from tmpAllocationsAdjWMS
	
	if @headers < 1
		break
	else
		continue
end
```

