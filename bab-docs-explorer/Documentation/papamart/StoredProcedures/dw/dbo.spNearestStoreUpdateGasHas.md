# dbo.spNearestStoreUpdateGasHas

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spNearestStoreUpdateGasHas"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[spNearestStoreUpdateGasHas] AS 
-- **********************************************************************************************************
-- **********************************************************************************************************
-- **********************************************************************************************************

-- get the nearest stores for each country's postal_code
IF (Object_ID('tempdb..#us_ca_current') IS NOT NULL) DROP TABLE #us_ca_current
select h.postal_code, h.store_key, s.latitude, s.longitude, round(dw.dbo.fnCalcDistance(s.latitude, s.longitude, c.lat, c.lon),0) distance
into #us_ca_current
from tblZipTop1_historical_us_ca h
	join store_dim s
	on s.store_key = h.store_key
	join dw..tblUSCANzipsCombined c
	on c.zip = h.postal_code
where date_key = 
(
	select max(date_key) from tblZipTop1_historical_us_ca
	where date_key <= (
		select date_key
		from date_dim
		where actual_date = cast(convert(varchar, getdate(),101) as datetime))
)
create index ix_us_ca_current on #us_ca_current(postal_code)

IF (Object_ID('tempdb..#us_ca_future') IS NOT NULL) DROP TABLE #us_ca_future
select h.postal_code, h.store_key, s.latitude, s.longitude, round(dw.dbo.fnCalcDistance(s.latitude, s.longitude, c.lat, c.lon),0) distance
into #us_ca_future
from tblZipTop1_historical_us_ca h
	join store_dim s
	on s.store_key = h.store_key
	join dw..tblUSCANzipsCombined c
	on c.zip = h.postal_code
where date_key = 
(
	select max(date_key) from tblZipTop1_historical_us_ca
	where date_key <= (
		select date_key
		from date_dim
		where actual_date = cast(convert(varchar, dateadd(ww, 6, getdate()),101) as datetime))
)
create index ix_us_ca_future on #us_ca_future(postal_code)

-- **********************************************************************************************************
-- **********************************************************************************************************
-- **********************************************************************************************************

IF (Object_ID('tempdb..#gb_current') IS NOT NULL) DROP TABLE #gb_current
select h.postal_code, h.store_key, s.latitude, s.longitude, round(dw.dbo.fnCalcDistance(s.latitude, s.longitude, c.lat, c.lon),0) distance
into #gb_current
from tblZipTop1_historical_gb h
	join store_dim s
	on s.store_key = h.store_key
	join dw..tblUKPostalCodes_centroids c
	on c.postcode = h.postal_code
where date_key = 
(
	select max(date_key) from tblZipTop1_historical_gb
	where date_key <= (
		select date_key
		from date_dim
		where actual_date = cast(convert(varchar, getdate(),101) as datetime))
)
create index ix_gb_current on #gb_current(postal_code)

IF (Object_ID('tempdb..#gb_future') IS NOT NULL) DROP TABLE #gb_future
select h.postal_code, h.store_key, s.latitude, s.longitude, round(dw.dbo.fnCalcDistance(s.latitude, s.longitude, c.lat, c.lon),0) distance
into #gb_future
from tblZipTop1_historical_gb h
	join store_dim s
	on s.store_key = h.store_key
	join dw..tblUKPostalCodes_centroids c
	on c.postcode = h.postal_code
where date_key = 
(
	select max(date_key) from tblZipTop1_historical_gb
	where date_key <= (
		select date_key
		from date_dim
		where actual_date = cast(convert(varchar, dateadd(ww, 6, getdate()),101) as datetime))
)
create index ix_gb_future on #gb_future(postal_code)
 

--select * From  dw..tblUKPostalCodes_centroids
--select * From  dw..tblZipTop1_historical_gb
--
--select *
--from #gb_current c
--	join #gb_future f
--	on f.postal_code = c.postal_code
--where f.store_key != c.store_key

 
-- **********************************************************************************************************
-- **********************************************************************************************************
-- **********************************************************************************************************

