# dbo.spMerchandisingOutputWhseInventoryShrink

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMerchandisingOutputWhseInventoryShrink"]
    dbo_tmpWhseInventoryShrink(["dbo.tmpWhseInventoryShrink"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tmpWhseInventoryShrink |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spMerchandisingOutputWhseInventoryShrink]
as
-- =====================================================================================================
-- Name: spMerchandisingOutputWhseInventoryShrink
--
-- Description:	Compares inventory by whse/style in merch versus data provided by warehouses, outputs difference
--
-- Input: N/A
--
-- Output: shrink file output to \\pipeapp01\E$\Company01\Text File to IM Import Tables- Import Shrink Adj
--
-- Dependencies: 
--
-- Revision History
--		Name:			Date:			Comments:
--		Dan Tweedie		04/02/2012		Created proc.	
--		Lizzy Timm		06/20/2023		Modified shrink type from 1 to 2 on header line
-- =====================================================================================================


begin
set nocount on

declare @whses int,
		@styles int,
		@whse varchar(4),
		@style varchar(6),
		@upc varchar(12),
		@qty int,
		@date varchar(20),
		@datetext varchar(10),
		@doc varchar(20)

select @date = convert(varchar, getdate(), 101)
select @datetext = cast(datepart(yyyy, getdate())as varchar) + cast(datepart(mm, getdate())as varchar) + cast(datepart(dd, getdate())as varchar)

select @whses = count(distinct location_code) from tmpWhseInventoryShrink
while @whses > 0
begin
	select @whse = min(location_code) from tmpWhseInventoryShrink
	select @doc = @datetext + @whse
	print 'H	A	' + @doc + '	' + @date + '	2	Nightly Sync	Nightly Sync	3	WhseSyncFile'
	select @styles = count(style_code) from tmpWhseInventoryShrink where location_code = @whse
	while @styles > 0
	begin
		select @style = min(style_code) from tmpWhseInventoryShrink where location_code = @whse
		select @upc = '000000' + @style from tmpWhseInventoryShrink where location_code = @whse
		select @qty = shrinkqty_distribution_multiple from tmpWhseInventoryShrink where location_code = @whse and style_code = @style
		print 'D	A	' + @doc + '	' + @whse + '	' + @upc + '					' + convert(varchar, @qty)
		delete from tmpWhseInventoryShrink where location_code = @whse and style_code = @style
		select @styles = count(style_code) from tmpWhseInventoryShrink where location_code = @whse
		if @style < 1
			break
				else
			continue
	end
    select @whses = count(distinct location_code) from tmpWhseInventoryShrink
	if @whse < 1
		break
			else
		continue

end		
		
end
```

