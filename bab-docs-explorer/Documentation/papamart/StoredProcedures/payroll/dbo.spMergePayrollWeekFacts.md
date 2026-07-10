# dbo.spMergePayrollWeekFacts

**Database:** payroll  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMergePayrollWeekFacts"]
    PayrollWeekFacts(["PayrollWeekFacts"]) --> SP
    PayrollWeekStage(["PayrollWeekStage"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| PayrollWeekFacts |
| PayrollWeekStage |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spMergePayrollWeekFacts]

as
--------------------------------------------------------------------------------------------
--Dan Tweedie	2018-10-29	Created proc to help with new ActualVsEarned / Payroll ETL
-------------------------------------------------------------------------------------------

set nocount on
if (
		select count(*) 
		from PayrollWeekStage
		where 
			week_actual= 0 
			AND 
			week_earned=0
	) 
> 0

begin
	delete from PayrollWeekStage 
	where 
		week_actual= 0 
		AND 
		week_earned=0
end
;

merge into PayrollWeekFacts as target
using PayrollWeekStage as source 
on 
	(
		target.store_key=source.store_key
		AND
		target.week_id=source.week_id
	)
when matched 
	and 
		(
			isnull(target.actual,0)<>isnull(source.week_actual,0)
			OR
			isnull(target.earned,0)<>isnull(source.week_earned,0)
		)
then update 
	set 
		target.actual=isnull(source.week_actual,0),
		target.earned=isnull(source.week_earned,0),
		target.updated_date = getdate()

when not matched by target 
	then insert 
		(
			store_key,
			period_id,
			week_id,
			actual,
			earned,
			loaded_date
		)
	values
		(
			source.store_key,
			source.period_id,
			source.week_id,
			isnull(source.week_actual,0),
			isnull(source.week_earned,0),
			getdate()
		)
;

dbo,dt_droppropertiesbyid,/*
**	Drop one or all the associated properties of an object or an attribute 
**
**	dt_dropproperties objid, null or '' -- drop all properties of the object itself
**	dt_dropproperties objid, property -- drop the property
*/
create procedure dbo.dt_droppropertiesbyid
	@id int,
	@property varchar(64)
as
	set nocount on

	if (@property is null) or (@property = '')
		delete from dbo.dtproperties where objectid=@id
	else
		delete from dbo.dtproperties 
			where objectid=@id and property=@property


dbo,dt_verstamp006,/*
**	This procedure returns the version number of the stored
**    procedures used by the Microsoft Visual Database Tools.
**    Current version is 7.0.00.
*/
create procedure dbo.dt_verstamp006
as
	select 7000
```

