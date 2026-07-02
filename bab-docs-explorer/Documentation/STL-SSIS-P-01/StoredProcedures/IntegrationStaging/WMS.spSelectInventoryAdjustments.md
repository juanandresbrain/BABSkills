# WMS.spSelectInventoryAdjustments

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["WMS.spSelectInventoryAdjustments"]
    WMS_InventoryAdjustments(["WMS.InventoryAdjustments"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| WMS.InventoryAdjustments |

## Stored Procedure Code

```sql
CREATE proc [WMS].[spSelectInventoryAdjustments]

as

-- =====================================================================================================
-- Name: spSelectInventoryAdjustments
--
--		Dan Tweedie		2019-07-2019	Created proc to format data for Aptos Pipeline file, called from another proc
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
		
set @docx = (convert(varchar, datepart(yyyy, getdate())) + convert(varchar, datepart(mm, getdate())) + convert(varchar, datepart(dd, getdate())) + convert(varchar, datepart(hh, getdate())) + convert(varchar, datepart(mi, getdate())) + convert(varchar, datepart(ss, getdate())))
set @date = convert(varchar, getdate(), 101)

set @counter_h = 1
select @total_headers = count(distinct ReasonCode) from WMS.InventoryAdjustments where TransmittedToAptos is NULL

declare header cursor for
		select distinct 'H', 'A', 
			((convert(varchar, datepart(yyyy, getdate())) + convert(varchar, datepart(mm, getdate())) + convert(varchar, datepart(dd, getdate())) + convert(varchar, datepart(hh, getdate())) + convert(varchar, datepart(mi, getdate())) + convert(varchar, datepart(ss, getdate())) + convert(varchar, datepart(ms, getdate()))) + convert(varchar, @counter_h)), 
				@date, '1', 'BEARHOUSE', ReasonCode, '3', 'WM'
		from WMS.InventoryAdjustments
		where Warehouse='9980'
		and TransmittedToAptos is NULL
		order by ReasonCode

open header

while @counter_h <= @total_headers
	begin
		fetch next from header into @recordtype_h, @actiontype_h, @documentno_h, @datesubmitted_h, @shrink_h, @performedby_h, @groupinglabel_h, @source_h, @externalsystemname_h
		print @recordtype_h + '	' + @actiontype_h + '	' + @documentno_h + '	' + @datesubmitted_h + '	' + @shrink_h + '	' + @performedby_h + '	' + @groupinglabel_h + '	' + @source_h + '	' + @externalsystemname_h

		declare detail cursor for
			select 'D', 'A', @documentno_h, '0980', ('000000' + ItemNumber), (AdjustedQuantity*-1) as AdjustedQuantity
			from WMS.InventoryAdjustments
			where Warehouse='9980'
			and TransmittedToAptos is NULL
			and ReasonCode = @groupinglabel_h
			order by ('000000' + ItemNumber)
		
		set @counter_d = 1
		select @total_details = count(ItemNumber) from WMS.InventoryAdjustments where TransmittedToAptos is NULL and ReasonCode = @groupinglabel_h
		
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
		
		update WMS.InventoryAdjustments
		set TransmittedToAptos=getdate()
		where TransmittedToAptos is NULL
		and ReasonCode = @groupinglabel_h

	end
	close header
	deallocate header
```

