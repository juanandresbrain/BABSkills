# WEB.vwProductStorefrontCatalogCategories

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["WEB.vwProductStorefrontCatalogCategories"]
    WEB_CategoryXREF(["WEB.CategoryXREF"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| WEB.CategoryXREF |

## View Code

```sql
CREATE view [WEB].[vwProductStorefrontCatalogCategories]

as 
-----------------------------------------------------------------------
--	Developer		--		Date		--		Details
--	Dan Tweedie				06-07-2017			Created view for the storefront category elements of the eCommerce product catalog storefront xml
-----------------------------------------------------------------------


WITH
Categories as
	(
		select distinct 
			'US' as Catalog,
			PrimaryCategoryID,
			SecondaryCategoryID,
			TertiaryCategoryID,
			QuaternaryCategoryID,
			PrimaryCategoryName,
			PrimaryCategorySortOrder,
			SecondaryCategoryName,
			SecondaryCategorySortOrder,
			TertiaryCategoryName,
			TertiaryCategorySortOrder,
			QuaternaryCategoryName,
			QuaternaryCategorySortOrder,
			OnlineStart,
			OnlineEnd,
			ShowInMenu
		from WEB.CategoryXREF
		where isnull(CountrySpecificCategory,'US') = 'US'
		UNION
		select distinct 
			'UK' as Catalog,
			PrimaryCategoryID,
			SecondaryCategoryID,
			TertiaryCategoryID,
			QuaternaryCategoryID,
			PrimaryCategoryName,
			PrimaryCategorySortOrder,
			SecondaryCategoryName,
			SecondaryCategorySortOrder,
			TertiaryCategoryName,
			TertiaryCategorySortOrder,
			QuaternaryCategoryName,
			QuaternaryCategorySortOrder,
			OnlineStart,
			OnlineEnd,
			ShowInMenu
		from WEB.CategoryXREF
		where isnull(CountrySpecificCategory,'UK') = 'UK'
	),
PrimaryMinMax as
	(
		select 
			PrimaryCategoryID, 
			min(OnlineStart) OnlineStart,
			max(OnlineEnd) OnlineEnd
		from Categories
		group by PrimaryCategoryID
	),
SecondaryMinMax as
	(
		select 
			SecondaryCategoryID, 
			min(OnlineStart) OnlineStart,
			max(OnlineEnd) OnlineEnd
		from Categories
		group by SecondaryCategoryID
	),
TertiaryMinMax as
	(
		select 
			TertiaryCategoryID, 
			min(OnlineStart) OnlineStart,
			max(OnlineEnd) OnlineEnd
		from Categories
		group by TertiaryCategoryID
	),
QuaternaryMinMax as
	(
		select 
			QuaternaryCategoryID, 
			min(OnlineStart) OnlineStart,
			max(OnlineEnd) OnlineEnd
		from Categories
		group by QuaternaryCategoryID		
	),
Unions as
	(
		select distinct 
			Catalog as CategoryID,
			NULL as Parent,
			'Storefront Catalog' as DisplayName,
			1 as CategoryLevel,
			'1999-12-31' OnlineStart,
			'2399-12-31' OnlineEnd,
			1 OnlineFlag,
			0 as Position,
			max(ShowInMenu) ShowInMenu 
		from Categories
		group by Catalog
		UNION
		select distinct 
			c.Catalog + '-' + c.QuaternaryCategoryID as CategoryID,
			c.Catalog + '-' + c.TertiaryCategoryID as Parent,
			c.QuaternaryCategoryName as DisplayName,
			2 as CategoryLevel,
			t.OnlineStart,
			t.OnlineEnd,
			case 
				when cast(getdate() as date) between t.OnlineStart and t.OnlineEnd
				then 1
				else 0
			end as OnlineFlag,
			c.QuaternaryCategorySortOrder as Position,
			max(ShowInMenu) ShowInMenu 
		from Categories c
		join QuaternaryMinMax t on c.QuaternaryCategoryID = t.QuaternaryCategoryID
		where c.QuaternaryCategoryID is NOT NULL
		group by 
			c.Catalog + '-' + c.QuaternaryCategoryID,
			c.Catalog + '-' + c.TertiaryCategoryID,
			c.QuaternaryCategoryName,
			t.OnlineStart,
			t.OnlineEnd,
			case 
				when cast(getdate() as date) between t.OnlineStart and t.OnlineEnd
				then 1
				else 0
			end,
			c.QuaternaryCategorySortOrder
		UNION
		select distinct 
			c.Catalog + '-' + c.TertiaryCategoryID as CategoryID,
			c.Catalog + '-' + c.SecondaryCategoryID as Parent,
			c.TertiaryCategoryName as DisplayName,
			2 as CategoryLevel,
			t.OnlineStart,
			t.OnlineEnd,
			case 
				when cast(getdate() as date) between t.OnlineStart and t.OnlineEnd
				then 1
				else 0
			end as OnlineFlag,
			c.TertiaryCategorySortOrder as Position,
			max(ShowInMenu) ShowInMenu 
		from Categories c
		join TertiaryMinMax t on c.TertiaryCategoryID = t.TertiaryCategoryID
		where c.TertiaryCategoryID is NOT NULL
		group by 
			c.Catalog + '-' + c.TertiaryCategoryID,
			c.Catalog + '-' + c.SecondaryCategoryID,
			c.TertiaryCategoryName,
			t.OnlineStart,
			t.OnlineEnd,
			case 
				when cast(getdate() as date) between t.OnlineStart and t.OnlineEnd
				then 1
				else 0
			end,
			c.TertiaryCategorySortOrder
		UNION
		select distinct 
			c.Catalog + '-' + c.SecondaryCategoryID as CategoryID,
			c.Catalog + '-' + c.PrimaryCategoryID as parent,
			c.SecondaryCategoryName as DisplayName,
			3 as CategoryLevel,
			s.OnlineStart,
			s.OnlineEnd,
			case 
				when cast(getdate() as date) between s.OnlineStart and s.OnlineEnd
				then 1
				else 0
			end as OnlineFlag,
			c.SecondaryCategorySortOrder as Position,
			max(ShowInMenu) ShowInMenu 
		from Categories c
		join SecondaryMinMax s on c.SecondaryCategoryID = s.SecondaryCategoryID
		where c.SecondaryCategoryID is NOT NULL
		group by 
			c.Catalog + '-' + c.SecondaryCategoryID,
			c.Catalog + '-' + c.PrimaryCategoryID,
			c.SecondaryCategoryName,
			s.OnlineStart,
			s.OnlineEnd,
			case 
				when cast(getdate() as date) between s.OnlineStart and s.OnlineEnd
				then 1
				else 0
			end,
			c.SecondaryCategorySortOrder
		UNION
		select distinct
			c.Catalog + '-' + c.PrimaryCategoryID as CategoryID,
			c.Catalog as Parent,
			c.PrimaryCategoryName as DisplayName,
			4 as CategoryLevel,
			p.OnlineStart,
			p.OnlineEnd,
			case 
				when cast(getdate() as date) between p.OnlineStart and p.OnlineEnd
				then 1
				else 0
			end as OnlineFlag,
			c.PrimaryCategorySortOrder as Position,
			max(ShowInMenu) ShowInMenu 
		from Categories c
		join PrimaryMinMax p on c.PrimaryCategoryID = p.PrimaryCategoryID
		group by 	
			c.Catalog + '-' + c.PrimaryCategoryID,
			c.Catalog,
			c.PrimaryCategoryName,
			p.OnlineStart,
			p.OnlineEnd,
			case 
				when cast(getdate() as date) between p.OnlineStart and p.OnlineEnd
				then 1
				else 0
			end,
			c.PrimaryCategorySortOrder
	)
select
	cast(CategoryID as nvarchar(200)) as CategoryID,
	cast(Parent as nvarchar(200)) as Parent,
	cast(DisplayName as nvarchar(52)) as DisplayName,
	cast(CategoryLevel as int) as CategoryLevel,
	OnlineStart,
	OnlineEnd,
	OnlineFlag,
	Position,
	ShowInMenu
from Unions
```