--for each address, figure out its nearest store data, time consuming, but accurate
IF (Object_ID('dave_neareststore_us') IS NOT NULL) DROP TABLE dave_neareststore_us
select distinct a.address_key, a.country, a.postal_code, 
	c.store_key nearest_store_key_new, c.distance distance_to_nearest_store_new,
	f.store_key nearest_futurestore_key_new, f.distance distance_to_nearest_futurestore_new
into dave_neareststore_us
from address_dim a with (nolock)
	join #us_ca_current c
	on c.postal_code = a.postal_code
	join #us_ca_future f
	on f.postal_code = a.postal_code
where 1=1
	and a.verified_address = 'Y'
 	and a.country in ('US', 'PR')
	and a.latitude is not null and a.longitude is not null -- not sure i really need this anymore

create index ix_dave_neareststore_us on dave_neareststore_us(address_key)
--1:03:39
--19758003	1:03:00
--20279945	1:34

IF (Object_ID('dave_neareststore_ca') IS NOT NULL) DROP TABLE dave_neareststore_ca
select distinct a.address_key, a.country, a.postal_code, 
	c.store_key nearest_store_key_new, c.distance distance_to_nearest_store_new,
	f.store_key nearest_futurestore_key_new, f.distance distance_to_nearest_futurestore_new
into dave_neareststore_ca
from address_dim a with (nolock)
	join #us_ca_current c
	on c.postal_code = substring(a.postal_code,1,3)
	join #us_ca_future f
	on f.postal_code = substring(a.postal_code,1,3)
where 1=1
	and a.verified_address = 'Y'
	and a.country in ('CA')
	and a.latitude is not null and a.longitude is not null -- not sure i really need this anymore

--649740
--650076	2:36
--719249	1:06
 
IF (Object_ID('dave_neareststore_gb') IS NOT NULL) DROP TABLE dave_neareststore_gb
select distinct a.address_key, a.country, a.postal_code, 
	c.store_key nearest_store_key_new, c.distance distance_to_nearest_store_new,
	f.store_key nearest_futurestore_key_new, f.distance distance_to_nearest_futurestore_new
into dave_neareststore_gb
from address_dim a with (nolock)
	join #gb_current c
	on c.postal_code = substring(a.postal_code, 1, charindex(' ',a.postal_code,1)-1)
	join #gb_future f
	on f.postal_code = substring(a.postal_code, 1, charindex(' ',a.postal_code,1)-1)
where 1=1
	and a.verified_address = 'Y'
	and a.country in ('GB')
	and a.latitude is not null and a.longitude is not null -- not sure i really need this anymore

--636066
--773565	1:07

-- **********************************************************************************************************
-- **********************************************************************************************************
-- **********************************************************************************************************

-- figure out which addresses in gas are wrong

IF (Object_ID('dave_neareststore_gas_diff') IS NOT NULL) DROP TABLE dave_neareststore_gas_diff
select distinct current_address_key, a.country,
 	nearest_store_key, distance_to_nearest_store,
	nearest_store_key_new, distance_to_nearest_store_new,
 	nearest_futurestore_key, distance_to_nearest_futurestore,
	nearest_futurestore_key_new, distance_to_nearest_futurestore_new,
	cast(null as datetime) processed_date
into dave_neareststore_gas_diff
from guest_activity_summary gas with (nolock)
	join dave_neareststore_us a with (nolock)
	on a.address_key = gas.current_address_key
where isnull(nearest_store_key,-1) != nearest_store_key_new
	or isnull(nearest_futurestore_key,-1) != nearest_futurestore_key_new
	or abs(isnull(distance_to_nearest_store,-1) - distance_to_nearest_store_new) > 2
	or abs(isnull(distance_to_nearest_futurestore,-1) - distance_to_nearest_futurestore_new) > 2

union

select distinct current_address_key, a.country,
 	nearest_store_key, distance_to_nearest_store,
	nearest_store_key_new, distance_to_nearest_store_new,
 	nearest_futurestore_key, distance_to_nearest_futurestore,
	nearest_futurestore_key_new, distance_to_nearest_futurestore_new,
	cast(null as datetime) processed_date
