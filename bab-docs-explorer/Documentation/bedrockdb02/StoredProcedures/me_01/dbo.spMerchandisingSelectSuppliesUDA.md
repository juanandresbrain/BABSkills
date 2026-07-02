# dbo.spMerchandisingSelectSuppliesUDA

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMerchandisingSelectSuppliesUDA"]
    dbo_UDASuppliesSold(["dbo.UDASuppliesSold"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.UDASuppliesSold |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spMerchandisingSelectSuppliesUDA]

as

-- =====================================================================================================
-- Name: spMerchandisingSelectSuppliesUDA
--
-- Description:	Outputs data in format for UDA file for Pipeline
--
-- Revision History
--		Name:			Date:			Comments:
--		Dan Tweedie		04/13/2015		Created proc
-- =====================================================================================================

set nocount on 


declare @date varchar(12),
		@location varchar(4),
		@upc varchar(12),
		@units varchar(100),
		@cost varchar(52),
		@locationCost varchar(52),
		@total int

select @date = convert(varchar, getdate(), 101)
select @total = count(*) from UDASuppliesSold 

print 'H' + '	' + 'A' + '	' + '' + '	' + @date + '	' + 'SLSPY' + '	' + 'UDA Upload' + '	' + 'SUPPLIES SOLD' + '	' + '3' + '	' + ''

while @total > 0
	BEGIN
		
		select @location = max(location_code) from UDASuppliesSold
		select @upc = max(upc) from UDASuppliesSold where location_code = @location
		select @units = units from UDASuppliesSold where location_code = @location and upc = @upc
		select @cost = cost from UDASuppliesSold where location_code = @location and upc = @upc
		select @LocationCost = locationCost from UDASuppliesSold where location_code = @location and upc = @upc

		print 'D' + '	' + 'A' + '	' + '' + '	' + 'S' + '	' + @location + '	' + @upc +  '	' +  '	' +  '	' +  '	' +  '	' + '	' + @units + '	' + @cost + '	' + @locationCost		
		
		delete from UDASuppliesSold where location_code = @location and upc = @upc
		
		select @total = count(*) from UDASuppliesSold 

		if @total = 0
			break
		else
			continue
	END
```

