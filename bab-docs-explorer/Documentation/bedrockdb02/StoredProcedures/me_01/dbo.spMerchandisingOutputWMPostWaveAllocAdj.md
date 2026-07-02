# dbo.spMerchandisingOutputWMPostWaveAllocAdj

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMerchandisingOutputWMPostWaveAllocAdj"]
    dbo_tmpPostWaveAllocationsAdjWM(["dbo.tmpPostWaveAllocationsAdjWM"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tmpPostWaveAllocationsAdjWM |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spMerchandisingOutputWMPostWaveAllocAdj]
as
-- =====================================================================================================
-- Name: spMerchandisingOutputWMPostWaveAllocAdj
--
-- Description:	selects allocation adjustment records, presented in a format that is readable by the Merchandising Pipeline.
--
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

select @headers = count(*) from tmpPostWaveAllocationsAdjWM
while @headers > 0 
begin
	select @document_no = max(distribution_no)
	from tmpPostWaveAllocationsAdjWM
	
	select @distro_line = max(distribution_line_no)
	from tmpPostWaveAllocationsAdjWM
	where distribution_no = @document_no
	
	print 'H' + '	' + 'C' + '	' +	@document_no + '	' + @distro_line + '	'
	
	select @upc = upc_no
	from tmpPostWaveAllocationsAdjWM
	where distribution_no = @document_no
	and distribution_line_no = @distro_line
			
	select @locations = count(location_code)
	from tmpPostWaveAllocationsAdjWM
	where distribution_no = @document_no
	and distribution_line_no = @distro_line
	
	while @locations > 0
	begin
	
		select @location = max(location_code)
		from tmpPostWaveAllocationsAdjWM
		where distribution_no = @document_no
		and distribution_line_no = @distro_line
		and upc_no = @upc
	
		select @qty = sum(allocated_units)
		from tmpPostWaveAllocationsAdjWM
		where distribution_no = @document_no
		and distribution_line_no = @distro_line
		and upc_no = @upc
		and location_code = @location
		
		print 'D' + '	' + 'C' + '	' +	@document_no + '	' + @distro_line + '	' + '	' + '	' + '	' + '	' + '	' + @upc + '	' + @location + '	' + @qty + '	'
			
		delete from tmpPostWaveAllocationsAdjWM 
		where distribution_no = @document_no
		and distribution_line_no = @distro_line
		and upc_no = @upc
		and location_code = @location
			
		select @locations = count(location_code)
		from tmpPostWaveAllocationsAdjWM
		where distribution_no = @document_no
		and distribution_line_no = @distro_line
			
			if @locations < 1
				break
			else
				continue	
	end

select @headers = count(*) from tmpPostWaveAllocationsAdjWM
	
	if @headers < 1
		break
	else
		continue
end
```

