# dbo.vwDW_Product_DimCurrent

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_Product_DimCurrent"]
    dbo_product_dim(["dbo.product_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.product_dim |

## View Code

```sql
CREATE VIEW [dbo].[vwDW_product_dimCurrent] --WIP]
AS
-- =============================================================================================================
-- Name: [dbo].[vwDW_product_dimWIP]
--
-- Description: View underlying the  Shared Product Dimension in the SSAS Papa Mart and Merch Cubes.   
-- Defines attributes for the dimension and levels for the hierarchies
--
-- Dependencies: 
--
-- Revision History
--		Name:					Date:			Comments:
--		Funmi Agbebi			3/31/2010		added fields for Jurisdiction and JurisdictionCodeKey
--												added fields for new Branded Merchandise Hierarchy Merch ClassCodeKey, Merch SubclassCodeKey, Merch StyleCodeKey
--												replaced dummy fields for sku 0 with single records in each division and jurisdiction
--												
--		Outside Consultant		2006			original creation
-- =============================================================================================================

	SELECT
		CAST(product_key AS varchar(50)) AS product_key, sku, activation_date, style_code, style_code + ' - ' + style_desc AS style_desc
		,subclass_code + '-' + style_code + '-' + color_code AS color_code, color_desc
		,product_desc, subclass_code + ' - ' + subclass AS subclass
		,SUBSTRING(subclass_code, 1, LEN(subclass_code) - 3) + ' - ' + class AS class
		,department_code + ' - ' + replace(replace(replace(department,'Can ',''),'Uk-',''),'Uk ','') AS department, department_code
		,SUBSTRING(subclass_code, 1, 5) + ' - ' + division AS division
		,chain, concept, priceline_code, subclass_code, class_code
		,SUBSTRING(subclass_code, 1, LEN(subclass_code) - 3) AS ClassCodeKey
		,SUBSTRING(subclass_code, 1, 5) AS DivisionCodeKey, subclass_code + '-' + style_code AS StyleCodeKey
		,primary_vendor_code, primary_vendor_name, alt_primary_vendor_code
		,current_retail, price_with_vat, euro_value, merch_status, ISNULL(wss_reportable, 'N') AS wss_reportable
		,ISNULL(reorder_flag, CAST(0 AS bit)) AS reorder_flag
		, current_selling_retail_home as USDollarCurrentRetail
		,cast(department_code  + '-' + jurisdiction_code as varchar(50)) as JurisdictionCodeKey
		,cast(jurisdiction_code + ' ' + replace(replace(replace(department,'Can ',''),'Uk-',''),'Uk ','') as varchar(100))  AS Jurisdiction     --  ,jurisdiction_code + ' ' + department AS Jurisdiction
		, CASE WHEN department_code like 'R-B-Z%'  
			   THEN cast(SUBSTRING(subclass_code, 1, LEN(subclass_code) - 3) + '-' + jurisdiction_code as varchar(75))
			   ELSE cast(SUBSTRING(subclass_code, 1, LEN(subclass_code) - 3) as varchar(75))
		 END AS MerchClassCodeKey
		, CASE WHEN department_code like 'R-B-Z%'  
			   THEN cast(subclass_code + '-' + jurisdiction_code as varchar(100))
			   ELSE cast(subclass_code as varchar(100)) 
		 END AS MerchSubclassCodeKey
		, CASE WHEN department_code like 'R-B-Z%'  
			   THEN cast(subclass_code + '-' + jurisdiction_code + '-' + style_code as varchar(150))
			   ELSE cast(subclass_code + '-' + style_code as varchar(150))
		 END AS MerchStyleCodeKey
	FROM papamart.dw.dbo.product_dim  with (nolock) 
--	FROM dwdev01.dw.dbo.product_dim_wip2 with (nolock) 
	WHERE subclass_code IS NOT NULL
```

