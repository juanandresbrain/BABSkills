# dbo.spMerchandisingSelectCNStockAdj

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMerchandisingSelectCNStockAdj"]
    dbo_cn_qty_convert(["dbo.cn_qty_convert"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.cn_qty_convert |

## Stored Procedure Code

```sql
create proc [dbo].[spMerchandisingSelectCNStockAdj]
as

-- =====================================================================================================
-- Name: spMerchandisingSelectCNStockAdj
--
-- Description:	formats shrink adjustment file for pipeline
--
-- Revision History
--		Name:			Date:			Comments:
--		Dan Tweedie		01/25/2016		Created proc.	
-- =====================================================================================================

set nocount on

declare @recordtype_h varchar(1),
		@actiontype_h varchar(1),
		@documentno_h varchar(22),
		@datesubmitted_h varchar(10),
		@shrink_h varchar(1),
		@performedby_h varchar(14),
		@groupinglabel_h varchar(52),
		@source_h varchar(1),
		@externalsystemname_h varchar(10),
		@recordtype_d varchar(1),
		@actiontype_d varchar(1),
		@documentno_d varchar(22),
		@locationcode_d varchar(4),
		@upc_d varchar(13),
		@units_d int,
		@counter_h int,
		@counter_d int,
		@total_headers int,
		@total_details int,
		@docx varchar(22),
		@date varchar(12)
		
set @docx = (convert(varchar, datepart(yyyy, getdate())) + convert(varchar, datepart(mm, getdate())) + convert(varchar, datepart(dd, getdate())) + convert(varchar, datepart(hh, getdate())) + convert(varchar, datepart(mi, getdate())))
set @date = convert(varchar, getdate(), 101)

set @counter_h = 1
select @total_headers = count(distinct description) from cn_qty_convert

declare header cursor for
		select distinct 'H', 'A', 
			((convert(varchar, datepart(yyyy, getdate())) + convert(varchar, datepart(mm, getdate())) + convert(varchar, datepart(dd, getdate())) + convert(varchar, datepart(hh, getdate())) + convert(varchar, datepart(mi, getdate()))) + convert(varchar, @counter_h)), 
				@date, '1', 'CNStockAdjFile', description, '3', 'CNDC'
		from cn_qty_convert
		order by description

open header

while @counter_h <= @total_headers
	begin
		fetch next from header into @recordtype_h, @actiontype_h, @documentno_h, @datesubmitted_h, @shrink_h, @performedby_h, @groupinglabel_h, @source_h, @externalsystemname_h
		print @recordtype_h + '	' + @actiontype_h + '	' + @documentno_h + '	' + @datesubmitted_h + '	' + @shrink_h + '	' + @performedby_h + '	' + @groupinglabel_h + '	' + @source_h + '	' + @externalsystemname_h

		declare detail cursor for
			select 'D', 'A', @documentno_h, location_code, ('000000' + style), converted_qty
			from cn_qty_convert
			where description = @groupinglabel_h
			order by ('000000' + style)
		
		set @counter_d = 1
		select @total_details = count(style) from cn_qty_convert where description = @groupinglabel_h
		
		open detail 
		
			while @counter_d <= @total_details
				begin
					fetch next from detail into @recordtype_d, @actiontype_d, @documentno_d, @locationcode_d, @upc_d, @units_d
					print @recordtype_d + '	' + @actiontype_d + '	' + @documentno_d + '	' + @locationcode_d + '	' + @upc_d + '	' + '	' + '	' + '	' + '	' + convert(varchar, @units_d)
					set @counter_d = @counter_d + 1
				end
				close detail
				deallocate detail
		set @counter_h = @counter_h + 1
	end
	close header
	deallocate header
```

