# dbo.vwDW_Product_Dim_ProductHierarchyChange

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_Product_Dim_ProductHierarchyChange"]
    dbo_product_dim(["dbo.product_dim"]) --> VIEW
    dbo_vwDW_Product_Common(["dbo.vwDW_Product_Common"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.product_dim |
| dbo.vwDW_Product_Common |

## View Code

```sql
CREATE VIEW [dbo].[vwDW_Product_Dim_ProductHierarchyChange]
AS -- =============================================================================================================
-- Name: [dbo].[vwDW_product_dim]
--
-- Description: View underlying the  Shared Product Dimension in the SSAS Papa Mart and Merch Cubes.   
-- Defines attributes for the dimension and levels for the hierarchies
--
-- Dependencies: 
--
-- Revision History
--		Name:					Date:			Comments:
--		Gary Murrish			5/10/2012		Added Merchandise Gender, Core/Fashion, Inline Codes
--		Gary Murrish			5/3/2012		Introduced -1 Entry
--		Gary Murrish			8/23/2011		Show Jursidiction as a seperate field
--		Funmi Agbebi			5/12/2010		added Canadian dollar field
--
--		Funmi Agbebi			4/30/2010		replaced single record dummy fields for sku 0 with dummy records
--												for each division, department and style, necessary to make
--												style-level MERCHDB01 views (e.g. vwDW_WeeklyOnHand_Style) work.
--												product_key for dummy styles is subclass_code + style_code + jurisdiction_id
--
--		Funmi Agbebi			3/31/2010		added fields for Jurisdiction and JurisdictionCodeKey
--												added fields for new Branded Merchandise Hierarchy Merch ClassCodeKey, Merch SubclassCodeKey, Merch StyleCodeKey
--												replaced dummy fields for sku 0 with single records in each division and jurisdiction
--												
--		Outside Consultant		2006			original creation
-- =============================================================================================================

SELECT cast(prd.product_key AS VARCHAR(50)) AS product_key
	 , sku
	 , activation_date
	 , style_code
	 , style_code + ' - ' + style_desc AS style_desc
	 , subclass_code + '-' + style_code + '-' + color_code AS color_code
	 , color_desc
	 , product_desc
	 , subclass_code + ' - ' + subclass AS subclass
	 , substring(subclass_code, 1, len(subclass_code) - 3) + ' - ' + class AS class
	 , department_code + ' - ' + replace(replace(replace(department, 'Can ', ''), 'Uk-', ''), 'Uk ', '') AS department
	 , department_code
	 , substring(subclass_code, 1, 5) + ' - ' + division AS division
	 , chain
	 , concept
	 , priceline_code
	 , subclass_code
	 , class_code
	 , substring(subclass_code, 1, len(subclass_code) - 3) AS ClassCodeKey
	 , substring(subclass_code, 1, 5) AS DivisionCodeKey
	 , subclass_code + '-' + style_code AS StyleCodeKey
	 , primary_vendor_code
	 , primary_vendor_name
	 , alt_primary_vendor_code
	 , current_retail
	 , price_with_vat
	 , euro_value
	 , merch_status
	 , isnull(wss_reportable, 'N') AS wss_reportable
	 , isnull(reorder_flag, cast(0 AS BIT)) AS reorder_flag
	 , current_selling_retail_home AS USDollarCurrentRetail
	 , cdn_value AS CADollarCurrentRetail
	 --Fields for R-B-Z division.  New addition starts (FA - 3/31/2010)
	 , cast(department_code + '-' + jurisdiction_code AS VARCHAR(50)) AS JurisdictionCodeKey
	 , cast(jurisdiction_code + ' ' + replace(replace(replace(department, 'Can ', ''), 'Uk-', ''), 'Uk ', '') AS VARCHAR(100)) AS Jurisdiction
	 , CASE
		   WHEN department_code LIKE 'R-B-Z%' THEN
			   cast(substring(subclass_code, 1, len(subclass_code) - 3) + '-' + jurisdiction_code AS VARCHAR(75))
		   ELSE
			   cast(substring(subclass_code, 1, len(subclass_code) - 3) AS VARCHAR(75))
	   END AS MerchClassCodeKey
	 , CASE
		   WHEN department_code LIKE 'R-B-Z%' THEN
			   cast(subclass_code + '-' + jurisdiction_code AS VARCHAR(100))
		   ELSE
			   cast(subclass_code AS VARCHAR(100))
	   END AS MerchSubclassCodeKey
	 , CASE
		   WHEN department_code LIKE 'R-B-Z%' THEN
			   cast(subclass_code + '-' + jurisdiction_code + '-' + style_code AS VARCHAR(150))
		   ELSE
			   cast(subclass_code + '-' + style_code AS VARCHAR(150))
	   END AS MerchStyleCodeKey
	 --Fields for R-B-Z division.  New addition ends (FA - 3/31/2010)
	 , jurisdiction_code AS plain_Jurisdiction
	 , CASE
		   WHEN department_code IN (

			   /* Excluded Products */

			   'R-B-D-65', 'R-B-D-70', 'R-B-D-51', 'R-B-D-60', 'R-B-D-45', 'R-B-D-46', 'R-B-D-47', 'R-B-D-50', 'R-B-D-75', 'R-B-D-80', 'R-B-U-60', 'R-B-U-70', 'R-B-U-45', 'R-B-U-46', 'R-B-U-47',

			   /*'R-B-U-48',*/

			   'R-B-U-50', 'R-B-U-75', 'R-B-U-80', 'R-B-C-60', 'R-B-C-45', 'R-B-C-46',

			   /*'R-B-C-48', */

			   'R-B-C-50', 'R-B-C-75', 'R-B-C-80', 'R-B-B-75', 'R-B-B-80') THEN
			   1
		   ELSE
			   0
	   END AS Exclude_From_WSS
	 , CASE
		   WHEN department_code IN (

			   /* Omitted Departments */

			   'R-B-D-65', 'R-B-D-70', 'R-B-D-51', 'R-B-D-60', 'R-B-U-60', 'R-B-U-70', 'R-B-C-60') THEN
			   'Y'
		   ELSE
			   'N'
	   END AS Omit_From_WSS
	 , cmn.cmn_department_code
	 , cmn.cmn_department
	 , cmn.cmn_class_code
	 , cmn.cmn_class
	 , cmn.cmn_subclass_code
	 , cmn.cmn_subclass
	 , cmn.cmn_style_code
	 , cmn.cmn_style
	 , isnull(prd.gender,'Unknown') AS Gender 
	 , isnull(prd.CORE_FASH_CD, 'Unknown') AS CoreFashion
	 , isnull(prd.INLINE_CD, 'Unknown') AS Inline
FROM
	wbnscoredev01.dw.dbo.product_dim prd WITH (NOLOCK)
	INNER JOIN wbnscoredev01.dw.dbo.vwDW_Product_Common cmn WITH (NOLOCK)
		ON cmn.product_key = prd.product_key
WHERE
	subclass_code IS NOT NULL
UNION ALL
SELECT cast(-1 AS VARCHAR(50)) AS product_key
	 , -1 AS sku
	 , cast('1/1/1900' AS DATETIME) AS activation_date
	 , 'Unknown' AS style_code
	 , 'Unknown' AS style_desc
	 , 'Unknown' AS color_code
	 , 'Unknown' AS color_desc
	 , 'Unknown' AS product_desc
	 , 'Unknown' AS subclass
	 , 'Unknown' AS class
	 , 'Unknown' AS department
	 , 'Unknown' AS department_code
	 , 'Unknown' AS division
	 , 'Unknown' AS chain
	 , 'Unknown' AS concept
	 , 'Unknown' AS priceline_code
	 , 'Unknown' AS subclass_code
	 , 'Unknown' AS class_code
	 , 'Unknown' AS ClassCodeKey
	 , 'Unk' AS DivisionCodeKey
	 , 'Unknown' AS StyleCodeKey
	 , 'Unknown' AS primary_vendor_code
	 , 'Unknown' AS primary_vendor_name
	 , 'Unknown' AS alt_primary_vendor_code
	 , 0 AS current_retail
	 , 0 AS price_with_vat
	 , 0 AS euro_value
	 , 'Unk' AS merch_status
	 , 'N' AS wss_reportable
	 , cast(0 AS BIT) AS reorder_flag
	 , 0 AS USDollarCurrentRetail
	 , 0 AS CADollarCurrentRetail
	 --Fields for R-B-Z division.  New addition starts (FA - 3/31/2010)
	 , 'Unknown' AS JurisdictionCodeKey
	 , 'Unknown' AS Jurisdiction
	 , 'Unknown' AS MerchClassCodeKey
	 , 'Unknown' AS MerchSubclassCodeKey
	 , 'Unknown' AS MerchStyleCodeKey
	 --Fields for R-B-Z division.  New addition ends (FA - 3/31/2010)
	 , 'Unknown' AS plain_Jurisdiction
	 , 1 AS Exclude_From_WSS
	 , 'Y' AS Omit_From_WSS
	 , 'Unknown' AS cmn_department_code
	 , 'Unknown' AS cmn_department
	 , 'Unknown' AS cmn_class_code
	 , 'Unknown' AS cmn_class
	 , 'Unknown' AS cmn_subclass_code
	 , 'Unknown' AS cmn_subclass
	 , 'Unknown' AS cmn_style_code
	 , 'Unknown' AS cmn_style
	 , 'Unknown' AS Gender 
	 , 'Unknown' AS CoreFashion
	 , 'Unknown' AS Inline
```

