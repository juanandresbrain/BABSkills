# dbo.spMerchandisingSelectFranchiseeUDA

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMerchandisingSelectFranchiseeUDA"]
    dbo_FranchiseeUDA(["dbo.FranchiseeUDA"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.FranchiseeUDA |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spMerchandisingSelectFranchiseeUDA]

as 

-- =====================================================================================================
-- Name: spMerchandisingSelectFranchiseeUDA
--
-- Description:	Outputs data in format for UDA file for Pipeline
--
-- Revision History
--		Name:			Date:			Comments:
--		Dan Tweedie		04/07/2015		Created proc
--		Dan Tweedie		06/10/2015		Added blank column to end of detail row per epicor's new spec
-- =====================================================================================================

set nocount on



declare @date varchar(12),
		@location varchar(4),
		@upc varchar(12),
		@units varchar(100),
		@total int

select @date = convert(varchar, getdate(), 101)
select @total = count(*) from FranchiseeUDA 

print 'H' + '	' + 'A' + '	' + '' + '	' + @date + '	' + 'INTNL' + '	' + 'UDA Upload' + '	' + 'FRANCHISEES' + '	' + '3' + '	' + ''

while @total > 0
	BEGIN
		
		select @location = max(location_code) from FranchiseeUDA
		select @upc = max(upc) from FranchiseeUDA where location_code = @location
		select @units = units from FranchiseeUDA where location_code = @location and upc = @upc

		print 'D' + '	' + 'A' + '	' + '' + '	' + 'S' + '	' + @location + '	' + @upc +  '	' +  '	' +  '	' +  '	' +  '	' + '	' + @units + '	'  + '	'
		
		delete from FranchiseeUDA where location_code = @location and upc = @upc
		
		select @total = count(*) from FranchiseeUDA 

		if @total = 0
			break
		else
			continue
	END
```