from guest_activity_summary gas with (nolock)
	join dave_neareststore_ca a with (nolock)
	on a.address_key = gas.current_address_key
where isnull(nearest_store_key,-1) != nearest_store_key_new
	or isnull(nearest_futurestore_key,-1) != nearest_futurestore_key_new
	or abs(isnull(distance_to_nearest_store,-1) - distance_to_nearest_store_new) > 2
	or abs(isnull(distance_to_nearest_futurestore,-1) - distance_to_nearest_futurestore_new) > 2

union

select distinct current_address_key, a.country,
 	nearest_store_key, distance_to_nearest_store,
	nearest_store_key_new, distance_to_nearest_store_new,
 	nearest_futurestore_key, distance_to_nearest_futurestore,
	nearest_futurestore_key_new, distance_to_nearest_futurestore_new,
	cast(null as datetime) processed_date
from guest_activity_summary gas with (nolock)
	join dave_neareststore_gb a with (nolock)
	on a.address_key = gas.current_address_key
where isnull(nearest_store_key,-1) != nearest_store_key_new
	or isnull(nearest_futurestore_key,-1) != nearest_futurestore_key_new
	or abs(isnull(distance_to_nearest_store,-1) - distance_to_nearest_store_new) > 2
	or abs(isnull(distance_to_nearest_futurestore,-1) - distance_to_nearest_futurestore_new) > 2

create index ix_dave_neareststore_gas_diff on dave_neareststore_gas_diff(current_address_key)
--7305994
--7588989
--13661572	5:35
--851749
--2697202

------ due to using the centroids, i don't want to update 13 mill addresses
--select count(*)
--from dave_neareststore_gas_diff
--where isnull(nearest_store_key,-1) != nearest_store_key_new
--	or isnull(nearest_futurestore_key,-1) != nearest_futurestore_key_new
--	or abs(distance_to_nearest_store - distance_to_nearest_store_new) > 2
--	or abs(distance_to_nearest_futurestore - distance_to_nearest_futurestore_new) > 2
----852243
----926196
----1187617
----2749205
----5056412


-- **********************************************************************************************************
-- **********************************************************************************************************
-- **********************************************************************************************************

-- figure out which addresses in has are wrong

IF (Object_ID('dave_neareststore_has_diff') IS NOT NULL) DROP TABLE dave_neareststore_has_diff
select distinct current_address_key, a.country,
	nearest_store, distance_to_nearest_store,
	nearest_store_key_new, distance_to_nearest_store_new,
	nearest_futurestore_key, distance_to_nearest_futurestore,
	nearest_futurestore_key_new, distance_to_nearest_futurestore_new,
	cast(null as datetime) processed_date
into dave_neareststore_has_diff
from household_activity_summary has with (nolock)
	join dave_neareststore_us a with (nolock)
	on a.address_key = has.current_address_key
where isnull(nearest_store,-1) != nearest_store_key_new
	or isnull(nearest_futurestore_key,-1) != nearest_futurestore_key_new
	or abs(isnull(distance_to_nearest_store,-1) - distance_to_nearest_store_new) > 2
	or abs(isnull(distance_to_nearest_futurestore,-1) - distance_to_nearest_futurestore_new) > 2

union

select distinct current_address_key, a.country,
	nearest_store, distance_to_nearest_store,
	nearest_store_key_new, distance_to_nearest_store_new,
	nearest_futurestore_key, distance_to_nearest_futurestore,
	nearest_futurestore_key_new, distance_to_nearest_futurestore_new,
	cast(null as datetime) processed_date
from household_activity_summary has with (nolock)
	join dave_neareststore_ca a with (nolock)
	on a.address_key = has.current_address_key
