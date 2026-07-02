# dbo.spMerchandisingOutputUKPOReceipts

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMerchandisingOutputUKPOReceipts"]
    dbo_tmpUKPOReceiptImport(["dbo.tmpUKPOReceiptImport"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tmpUKPOReceiptImport |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spMerchandisingOutputUKPOReceipts]

as 

-- =====================================================================================================
-- Name: spMerchandisingOutputUKPOReceipts
--
-- Description:	Produces PO Receipt file, based on data provided in file from UK Warehouse.
--				Note, special handling since the UK original file contains UK date format (DD/MM/YYYY)
--
-- Input: NA
--
-- Output: Resultset formatted to meet Epicor requirements for PO Receipt Import.
--
-- Revision History
--		Name:			Date:			Comments:
--		Dan Tweedie		09/05/2013		Created proc.	
-- =====================================================================================================

set nocount on

---prepare data for printing po receipt file
declare @date varchar(12),
		@counterH int,
		@counterD int,
		@totalH int,
		@totalD int,
		@docnbr varchar(20),
		@po varchar(20),
		@UPC varchar(12),
		@Rcvd_Units int,
		@dmg_units int

select @totalH = count(distinct (convert(varchar, receipt_date, 112)+po_no)) from tmpUKPOReceiptImport
set @counterH = 1

declare header cursor for
	select convert(varchar, receipt_date, 101), convert(varchar, receipt_date, 112) + po_no, po_no
	from tmpUKPOReceiptImport
	group by receipt_date, convert(varchar, receipt_date, 112) + po_no, po_no
	order by receipt_date, convert(varchar, receipt_date, 112) + po_no, po_no

open header
while @counterH <= @totalH
	begin
		fetch next from header into @date, @docnbr, @po
		print 'H' + '	' + 'A' + '	' + @docnbr + '	' + '	' + @date + '	' + '2970' + '	' + @po + '	' + 'Administrator' + '	' + '	' + '	' + '	' + '	' + '	' + '	' + '	' + '	' + '	' + '	' + '	' + '	' + '	' + '	' + '	' + 'N' + '	'
			--detail cursor
				set @counterD = 1
				select @totalD = count(style_code) from tmpUKPOReceiptImport where po_no = @po and convert(varchar, receipt_date, 112) + po_no = @docnbr and convert(varchar, receipt_date, 101) = @date
												
				declare detail cursor for
					select style_code, qty, dam
					from tmpUKPOReceiptImport
					where po_no = @po and convert(varchar, receipt_date, 112) + po_no = @docnbr and convert(varchar, receipt_date, 101) = @date
					order by style_code
				
				open detail
				while @counterD <= @totalD
					begin
						fetch next from detail into @upc, @rcvd_units, @dmg_units
						print 'D' + '	' + 'A' + '	' + @docnbr + '	' + '	' + @upc + '	' + + '	' +  + '	' +  + '	' +  + '	' +  + '	' +  convert(varchar, @rcvd_units) + '	' + convert(varchar, @dmg_units)
						set @counterD = @counterD + 1
					end
				close detail
				deallocate detail
		
		set @counterH = @counterH + 1

	end

close header
deallocate header
```

