# dbo.Azure_vwProducts

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.Azure_vwProducts"]
    dbo_Azure_vwPricing(["dbo.Azure_vwPricing"]) --> VIEW
    dbo_attribute_dim(["dbo.attribute_dim"]) --> VIEW
    dbo_azure_prodfactory(["dbo.azure_prodfactory"]) --> VIEW
    dbo_azure_prodlicense(["dbo.azure_prodlicense"]) --> VIEW
    dbo_azure_prodmstat(["dbo.azure_prodmstat"]) --> VIEW
    dbo_azure_productchainonhandcost(["dbo.azure_productchainonhandcost"]) --> VIEW
    dbo_azure_productsbrf(["dbo.azure_productsbrf"]) --> VIEW
    dbo_azure_styleattributes(["dbo.azure_styleattributes"]) --> VIEW
    dbo_azure_webactivedate(["dbo.azure_webactivedate"]) --> VIEW
    dbo_integrationstaging_web_inventoryfact(["dbo.integrationstaging_web_inventoryfact"]) --> VIEW
    dbo_product_dim(["dbo.product_dim"]) --> VIEW
    dbo_vwFranchiseeProductAttribute(["dbo.vwFranchiseeProductAttribute"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Azure_vwPricing |
| dbo.attribute_dim |
| dbo.azure_prodfactory |
| dbo.azure_prodlicense |
| dbo.azure_prodmstat |
| dbo.azure_productchainonhandcost |
| dbo.azure_productsbrf |
| dbo.azure_styleattributes |
| dbo.azure_webactivedate |
| dbo.integrationstaging_web_inventoryfact |
| dbo.product_dim |
| dbo.vwFranchiseeProductAttribute |

## View Code

```sql
CREATE VIEW dbo.Azure_vwProducts AS WITH  Attibutes AS  	( 		SELECT         			RIGHT(CAST('000000' AS varchar(6)) + CAST(style_code AS varchar(6)), 6) AS Style_Code,  			AttributeName,  			AttributeValue         FROM  dbo.attribute_dim          WHERE   			AttributeName IN ('IDATE', 'ODATE', 'ONOTE', 'OUTLET', 'OMSTAT') 	),  AttrPivot AS     ( 		SELECT         			RIGHT(CAST('000000' AS varchar(6)) + CAST(Style_Code AS varchar(6)), 6) AS style_code,  			CASE  				WHEN AttributeName = 'IDATE'  					THEN --AttributeValue  						MIN(cast( 								case 									when isdate(replace(replace(replace(replace(AttributeValue, '\', '-'), '/', '-'), '.', '-'), ' ', '')) = 1 									then cast( replace(replace(replace(replace(AttributeValue, '\', '-'), '/', '-'), '.', '-'), ' ', '') as date) 									--else '1999-12-31' 									else NULL 								end 						as date)) 				ELSE NULL  			END AS IDATE,              CASE  				WHEN AttributeName = 'ODATE'  					THEN --AttributeValue  					MAX(cast( 								case 									when isdate(replace(replace(replace(replace(AttributeValue, '\', '-'), '/', '-'), '.', '-'), ' ', '')) = 1 									then cast( replace(replace(replace(replace(AttributeValue, '\', '-'), '/', '-'), '.', '-'), ' ', '') as date) 									--else '1999-12-31' 									else NULL 								end 						as date)) 				ELSE NULL  			END AS ODATE,  			CASE  				WHEN AttributeName = 'ONOTE'  					THEN AttributeValue  				ELSE NULL  			END AS ONOTE,              CASE  				WHEN AttributeName = 'OUTLET'  					THEN AttributeValue  				ELSE NULL  			END AS OUTLET,  			CASE  				WHEN AttributeName = 'OMSTAT'  					THEN AttributeValue  				ELSE NULL  			END AS OMSTAT 		FROM Attibutes 		group by  			RIGHT(CAST('000000' AS varchar(6)) + CAST(Style_Code AS varchar(6)), 6), 			AttributeName, 			AttributeValue 	),  MaxAttr AS     ( 		SELECT         			RIGHT(CAST('000000' AS varchar(6)) + CAST(style_code AS varchar(6)), 6) AS style_code,  			MIN(IDATE) AS IDATE,  			MAX(ODATE) AS ODATE,  			MAX(ONOTE) AS ONOTE,  			MAX(OUTLET) AS OUTLET,  			MAX(OMSTAT) AS OMSTAT 		FROM  AttrPivot 		--where isnull(ODATE, getdate()) <= getdate() 		GROUP BY style_code 	),  FilteredKeystories AS     ( 		SELECT 			CAST(style_code AS varchar(10)) AS Style_Code,  			MIN(AttributeValue) AS KeyStory 		FROM  dbo.attribute_dim 		WHERE  AttributeName = 'KEYSTY' 		GROUP BY style_code 	),  KeyStories AS     ( 		SELECT         			s.style_code,  			MAX(s.KeyStory) AS KeyStory       FROM             		dbo.product_dim AS s  		--WHERE  		--	 ecp.parent_type = 1  		--		AND ecp.custom_property_id = 60       GROUP BY s.style_code 	 ), unitCost as 	( 		select  			ProductKey, 			ChainAverageOnHandCost, 			ChainAverageOnHandCostGBP 		from [dbo].[azure_productchainonhandcost] -->> this table is loaded nightly at 1am via stl-ssis-p-01 sql agent UKLoyaltyLoad --> job does other ETLs then loads this table via [Azure].[spProductChainAverageOnHandCost] 	), webInventory as 	( 	select  			  StyleCode, 			  max(UnbufferedQty) as 'UnbufferedQty' 		from LH_Source.dbo.integrationstaging_web_inventoryfact 		where LocationCode in ( '0013', '2013') 		group by StyleCode     ) SELECT         	pd.product_key AS ProductKey,  	pd.style_code AS Style,  	ISNULL(pd.style_desc, pd.product_desc) AS StyleDescription,  	pd.color_desc AS Color,  	pd.concept,  	pd.chain,  	pd.division,  	pd.department,  	pd.class,  	pd.subclass,      pd.department_code AS DeptCode,  	pd.subclass_code AS SubClassCode,  	pd.ScorecardCategory,  	pd.primary_vendor_code AS PrimaryVendorCode,  	pd.primary_vendor_name AS PrimaryVendorName,      pd.alt_primary_vendor_code AS AltPrimaryVendorCode,  	pd.current_retail AS CurrentRetail,  	pd.original_retail AS OriginalRetail,  	pd.current_selling_retail_home AS CurrentSellingRetailHome,  	pd.price_with_vat AS PriceWithVat,      pd.euro_value AS EuroValue,  	pd.cdn_value AS CanValue,  	pd.merch_status AS MerchStatus,  	pd.jurisdiction_code AS JurisdictionCode,  	pd.GENDER,  	pd.CORE_FASH_CD AS CoreFashCode,  	pd.INLINE_CD AS InlineCode,      CAST(pd.activation_date AS date) AS ActivationDate,  	KeyStories.KeyStory,  	ma.IDATE,  	ma.ODATE,  	ma.ONOTE,  	ma.OUTLET,  	ma.OMSTAT,  	ISNULL(CA.AU_CustomAttribute1, KeyStories.KeyStory) AS altKeyStory,      P.Current_Selling_Retail AS HomeCurrentRetail,  	P.Original_Selling_Retail AS HomeOriginalRetail,  	P.IE_Current_Retail AS IECurrentRetail,  	P.IE_Original_Retail AS IEOriginalRetail,  	P.DK_Current_Retail AS DKCurrentRetail,      P.DK_Original_Retail AS DKOriginalRetail,  	b01.LicenseCode,  	b01.LicenseDescription,  	b02.FactoryCode,  	b02.FactoryName,  	b01.Primary_Vendor_Cur_Cost,  	b04.MSTAT, 0 AS BufferQTY,  	WA.WebActiveDate,  	SA.RoyaltyStyle,      SA.WebStatus,  	SA.WholeSaleStatus, 	isnull(UC.ChainAverageOnHandCost,0) as ChainAverageOnHandCost, 	isnull(UC.ChainAverageOnHandCostGBP,0) as ChainAverageOnHandCostGBP, 	isnull(brf.isBRFstyle,0) as isBRFstyle, 	isnull(wi.UnbufferedQty,0) as WebInventory FROM  dbo.product_dim AS pd  left join MaxAttr AS ma ON pd.style_code = ma.style_code  left join FilteredKeystories AS fk ON pd.style_code = fk.Style_Code  left join dbo.vwFranchiseeProductAttribute AS CA ON pd.style_code = CA.StyleCode  left join KeyStories ON pd.style_code = KeyStories.style_code  left join dbo.Azure_vwPricing AS P ON pd.product_key = P.ProductKey  left join [dbo].[azure_prodlicense] AS b01 ON pd.product_key = b01.ProductKey  left join [dbo].[azure_prodfactory] AS b02 ON pd.product_key = b02.ProductKey  left join [dbo].[azure_prodmstat] AS b04 ON pd.product_key = b04.ProductKey  left join [dbo].[azure_webactivedate] AS WA ON pd.style_code = WA.Style  left join [dbo].[azure_styleattributes] AS SA ON pd.style_code = SA.StyleCode left join unitCost as UC ON pd.product_key = UC.ProductKey left join dbo.azure_productsbrf brf on pd.product_key = brf.ProductKey left join webInventory wi on wi.StyleCode = pd.style_code  WHERE    	pd.style_code IS NOT NULL  	AND pd.style_code <> 'N/A'        					 ----------------------------------------------------------------------------------------------------------------------------------
```

