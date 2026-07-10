# dbo.spMergePayrollMonthFacts

**Database:** payroll  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMergePayrollMonthFacts"]
    PayrollMonthFacts(["PayrollMonthFacts"]) --> SP
    PayrollMonthStage(["PayrollMonthStage"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| PayrollMonthFacts |
| PayrollMonthStage |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spMergePayrollMonthFacts]

as
--------------------------------------------------------------------------------------------
--Dan Tweedie	2018-10-29	Created proc to help with new ActualVsEarned / Payroll ETL
-------------------------------------------------------------------------------------------

set nocount on

merge into PayrollMonthFacts as target
using PayrollMonthStage as source 
on 
	(
		target.store_key=source.store_key
		AND
		target.period_id=source.period_id
	)
when matched 
	and 
		(
			isnull(target.adj_actual,0)<>isnull(source.monthly_adj_actual,0)
			OR
			isnull(target.adj_earned,0)<>isnull(source.monthly_adj_earned,0)
			OR
			isnull(target.actual,0)<>isnull(source.monthly_actual,0)
			OR
			isnull(target.earned,0)<>isnull(source.monthly_earned,0)
		)
then update 
	set 
		target.adj_actual=isnull(source.monthly_adj_actual,0),
		target.adj_earned=isnull(source.monthly_adj_earned,0),
		target.actual=isnull(source.monthly_actual,0),
		target.earned=isnull(source.monthly_earned,0),
		target.updated_date = getdate()

when not matched by target 
	then insert 
		(
			store_key,
			period_id,
			adj_actual,
			adj_earned,
			actual,
			earned,
			loaded_date
		)
	values
		(
			source.store_key,
			source.period_id,
			isnull(source.monthly_adj_actual,0),
			isnull(source.monthly_adj_earned,0),
			isnull(source.monthly_actual,0),
			isnull(source.monthly_earned,0),
			getdate()
		)
;

dbo,dt_dropuserobjectbyid,/*
**	Drop an object from the dbo.dtproperties table
*/
create procedure dbo.dt_dropuserobjectbyid
	@id int
as
	set nocount on
	delete from dbo.dtproperties where objectid=@id
```

