# dbo.vwWebProductMasterCatalogCategories

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwWebProductMasterCatalogCategories"]
    dbo_vwWebHierarchy(["dbo.vwWebHierarchy"]) --> VIEW
    dbo_vwWebIncludedStyles(["dbo.vwWebIncludedStyles"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.vwWebHierarchy |
| dbo.vwWebIncludedStyles |

## View Code

```sql
CREATE view [dbo].[vwWebProductMasterCatalogCategories] 

as


-----------------------------------------------------------------------
--	Developer		--		Date		--		Details
--	Dan Tweedie				05-09-2017			Created view for the category elements of the eCommerce product catalog xml
-----------------------------------------------------------------------


with 
Categories as 
	(
		select distinct
			--s.SellingGeography as Catalog,
			'root' as Catalog,
			lower(h.Department) as Department,
			lower(h.Class) as Class,
			lower(h.SubClass) as SubClass
		from vwWebIncludedStyles s
		join vwWebHierarchy h on s.hierarchy_group_id = h.SubClassHierarchyGroupID
	),
Unions as
	(
		select distinct 
			Catalog as CategoryID,
			NULL as Parent,
			'Build-A-Bear Master Catalog' as DisplayName,
			1 as CategoryLevel
		from Categories
		UNION
		select distinct
			--Catalog + '-' +  Department as CategoryID,
			Department as CategoryID,
			Catalog as Parent,
			Department as DisplayName,
			2 as CategoryLevel
		from Categories
		UNION
		select distinct
			--Catalog + '-' +  Department + '-' + Class as CategoryID,
			Department + '-' + Class as CategoryID,
			--Catalog + '-' +  Department as Parent,
			Department as Parent,
			Class as DisplayName,
			3 as CategoryLevel
		from Categories
		UNION
		select distinct 
			--Catalog + '-' +  Department + '-' + Class + '-' + SubClass as CategoryID,
			Department + '-' + Class + '-' + SubClass as CategoryID,
			--Catalog + '-' +  Department + '-' + Class as Parent,
			Department + '-' + Class as Parent,
			SubClass as DisplayName,
			4 as CategoryLevel
		from Categories	
	)
select
	cast(CategoryID as nvarchar(200)) as CategoryID,
	cast(Parent as nvarchar(200)) as Parent,
	cast(DisplayName as nvarchar(52)) as DisplayName,
	cast(CategoryLevel as int) as CategoryLevel
from Unions
```

