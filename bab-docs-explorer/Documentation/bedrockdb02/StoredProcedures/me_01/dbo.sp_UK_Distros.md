# dbo.sp_UK_Distros

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_UK_Distros"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table references detected._

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[sp_UK_Distros]
AS
BEGIN
	set nocount on

IF (Object_ID('tempdb..#tempme') IS NOT NULL) DROP TABLE #tempme
select      ddas.destid as destid,
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
			s.distribution_multiple
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
where ddas.sourceid = 2970
and cast(convert(varchar, ddas.release_date,101)as datetime)  = cast(convert(varchar, getdate(),101)as datetime)
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
and       ddas.distribution_number not in (select distribution_number from UK_PROCESS_CONTROL)


declare @destid int
declare @rec_type varchar(10)
declare @style_code varchar(20)
declare @quantity int
declare @distribution_number varchar(50)
declare @distribution_multiple int

declare curDistro cursor
for	
	select destid, rec_type, style_code, quantity, distribution_number, distribution_multiple
	from #tempme
	where quantity != distribution_multiple
--	and destid = '0119' and rec_type = 1 and style_code = '100582'
--destid	rec_type	quantity	style_code	distribution_number	count
--0119	1	150	100582	001081	3
open curDistro

fetch next from curDistro into @destid, @rec_type, @style_code, @quantity, @distribution_number, @distribution_multiple
while (@@fetch_STATUS <> -1)
begin
	while @quantity > 0 
	begin
		set @quantity = @quantity - @distribution_multiple

		insert into #tempme(destid, rec_type, message, style_code, quantity, release_date, distribution_number, ref_field_1, short_desc, vendor_style, color_code)
		select destid, rec_type, message, style_code, @distribution_multiple, release_date, distribution_number, ref_field_1, short_desc, vendor_style, color_code
		from #tempme
		where destid = @destid
			and rec_type = @rec_type
			and style_code = @style_code
			and distribution_number = @distribution_number
			and distribution_multiple is not null
	end

	delete from #tempme
--	select * from #tempme
	where destid = @destid
		and rec_type = @rec_type
		and style_code = @style_code
		and distribution_number = @distribution_number
		and distribution_multiple is not null

	fetch next from curDistro into @destid, @rec_type, @style_code, @quantity, @distribution_number, @distribution_multiple
end
close curDistro
deallocate curDistro

select destid, rec_type, message, style_code, quantity, release_date, distribution_number, ref_field_1, short_desc, vendor_style, color_code
from #tempme
order by destid, ddas.rec_type, convert(varchar, release_date,101), style_code



END
```

