# dbo.sp_UPS_Distros

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_UPS_Distros"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table references detected._

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[sp_UPS_Distros]
AS
BEGIN
	set nocount on

IF (Object_ID('tempdb..#tempme') IS NOT NULL) DROP TABLE #tempme
select		ddas.id,
			ddas.destid as destid,
            ddas.rec_type,
            rt.message,
            ddas.style_code, 
            
            case when SUBSTRING(hg.hierarchy_group_code, 7, 2) = '60'
                  then  ddas.quantity * s.distribution_multiple-- Canada deals in Cases.
                  else  ddas.quantity * s.distribution_multiple
            end as quantity, 
 
            convert(varchar, ddas.release_date,101) as release_date,
            ddas.distribution_number, 
            ddas.ref_field_1,
            s.short_desc, --include french too?             
            sv.vendor_style,
            c.color_code,
			s.order_multiple,
			s.distribution_multiple,
			ddas.sourceid
into #tempme
from  distribution_data_after_split ddas,
            rec_type rt,
            location l,
            hierarchy_group hg,
            style_group sg,
            style s,
            style_vendor sv,
            entity_custom_property ecp,
            upc u,
            sku sk,
            style_color sc,
            color c
where ddas.sourceid between '9913' and '9925'
--and cast(convert(varchar, ddas.release_date,101)as datetime)  = cast(convert(varchar, getdate()-1,101)as datetime)
and         ddas.rec_type = rt.rectype
and         ddas.destid = l.location_code
and         ddas.style_code = s.style_code
and         s.style_id = sg.style_id
and         sg.hierarchy_group_id = hg.hierarchy_group_id
and         s.style_id = sv.style_id
and         sv.primary_vendor_flag = 1
and         '000000'+s.style_code = u.upc_number
and         u.sku_id = sk.sku_id
and         sk.style_color_id = sc.style_color_id
and         sc.color_id = c.color_id
and         s.style_id *= ecp.parent_id
and         ecp.custom_property_id = 2
and         ecp.parent_type = 1
--and			(cast(rt.rectype as int) >= 50
--or			(cast(rt.rectype as int) < 50 and datepart(hh,getdate()) >= 18))
--and       ddas.distribution_number not in (select distribution_number from CAN_PROCESS_CONTROL)
and ddas.released is null

--and s.style_code = '014209'
--and	ddas.destid = '0001'
--and ddas.distribution_number = '150790'

----- First pass for order multiple


declare @destid int
declare @sourceid int
declare @rec_type varchar(10)
declare @style_code varchar(20)
declare @quantity int
declare @distribution_number varchar(50)
declare @distribution_multiple int
declare @order_multiple int

declare curDistro cursor
for	
	select destid, rec_type, style_code, quantity, distribution_number, order_multiple, distribution_multiple, sourceid
	from #tempme
	where quantity != distribution_multiple
open curDistro

fetch next from curDistro into @destid, @rec_type, @style_code, @quantity, @distribution_number, @order_multiple, @distribution_multiple, @sourceid
while (@@fetch_STATUS <> -1)
begin
	while @quantity >= @distribution_multiple
	begin
		
		insert into #tempme(id,destid, rec_type, message, style_code, quantity, release_date, distribution_number, ref_field_1, short_desc, vendor_style, color_code, order_multiple, distribution_multiple,sourceid)
		select id, destid, rec_type, message, style_code, --@distribution_multiple, 
		
		case when @quantity > @order_multiple --(select distribution_multiple from style where style_code = @style_code)
		then @order_multiple
		else @quantity 
		end,
		release_date, distribution_number, ref_field_1, short_desc, null as vendor_style, color_code,  order_multiple, distribution_multiple, sourceid
		from #tempme
		where destid = @destid
			and rec_type = @rec_type
			and style_code = @style_code
			and distribution_number = @distribution_number
			and sourceid = @sourceid
			and vendor_style is not null
		
		set @quantity = @quantity - @order_multiple

	end

	delete from #tempme
--	select * from #tempme
	where destid = @destid
		and rec_type = @rec_type
		and style_code = @style_code
		and distribution_number = @distribution_number
		and sourceid = @sourceid
		and vendor_style is not null

	fetch next from curDistro into @destid, @rec_type, @style_code, @quantity, @distribution_number, @order_multiple, @distribution_multiple, @sourceid
end
close curDistro
deallocate curDistro

------ Second pass for distribution multiple

declare curDistro cursor
for	
	select destid, rec_type, style_code, quantity, distribution_number, order_multiple, distribution_multiple, sourceid
	from #tempme
	where quantity < order_multiple and quantity <> distribution_multiple
open curDistro

fetch next from curDistro into @destid, @rec_type, @style_code, @quantity, @distribution_number, @order_multiple, @distribution_multiple, @sourceid
while (@@fetch_STATUS <> -1)
begin
	while @quantity > 0 --<> @distribution_multiple
	begin
		
		insert into #tempme(id,destid, rec_type, message, style_code, quantity, release_date, distribution_number, ref_field_1, short_desc, vendor_style, color_code, order_multiple, distribution_multiple, sourceid)
		select id, destid, rec_type, message, style_code,-- @distribution_multiple, 
		case when @quantity > @distribution_multiple --(select distribution_multiple from style where style_code = @style_code)
		then @distribution_multiple
		else @quantity 
		end,
		release_date, distribution_number, ref_field_1, short_desc, null as vendor_style, 'AAA' as color_code,  order_multiple, distribution_multiple, sourceid
		from #tempme
		where destid = @destid
			and rec_type = @rec_type
			and style_code = @style_code
			and distribution_number = @distribution_number
			and sourceid = @sourceid
			and color_code <> 'AAA'--is not null
			and	quantity < @order_multiple
	
			set @quantity = @quantity - @distribution_multiple

	end

	delete from #tempme
--	select * from #tempme order by destid
	where destid = @destid
		and rec_type = @rec_type
		and style_code = @style_code
		and distribution_number = @distribution_number
		and sourceid = @sourceid
		and color_code <> 'AAA'--is not null
		and quantity <> @order_multiple
		--and quantity > @distribution_multiple

	fetch next from curDistro into @destid, @rec_type, @style_code, @quantity, @distribution_number, @order_multiple, @distribution_multiple, @sourceid
end
close curDistro
deallocate curDistro


insert into store_shipment_ups
select destid, sourceid,rec_type, message, style_code, quantity, release_date, distribution_number, ref_field_1, short_desc, vendor_style, color_code, null as exported_date
from #tempme
order by destid, ddas.rec_type, convert(varchar, release_date,101), style_code

--- update distribution_data_after_split
update distribution_data_after_split set released = 1
--select  ddas.*
from	store_shipment_ups ssu,
		distribution_data_after_split ddas
where	ddas.destid = ssu.destid
and		ddas.sourceid = ssu.sourceid
and		ddas.distribution_number = ssu.distribution_number
and		ssu.exported_date is null
and		ddas.released is null

END
```

