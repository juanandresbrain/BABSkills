# dbo.spMerchandisingImportCNPOReceipts

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMerchandisingImportCNPOReceipts"]
    dbo_D365_PurchaseOrderReceiptStage(["dbo.D365_PurchaseOrderReceiptStage"]) --> SP
    dbo_entity_custom_property(["dbo.entity_custom_property"]) --> SP
    dbo_hierarchy_group(["dbo.hierarchy_group"]) --> SP
    dbo_style(["dbo.style"]) --> SP
    dbo_style_group(["dbo.style_group"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.D365_PurchaseOrderReceiptStage |
| dbo.entity_custom_property |
| dbo.hierarchy_group |
| dbo.style |
| dbo.style_group |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spMerchandisingImportCNPOReceipts]

as 

-- =====================================================================================================
-- Name: spMerchandisingImportCNPOReceipts
--
-- Description:	Bulk insert PO receipt file from CN warehouse, stages data, calls another proc to output the pipeline file
--
-- Revision History
--		Name:			Date:			Comments:
--		Dan Tweedie		01/21/2016		Created proc.
--		Keith Lee		03/24/2016		Fixed file path on kermode.
--		Dan Tweedie		2017-11-21		Added statement to insert PO Receipts data into D365_PurchaseOrderReceiptStage so another process can integrate to D365 as needed
--		Tim Callahan	06/28/2018		Added statement to remove D365 PO receipt date from staging table, otherwise these receipts would bomb out in Merch\Pipeline 
--		Lizzy Timm		01/09/2025		Added bonded China Warehouses 9942 to be included
-- =====================================================================================================

set nocount on

--check the directory to see if there are distro CSV files ready to import
-------------do a DIR command and store the results in a temp table
IF (Object_ID('tempdb..#DIR') IS NOT NULL) DROP TABLE #DIR
create table #DIR (output varchar(1000))
insert #DIR exec master..xp_cmdshell 'dir \\kermode\FileRepository\MERCHANDISING\CN_Distro\INBOUND\RECEIPTS\*.csv /B'
delete from #DIR where output is null or output = 'File Not Found'

------------query temp table to see if there are CSV files
if (select count(*) from #DIR) > 0
---find files with spaces in the name, rename to remove the spaces

BEGIN

		if (object_id('tempdb..#CNPOR') is not null) drop table #CNPOR
		create table #CNPOR
		(location_code varchar(4),
		 receipt_date varchar(10),
		 po_no varchar(20),
		 style_code varchar(6),
		 qty int)

			
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

		select @filepath = '\\kermode\FileRepository\MERCHANDISING\CN_Distro\INBOUND\RECEIPTS\'
		select @files = count(*) from #dir
		
		
---------Bulk Insert Loop
		while @files > 0
			begin
			    select @timestamp = replace( ( convert(varchar, getdate(), 112) + convert(varchar, getdate(), 114) ), ':', '')
				select @filename = max(output) from #dir
								
				select @bulkinsert = 'bulk insert #CNPOR from ''' + @filepath + @filename + ''' with (FIELDTERMINATOR = '','', ROWTERMINATOR = ''\n'')'
				exec (@bulkinsert)
				
				select @rename = 'ren ' + @filepath + @filename + ' ' + @filename + '.' + @timestamp + '.csv'
				exec master..xp_cmdshell @rename
				
				select @move = 'move ' + @filepath + @filename + '.' + @timestamp + '.csv' + ' \\kermode\FileRepository\MERCHANDISING\CN_Distro\INBOUND\RECEIPTS\Done\'
		        exec master..xp_cmdshell @move
				
				delete from #dir where output = @filename
				select @files = count(*) from #dir
								
				if @files < 1
					break
				else
					continue
			end


			--------------------------------------------------------
			--Added 2017-11-21
			if (select count(*) from #CNPOR) > 0
					begin
						insert D365_PurchaseOrderReceiptStage 
						select 
							po_no as PurchaseOrderNumber,
							case 
								when location_code = '3970' then '9940' 
								when location_code = '3980' then '9941'
								else location_code
							end as ReceiptLocation,
							cast(receipt_date as date) as ReceiptDate, 
							style_code as ItemID,
							sum(qty) as Qty,
							getdate(),
							case when location_code IN ('3980','9942') then '1200' else '3001' end as Entity
						from #CNPOR
						group by po_no, location_code, cast(receipt_date as date), style_code
					end


-- Aded 06/28/2018 to remove D365 PO receipt data after captured above 
	
	delete 
	from #CNPOR
	where po_no like 'PO%' 


		
---convert qty for supplies - stage into holding table
if (object_id('me_01..tmpCNPOReceiptImport') is not null) drop table tmpCNPOReceiptImport;
WITH 
Receipts (location_code, receipt_date, po_no, style_code, qty, dam)
	as (
		select u.location_code, u.receipt_date, u.po_no, right(('000000000000' + u.style_code),12) style_code, 
		case when ecp.custom_property_value is not null and substring(hg.hierarchy_group_code,7,2)='60'
				then (u.qty / ecp.custom_property_value)
				else u.qty
			end as qty,
			'0' as dam
		from #CNPOR u
		join style s (nolock) on u.style_code = s.style_code
		join style_group sg (nolock) on s.style_id = sg.style_id
		join hierarchy_group hg (nolock) on hg.hierarchy_group_id = sg.hierarchy_group_id
		left join entity_custom_property ecp (nolock) on ecp.parent_id = s.style_id
			and ecp.custom_property_id = 2 -- FRCSTM
			and	parent_type = 1
	   )
select location_code, convert(date,receipt_date) as receipt_date, po_no, style_code, sum(qty) qty, dam
into tmpCNPOReceiptImport
from Receipts
group by location_code,receipt_date, po_no, style_code, dam
	   

---generate po receipt file for pipeline
declare @query1 varchar(1000),
		@file_location1 varchar(100),
		@file_name1 varchar(100),
		@server1 varchar(52),
		@database1 varchar(52),
		@username1 varchar(52),
		@password1 varchar(52),
		@sqlcmd varchar(1000)

	
set @query1 = 'set nocount on exec spMerchandisingOutputCNPOReceipts'
set @file_location1 = '\\pipeapp01\Company01\Text File to IM - Import PO Receipts\'
set @file_name1 = 'STSIMPORECEIPT.CN.' + @timestamp + '.GO'
set @server1 = 'bedrockdb02'
set @database1 = 'me_01'
set @sqlcmd = 'sqlcmd -S' + @server1 + ' -d' + @database1 + ' -Q' + '"' + @query1 + '"' + ' -o' + '"' + @file_location1 + @file_name1 + '"' + ' -s"," -w100 -W'
exec master..xp_cmdshell @sqlcmd


END
```

