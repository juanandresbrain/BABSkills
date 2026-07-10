# dbo.vwDW_Registrations_Cube_V3

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_Registrations_Cube_V3"]
    date_dim(["date_dim"]) --> VIEW
    NameMeTransactionFact(["NameMeTransactionFact"]) --> VIEW
    StoreCompDetail_Dim(["StoreCompDetail_Dim"]) --> VIEW
    time_dim(["time_dim"]) --> VIEW
    dbo_vwDW_Product_Dim_V3(["dbo.vwDW_Product_Dim_V3"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| date_dim |
| NameMeTransactionFact |
| StoreCompDetail_Dim |
| time_dim |
| dbo.vwDW_Product_Dim_V3 |

## View Code

```sql
CREATE VIEW [dbo].[vwDW_Registrations_Cube_V3] AS

-- =============================================================================================================
-- Name: [dbo].[vwDW_Registrations_Cube]
--
-- Description: View underlying the SSAS Registrations Cube used on the dashboard.   
-- Aggregates Kiosk registrations and product group metrics by store and date
--
--
-- Dependencies: 
--
-- Revision History
--		Name:				Date:			Comments:
--		Gary Murrish		8/1/2012		Added Tourist Information
--		Gary Murrish		5/10/2012		Changed Store Comp Storage
--		Gary Murrish		5/2/2012		Added indicator whether or not this was within 15 days of Birthday
--		Gary Murrish		4/13/2012		Initial deployment
--		Tim Bytnar			5/22/2018		Lots of changes made to support the decommission of the Guest Load
-- =============================================================================================================


SELECT CASE
		   WHEN wrk.hasRecipientAge = 0 OR wrk.ReceipientAge < 0 THEN
			   CAST(-1 AS DECIMAL(4, 1)) -- Unspecified
		   WHEN wrk.ReceipientAge > 101 THEN
			   CAST(101 AS DECIMAL(4, 1))
		   ELSE
			   wrk.ReceipientAge
	   END AS RecepientAgeID
	 , wrk.RecepientID
	 , wrk.AddressID
	 , wrk.store_key
	 , wrk.date_key
	 , wrk.time_key
	 , ISNULL(pd.product_key, -1) AS product_key
	 , wrk.GST_VST_RECUR_CD
	 , wrk.ADDR_VST_RECUR_CD
	 , wrk.GIFT_IND
	 , wrk.GNDR_CD
	 , wrk.ReceipientAge
	 , wrk.hasRecipientAge
	 , wrk.PurchaserAge
	 , wrk.hasPurchaserAge
	 , wrk.DistanceToStore
	 , wrk.hasDistanceToStore
	 , wrk.isForeign
	 , wrk.TourismBand
	 , wrk.[5to25_MileBand]
	 , wrk.isComp
	 , wrk.isCompNextYear
	 , wrk.calc
	 , CASE
		   WHEN wrk.daysFromGstBirthDay < 0 AND wrk.daysFromReceipBirthDay < 0 THEN
			   -1
		   WHEN wrk.daysFromGstBirthDay BETWEEN 0 AND 15 OR wrk.daysFromGstBirthDay >= 300 OR wrk.daysFromReceipBirthDay BETWEEN 0 AND 15 OR wrk.daysFromReceipBirthDay >= 300 THEN
			   1
		   ELSE
			   0
	   END AS isNearBirthday
	 , wrk.isTourist
	 , wrk.GuestID
	 , wrk.isSOTF
	 , wrk.isShopperTrak
	 , wrk.isShopperTrakCompTY
	 , wrk.isShopperTrakCompNY
	 , wrk.TKF_ID
FROM
	(SELECT NTF.NameMeTransactionKey as TKF_ID
		  , -1 AS RecepientID
		  , -1 AS AddressID
		  , NTF.StoreKey AS store_key
		  , dd.date_key AS date_key
		  , CASE
				WHEN NTF.ProductKey <= 0 THEN
					-1
				ELSE
					NTF.ProductKey
			END AS product_key
		  , td.time_key AS time_key
		  , 'N' as GST_VST_RECUR_CD
		  , 'N' as ADDR_VST_RECUR_CD
		  , 'N' as GIFT_IND
		  , 'U' AS GNDR_CD
		  , 0.0 AS ReceipientAge
		  , 0 AS hasRecipientAge
		  , 0.0 AS PurchaserAge
		  , 0 AS hasPurchaserAge
		  , 0 AS DistanceToStore
		  , 0 AS hasDistanceToStore
		  , 0 AS isForeign
		  , -1 AS TourismBand
		  , -1 AS [5to25_MileBand]
		  , cast(isnull(cmp.isCompTY, 0) AS INTEGER) AS isComp
		  , cast(isnull(cmp.isCompNY, 0) AS INTEGER) AS isCompNextYear
		  , 1 AS calc
		  , 0 AS daysFromGstBirthDay
		  , 0 AS daysFromReceipBirthDay
		  , 0 AS isTourist
		  , -1 AS GuestID
		  , -1 AS Tourist_Addr_ID
		  , cast(isnull(cmp.isSOTF, 0) AS INTEGER) AS isSOTF
		  , cast(CASE
				WHEN cmp.isShopperTrak IS NULL THEN
					0
				WHEN cmp.isShopperTrak = 1 AND td.hour BETWEEN cmp.ShopperTrakStartHour AND cmp.ShopperTrakEndHour THEN
					1
				ELSE
					0
			END AS INTEGER) AS isShopperTrak
		  , cast(CASE
				WHEN cmp.isShopperTrakCompTY IS NULL THEN
					0
				WHEN cmp.isShopperTrakCompTY = 1 AND td.hour BETWEEN cmp.ShopperTrakStartHour AND cmp.ShopperTrakEndHour THEN
					1
				ELSE
					0
			END AS INTEGER) AS isShopperTrakCompTY
		  , cast(CASE
				WHEN cmp.isShopperTrakCompNY IS NULL THEN
					0
				WHEN cmp.isShopperTrakCompNY = 1 AND td.hour BETWEEN cmp.ShopperTrakStartHour AND cmp.ShopperTrakEndHour THEN
					1
				ELSE
					0
			END AS INTEGER) AS isShopperTrakCompNY
	 FROM
		 NameMeTransactionFact NTF WITH(NOLOCK)
		 LEFT JOIN date_dim dd
			ON CAST(NTF.TransactionStartDate as Date) = dd.actual_date
		 LEFT JOIN StoreCompDetail_Dim cmp WITH(NOLOCK)
			 ON cmp.store_key = NTF.StoreKey 
				AND cmp.date_key = dd.date_key
		LEFT JOIN time_dim td WITH(NOLOCK)
			ON DATEPART(hour,ntf.TransactionStartDate) = td.hour
				AND DATEPART(minute, ntf.TransactionStartDate) = td.minute
	) wrk
	LEFT OUTER JOIN dbo.vwDW_Product_Dim_V3 pd WITH(NOLOCK)
		ON pd.product_key = wrk.product_key
```

