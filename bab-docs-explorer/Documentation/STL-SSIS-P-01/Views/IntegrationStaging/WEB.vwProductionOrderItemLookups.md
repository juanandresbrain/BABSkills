# WEB.vwProductionOrderItemLookups

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["WEB.vwProductionOrderItemLookups"]
    WEB_ProductCatalogMasterAttributes(["WEB.ProductCatalogMasterAttributes"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| WEB.ProductCatalogMasterAttributes |

## View Code

```sql
create view WEB.vwProductionOrderItemLookups

as

----------------------------------------------------------------------------------------------------------------
--DanTweedie 2017-10-25 -- created view for lookup from ssis for specific web reporting, this may go away
---------------------------------------------------------------------------------------------------------------

select 
	BABWProductID,
	cast(Department as nvarchar(32)) as Department,
	cast(ClassName as nvarchar(32)) as ClassName,
	cast(HierarchyGroupCode as nvarchar(32)) as SubClass,
	case 
		when SAC = 'true' 
			then 1 
		else 0
	end as ProductionOrderItemIsPreBuilt,
	case
		when HierarchyGroupCode in 
			(
				'W-C-K-12-01-07',
				'W-D-K-12-01-07',
				'W-E-K-12-01-07',
				'W-F-K-12-01-07'
			)
		OR ClassName in ('sound', 'sounds')
			then 1
		else 0
	end as ProductionOrderItemIsSound,
	case
		when SkinType is not NULL
			then 1
		else 0
	end as ProductionOrderItemIsAnimal,
	case
		when left(HierarchyGroupCode,8) in ('R-B-D-80', 'R-B-U-80 ') 
			AND HierarchyGroupCode NOT in ('R-B-D-80-02-00','R-B-U-80-02-00') 
			then 1
		else 0
	end as ProductionOrderItemIsPhysicalGiftCard,
	case 
		when HierarchyGroupCode in 
			(
				'R-B-D-80-02-00',
				'R-B-U-80-02-00'
			) then 1
		else 0
	end as ProductionOrderItemIsVirtualGiftCard,
	case 
		when AccessoryType is not NULL
			then 1
		else 0
	end as ProductionOrderItemIsAccessory,
	NULL as ProductionOrderItemIsDoll, --come back to this
	case 
		when left(HierarchyGroupCode,8) in 
			(
				'R-B-D-65'
			) then 1
		else 0
	end as ProductionOrderItemIsEmbroidery,
	CAST(CommodityCode as nvarchar(50)) as ProductionOrderItemCommodityCode,
	ManufacturerCountry as ProductionOrderItemCountryOfManufacture,
	case 
		when HierarchyGroupCode in 
			(
				'W-C-K-12-01-07',
				'W-D-K-12-01-07',
				'W-E-K-12-01-07',
				'W-F-K-12-01-07'
			) 
		OR
		 HierarchyGroupCode in 
			(
				'R-B-D-80-02-00',
				'R-B-U-80-02-00'
			) 
		OR
		 left(HierarchyGroupCode,8) in 
			(
				'R-B-D-46',
				'R-B-U-46',
				'R-B-D-65'
			) 
		then 1 
		else 0
	end as ProductionOrderItemIsVirtualItem
from WEB.ProductCatalogMasterAttributes
WEB,vwProductMasterCatalogCategories,CREATE VIEW WEB.vwProductMasterCatalogCategories
AS

WITH Categories
AS (
	SELECT DISTINCT 'root' AS CATALOG
		,w.BaseID
		,w.StyleCode
		,LOWER(d.Value) AS Department
		,LOWER(c.Value) AS Class
		,LOWER(sc.Value) AS SubClass
	FROM WEB.WebIncludedStyles w WITH (NOLOCK)
	JOIN WEB.WebStyleAttributes sc WITH (NOLOCK) ON w.BaseID = sc.BaseID
		AND w.StyleCode = sc.StyleCode
		AND sc.Type = 'Class'
		AND sc.Field = 'SubClass'
	JOIN WEB.WebStyleAttributes c WITH (NOLOCK) ON w.BaseID = c.BaseID
		AND w.StyleCode = c.StyleCode
		AND c.Type = 'Class'
		AND c.Field = 'Class'
	JOIN WEB.WebStyleAttributes d WITH (NOLOCK) ON w.BaseID = d.BaseID
		AND w.StyleCode = d.StyleCode
		AND d.Type = 'Class'
		AND d.Field = 'Department'
	WHERE 1 = 1
	)
	,Unions
AS (
	SELECT DISTINCT CATALOG AS CategoryID
		,NULL AS Parent
		,'Build-A-Bear Master Catalog' AS DisplayName
		,1 AS CategoryLevel
	FROM Categories
	
	UNION
	
	SELECT DISTINCT Department AS CategoryID
		,CATALOG AS Parent
		,Department AS DisplayName
		,2 AS CategoryLevel
	FROM Categories
	
	UNION
	
	SELECT DISTINCT Department + '-' + Class AS CategoryID
		,Department AS Parent
		,Class AS DisplayName
		,3 AS CategoryLevel
	FROM Categories
	
	UNION
	
	SELECT DISTINCT Department + '-' + Class + '-' + SubClass AS CategoryID
		,Department + '-' + Class AS Parent
		,SubClass AS DisplayName
		,4 AS CategoryLevel
	FROM Categories
	)
SELECT cast(CategoryID AS NVARCHAR(200)) AS CategoryID
	,cast(Parent AS NVARCHAR(200)) AS Parent
	,cast(DisplayName AS NVARCHAR(52)) AS DisplayName
	,cast(CategoryLevel AS INT) AS CategoryLevel
FROM Unions
```

