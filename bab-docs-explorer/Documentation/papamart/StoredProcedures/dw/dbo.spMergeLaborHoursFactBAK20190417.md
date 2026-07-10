# dbo.spMergeLaborHoursFactBAK20190417

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMergeLaborHoursFactBAK20190417"]
    date_dim(["date_dim"]) --> SP
    fnUTAExtractAllHours(["fnUTAExtractAllHours"]) --> SP
    Labor_Hours_Fact(["Labor_Hours_Fact"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| date_dim |
| fnUTAExtractAllHours |
| Labor_Hours_Fact |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spMergeLaborHoursFactBAK20190417]

as

--=========================================
--	Dan Tweedie	2019-01-25	Created proc - 
--=========================================

set nocount on

declare 
	@LogID int

select @LogID = max(etl_log_id)+1 from Labor_Hours_Fact;

--updates and/or inserts
merge into Labor_Hours_Fact as target
using 
	(
		select 
			start_time,
			max(end_time) end_time,
			sum(WRKD_MINUTES) WRKD_MINUTES,
			store_key,
			job_key,
			hourtype_key,
			timecode_key,
			date_key,
			emp_key
		from fnUTAExtractAllHours(getdate()-21, getdate())
		group by 
			start_time,
			store_key,
			job_key,
			hourtype_key,
			timecode_key,
			date_key,
			emp_key
	) as source
	on 
		(
			target.store_key=source.store_key
			and
			target.date_key=source.date_key
			and 
			target.emp_key=source.emp_key
			and
			target.start_time=source.start_time
			and 
			target.job_key=source.job_key
			and
			target.timecode_key=source.timecode_key
			and
			target.hourtype_key=source.hourtype_key
		)
when matched 
	and
		(
			isnull(target.end_Time, '3030-12-31')<>isnull(source.end_Time, '3030-12-31') OR
			isnull(target.wrkd_minutes,0)<>isnull(source.wrkd_minutes,0) 
		)
	then Update
		set 
			target.end_Time=source.end_Time, 
			target.wrkd_minutes=source.wrkd_minutes, 
			target.UpdateDate=getdate()
when not matched by target
	then Insert 
		(
			store_key,
			date_key,
			emp_key,
			start_time,
			end_time,
			job_key,
			timecode_key,
			wrkd_minutes,
			HourType_Key,
			source_system,
			etl_log_id,
			etl_evnt_id,
			INS_Dt
		)
	values 
			(
				source.store_key,
				source.date_key,
				source.emp_key,
				source.start_time,
				source.end_time,
				source.job_key,
				source.timecode_key,
				source.wrkd_minutes,
				source.HourType_Key,
				1,
				@LogID,
				@LogID,
				getdate()
			)
;
---deletes
IF (Object_ID('tempdb..#MergeDelete') IS NOT NULL) DROP TABLE #MergeDelete
SELECT        
	f.recID, 
	f.store_key, 
	f.date_key, 
	f.emp_key, 
	f.start_Time, 
	f.end_Time, 
	f.wrkd_minutes, 
	f.hourtype_key,
	NULL as DeleteRow
into #MergeDelete
FROM Labor_Hours_Fact f with (nolock)
inner join date_dim d with (nolock)
	on f.date_key = d.date_key
WHERE d.actual_date between getdate()-21 and getdate()


merge into #MergeDelete as target
using 
	(
		select * from fnUTAExtractAllHours(getdate()-21, getdate())
	) as source
	on 
		(
			isnull(target.store_key,0)=isnull(source.store_key,0)
			and
			isnull(target.date_key,0)=isnull(source.date_key,0)
			and 
			isnull(target.emp_key,0)=isnull(source.emp_key,0)
			and
			isnull(target.start_time,'3030-12-31')=isnull(source.start_time,'3030-12-31')
		)
when not matched by source 
then update 
	set target.DeleteRow = 1
;


delete from Labor_Hours_Fact 
where recID in (select recID from #MergeDelete where DeleteRow = 1)
```

