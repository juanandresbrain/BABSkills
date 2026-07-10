# dbo.spDistro_UnshippedDistrosFrom980

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spDistro_UnshippedDistrosFrom980"]
    dbo_sp_send_dbmail(["dbo.sp_send_dbmail"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.sp_send_dbmail |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[spDistro_UnshippedDistrosFrom980] AS

-- =============================================================================================================
-- Name: spDistro_UnshippedDistrosFrom980
--
-- Description:	

--
-- Input:		
--				
--
--
-- Output: 
--
-- Dependencies: 
--
-- Revision History
--		Name:			Date:			Comments:
--		GaryD			20090914		Update recipients
--		MikeP			20140114		Update recipients
--		MikeP			20140724		replaced email procedure with sp_send_dbmail
-- =============================================================================================================

declare @sql varchar(8000)
declare @documentnumber varchar(8000)
declare @startdate	datetime
declare @stopdate	datetime

set @startdate 	= cast(convert(varchar(10), dateadd(dd,-2,getdate()), 101) + ' 00:00:00' as datetime)
set @stopdate 	= cast(convert(varchar(10), dateadd(dd,-1,getdate()), 101) + ' 23:59:59' as datetime)

-- 10.0.0.161 = bedrockdb02
IF (Object_ID('tempdb..##distro_transfers_P94') IS NOT NULL) DROP TABLE ##distro_transfers_P94
set @sql = '
select * 
into ##distro_transfers_P94
FROM OPENROWSET(''SQLOLEDB'', ''bedrockdb02''; ''link_readonly'' ; ''l1nkr'',
''
select *
from me_01.dbo.distro_transfers
where convert(varchar(10), loaded_date, 101) between cast(''''' + cast(@startdate as varchar) + ''''' as datetime) and cast(''''' + cast(@stopdate as varchar) + ''''' as datetime)
		and sourceid=980

''
)'
--print @sql
exec (@sql)


IF (Object_ID('tempdb..##warehouse_P94') IS NOT NULL) DROP TABLE ##warehouse_P94
create table ##warehouse_P94 (
	wh_po_nbr		varchar(20),
	wh_seq_nbr		int,
	wh_dsgnated_serv_lvl	varchar(8),
	wh_store_nbr	varchar(10),
	wh_style		varchar(10),
	wh_create_date_time	datetime,
	wh_mod_date_time		datetime,
	wh_orig_req_qty		numeric(13, 5),
	wh_wave_alloc_qty		numeric(13, 5),
	wh_user_id		varchar(15)
)

declare @all_docs	varchar(8000)
declare @count	int
-- declare @documentnumber	varchar(10)
-- declare @sql varchar(8000)

set @all_docs = ''
declare @total_count int
declare @process_count int

set @total_count = (select count(distinct documentnumber) from ##distro_transfers_P94)
set @process_count = 0
set @count = 0

declare curDocNum cursor
for	select distinct documentnumber from ##distro_transfers_P94 order by documentnumber
open curDocNum

fetch next from curDocNum into @documentnumber
while (@@fetch_STATUS <> -1)
begin
	set @all_docs = @all_docs + ',' + @documentnumber
	set @count = @count + 1

	if @count = 100 or @process_count = @total_count-1
	begin
--		print 'hi'

		set @all_docs = substring(@all_docs, 2, 8000)
--		print @all_docs

		IF (Object_ID('tempdb..##warehouse_P94_temp') IS NOT NULL) DROP TABLE ##warehouse_P94_temp
		set @sql = '
		select * 
		into ##warehouse_P94_temp
		from OPENROWSET(''SQLOLEDB'', ''wmdb01''; ''wmadmin'' ; ''wm@dm1n'',
		''
		select 
			sd.po_nbr wh_po_nbr,
			seq_nbr wh_seq_nbr,
			dsgnated_serv_lvl,
			cast(sd.store_nbr as varchar(10)) wh_store_nbr,
			im.style wh_style,
			sd.create_date_time wh_create_date_time,
			sd.mod_date_time wh_mod_date_time,
			sd.orig_req_qty wh_orig_req_qty,
			sd.wave_alloc_qty wh_wave_alloc_qty,
			sd.user_id	wh_user_id
		from	
			wmprod.dbo.store_distro sd with (nolock)
			left join wmprod.dbo.item_master im with (nolock)
			on im.sku_id = sd.sku_id
		where sd.po_nbr in (' + @all_docs + ')
			and wave_alloc_qty = 0
		''
		)'
		print @sql
		exec (@sql)

		insert into ##warehouse_P94
		select * from ##warehouse_P94_temp

		set @count = 0
		set @all_docs = ''
	end
	set @process_count = @process_count + 1

	fetch next from curDocNum into @documentnumber
end
close curDocNum
deallocate curDocNum


-- *******************************************************
-- * OUTPUT
-- *******************************************************
-- OUTPUT FILE:  UnprocessedDistros.csv
-- set nocount on
-- select  groupinglabel, rec_type, reasoncode, documentnumber, linenumber, sourceid, destid, upc_number, p.style_desc, 

-- declare @sql varchar(8000)
set @sql = '
select  rec_type, reasoncode, documentnumber, sourceid, destid, upc_number, p.style_desc, 
	convert(varchar, wh_create_date_time, 120) wh_create_date_time, convert(varchar, wh_mod_date_time, 120) wh_mod_date_time, wh_orig_req_qty, wh_wave_alloc_qty, wh_user_id
from ##warehouse_P94 wh
	join ##distro_transfers_P94 dt
	on dt.documentnumber = wh.wh_po_nbr
	and dt.linenumber= wh.wh_seq_nbr
	left join dw..product_dim p
 	on p.style_code = wh.wh_style
	left join (
		select  wh_po_nbr, wh_seq_nbr 
		from ##warehouse_P94 wh
		where wh_create_date_time = wh_mod_date_time
			and wh_create_date_time > cast(convert(varchar(10), dateadd(dd,-1,getdate()), 101) + '' 11:00:00'' as datetime)
	) d
	on d.wh_po_nbr = wh.wh_po_nbr
	and d.wh_seq_nbr = wh.wh_seq_nbr
where d.wh_po_nbr is null
order by documentnumber, linenumber
'

declare @filename  varchar(100)
declare @char_separator varchar(12)
declare @message varchar(200)
set @filename='UnshippedDistros'+replace(convert(varchar(12), @stopdate, 102),'.','')+'.xls'
set @char_separator = char(9)
set @message = 'The attached list contains unshipped distros for 980 placed between ' + cast(@startdate as varchar) + ' and ' + cast(@stopdate as varchar) + '.'

EXEC msdb.dbo.sp_send_dbmail 
	@recipients = 'Develobears@buildabear.com; corieb@buildabear.com; purchasing@buildabear.com; dant@buildabear.com;keithl@buildabear.com',
	@body = @message, 
	@subject = 'Unshipped Distros from 980',
	@query_result_width = 500,
	@query = @sql,
	@attach_query_result_as_file = 1,
	@query_result_separator = @char_separator,
	@query_attachment_filename = @filename
```

