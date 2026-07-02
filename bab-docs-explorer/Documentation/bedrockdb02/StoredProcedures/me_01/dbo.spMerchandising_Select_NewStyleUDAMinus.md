# dbo.spMerchandising_Select_NewStyleUDAMinus

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMerchandising_Select_NewStyleUDAMinus"]
    dbo_styles_uda(["dbo.styles_uda"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.styles_uda |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spMerchandising_Select_NewStyleUDAMinus]
-- =====================================================================================================
-- Name: spMerchandising_Select_NewStyleUDAMinus
--
-- Description:	Captures data for new styles, printed per Epicor's User Defined Adjustment file layout spec.
--
--
-- Input:	NA
--			
--
-- Output: Resultset formatted to meet Epicor requirements for User Defined Adjustment file.
--			
--
-- Dependencies: spMerchandising_Report_NewStyleUDA
--				 spMerchandising_Select_NewStyleUDAPlus
--				 
--
-- Revision History
--		Name:			Date:			Comments:
--		Dan Tweedie		05/27/2010		Created proc.	
--		Dan Tweedie		06/10/2015		Added blank field at end of detail row for epicor's new spec
-- =====================================================================================================
as 
set nocount on
declare @date varchar(12),
		@counter int,
		@total int,
		@recordtype varchar(1),
		@action_type varchar(1),
		@docnbr varchar(52),
		@recordtype2 varchar(1),
		@location varchar(4),
		@upc varchar(12),
		@units varchar(2)

set @date = convert(varchar, getdate(), 101)
set @counter = 1
select @total = count(distinct style) from styles_uda
select @docnbr = convert(varchar, datestamp) + convert(varchar, id) + 'B' from styles_uda
				
declare style cursor for 
						select ('000000' + style)
						from styles_uda
						order by style

print 'H' + '	' + 'A' + '	' + convert(varchar, @docnbr) + '	' + @date + '	' + 'U' + '	' + 'MerchAdmin' + '	' + 'NewStyle' + '	' + '3' + '	' + 'NewStyleUDAProc'

					
open style

	while @counter <= @total

		begin
			fetch next from style into @upc
	
			print 'D' + '	' + 'A' + '	' + convert(varchar, @docnbr) + '	' + 'S' + '	' + '9990' + '	' + @upc +  '	' +  '	' +  '	' +  '	' +  '	' + '	' + '-1' + '	'  + '	' 
							
			set @counter = @counter + 1

		end	

close style
deallocate style
```

