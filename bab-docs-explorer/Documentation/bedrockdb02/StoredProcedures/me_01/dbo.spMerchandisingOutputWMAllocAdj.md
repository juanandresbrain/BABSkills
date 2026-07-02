# dbo.spMerchandisingOutputWMAllocAdj

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMerchandisingOutputWMAllocAdj"]
    dbo_tmpAllocationsAdjWM(["dbo.tmpAllocationsAdjWM"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tmpAllocationsAdjWM |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spMerchandisingOutputWMAllocAdj]
as
-- =====================================================================================================
-- Name: spMerchandisingOutputWMAllocAdj
--
-- Description:	selects allocation adjustment records, presented in a format that is readable by the Merchandising Pipeline.
-- Revision History
--		Name:			Date:			Comments:
--		Dan Tweedie		05/04/2015		created proc
-- =====================================================================================================

set nocount on

declare @headers int,
		@locations int,
		@distro_lines int,
		@document_no varchar(10),
		@distro_line varchar(3), -- Changed from 2 to 3 on 5/13/2025 --- Lizzy T
		@upc varchar(12),
		@location varchar(4),
		@qty varchar(10)

select @headers = count(*) from tmpAllocationsAdjWM
while @headers > 0 
begin
	select @document_no = max(distribution_number)
	from tmpAllocationsAdjWM
	
	select @distro_line = max(dist_line_id)
	from tmpAllocationsAdjWM
	where distribution_number = @document_no
	
	print 'H' + '	' + 'C' + '	' +	@document_no + '	' + @distro_line + '	'
	
	select @upc = upc_no
	from tmpAllocationsAdjWM
	where distribution_number = @document_no
	and dist_line_id = @distro_line
			
	select @locations = count(location_code)
	from tmpAllocationsAdjWM
	where distribution_number = @document_no
	and dist_line_id = @distro_line
	
	while @locations > 0
	begin
	
		select @location = max(location_code)
		from tmpAllocationsAdjWM
		where distribution_number = @document_no
		and dist_line_id = @distro_line
		and upc_no = @upc
	
		select @qty = sum(adj_qty)
		from tmpAllocationsAdjWM
		where distribution_number = @document_no
		and dist_line_id = @distro_line
		and upc_no = @upc
		and location_code = @location
		
		print 'D' + '	' + 'C' + '	' +	@document_no + '	' + @distro_line + '	' + '	' + '	' + '	' + '	' + '	' + @upc + '	' + @location + '	' + @qty + '	'
			
		delete from tmpAllocationsAdjWM 
		where distribution_number = @document_no
		and dist_line_id = @distro_line
		and upc_no = @upc
		and location_code = @location
			
		select @locations = count(location_code)
		from tmpAllocationsAdjWM
		where distribution_number = @document_no
		and dist_line_id = @distro_line
			
			if @locations < 1
				break
			else
				continue	
	end

select @headers = count(*) from tmpAllocationsAdjWM
	
	if @headers < 1
		break
	else
		continue
end
```

