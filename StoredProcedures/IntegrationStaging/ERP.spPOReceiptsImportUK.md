# ERP.spPOReceiptsImportUK

**Database:** IntegrationStaging  

## Architecture Diagram

```mermaid
flowchart LR
    SP["ERP.spPOReceiptsImportUK"]
    ERP_PurchaseOrderReceiptPreStage(["ERP.PurchaseOrderReceiptPreStage"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| ERP.PurchaseOrderReceiptPreStage |

## Stored Procedure Code

```sql
CREATE proc [ERP].[spPOReceiptsImportUK]
as 

-- =====================================================================================================
-- Name: ERP.spPOReceiptsImportUK
--
-- Description:	Bulk insert PO receipt file from UK warehouse and stage data
--
-- Input: \\stl-ssis-p-01\IntegrationStaging\3PW\uk_distro\RECEIPTS\
--
-- Revision History
--		Name:			Date:			Comments:
--		Lizzy Timm		03/03/2025		Created proc. based on bedrockdb02.me_01.spMerchandisingSelectUKPOReceipts
-- =====================================================================================================

set nocount on

--check the directory to see if there are distro CSV files ready to import
-------------do a DIR command and store the results in a temp table
IF (Object_ID('tempdb..#DIR') IS NOT NULL) DROP TABLE #DIR
create table #DIR (output varchar(1000))
insert #DIR exec master..xp_cmdshell 'dir \\stl-ssis-p-01\IntegrationStaging\3PW\uk_distro\RECEIPTS\*.dat /B'
delete from #DIR where output is null or output = 'File Not Found'

------------query temp table to see if there are CSV files
if (select count(*) from #DIR) > 0
---find files with spaces in the name, rename to remove the spaces

BEGIN

		if (object_id('tempdb..#UKPOR') is not null) drop table #UKPOR
		create table #UKPOR
		(receipt_date smalldatetime,
		po_no varchar(52),
		style_code varchar(52),
		qty int,
		dam int)

			
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

		select @filepath = '\\stl-ssis-p-01\IntegrationStaging\3PW\uk_distro\RECEIPTS\'
		select @files = count(*) from #dir
		
		
---------Bulk Insert Loop
		while @files > 0
			begin
			    select @timestamp = cast(datepart(yyyy, getdate()) as varchar) + cast(datepart(mm, getdate()) as varchar) + cast(datepart(dd, getdate()) as varchar) + cast(datepart(hh, getdate()) as varchar) + cast(datepart(mi, getdate()) as varchar) + cast(datepart(ss, getdate()) as varchar)
				select @filename = max(output) from #dir
								
				select @bulkinsert = 'set language ''British'' bulk insert #UKPOR from ''' + @filepath + @filename + ''' with (FIELDTERMINATOR = '','', ROWTERMINATOR = ''\n'')'
				exec (@bulkinsert)
				
				select @rename = 'ren ' + @filepath + @filename + ' ' + @filename + '.' + @timestamp + '.DAT'
				exec master..xp_cmdshell @rename
				
				select @move = 'move ' + @filepath + @filename + '.' + @timestamp + '.dat' + ' \\stl-ssis-p-01\IntegrationStaging\3PW\uk_distro\RECEIPTS\Done\'
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
				if (select count(*) from #UKPOR) > 0
					begin
						insert ERP.PurchaseOrderReceiptPreStage 
						select 
							po_no as PurchaseOrderNumber,
							'9970' as ReceiptLocation,
							cast(receipt_date as date) as ReceiptDate, 
							style_code as ItemID,
							sum(qty) as Qty,
							getdate(),
							'2110' as Entity
						from #UKPOR
						group by po_no, cast(receipt_date as date), style_code
					end
			--------------------------------------------------------
END
```

