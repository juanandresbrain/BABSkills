# dbo.vwDW_Generate_StoreCompDetail

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_Generate_StoreCompDetail"]
    date_dim(["date_dim"]) --> VIEW
    StoreComp_Dim(["StoreComp_Dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| date_dim |
| StoreComp_Dim |

## View Code

```sql
CREATE VIEW [dbo].[vwDW_Generate_StoreCompDetail] AS
-- =============================================================================================================
-- Name: [dbo].[vwDW_Generate_StoreCompDetail]
--
-- Description: View underlying the construction of the StoreCompDetail_Dim table
-- Determines this year and next year comps for a store for a specific date.
--	Used by the SSIS Package:Sync Company Store Comps
--
-- Dependencies: 
--
-- Revision History
--		Name:				Date:			Comments:
--		Gary Murrish		5/7/2012		Initial deployment
--		Kevin Shyr			11/11/2014		Change to 52 wk comp instead of fiscal year
-- =============================================================================================================
SELECT base.store_key
	 , base.date_key
	 , CAST(MAX(isCompTY) AS BIT) AS isCompTY
	 , CAST(MAX(isCompNY) AS BIT) AS isCompNY
FROM (SELECT scd.store_key
		  , cal.tyDate_key AS date_key
		  , CAST(CASE
					 WHEN cal.tyDate_key BETWEEN scd.date_key_from AND scd.date_key_thru THEN 
						 1
					 ELSE
						 0
				 END AS TINYINT) AS isCompTY
		  , CAST(CASE
					 WHEN ISNULL(cal.nyDate_key,999999) BETWEEN scd.date_key_from AND scd.date_key_thru THEN
						 1
					 ELSE
						 0
				 END AS TINYINT) AS isCompNY
	 FROM StoreComp_Dim scd WITH(NOLOCK)
		 INNER JOIN (SELECT ty.date_key AS tyDate_key
						  , ny.date_key AS nyDate_key
					 FROM date_dim ty WITH(NOLOCK)
						 LEFT JOIN date_dim ny WITH(NOLOCK)
							 ON ny.week_id = ty.week_id + 52 
								AND ny.day_of_week = ty.day_of_week
		) cal
			 ON cal.tyDate_key BETWEEN scd.date_key_from AND scd.date_key_thru 
				OR ISNULL(cal.nyDate_key,999999) BETWEEN scd.date_key_from AND scd.date_key_thru
	) base
GROUP BY
	base.store_key
  , base.date_key
```

