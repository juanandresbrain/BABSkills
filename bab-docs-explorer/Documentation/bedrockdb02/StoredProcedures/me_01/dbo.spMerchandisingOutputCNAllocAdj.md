# dbo.spMerchandisingOutputCNAllocAdj

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMerchandisingOutputCNAllocAdj"]
    dbo_tmpAllocationsAdjCN(["dbo.tmpAllocationsAdjCN"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tmpAllocationsAdjCN |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spMerchandisingOutputCNAllocAdj]
as
-- =====================================================================================================
-- Name: spMerchandisingOutputCNAllocAdj
--
-- Description:	selects allocation adjustmen records, presented in a format that is readable by the Merchandising Pipeline.
-- Revision History
--		Name:			Date:			Comments:
--		Dan Tweedie		01/25/2016		created proc
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

--select * from tmpAllocationsAdj
select @headers = count(*) from tmpAllocationsAdjCN
while @headers > 0 
begin
	select @document_no = max(distribution_number)
	from tmpAllocationsAdjCN
	
	select @distro_line = max(distribution_line)
	from tmpAllocationsAdjCN
	where distribution_number = @document_no
	
	print 'H' + '	' + 'C' + '	' +	@document_no + '	' + @distro_line + '	'
	
	select @upc = upc
	from tmpAllocationsAdjCN
	where distribution_number = @document_no
	and distribution_line = @distro_line
			
	select @locations = count(location_code)
	from tmpAllocationsAdjCN
	where distribution_number = @document_no
	and distribution_line = @distro_line
	
	while @locations > 0
	begin
	
		select @location = max(location_code)
		from tmpAllocationsAdjCN
		where distribution_number = @document_no
		and distribution_line = @distro_line
		and upc = @upc
	
		select @qty = adj_qty
		from tmpAllocationsAdjCN
		where distribution_number = @document_no
		and distribution_line = @distro_line
		and upc = @upc
		and location_code = @location
		
		print 'D' + '	' + 'C' + '	' +	@document_no + '	' + @distro_line + '	' + '	' + '	' + '	' + '	' + '	' + '000000' + @upc + '	' + @location + '	' + @qty + '	'
			
		delete from tmpAllocationsAdjCN 
		where distribution_number = @document_no
		and distribution_line = @distro_line
		and upc = @upc
		and location_code = @location
			
		select @locations = count(location_code)
		from tmpAllocationsAdjCN
		where distribution_number = @document_no
		and distribution_line = @distro_line
			
			if @locations < 1
				break
			else
				continue	
	end

select @headers = count(*) from tmpAllocationsAdjCN
	
	if @headers < 1
		break
	else
		continue
end
```

