# dbo.spMerchandisingOutputnNonWhseInventoryShrinkBatched

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMerchandisingOutputnNonWhseInventoryShrinkBatched"]
    dbo_tmpNightlyNonWhseInventoryShrink(["dbo.tmpNightlyNonWhseInventoryShrink"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tmpNightlyNonWhseInventoryShrink |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spMerchandisingOutputnNonWhseInventoryShrinkBatched]
@LocationCodeStart int ,
@LocationCodeEnd int 
as

-- =====================================================================================================
-- Name: spMerchandisingOutputnNonWhseInventoryShrink
--
-- Description:	Compares inventory by whse/style in merch versus data provided by stores from Dynamics, outputs difference
--
--
-- Revision History
--		Name:			Date:			Comments:
--		Dan Tweedie		2022-07-06		Created proc.	
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

select @whses = count(distinct location_code) from tmpNightlyNonWhseInventoryShrink where location_code between @LocationCodeStart and @LocationCodeEnd
while @whses > 0
begin
	select @whse = min(location_code) from tmpNightlyNonWhseInventoryShrink where location_code between @LocationCodeStart and @LocationCodeEnd
	select @doc = @datetext + @whse
	print 'H	A	' + @doc + '	' + @date + '	2	Nightly Sync	Nightly Sync	3	WhseSyncFile'
	select @styles = count(style_code) from tmpNightlyNonWhseInventoryShrink where location_code = @whse
	while @styles > 0
	begin
		select @style = min(style_code) from tmpNightlyNonWhseInventoryShrink where location_code = @whse
		select @upc = '000000' + @style from tmpNightlyNonWhseInventoryShrink where location_code = @whse
		select @qty = shrinkqty_distribution_multiple from tmpNightlyNonWhseInventoryShrink where location_code = @whse and style_code = @style
		print 'D	A	' + @doc + '	' + @whse + '	' + @upc + '					' + convert(varchar, @qty)
		delete from tmpNightlyNonWhseInventoryShrink where location_code = @whse and style_code = @style
		select @styles = count(style_code) from tmpNightlyNonWhseInventoryShrink where location_code = @whse
		if @style < 1
			break
				else
			continue
	end
    select @whses = count(distinct location_code) from tmpNightlyNonWhseInventoryShrink where location_code between @LocationCodeStart and @LocationCodeEnd
	if @whse < 1
		break
			else
		continue

end		
		
end
```

