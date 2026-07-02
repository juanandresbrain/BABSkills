# dbo.spMerchandisingSelect960LockTransfers

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMerchandisingSelect960LockTransfers"]
    dbo_tmp960LockTransfers(["dbo.tmp960LockTransfers"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tmp960LockTransfers |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spMerchandisingSelect960LockTransfers]

as

-- =====================================================================================================
-- Name: spMerchandisingSelect960LockTransfers
--
-- Description:	Creates a transfer document to import into Merchandising via the Pipeline. 
--				
--				 
-- Revision History
--		Name:			Date:			Comments:
--		Dan Tweedie		05/14/2015		Created proc.	
-- =====================================================================================================

set nocount on 

IF (Object_ID('tempdb..#lock') IS NOT NULL) DROP TABLE #lock
select *
into #lock
from tmp960LockTransfers
where description = 'Lock'

IF (Object_ID('tempdb..#unlock') IS NOT NULL) DROP TABLE #unlock
select *
into #unlock
from tmp960LockTransfers
where description = 'Unlock'

declare
		@dateparts varchar(10),
		@document varchar(20),
		@from varchar(4),
		@to varchar(4),
		@date varchar(12),
		@reason varchar(5),
		@grouping varchar(20),
		@carton varchar(20),
		@upc varchar(20),
		@send_units int,
		@totalLockStyles int,
		@totalUnlockStyles int

if (select count(*) from #lock) > 0

	BEGIN

	select @dateparts = cast(datepart(yyyy, getdate()) as varchar) + cast(datepart(mm, getdate()) as varchar) + cast(datepart(dd, getdate()) as varchar) + cast(datepart(mi, getdate()) as varchar)		
	select @document = '0960_1001_' + @dateparts
	select @from = '0960'
	select @to = '1001'
	select @date = convert(varchar, getdate(), 101)
	select @reason = 'CORR'
	select @grouping = 'DDC Locked'
	select @totalLockStyles = count(*) from #lock
	select @carton = right(('00000000009601001' + @dateparts), 20)

	print 'H' + '	'	+ 'A' +	'	'+ @document + '	' + '	' + '	' + @from + '	' + '	' + @to + '	' + '	' + '	' + '	' + '	' + @date + '	' + '	' + '	' + '	' + '	' + '	' + @reason + '	' + '	'+ '	' + '	' + @grouping + '	' + '	' + '	' + 'T'

	while @totalLockStyles > 0
		begin
			select @upc = max(style) from #lock
			select @send_units = abs_qty from #lock where style = @upc

			print 'D' + '	' + 'A' + '	' + @document + '	' + @carton + '	' + @upc + '	' + '	' + '	' + '	' + '	' + '	' + convert(varchar, @send_units)
	
			delete from #lock where style = @upc

			if (select count(*) from #lock) = 0
				break
			else
				continue
		end

	END

if (select count(*) from #unlock) > 0

	BEGIN

	select @dateparts = cast(datepart(yyyy, getdate()) as varchar) + cast(datepart(mm, getdate()) as varchar) + cast(datepart(dd, getdate()) as varchar) + cast(datepart(mi, getdate()) as varchar)		
	select @document = '1001_0960_' + @dateparts
	select @from = '1001'
	select @to = '0960'
	select @date = convert(varchar, getdate(), 101)
	select @reason = 'CORR'
	select @grouping = 'DDC UnLocked'
	select @totalLockStyles = count(*) from #Unlock
	select @carton = right(('00000000010010960' + @dateparts), 20)

	print 'H' + '	'	+ 'A' +	'	'+ @document + '	' + '	' + '	' + @from + '	' + '	' + @to + '	' + '	' + '	' + '	' + '	' + @date + '	' + '	' + '	' + '	' + '	' + '	' + @reason + '	' + '	'+ '	' + '	' + @grouping + '	' + '	' + '	' + 'T'

	while @totalLockStyles > 0
		begin
			select @upc = max(style) from #unlock
			select @send_units = abs_qty from #unlock where style = @upc

			print 'D' + '	' + 'A' + '	' + @document + '	' + @carton + '	' + @upc + '	' + '	' + '	' + '	' + '	' + '	' + convert(varchar, @send_units)
	
			delete from #unlock where style = @upc

			if (select count(*) from #unlock) = 0
				break
			else
				continue
		end

	END
```

