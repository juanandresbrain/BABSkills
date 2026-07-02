# dbo.vwItem_BABWSupplyItems_v4

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwItem_BABWSupplyItems_v4"]
    dbo_attribute_set(["dbo.attribute_set"]) --> VIEW
    dbo_entity_attribute_set(["dbo.entity_attribute_set"]) --> VIEW
    dbo_entity_custom_property(["dbo.entity_custom_property"]) --> VIEW
    dbo_hierarchy_group(["dbo.hierarchy_group"]) --> VIEW
    dbo_keith_average_cost(["dbo.keith_average_cost"]) --> VIEW
    dbo_sku(["dbo.sku"]) --> VIEW
    dbo_style(["dbo.style"]) --> VIEW
    dbo_style_detail(["dbo.style_detail"]) --> VIEW
    dbo_style_group(["dbo.style_group"]) --> VIEW
    dbo_upc(["dbo.upc"]) --> VIEW
    WMS_ItemMaster(["WMS.ItemMaster"]) --> VIEW
    WMS_ItemMasterProducts(["WMS.ItemMasterProducts"]) --> VIEW
    WMS_ItemsUOM(["WMS.ItemsUOM"]) --> VIEW
    WMS_vwItemType(["WMS.vwItemType"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.attribute_set |
| dbo.entity_attribute_set |
| dbo.entity_custom_property |
| dbo.hierarchy_group |
| dbo.keith_average_cost |
| dbo.sku |
| dbo.style |
| dbo.style_detail |
| dbo.style_group |
| dbo.upc |
| WMS.ItemMaster |
| WMS.ItemMasterProducts |
| WMS.ItemsUOM |
| WMS.vwItemType |

## View Code

```sql
CREATE VIEW [dbo].[vwItem_BABWSupplyItems_v4] AS

WITH d365Supplies_NA
AS
(
	SELECT RIGHT('000000000000' + im.ProductNumber, 12) AS 'upc_number'
				   ,d.PRODUCTNAME AS 'short_desc'
				   ,d.PRODUCTNAME AS 'long_desc'
				   ,'R-B-D-60-00-00' AS 'hierarchy_group_code'
				   --,c1.FACTOR as 'distribution_multiple'
				   ,1 as 'distribution_multiple'
				   ,im.ProductNumber AS 'style_code'
				   ,im.UnitCost AS 'cost'
				   ,c2.FACTOR as 'std_pack_qty'
	--INTO #SVWORKV11_1  
	FROM [STL-SSIS-P-01].[IntegrationStaging].[WMS].[ItemMaster] im
    INNER JOIN [STL-SSIS-P-01].[IntegrationStaging].WMS.vwItemType it WITH (NOLOCK) ON im.ProductNumber=it.ItemNumber and im.Entity=it.entity
	--LEFT JOIN [STL-SSIS-T-01].[IntegrationStaging].WMS.ItemsUOM c1 WITH (NOLOCK) ON im.ProductNumber = c1.PRODUCTNUMBER AND c1.Entity = 1100 AND im.InventoryUnitSymbol = c1.FROMUNITSYMBOL
	LEFT JOIN [STL-SSIS-P-01].[IntegrationStaging].WMS.ItemsUOM c2 WITH (NOLOCK) ON im.ProductNumber = c2.PRODUCTNUMBER AND c2.Entity = 1100 AND im.PurchaseUnitSymbol = c2.FROMUNITSYMBOL AND c2.ToUnitSymbol = 'WMEA'
	LEFT JOIN [STL-SSIS-P-01].[IntegrationStaging].WMS.ItemMasterProducts d WITH (NOLOCK) ON im.ProductNumber = d.PRODUCTNUMBER
	WHERE im.Entity = 1100 AND it.ItemType = 'Supplies' 
	--GROUP BY im.ProductNumber, d.PRODUCTNAME, im.UnitCost
	--ORDER BY a.PRODUCTNUMBER
 
),
d365Supplies_UK
AS
(
	SELECT RIGHT('000000000000' + im.ProductNumber, 12) AS 'upc_number'
				   ,d.PRODUCTNAME AS 'short_desc'
				   ,d.PRODUCTNAME AS 'long_desc'
				   ,'R-B-D-60-00-00' AS 'hierarchy_group_code'
				   --,c1.FACTOR as 'distribution_multiple'
				   ,1 as 'distribution_multiple'
				   ,im.ProductNumber AS 'style_code'
				   ,im.UnitCost AS 'cost'
				   ,c2.FACTOR as 'std_pack_qty'
	--INTO #SVWORKV11_1  
	FROM [STL-SSIS-P-01].[IntegrationStaging].[WMS].[ItemMaster] im
    INNER JOIN [STL-SSIS-P-01].[IntegrationStaging].WMS.vwItemType it WITH (NOLOCK) ON im.ProductNumber=it.ItemNumber and im.Entity=it.entity
	--LEFT JOIN [STL-SSIS-T-01].[IntegrationStaging].WMS.ItemsUOM c1 WITH (NOLOCK) ON im.ProductNumber = c1.PRODUCTNUMBER AND c1.Entity = 2110 AND im.InventoryUnitSymbol = c1.FROMUNITSYMBOL
	LEFT JOIN [STL-SSIS-P-01].[IntegrationStaging].WMS.ItemsUOM c2 WITH (NOLOCK) ON im.ProductNumber = c2.PRODUCTNUMBER AND c2.Entity = 2110 AND im.PurchaseUnitSymbol = c2.FROMUNITSYMBOL AND c2.ToUnitSymbol = 'WMEA'
	LEFT JOIN [STL-SSIS-P-01].[IntegrationStaging].WMS.ItemMasterProducts d WITH (NOLOCK) ON im.ProductNumber = d.PRODUCTNUMBER
	WHERE im.Entity = 2110 AND it.ItemType = 'Supplies' 
	--GROUP BY im.ProductNumber, d.PRODUCTNAME, im.UnitCost
	--ORDER BY a.PRODUCTNUMBER
 
),
d365Supplies_UK_preUnion
AS
(
	SELECT upc_number
	FROM d365Supplies_UK
	EXCEPT 
	SELECT upc_number
	FROM d365Supplies_NA
),
d365Supplies
AS
(
	SELECT *
	FROM d365Supplies_NA
	UNION
	SELECT *
	FROM d365Supplies_UK
	WHERE upc_number IN (SELECT upc_number FROM d365Supplies_UK_preUnion)
),
merchItems_availb
AS
(
	SELECT u.upc_number
	,st.short_desc
	,st.long_desc
	,hierarchy_group_code
	,st.distribution_multiple
	,st.style_code
	,isnull(average_cost, 0.00) as cost
 	,max(case when ecp.custom_property_value is null then st.distribution_multiple else cast(cast(ecp.custom_property_value as float) as int) end) std_pack_qty
	FROM 	me_01.dbo.upc u WITH (NOLOCK)
	INNER JOIN me_01.dbo.sku sku WITH (NOLOCK) on u.sku_id = sku.sku_id 
	INNER JOIN me_01.dbo.style st WITH (NOLOCK) on st.style_id = sku.style_id 
	INNER JOIN me_01.dbo.style_detail sd WITH (NOLOCK) on sd.style_id = st.style_id
	INNER JOIN me_01.dbo.style_group sg WITH (NOLOCK) on sg.style_id = st.style_id	
	INNER JOIN me_01.dbo.hierarchy_group hg WITH (NOLOCK) on hg.hierarchy_group_id = sg.hierarchy_group_id
	INNER JOIN me_01.dbo.entity_attribute_set eas WITH (NOLOCK) on st.style_id = eas.parent_id
	--INNER JOIN me_01.dbo.attribute_set att WITH (NOLOCK) on eas.attribute_set_id = att.attribute_set_id
	LEFT JOIN me_01.dbo.entity_custom_property ecp WITH (NOLOCK) on ecp.parent_id = st.style_id and custom_property_id = 2 --number of units in a pack
	LEFT JOIN me_01.dbo.keith_average_cost ac WITH (NOLOCK) on (CAST(u.upc_number AS bigINT) = ac.style_code)--average_cost by style_code
	WHERE (eas.attribute_id = 572 AND eas.attribute_set_id IN( 57200002,57200003,57200005, 57200004,57200006, 57200009)  --US, CA, USWEB, UK, UKWEB)
		AND CAST(u.upc_number AS BIGINT) <= 999999)
    GROUP BY u.upc_number,st.short_desc,st.long_desc,hierarchy_group_code,st.distribution_multiple,st.style_code,
		average_cost
),
merchitems_intsupplies
AS
(
	SELECT u.upc_number
	,st.short_desc
	,st.long_desc
	,hierarchy_group_code
	,st.distribution_multiple
	,st.style_code
	,isnull(average_cost, 0.00) as cost
 	,max(case when ecp.custom_property_value is null then st.distribution_multiple else cast(cast(ecp.custom_property_value as float) as int) end) std_pack_qty
	FROM 	me_01.dbo.upc u WITH (NOLOCK)
	INNER JOIN me_01.dbo.sku sku WITH (NOLOCK) on u.sku_id = sku.sku_id 
	INNER JOIN me_01.dbo.style st WITH (NOLOCK) on st.style_id = sku.style_id 
	INNER JOIN me_01.dbo.style_detail sd WITH (NOLOCK) on sd.style_id = st.style_id
	INNER JOIN me_01.dbo.style_group sg WITH (NOLOCK) on sg.style_id = st.style_id	
	INNER JOIN me_01.dbo.hierarchy_group hg WITH (NOLOCK) on hg.hierarchy_group_id = sg.hierarchy_group_id
	INNER JOIN me_01.dbo.entity_attribute_set eas WITH (NOLOCK) on st.style_id = eas.parent_id
	INNER JOIN me_01.dbo.attribute_set att WITH (NOLOCK) on eas.attribute_set_id = att.attribute_set_id
	LEFT JOIN me_01.dbo.entity_custom_property ecp WITH (NOLOCK) on ecp.parent_id = st.style_id and custom_property_id = 2 --number of units in a pack
	LEFT JOIN me_01.dbo.keith_average_cost ac WITH (NOLOCK) on (CAST(u.upc_number AS bigINT) = ac.style_code)--average_cost by style_code
	WHERE (att.attribute_id IN (114, 254) and att.attribute_set_label = 'YES'
		AND CAST(u.upc_number AS BIGINT) < 600000)
    GROUP BY u.upc_number,st.short_desc,st.long_desc,hierarchy_group_code,st.distribution_multiple,st.style_code,
		average_cost
),
merchitems_testchain
AS
(
	SELECT u.upc_number
	,st.short_desc
	,st.long_desc
	,hierarchy_group_code
	,st.distribution_multiple
	,st.style_code
	,isnull(average_cost, 0.00) as cost
 	,max(case when ecp.custom_property_value is null then st.distribution_multiple else cast(cast(ecp.custom_property_value as float) as int) end) std_pack_qty
	FROM 	me_01.dbo.upc u WITH (NOLOCK)
	INNER JOIN me_01.dbo.sku sku WITH (NOLOCK) on u.sku_id = sku.sku_id 
	INNER JOIN me_01.dbo.style st WITH (NOLOCK) on st.style_id = sku.style_id 
	INNER JOIN me_01.dbo.style_detail sd WITH (NOLOCK) on sd.style_id = st.style_id
	INNER JOIN me_01.dbo.style_group sg WITH (NOLOCK) on sg.style_id = st.style_id	
	INNER JOIN me_01.dbo.hierarchy_group hg WITH (NOLOCK) on hg.hierarchy_group_id = sg.hierarchy_group_id
	INNER JOIN me_01.dbo.entity_attribute_set eas WITH (NOLOCK) on st.style_id = eas.parent_id
	INNER JOIN me_01.dbo.attribute_set att WITH (NOLOCK) on eas.attribute_set_id = att.attribute_set_id
	LEFT JOIN me_01.dbo.entity_custom_property ecp WITH (NOLOCK) on ecp.parent_id = st.style_id and custom_property_id = 2 --number of units in a pack
	LEFT JOIN me_01.dbo.keith_average_cost ac WITH (NOLOCK) on (CAST(u.upc_number AS bigINT) = ac.style_code)--average_cost by style_code
	WHERE (left(hg.hierarchy_group_code,11) in ('R-B-D-70-03', 'R-B-D-75-01') OR hg.hierarchy_group_code LIKE 'F%')	--Test Test Chain Test Division	--temporarily added to do testing for the 960 warehouse - dave 6/9/2004
			and cast(u.upc_number as bigint) BETWEEN  234 AND 999999
    GROUP BY u.upc_number,st.short_desc,st.long_desc,hierarchy_group_code,st.distribution_multiple,st.style_code,
		average_cost
),
merchItems
AS
(
	SELECT TOP 100 PERCENT *
	FROM
	(
		SELECT * 
		FROM merchitems_availb
		UNION
		SELECT * 
		FROM merchitems_intsupplies
		UNION
		SELECT * 
		FROM merchitems_testchain
	) AS innerQry
	GROUP BY upc_number, short_desc, long_desc,hierarchy_group_code, distribution_multiple, style_code,
		cost, std_pack_qty
	ORDER BY upc_number
),
merchItemsSansD365
AS
(
	SELECT [upc_number]
	FROM merchItems
	EXCEPT
	SELECT [upc_number]
	FROM d365Supplies
)
SELECT *
FROM d365Supplies
UNION
SELECT *
FROM merchItems
WHERE upc_number IN (SELECT upc_number FROM merchItemsSansD365)
```

