# dbo.spMerchandisingOutputUKAllocAdj

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMerchandisingOutputUKAllocAdj"]
    dbo_tmpAllocationsAdjUK(["dbo.tmpAllocationsAdjUK"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tmpAllocationsAdjUK |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spMerchandisingOutputUKAllocAdj]
as
-- =====================================================================================================
-- Name: spMerchandisingOutputUKAllocAdj
--
-- Description:	selects allocation adjustmen records, presented in a format that is readable by the Merchandising Pipeline.
--				
-- Input:	
--
-- Output: 

-- Dependencies: Is called by spMerchandisingSelectUKStoreShipments
--				 
-- Revision History
--		Name:			Date:			Comments:
--		Dan Tweedie		09/10/2013		created proc
--		Dan Tweedie		04/15/2015		Updated @qty to be sum(adj_qty) instead of (sum(adj_qty) * -1)
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

select @headers = count(*) from tmpAllocationsAdjUK
while @headers > 0 
begin
	select @document_no = max(distribution_number)
	from tmpAllocationsAdjUK
	
	select @distro_line = max(distribution_line)
	from tmpAllocationsAdjUK
	where distribution_number = @document_no
	
	print 'H' + '	' + 'C' + '	' +	@document_no + '	' + @distro_line + '	'
	
	select @upc = upc
	from tmpAllocationsAdjUK
	where distribution_number = @document_no
	and distribution_line = @distro_line
			
	select @locations = count(location_code)
	from tmpAllocationsAdjUK
	where distribution_number = @document_no
	and distribution_line = @distro_line
	
	while @locations > 0
	begin
	
		select @location = max(location_code)
		from tmpAllocationsAdjUK
		where distribution_number = @document_no
		and distribution_line = @distro_line
		and upc = @upc
	
		select @qty = sum(adj_qty)--(sum(adj_qty) * -1) --04/15/2015 - Dan T
		from tmpAllocationsAdjUK
		where distribution_number = @document_no
		and distribution_line = @distro_line
		and upc = @upc
		and location_code = @location
		
		print 'D' + '	' + 'C' + '	' +	@document_no + '	' + @distro_line + '	' + '	' + '	' + '	' + '	' + '	' + @upc + '	' + @location + '	' + @qty + '	'
			
		delete from tmpAllocationsAdjUK 
		where distribution_number = @document_no
		and distribution_line = @distro_line
		and upc = @upc
		and location_code = @location
			
		select @locations = count(location_code)
		from tmpAllocationsAdjUK
		where distribution_number = @document_no
		and distribution_line = @distro_line
			
			if @locations < 1
				break
			else
				continue	
	end

select @headers = count(*) from tmpAllocationsAdjUK
	
	if @headers < 1
		break
	else
		continue
end
```

