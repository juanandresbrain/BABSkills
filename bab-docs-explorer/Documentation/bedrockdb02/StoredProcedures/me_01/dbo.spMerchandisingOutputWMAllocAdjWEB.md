# dbo.spMerchandisingOutputWMAllocAdjWEB

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMerchandisingOutputWMAllocAdjWEB"]
    dbo_tmpAllocationsAdjWMweb(["dbo.tmpAllocationsAdjWMweb"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tmpAllocationsAdjWMweb |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spMerchandisingOutputWMAllocAdjWEB]
as
-- =====================================================================================================
-- Name: spMerchandisingOutputWMAllocAdjWEB
--
-- Description:	selects allocation adjustment records (980 to web), presented in a format that is readable by the Merchandising Pipeline.
-- Revision History
--		Name:			Date:			Comments:
--		Dan Tweedie		05/07/2015		created proc
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

select @headers = count(*) from tmpAllocationsAdjWMweb
while @headers > 0 
begin
	select @document_no = max(distribution_number)
	from tmpAllocationsAdjWMweb
	
	select @distro_line = max(dist_line_id)
	from tmpAllocationsAdjWMweb
	where distribution_number = @document_no
	
	print 'H' + '	' + 'C' + '	' +	@document_no + '	' + @distro_line + '	'
	
	select @upc = upc_no
	from tmpAllocationsAdjWMweb
	where distribution_number = @document_no
	and dist_line_id = @distro_line
			
	select @locations = count(location_code)
	from tmpAllocationsAdjWMweb
	where distribution_number = @document_no
	and dist_line_id = @distro_line
	
	while @locations > 0
	begin
	
		select @location = max(location_code)
		from tmpAllocationsAdjWMweb
		where distribution_number = @document_no
		and dist_line_id = @distro_line
		and upc_no = @upc
	
		select @qty = sum(adj_qty)
		from tmpAllocationsAdjWMweb
		where distribution_number = @document_no
		and dist_line_id = @distro_line
		and upc_no = @upc
		and location_code = @location
		
		print 'D' + '	' + 'C' + '	' +	@document_no + '	' + @distro_line + '	' + '	' + '	' + '	' + '	' + '	' + @upc + '	' + @location + '	' + @qty + '	'
			
		delete from tmpAllocationsAdjWMweb 
		where distribution_number = @document_no
		and dist_line_id = @distro_line
		and upc_no = @upc
		and location_code = @location
			
		select @locations = count(location_code)
		from tmpAllocationsAdjWMweb
		where distribution_number = @document_no
		and dist_line_id = @distro_line
			
			if @locations < 1
				break
			else
				continue	
	end

select @headers = count(*) from tmpAllocationsAdjWMweb
	
	if @headers < 1
		break
	else
		continue
end
```

