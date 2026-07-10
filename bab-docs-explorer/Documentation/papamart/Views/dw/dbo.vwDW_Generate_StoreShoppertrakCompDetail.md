# dbo.vwDW_Generate_StoreShoppertrakCompDetail

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_Generate_StoreShoppertrakCompDetail"]
    date_dim(["date_dim"]) --> VIEW
    Store_Shoppertrak_Comp_Dim(["Store_Shoppertrak_Comp_Dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| date_dim |
| Store_Shoppertrak_Comp_Dim |

## View Code

```sql
CREATE VIEW [dbo].[vwDW_Generate_StoreShoppertrakCompDetail]
AS
-- =============================================================================================================
-- Name: [dbo].[vwDW_Generate_StoreShoppertrakCompDetail]
--
-- Description: View underlying the construction of the Store_Shoppertrak_CompDetail_Dim table
-- Determines this year and next year comps for a store for ShopperTrak for a specific date.
--	Used by the SSIS Package:Sync Company Store Comps
--
-- Dependencies: 
--
-- Revision History
--		Name:				Date:			Comments:
--		Kevin Shyr			8/12/2015		change to use 52 week logic
--		Gary Murrish		2/20/2013		Block out the date 0
--		Gary Murrish		1/29/2013		Used the Store_Shoppertrak_Comp_Dim table as the base
--		Gary Murrish		8/23/2012		Revised to automatically consider a ShopperTrak store Comp 1 year 
--											after installation
--		Gary Murrish		6/8/2012		Initial deployment
-- =============================================================================================================
SELECT
	base.store_key,
	base.date_key,
	CAST(MAX(isCompTY) AS bit) AS isCompTY,
	CAST(MAX(isCompNY) AS bit) AS isCompNY
FROM
	(SELECT
			scd.store_key,
			cal.tyDate_key AS date_key,
			CAST(CASE
					WHEN cal.tyDate_key BETWEEN scd.date_key_from AND scd.date_key_thru THEN 1
					ELSE 0
				END AS tinyint) AS isCompTY,
			CAST(CASE
					WHEN ISNULL(cal.nyDate_key,999999) BETWEEN scd.date_key_from AND scd.date_key_thru THEN 1
					ELSE 0
				END AS tinyint) AS isCompNY

		FROM
			Store_Shoppertrak_Comp_Dim scd WITH (NOLOCK)
			INNER JOIN (SELECT
					ty.date_key AS tyDate_key,
					ny.date_key AS nyDate_key
				FROM
					date_dim ty WITH (NOLOCK)
					left JOIN date_dim ny WITH (NOLOCK)
					ON ny.week_id = ty.week_id + 52 
						AND ny.day_of_week = ty.day_of_week
					--ny.fiscal_year = ty.fiscal_year + 1
					--AND ny.fiscal_week = ty.fiscal_week
					--AND ny.day_of_week = ty.day_of_week
					)
					cal
				ON cal.tyDate_key BETWEEN scd.date_key_from AND scd.date_key_thru
				OR ISNULL(cal.nyDate_key,999999) BETWEEN scd.date_key_from AND scd.date_key_thru)
	base
	WHERE base.date_key > 0

GROUP BY	base.store_key,
			base.date_key
```

