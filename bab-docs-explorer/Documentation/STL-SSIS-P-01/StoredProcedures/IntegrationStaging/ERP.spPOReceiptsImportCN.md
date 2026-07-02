# ERP.spPOReceiptsImportCN

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["ERP.spPOReceiptsImportCN"]
    ERP_PurchaseOrderReceiptPreStage(["ERP.PurchaseOrderReceiptPreStage"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| ERP.PurchaseOrderReceiptPreStage |

## Stored Procedure Code

```sql
CREATE proc [ERP].[spPOReceiptsImportCN]
as 

-- =====================================================================================================
-- Name: ERP.spPOReceiptsImportCN
--
-- Description:	Bulk insert PO receipt file from CN warehouse and stage data
--
-- Input: \\stl-ssis-p-01\IntegrationStaging\3PW\CN_Distro\INBOUND\RECEIPTS\
--
-- Revision History
--		Name:			Date:			Comments:
--		Lizzy Timm		03/03/2025		Created proc. based on bedrockdb02.me_01.spMerchandisingImportCNPOReceipts
-- =====================================================================================================

set nocount on

--check the directory to see if there are distro CSV files ready to import
-------------do a DIR command and store the results in a temp table
IF (Object_ID('tempdb..#DIR') IS NOT NULL) DROP TABLE #DIR
create table #DIR (output varchar(1000))
insert #DIR exec master..xp_cmdshell 'dir \\stl-ssis-p-01\IntegrationStaging\3PW\CN_Distro\INBOUND\RECEIPTS\*.csv /B'
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

		select @filepath = '\\stl-ssis-p-01\IntegrationStaging\3PW\CN_Distro\INBOUND\RECEIPTS\'
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
				
				select @move = 'move ' + @filepath + @filename + '.' + @timestamp + '.csv' + ' \\stl-ssis-p-01\IntegrationStaging\3PW\CN_Distro\INBOUND\RECEIPTS\Done\'
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
						insert ERP.PurchaseOrderReceiptPreStage 
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
END
```

