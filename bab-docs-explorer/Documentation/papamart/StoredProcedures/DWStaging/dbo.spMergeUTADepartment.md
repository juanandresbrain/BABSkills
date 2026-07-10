# dbo.spMergeUTADepartment

**Database:** DWStaging  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMergeUTADepartment"]
    dbo_UTADepartment(["dbo.UTADepartment"]) --> SP
    dbo_UTADepartmentStage(["dbo.UTADepartmentStage"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.UTADepartment |
| dbo.UTADepartmentStage |

## Stored Procedure Code

```sql
create proc [dbo].[spMergeUTADepartment]

as 

-------------------------------------------------------------------------------------------------------
-- Dan Tweedie	2019-01-16	Created Proc for merging data from new UTA system that replaces Workbrain
-------------------------------------------------------------------------------------------------------

set nocount on

merge into DW.dbo.UTADepartment as target
using DWStaging.dbo.UTADepartmentStage as source 
on 
	(
		target.Dept_ID=source.Dept_ID
	)
When Matched and
	(
		isnull(target.Dept_Name,'x')<>isnull(source.Dept_Name,'x')
		OR
		isnull(target.Dept_Desc,'x')<>isnull(source.Dept_Desc,'x')
	)
Then Update
	set 
		target.Dept_Name=source.Dept_Name,
		target.Dept_Desc=source.Dept_Desc,
		target.UpdateDate=getdate()
When Not Matched by target
Then Insert
	(
		Dept_ID,
		Dept_Name,
		Dept_Desc,
		InsertDate
	)
Values
	(
		source.Dept_ID,
		source.Dept_Name,
		source.Dept_Desc,
		getdate()
	)
;
```

