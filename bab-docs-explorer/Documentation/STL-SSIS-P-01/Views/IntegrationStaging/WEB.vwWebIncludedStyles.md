# WEB.vwWebIncludedStyles

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["WEB.vwWebIncludedStyles"]
    WEB_ProductCatalogMasterAttributes(["WEB.ProductCatalogMasterAttributes"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| WEB.ProductCatalogMasterAttributes |

## View Code

```sql
CREATE view WEB.[vwWebIncludedStyles]

as




-- =====================================================================================================
-- Name: WEB.vwWebIncludedStyles
--
-- Purpose: Captures style, description AND UPC for products which will be included IN eCommerce integration.
--						Included style criteria:
--						Does NOT have WEBNO style attribute
--						Does have AVAILB style attribute set to one of these values:  ('US', 'USWEB', 'DINO', 'UK', 'UKWEB')
--						Logically captures UPC based on being either one of our purchased UPCs (GS1), having max(date) or max(upc)
--
-- Revision History
--		Name:			Date:			Comments:
--		lizzy Timm		02/26/2025		Created view based on bedrockdb02.IntegrationStaging.vwWebIncludedStyles
-- =====================================================================================================


WITH
Styles as
	(
		SELECT DISTINCT 
			style_code
			, DisplayName AS SKUDescription
			, HierarchyGroupCode
		FROM IntegrationStaging.WEB.ProductCatalogMasterAttributes s
		WHERE 1=1
		AND AVAILB = 'True'
	),
ExcludedStyles as
	(
		SELECT DISTINCT Style_Code
		FROM IntegrationStaging.WEB.ProductCatalogMasterAttributes 
		WHERE Web = 'WEBNO'
	),
IncludedStyles as 
	(
		SELECT DISTINCT 
			style_code
			,ProductSellingGeography AS SellingGeography
		FROM IntegrationStaging.WEB.ProductCatalogMasterAttributes s
		WHERE 1=1
		AND AVAILB = 'True'
		AND ProductSellingGeography IN ('UK','US')
		AND NOT EXISTS (select e.style_code from ExcludedStyles e where e.style_code = s.style_code)
	), 
UPCs as
	(

		SELECT DISTINCT BaseID
			, Style_Code
			, ColorCode [Color]
			, UPC
		FROM IntegrationStaging.WEB.ProductCatalogMasterAttributes u 		
		WHERE EXISTS (SELECT s.Style_Code FROM IncludedStyles s WHERE s.Style_Code = u.Style_Code)
	),
OWNRSP as 
	(

		SELECT DISTINCT 
			style_code
		FROM IntegrationStaging.WEB.ProductCatalogMasterAttributes s
		WHERE 1=1
		AND NOT EXISTS (select i.style_code from IncludedStyles i where i.style_code = s.style_code)
		AND CAST(LEFT(Style_Code,1) AS int) NOT IN (1,8) -- Exclude CN and CAN OWNRSP
	),
StoreFrontEligible as
	(
		SELECT 
			s.style_code,
			s.HierarchyGroupCode,
			cast(s.SKUDescription as varchar(120)) as SKUDescription,
			u.Color,
			cast(u.UPC as varchar(20)) as UPC,
			i.SellingGeography,
			1 as StoreFrontEligible
		FROM styles s
		JOIN UPCs u on s.style_code = u.style_code
		JOIN IncludedStyles i on s.style_code = i.style_code
	),
NotStoreFrontEligible as
	(
		SELECT 
			s.style_code,
			s.HierarchyGroupCode,
			cast(s.SKUDescription as varchar(120)) as SKUDescription,
			NULL as Color,
			NULL as UPC,
			NULL as SellingGeography,
			0 as StoreFrontEligible
		FROM styles s
		JOIN OWNRSP O on s.style_code = O.style_code
		WHERE NOT EXISTS (SELECT i.style_code FROM StoreFrontEligible i WHERE i.style_code = s.style_code)
	),
UNIONS as
	(
		SELECT * FROM StoreFrontEligible
		UNION
		SELECT * FROM NotStoreFrontEligible
	)
SELECT * 
FROM UNIONS












WEB,vwWebLocations,CREATE VIEW WEB.vwWebLocations
AS
WITH OpenStores AS
(--this view returns open stores, based on open/close dates in Store MDM
	SELECT StoreID
	FROM kodiak.babwmstrdata.dbo.vwDW_OpenStores
)
, LocationCode AS
(
	SELECT DISTINCT WarehouseID -- D365
		, RIGHT('0000'+ISNULL(LocationCode,''),4) LocationCode -- Aptos
		, CAST(LocationCode AS INT) StoreID
		, Entity
	FROM ERP.vwWarehouseIDToLocationCode
	WHERE 1=1
		AND CAST(LocationCode AS INT) IN (SELECT DISTINCT StoreID FROM OpenStores)
)
SELECT DISTINCT 
	 sd.store_name  AS LocationName
	, UPPER(sd.postal_code) AS ZipCode
	, lc.LocationCode AS Code
	, CASE WHEN UPPER(sd.Country) in ('CAN', 'CAF', 'CA', 'MX', 'MEX', 'US', 'USA') 
		THEN 'US' 
		else 'UK'
	END AS SiteID
	, CASE WHEN lc.LocationCode in ('0013', '2013') 
		THEN 'Warehouse'
		else 'Store'
	END AS LocationType
  FROM Papamart.DW.dbo.store_dim sd (nolock)
	JOIN LocationCode lc ON sd.Store_ID = lc.StoreID 
	JOIN OpenStores os on cast(lc.StoreID as int) = os.StoreID 
  WHERE 1=1
	AND UPPER(sd.Country) NOT IN ('CN','CHN')
```