where isnull(nearest_store,-1) != nearest_store_key_new
	or isnull(nearest_futurestore_key,-1) != nearest_futurestore_key_new
	or abs(isnull(distance_to_nearest_store,-1) - distance_to_nearest_store_new) > 2
	or abs(isnull(distance_to_nearest_futurestore,-1) - distance_to_nearest_futurestore_new) > 2

union

select distinct current_address_key, a.country,
	nearest_store, distance_to_nearest_store,
	nearest_store_key_new, distance_to_nearest_store_new,
	nearest_futurestore_key, distance_to_nearest_futurestore,
	nearest_futurestore_key_new, distance_to_nearest_futurestore_new,
	cast(null as datetime) processed_date
from household_activity_summary has with (nolock)
	join dave_neareststore_gb a with (nolock)
	on a.address_key = has.current_address_key
where isnull(nearest_store,-1) != nearest_store_key_new
	or isnull(nearest_futurestore_key,-1) != nearest_futurestore_key_new
	or abs(isnull(distance_to_nearest_store,-1) - distance_to_nearest_store_new) > 2
	or abs(isnull(distance_to_nearest_futurestore,-1) - distance_to_nearest_futurestore_new) > 2

create index ix_dave_neareststore_has_diff on dave_neareststore_has_diff(current_address_key)
--7956782
--7958059
--13645052
--797959
--

---- due to using the centroids, i don't want to update 13 mill addresses
--select count(*)
--from dave_neareststore_has_diff
--where isnull(nearest_store,-1) != nearest_store_key_new
--	or isnull(nearest_futurestore_key,-1) != nearest_futurestore_key_new
--	or abs(distance_to_nearest_store - distance_to_nearest_store_new) > 2
--	or abs(distance_to_nearest_futurestore - distance_to_nearest_futurestore_new) > 2
----797959
----2742944


-- **********************************************************************************************************
-- **********************************************************************************************************
-- **********************************************************************************************************

declare @BatchLoopMax as integer
declare @UpdateLoopCounter as integer
declare @BatchLoopCounter as integer
declare @RowsToUpdate as integer
declare @Count as integer
declare @RowsToPull as integer
declare @sql varchar(8000)
declare @processed_date datetime
declare @startrow int
declare @stoprow int

declare @starttime	datetime
declare @starttime_begin	datetime

declare
	@iErr		integer,
	@iRetVal 		integer,
	@iTranCount 	integer,
	@iRowCount 	integer,
	@sErrMsg 		varchar(100)

-- rollback tran
--set @BatchLoopCounter = 1
--set @BatchLoopMax = 1
--set @RowsToPull = 100
--set @RowsToUpdate = 100

set @BatchLoopCounter = 1
set @BatchLoopMax = 5
--set @RowsToPull = 1000
--set @RowsToUpdate = 100
set @RowsToPull = 100000
set @RowsToUpdate = 1000

-- **********************************************************************************************************
-- **********************************************************************************************************
-- **********************************************************************************************************
-- do the gas updates

-- DBCC SHOWCONTIG (Guest_Activity_Summary) WITH TABLERESULTS, ALL_INDEXES, FAST
-- DBCC SHOWCONTIG (Household_Activity_Summary) WITH TABLERESULTS, ALL_INDEXES, FAST

set @iErr = 0
set @sErrMsg = 'No Error'


drop index Guest_Activity_Summary.idxN_U_guest_activity_summary_keys_nearstore

while (@BatchLoopCounter <= @BatchLoopMax)
begin
	set @starttime = getdate()
	set @processed_date = getdate()
	
	IF (Object_ID('tempdb..##updateme_gas_store_diff') IS NOT NULL) DROP TABLE ##updateme_gas_store_diff
	set @sql = '
		select top ' + cast(@RowsToPull as varchar) + '  *
		into ##updateme_gas_store_diff
		from dave_neareststore_gas_diff
		where 1=1
			and processed_date is null
		alter table ##updateme_gas_store_diff add tblKey int IDENTITY (1, 1) NOT FOR REPLICATION  NOT NULL
	'
	print @sql
	exec (@sql)

