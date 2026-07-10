# dbo.spFranchiseeFilesImportFileCheck

**Database:** DWStaging  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spFranchiseeFilesImportFileCheck"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## Stored Procedure Code

```sql
CREATE proc [dbo].[spFranchiseeFilesImportFileCheck]
@franchisee varchar(2)

as

-- =====================================================================================================
-- Name: spFranchiseeFilesImportFileCheck
--
--Description: Captures existence of files ready to be imported into DWStaging
-- Revision History
--		Name:			Date:			Comments:
--		Dan Tweedie		11/15/2015		Created proc.	
-- =====================================================================================================
set nocount on

declare @dir varchar(1000)
select @dir = 'dir \\ftp01\files\International\MerchData\' + @franchisee + '\*.csv /B'

IF (Object_ID('tempdb..#dir') IS NOT NULL) DROP TABLE #dir
create table #dir
(DIR nvarchar(max) )
	
Insert #dir
exec master..xp_cmdshell @dir 
delete from #dir where DIR is null or DIR = 'File Not Found'

-- =====================================================================================================
Declare @TransactionHeader int,
		@TransactionPayment int,
		@TransactionMerchandise int,
		@TransactionGiftCard int,
		@Inventory int,
		@PurchaseOrder int,
		@SalesPlan int,
		@FileCount varchar(1000)

select @TransactionHeader = case when exists (select DIR from #dir where DIR = 'TransactionHeader.csv') then 1 else 0 end 
select @TransactionPayment = case when exists (select DIR from #dir where DIR = 'TransactionPayment.csv') then 1 else 0 end 
select @TransactionMerchandise = case when exists (select DIR from #dir where DIR = 'TransactionMerchandise.csv') then 1 else 0 end 
select @TransactionGiftCard = case when exists (select DIR from #dir where DIR = 'TransactionGiftCard.csv') then 1 else 0 end 
select @Inventory = case when exists (select DIR from #dir where DIR = 'Inventory.csv') then 1 else 0 end 
select @PurchaseOrder = case when exists (select DIR from #dir where DIR = 'PurchaseOrder.csv') then 1 else 0 end 
select @SalesPlan = case when exists (select DIR from #dir where DIR = 'SalesPlan.csv') then 1 else 0 end 
select @FileCount = @TransactionHeader + @TransactionPayment + @TransactionMerchandise + @TransactionGiftCard + @Inventory + @PurchaseOrder + @SalesPlan

select @TransactionHeader as TransactionHeader,
	   @TransactionPayment as TransactionPayment,
	   @TransactionMerchandise as TransactionMerchandise,
	   @TransactionGiftCard as TransactionGiftCard,
	   @Inventory as Inventory,
	   @PurchaseOrder as PurchaseOrder,
	   @SalesPlan as SalesPlan,
	   @FileCount as FileCount
```

