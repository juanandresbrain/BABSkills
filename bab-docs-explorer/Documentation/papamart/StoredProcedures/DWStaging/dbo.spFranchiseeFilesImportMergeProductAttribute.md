# dbo.spFranchiseeFilesImportMergeProductAttribute

**Database:** DWStaging  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spFranchiseeFilesImportMergeProductAttribute"]
    dbo_FranchiseeProductAttribute(["dbo.FranchiseeProductAttribute"]) --> SP
    dbo_FranchiseeProductAttributeStage(["dbo.FranchiseeProductAttributeStage"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.FranchiseeProductAttribute |
| dbo.FranchiseeProductAttributeStage |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spFranchiseeFilesImportMergeProductAttribute]

as 
-------------------------------------------------
-- Dan Tweedie	-	2018-07-17	- Created proc --
-------------------------------------------------

set nocount on

merge into dw.dbo.FranchiseeProductAttribute as target
using dwstaging.dbo.FranchiseeProductAttributeStage as source 
on 
	(
		target.StyleCode=source.StyleCode
		and
		target.Franchisee=source.Franchisee
	)
when matched 
	and 
		target.CustomAttribute1<>source.CustomAttribute1
then update
	set 
		target.CustomAttribute1=source.CustomAttribute1,
		target.UpdateDate=getdate()
when not matched by target
	then insert
		(
			Franchisee,
			StyleCode,
			CustomAttribute1,
			InsertDate
		)
	values
		(
			source.Franchisee,
			source.StyleCode,
			source.CustomAttribute1,
			getdate()
		)
;
```