--		create index ix_updateme_gas_store_diff on ##updateme_gas_store_diff(current_address_key)

	print 'after temp table pull: ' + cast(datediff(ss, @starttime,getdate()) as varchar)

	set @UpdateLoopCounter = 0
	set @Count = (select count(*) from ##updateme_gas_store_diff)

	print @Count
	
	while (@UpdateLoopCounter * @RowsToUpdate < @Count)
	begin
		set @starttime = getdate()
		set @starttime_begin = getdate()

		print cast(@BatchLoopCounter as varchar) + ':' + cast(@UpdateLoopCounter as varchar) + ':' + cast((@BatchLoopCounter-1)*@RowsToPull + @UpdateLoopCounter * @RowsToUpdate as varchar)

		set @startrow = @UpdateLoopCounter * @RowsToUpdate+1 
		set @stoprow = (@UpdateLoopCounter+1) * @RowsToUpdate

		begin tran	

		update guest_activity_summary
		set	nearest_store_key = u.nearest_store_key_new,
			distance_to_nearest_store = u.distance_to_nearest_store_new,
			nearest_futurestore_key = u.nearest_futurestore_key_new,
			distance_to_nearest_futurestore = u.distance_to_nearest_futurestore_new
-- 		from guest_activity_summary gas (index=idxN_NU_GAS_current_address_key)
		from guest_activity_summary gas
			join ##updateme_gas_store_diff u
			on u.current_address_key = gas.current_address_key
		where u.tblKey between @startrow and @stoprow
		set @iErr = @@ERROR
		if @iErr <> 0
		begin
			set @sErrMsg = 'error after update from gas'
			goto ExitHandler_gas
		end

--  	print 'update from gas: ' + cast(datediff(ss, @starttime,getdate()) as varchar)
-- 	set @starttime = getdate()
		
		update dave_neareststore_gas_diff
		set processed_date = getdate()
		from dave_neareststore_gas_diff m
			join ##updateme_gas_store_diff u
			on u.current_address_key = m.current_address_key
		where u.tblKey between @startrow and @stoprow
		set @iErr = @@ERROR
		if @iErr <> 0
		begin
			set @sErrMsg = 'error after update into dave_neareststore_gas_diff'
			goto ExitHandler_gas
		end

-- 		rollback tran
		commit tran

		print '**** after commit ****: ' + cast(datediff(ss, @starttime_begin, getdate()) as varchar)
	
		set @UpdateLoopCounter = @UpdateLoopCounter + 1
	end

	set @BatchLoopCounter = @BatchLoopCounter + 1
end

ExitHandler_gas:

--=====  Start - Start Transaction (Standard) ==========
if @@TRANCOUNT > 0 
--if @iTranCount = 0 AND @@TRANCOUNT > 0 
begin
	IF @iErr = 0 
	begin
		print 'no error'
		rollback tran
--		commit tran
	end
	else 
	begin
		print @sErrMsg
		print 'rollback'
		rollback tran
	end
end

CREATE  INDEX [idxN_U_guest_activity_summary_keys_nearstore] ON [dbo].[Guest_Activity_Summary]([Household_key], [Customer_key], [Current_Address_key], [Distance_To_Nearest_Store], [Nearest_Store_Key]) WITH  FILLFACTOR = 90 ON [PRIMARY]

--  CREATE  INDEX [idxN_NU_GAS_household_key] ON [dbo].[Guest_Activity_Summary]([Household_key]) WITH  FILLFACTOR = 90 ON [INDEXES]
-- go
--  CREATE  INDEX [idxN_NU_GAS_first_visit_date_key] ON [dbo].[Guest_Activity_Summary]([First_Visit_date_key]) WITH  FILLFACTOR = 90 ON [INDEXES]
-- go
--  CREATE  INDEX [idxN_NU_GAS_last_visit_date_key] ON [dbo].[Guest_Activity_Summary]([Last_Visit_date_key]) WITH  FILLFACTOR = 90 ON [INDEXES]
-- go


-- **********************************************************************************************************
-- **********************************************************************************************************
-- **********************************************************************************************************
-- do the has updates

drop index Household_Activity_Summary.idxN_NU_HAS_Distance_Recency_NumVisits

set @BatchLoopCounter = 1

while (@BatchLoopCounter <= @BatchLoopMax)
begin
	set @starttime = getdate()
	set @processed_date = getdate()
	
	IF (Object_ID('tempdb..##updateme_has_store_diff') IS NOT NULL) DROP TABLE ##updateme_has_store_diff
	set @sql = '
		select top ' + cast(@RowsToPull as varchar) + '  *
		into ##updateme_has_store_diff
		from dave_neareststore_has_diff
		where 1=1
			and processed_date is null
		alter table ##updateme_has_store_diff add tblKey int IDENTITY (1, 1) NOT FOR REPLICATION  NOT NULL
	'
	print @sql
	exec (@sql)

	print 'after temp table pull: ' + cast(datediff(ss, @starttime,getdate()) as varchar)

	set @UpdateLoopCounter = 0
	set @Count = (select count(*) from ##updateme_has_store_diff)

	print @Count
	
	while (@UpdateLoopCounter * @RowsToUpdate < @Count)
	begin
		set @starttime = getdate()
		set @starttime_begin = getdate()

		print cast(@BatchLoopCounter as varchar) + ':' + cast(@UpdateLoopCounter as varchar) + ':' + cast((@BatchLoopCounter-1)*@RowsToPull + @UpdateLoopCounter * @RowsToUpdate as varchar)

		set @startrow = @UpdateLoopCounter * @RowsToUpdate+1 
		set @stoprow = (@UpdateLoopCounter+1) * @RowsToUpdate

		begin tran	

		update household_activity_summary
		set	nearest_store = u.nearest_store_key_new,
			distance_to_nearest_store = u.distance_to_nearest_store_new,
			nearest_futurestore_key = u.nearest_futurestore_key_new,
			distance_to_nearest_futurestore = u.distance_to_nearest_futurestore_new
		from household_activity_summary gas (index=idxN_NU_GAS_current_address_key)
			join ##updateme_has_store_diff u
			on u.current_address_key = gas.current_address_key
		where u.tblKey between @startrow and @stoprow
		set @iErr = @@ERROR
		if @iErr <> 0
		begin
			set @sErrMsg = 'error after update from gas'
			goto ExitHandler_has
		end

-- 	print 'update from gas: ' + cast(datediff(ss, @starttime,getdate()) as varchar)
-- 	set @starttime = getdate()
		
		update dave_neareststore_has_diff
		set processed_date = getdate()
		from dave_neareststore_has_diff m
			join ##updateme_has_store_diff u
			on u.current_address_key = m.current_address_key
		where u.tblKey between @startrow and @stoprow
		set @iErr = @@ERROR
		if @iErr <> 0
		begin
			set @sErrMsg = 'error after update into dave_neareststore_has_diff'
			goto ExitHandler_has
		end

-- 		rollback tran
		commit tran

		print '**** after commit ****: ' + cast(datediff(ss, @starttime_begin, getdate()) as varchar)
	
		set @UpdateLoopCounter = @UpdateLoopCounter + 1
	end

	set @BatchLoopCounter = @BatchLoopCounter + 1
end

ExitHandler_has:

--=====  Start - Start Transaction (Standard) ==========
if @@TRANCOUNT > 0 
--if @iTranCount = 0 AND @@TRANCOUNT > 0 
begin
	IF @iErr = 0 
	begin
		print 'no error'
		rollback tran
--		commit tran
	end
	else 
	begin
		print @sErrMsg
		print 'rollback'
		rollback tran
	end
end

CREATE  INDEX [idxN_NU_HAS_Distance_Recency_NumVisits] ON [dbo].[Household_Activity_Summary]([Distance_To_Nearest_Store], [Recency_in_Months], [Number_Of_Visits]) WITH  FILLFACTOR = 51 ON [PRIMARY]


-- **********************************************************************************************************
-- **********************************************************************************************************
-- **********************************************************************************************************
```

