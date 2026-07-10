# dbo.vwDW_ShopperTrak_Cube_V3_bak_20200603

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_ShopperTrak_Cube_V3_bak_20200603"]
    date_dim(["date_dim"]) --> VIEW
    SHPR_TRK_TRFC_FCT(["SHPR_TRK_TRFC_FCT"]) --> VIEW
    StoreCompDetail_Dim(["StoreCompDetail_Dim"]) --> VIEW
    time_dim(["time_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| date_dim |
| SHPR_TRK_TRFC_FCT |
| StoreCompDetail_Dim |
| time_dim |

## View Code

```sql
CREATE VIEW [dbo].[vwDW_ShopperTrak_Cube_V3_bak_20200603] AS
-- =============================================================================================================
-- Name: [dbo].[vwDW_ShopperTrak_Cube_V3]
--
-- Description: View underlying the SSAS ShopperTrak Cube used on the dashboard.   
-- Aggregates ShopperTrak metrics by store and date
--
--
-- Dependencies: 
--
-- Revision History
--		Name:				Date:			Comments:
--		Gary Murrish		9/12/2012		Changed source for ShopperTrak Comp information
--		Gary Murrish		6/8/2012		Added ShopperTrak Comp and isShopperTrakHours
--		Gary Murrish		5/24/2012		Added Calc Attribute
--		Gary Murrish		5/7/2012		Initial deployment
--		Dan Tweedie			06/21/2016		Added hasTraffic column
--		Dan Tweedie			06/29/2016		Removed 'AND td.hour BETWEEN cmp.ShopperTrakStartHour AND cmp.ShopperTrakEndHour'  so no longer filtering by this
-- =============================================================================================================

WITH hasTraf as
	(
		select 
			STR_KEY AS store_key,
			DT_KEY AS date_key,
			case when sum(EXITS) = 0 
					then 0
				else 1
			end as hasTraffic
		FROM
			SHPR_TRK_TRFC_FCT STTF WITH (NOLOCK)
		group by 
			STR_KEY,
			DT_KEY
	)

SELECT STR_KEY AS store_key
	 , DT_KEY AS date_key
	 , TM_KEY AS time_key
	 , ENTERS
	 , EXITS
	 , 1 AS calc
	 , cast(CASE
		   WHEN cmp.isShopperTrak IS NULL THEN
			   0
		   WHEN cmp.isShopperTrak = 1 
		   --AND td.hour BETWEEN cmp.ShopperTrakStartHour AND cmp.ShopperTrakEndHour 
			   THEN
				   1
		   ELSE
			   0
	   END AS SMALLINT) AS isShopperTrakHours
	 , cast(CASE
		   WHEN cmp.isShopperTrakCompTY IS NULL THEN
			   0
		   WHEN cmp.isShopperTrakCompTY = 1 
		   --AND td.hour BETWEEN cmp.ShopperTrakStartHour AND cmp.ShopperTrakEndHour 
			   THEN
				   1
		   ELSE
			   0
	   END AS INTEGER) AS isSTComp
	 , cast(CASE
		   WHEN cmp.isShopperTrakCompNY IS NULL THEN
			   0
		   WHEN cmp.isShopperTrakCompNY = 1 
		   --AND td.hour BETWEEN cmp.ShopperTrakStartHour AND cmp.ShopperTrakEndHour 
			   THEN
				   1
		   ELSE
			   0
	   END AS INTEGER) AS isSTCompNextYear
	 , cast(isnull(cmp.isCompTY, 0) AS INTEGER) AS isCompThisYear
	 , cast(isnull(cmp.isCompNY, 0) AS INTEGER) AS isCompNextYear
	 , cast(isnull(cmp.isSOTF, 0) AS INTEGER) AS isSOTF
	 , hasTraffic
FROM
	SHPR_TRK_TRFC_FCT STTF WITH (NOLOCK)
	INNER JOIN date_dim dd WITH (NOLOCK)
		ON dd.date_key = STTF.DT_KEY
	INNER JOIN time_dim td WITH (NOLOCK)
		ON td.time_key = STTF.TM_KEY
	LEFT JOIN StoreCompDetail_Dim cmp WITH (NOLOCK)
		ON cmp.store_key = STTF.STR_KEY AND cmp.date_key = STTF.DT_KEY
	INNER JOIN hasTraf ht on STTF.STR_KEY = ht.store_key
		and dd.date_key = ht.date_key

WHERE
	(ENTERS <> 0
	OR EXITS <> 0)
```

