# dbo.spMerchandisingOutputWCAllocAdj

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMerchandisingOutputWCAllocAdj"]
    dbo_tmpAllocationsAdj(["dbo.tmpAllocationsAdj"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tmpAllocationsAdj |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spMerchandisingOutputWCAllocAdj]
as
-- =====================================================================================================
-- Name: spMerchandisingOutputWCAllocAdj
--
-- Description:	selects allocation adjustmen records, presented in a format that is readable by the Merchandising Pipeline.
--				
-- Input:	
--
-- Output: 

-- Dependencies: this is designed to be called from spMerchandisingProcessWCShipmentsAllocAdj
--				 
-- Revision History
--		Name:			Date:			Comments:
--		Dan Tweedie		03/15/2012		created proc
-- =====================================================================================================

set nocount on

declare @headers int,
		@locations int,
		@distro_lines int,
		@document_no varchar(10),
		@distro_line varchar(3), -- Changed from 2 to 3 on 5/13/2025 --- Tim C
		@upc varchar(12),
		@location varchar(4),
		@qty varchar(10)

--select * from tmpAllocationsAdj
select @headers = count(*) from tmpAllocationsAdj
while @headers > 0 
begin
	select @document_no = max(distribution_no)
	from tmpAllocationsAdj
	
	select @distro_line = max(distribution_line)
	from tmpAllocationsAdj
	where distribution_no = @document_no
	
	print 'H' + '	' + 'C' + '	' +	@document_no + '	' + @distro_line + '	'
	
	select @upc = upc
	from tmpAllocationsAdj
	where distribution_no = @document_no
	and distribution_line = @distro_line
			
	select @locations = count(location_code)
	from tmpAllocationsAdj
	where distribution_no = @document_no
	and distribution_line = @distro_line
	
	while @locations > 0
	begin
	
		select @location = max(location_code)
		from tmpAllocationsAdj
		where distribution_no = @document_no
		and distribution_line = @distro_line
		and upc = @upc
	
		select @qty = adj_qty
		from tmpAllocationsAdj
		where distribution_no = @document_no
		and distribution_line = @distro_line
		and upc = @upc
		and location_code = @location
		
		print 'D' + '	' + 'C' + '	' +	@document_no + '	' + @distro_line + '	' + '	' + '	' + '	' + '	' + '	' + @upc + '	' + @location + '	' + @qty + '	'
			
		delete from tmpAllocationsAdj 
		where distribution_no = @document_no
		and distribution_line = @distro_line
		and upc = @upc
		and location_code = @location
			
		select @locations = count(location_code)
		from tmpAllocationsAdj
		where distribution_no = @document_no
		and distribution_line = @distro_line
			
			if @locations < 1
				break
			else
				continue	
	end

select @headers = count(*) from tmpAllocationsAdj
	
	if @headers < 1
		break
	else
		continue
end
```

