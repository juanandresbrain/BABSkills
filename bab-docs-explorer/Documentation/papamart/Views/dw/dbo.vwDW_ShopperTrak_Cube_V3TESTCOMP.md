# dbo.vwDW_ShopperTrak_Cube_V3TESTCOMP

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_ShopperTrak_Cube_V3TESTCOMP"]
    date_dim(["date_dim"]) --> VIEW
    ShopperTrackFact(["ShopperTrackFact"]) --> VIEW
    StoreCompDetail_Dim(["StoreCompDetail_Dim"]) --> VIEW
    time_dim(["time_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| date_dim |
| ShopperTrackFact |
| StoreCompDetail_Dim |
| time_dim |

## View Code

```sql
CREATE view [dbo].[vwDW_ShopperTrak_Cube_V3TESTCOMP] --WITH SCHEMABINDING
as

WITH hasTraf as
	(
		select 
			StoreKey AS store_key,
			DateKey AS date_key,
			case when sum(EXITS) = 0 
					then 0
				else 1
			end as hasTraffic
		FROM
			ShopperTrackFact STTF WITH (NOLOCK)
		group by 
			StoreKey,
			DateKey
	)

SELECT StoreKey AS store_key
	 , DateKey AS date_key
	 , TimeKey AS time_key
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
	   END AS INTEGER) AS isSTComp,
	 
	 --, cast(isnull(cmpFuture.isShopperTrakCompTY,0) as Integer) as isSTCompNextYear --ADDED 2022-08-08
	 cast(CASE
		   WHEN cmp.isShopperTrakCompTY IS NULL THEN
			   0
		   WHEN cmp.isShopperTrakCompTY = 1 
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
	ShopperTrackFact STTF WITH (NOLOCK)
	INNER JOIN date_dim dd WITH (NOLOCK)
		ON dd.date_key = STTF.DateKey
	INNER JOIN time_dim td WITH (NOLOCK)
		ON td.time_key = STTF.TimeKey
	LEFT JOIN StoreCompDetail_Dim cmp WITH (NOLOCK)
		ON cmp.store_key = STTF.StoreKey AND cmp.date_key = STTF.DateKey
	INNER JOIN hasTraf ht on STTF.StoreKey = ht.store_key
		and dd.date_key = ht.date_key
--NEW 20220808
left join date_dim ddFuture with (nolock)
	on dd.week_id+(52*2)=ddFuture.week_id
	and dd.day_of_week=ddFuture.day_of_week
left join StoreCompDetail_Dim cmpFuture WITH (NOLOCK)
		ON cmp.store_key = cmpFuture.store_key
		AND ddFuture.date_key=cmpFuture.date_key
WHERE
	(ENTERS <> 0
	OR EXITS <> 0)
```

