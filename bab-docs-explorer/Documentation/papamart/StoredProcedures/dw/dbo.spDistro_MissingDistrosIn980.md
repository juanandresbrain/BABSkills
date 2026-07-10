# dbo.spDistro_MissingDistrosIn980

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spDistro_MissingDistrosIn980"]
    dbo_sp_send_dbmail(["dbo.sp_send_dbmail"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.sp_send_dbmail |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[spDistro_MissingDistrosIn980] AS

-- =============================================================================================================
-- Name: spDistro_MissingDistrosIn980
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
--		MikeP			20140114		Updated recipients comments
--		MikeP			20140724		Replaced email procedure call with sp_send_dbmail
-- =============================================================================================================

declare @sql varchar(8000)
declare @documentnumber varchar(8000)

-- 10.0.0.161 = bedrockdb02
IF (Object_ID('tempdb..##distro_transfers_Z35') IS NOT NULL) DROP TABLE ##distro_transfers_Z35
set @sql = '
select * 
into ##distro_transfers_Z35
FROM OPENROWSET(''SQLOLEDB'', ''bedrockdb02''; ''link_readonly'' ; ''l1nkr'',
''
select *
from me_01.dbo.distro_transfers with (nolock)
where exported_date between dateadd(hh,-3,getdate()) and dateadd(mi, -15, getdate())
		and sourceid=980

''
)'
-- print @sql
exec (@sql)

create index ix_distro_transfers2 on ##distro_transfers_Z35(documentnumber, linenumber)


IF (Object_ID('tempdb..##warehouse_Z35') IS NOT NULL) DROP TABLE ##warehouse_Z35
set @sql = '
select * 
into ##warehouse_Z35
from OPENROWSET(''SQLOLEDB'', ''wmdb01''; ''wmadmin'' ; ''wm@dm1n'',
''
select 
	po_nbr,
	seq_nbr
from	
	wmprod.dbo.store_distro sd with (nolock)
where create_date_time between dateadd(hh,-3,getdate()) and getdate()
''
)'
-- print @sql
exec (@sql)

create index ix_warehouse_temp on ##warehouse_Z35(po_nbr, seq_nbr)

set nocount on

IF (Object_ID('tempdb..##missing_Z35') IS NOT NULL) DROP TABLE ##missing_Z35
select dt.*
into ##missing_Z35
from ##distro_transfers_Z35 dt
	left join ##warehouse_Z35 wh
	on wh.po_nbr = dt.documentnumber
	and wh.seq_nbr = dt.linenumber
where wh.seq_nbr is null
order by documentnumber, linenumber

if (select count(*) from ##missing_Z35) > 0
begin
	set @sql = 'select * from ##missing_Z35'

	declare @filename  varchar(100)
	declare @char_separator varchar(12)
	declare @message varchar(200)
	set @filename='MissingDistros.xls'
	set @char_separator = char(9)
	set @message = 'The attached list contains missing distros that should be in 980 that were placed in the last 3 hours'

	EXEC msdb.dbo.sp_send_dbmail 
 		@recipients = 'Databears@buildabear.com',
@message = @message, 
		@subject = 'Missing Distros in 980',
		@query_result_width = 500,
		@query = @sql,
		@attach_query_result_as_file = 1,
		@query_result_separator = @char_separator,
		@query_attachment_filename = @filename 
end
```

