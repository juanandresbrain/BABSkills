# dbo.spMerchandisingImportCNTransfers

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMerchandisingImportCNTransfers"]
    dbo_entity_custom_property(["dbo.entity_custom_property"]) --> SP
    dbo_hierarchy_group(["dbo.hierarchy_group"]) --> SP
    dbo_style(["dbo.style"]) --> SP
    dbo_style_group(["dbo.style_group"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.entity_custom_property |
| dbo.hierarchy_group |
| dbo.style |
| dbo.style_group |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spMerchandisingImportCNTransfers]

as 

-- =====================================================================================================
-- Name: spMerchandisingImportCNTransfers
--
-- Description:	Bulk insert Transfer file from CN warehouse, stages data
--
-- Revision History
--		Name:			Date:			Comments:
--		Dan Tweedie		01/25/2016		Created proc.	
-- =====================================================================================================

set nocount on

--check the directory to see if there are distro CSV files ready to import
-------------do a DIR command and store the results in a temp table
IF (Object_ID('tempdb..#DIR') IS NOT NULL) DROP TABLE #DIR
create table #DIR (output varchar(1000))
insert #DIR exec master..xp_cmdshell 'dir \\kermode\FileRepository\MERCHANDISING\cn_distro\TRANSFERS\*.csv /B'
delete from #DIR where output is null or output = 'File Not Found'

------------query temp table to see if there are CSV files
if (select count(*) from #DIR) > 0
---find files with spaces in the name, rename to remove the spaces

BEGIN

		if (object_id('tempdb..#CNTRANSFER') is not null) drop table #CNTRANSFER
		create table #CNTRANSFER
		(from_location_code varchar(4),
		 transfer_no varchar(10),
		 to_location_code varchar(4),
		 shipped_date varchar(10),
		 style_code varchar(6),
		 qty int,
		 carton_no varchar(25))

			
		declare @files int,
				@filename varchar(100),
				@filepath varchar(100),
				@bulkinsert varchar(4000),
				@bulkinsertArchive varchar(4000),
				@del varchar(100),
				@move varchar(1000),
				@query varchar(1000),
				@file_name varchar(100),
				@file_location varchar(100),
				@server varchar(20),
				@database varchar(20),
				@bcp varchar(1000),
				@timestamp varchar(52),
				@rename varchar(1000),
				@nameage varchar(104),
				@documentNumber varchar(9)

		select @filepath = '\\kermode\FileRepository\MERCHANDISING\cn_distro\TRANSFERS\'
		select @files = count(*) from #dir
		
		
---------Bulk Insert Loop
		while @files > 0
			begin
			    select @timestamp = replace( ( convert(varchar, getdate(), 112) + convert(varchar, getdate(), 114) ), ':', '')
				select @filename = max(output) from #dir
								
				select @bulkinsert = 'bulk insert #CNTRANSFER from ''' + @filepath + @filename + ''' with (FIELDTERMINATOR = '','', ROWTERMINATOR = ''\n'')'
				exec (@bulkinsert)
				
				select @rename = 'ren ' + @filepath + @filename + ' ' + @filename + '.' + @timestamp + '.csv'
				exec master..xp_cmdshell @rename
				
				select @move = 'move ' + @filepath + @filename + '.' + @timestamp + '.csv' + ' \\kermode\FileRepository\MERCHANDISING\cn_distro\TRANSFERS\Done\'
		        exec master..xp_cmdshell @move
				
				delete from #dir where output = @filename
				select @files = count(*) from #dir
								
				if @files < 1
					break
				else
					continue
			end


	if (object_id('me_01..tmpCNTransferImport') is not null) drop table tmpCNTransferImport;
	WITH 
	Transfers (from_location_code, transfer_no, to_location_code, shipped_date, style_code, qty, carton_no)
		as (
			select u.from_location_code, u.transfer_no, u.to_location_code, u.shipped_date, u.style_code, u.carton_no,
			case when ecp.custom_property_value is not null and substring(hg.hierarchy_group_code,7,2)='60'
					then (u.qty / ecp.custom_property_value)
					else u.qty
				end as qty
			from #CNTRANSFER u
			join style s (nolock) on u.style_code = s.style_code
			join style_group sg (nolock) on s.style_id = sg.style_id
			join hierarchy_group hg (nolock) on hg.hierarchy_group_id = sg.hierarchy_group_id
			left join entity_custom_property ecp (nolock) on ecp.parent_id = s.style_id
				and ecp.custom_property_id = 2 -- FRCSTM
				and	parent_type = 1
		   )
	select from_location_code, transfer_no, to_location_code, shipped_date, style_code, sum(qty), carton_no
	into tmpCNTransferImport
	from Transfers
	group by from_location_code, transfer_no, to_location_code, shipped_date, style_code, carton_no
	   

	---generate transfer file for pipeline
	declare @query1 varchar(1000),
			@file_location1 varchar(100),
			@file_name1 varchar(100),
			@server1 varchar(52),
			@database1 varchar(52),
			@username1 varchar(52),
			@password1 varchar(52),
			@sqlcmd varchar(1000)

	
	set @query1 = 'set nocount on exec spMerchandisingOutputCNTransfers'
	set @file_location1 = '\\pipeapp01\Company01\Text File to IM Import Tables - Import Outbound Xfers\'
	set @file_name1 = 'STSIMOUTBOUNDTRANSFER.CN.' + @timestamp + '.GO'
	set @server1 = 'bedrockdb02'
	set @database1 = 'me_01'
	set @sqlcmd = 'sqlcmd -S' + @server1 + ' -d' + @database1 + ' -Q' + '"' + @query1 + '"' + ' -o' + '"' + @file_location1 + @file_name1 + '"' + ' -s"," -w100 -W'
	exec master..xp_cmdshell @sqlcmd


END
```

