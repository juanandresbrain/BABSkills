# dbo.spMerchandisingOutputCNPOReceipts

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMerchandisingOutputCNPOReceipts"]
    dbo_tmpCNPOReceiptImport(["dbo.tmpCNPOReceiptImport"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tmpCNPOReceiptImport |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spMerchandisingOutputCNPOReceipts]

as 

-- =====================================================================================================
-- Name: spMerchandisingOutputCNPOReceipts
--
-- Description:	Produces PO Receipt file, based on data provided in file from CN Warehouse.
--				Uses a cursor, but datasets will always be small and run in a matter of seconds!
-- Revision History
--		Name:			Date:			Comments:
--		Dan Tweedie		01/21/2016		Created proc.	
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
		@dmg_units int,
		@location varchar(4)

select @totalH = count(distinct (convert(varchar, receipt_date, 112)+po_no)) from tmpCNPOReceiptImport
set @counterH = 1

declare header cursor for 
	select location_code, convert(varchar, receipt_date, 101), convert(varchar, receipt_date, 112) + po_no, po_no
	from tmpCNPOReceiptImport
	group by location_code, receipt_date, convert(varchar, receipt_date, 112) + po_no, po_no
	order by receipt_date, convert(varchar, receipt_date, 112) + po_no, po_no

open header
while @counterH <= @totalH
	begin
		fetch next from header into @location, @date, @docnbr, @po
		print 'H' + '	' + 'A' + '	' + @docnbr + '	' + '	' + @date + '	' + @location + '	' + @po + '	' + 'Administrator' + '	' + '	' + '	' + '	' + '	' + '	' + '	' + '	' + '	' + '	' + '	' + '	' + '	' + '	' + '	' + '	' + 'N' + '	'
			--detail cursor
				set @counterD = 1
				select @totalD = count(style_code) from tmpCNPOReceiptImport where location_code = @location and po_no = @po and convert(varchar, receipt_date, 112) + po_no = @docnbr and convert(varchar, receipt_date, 101) = @date
												
				declare detail cursor for
					select style_code, qty, dam
					from tmpCNPOReceiptImport
					where location_code = @location and po_no = @po and convert(varchar, receipt_date, 112) + po_no = @docnbr and convert(varchar, receipt_date, 101) = @date
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

