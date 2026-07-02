# dbo.vwItem_BABWSupplyItems_DELETEAFTER20170228

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwItem_BABWSupplyItems_DELETEAFTER20170228"]
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

## View Code

```sql
CREATE VIEW [dbo].[vwItem_BABWSupplyItems_DELETEAFTER20170228] AS
SELECT u.upc_number
	,st.short_desc
	,st.long_desc
	,hierarchy_group_code
	,st.distribution_multiple
	,st.style_code
	,isnull(average_cost, 0.00) as cost
 	,max(case when ecp.custom_property_value is null then st.distribution_multiple else cast(cast(ecp.custom_property_value as float) as int) end) std_pack_qty
from 	me_01.dbo.upc u 
INNER JOIN me_01.dbo.sku sku on u.sku_id = sku.sku_id 
INNER JOIN me_01.dbo.style st on st.style_id = sku.style_id 
INNER JOIN me_01.dbo.style_detail sd on sd.style_id = st.style_id
INNER JOIN me_01.dbo.style_group sg on sg.style_id = st.style_id	
INNER JOIN me_01.dbo.hierarchy_group hg on hg.hierarchy_group_id = sg.hierarchy_group_id
LEFT JOIN me_01.dbo.entity_custom_property ecp on ecp.parent_id = st.style_id and custom_property_id = 2 --number of units in a pack
	and	parent_type = 1 and hg.hierarchy_group_code like 'R-%-%-60%'
LEFT JOIN me_01.dbo.keith_average_cost ac on (CAST(u.upc_number AS bigINT) = ac.style_code)--average_cost by style_code
WHERE CAST(u.upc_number as bigint) = 5428 -- this item accidently got put in the wrong hierarchy - dave 3/29/2004
OR 
st.style_id IN (
	SELECT s.style_id 
	FROM me_01.dbo.style s (nolock)
	INNER JOIN me_01.dbo.entity_attribute_set eas (nolock) on s.style_id = eas.parent_id
	INNER JOIN me_01.dbo.attribute_set att (nolock) on eas.attribute_set_id = att.attribute_set_id
	WHERE eas.attribute_id = 572 AND eas.attribute_set_id IN( 57200002,57200003,57200005)  --US, CA, USWEB)
	AND CAST(u.upc_number AS BIGINT) < 600000 
	UNION ALL
	SELECT sku.style_id
	from 	me_01.dbo.upc u 
	INNER JOIN me_01.dbo.sku sku on u.sku_id = sku.sku_id 
	INNER JOIN me_01.dbo.style_detail sd on sd.style_id = sku.style_id
	INNER JOIN me_01.dbo.style_group sg on sg.style_id = sku.style_id	
	INNER JOIN me_01.dbo.hierarchy_group hg on hg.hierarchy_group_id = sg.hierarchy_group_id
	INNER JOIN me_01.dbo.entity_attribute_set eas ON sku.style_id = eas.parent_id
	INNER JOIN me_01.dbo.attribute_set att ON eas.attribute_set_id = att.attribute_set_id
	WHERE att.attribute_id IN (114, 254) and att.attribute_set_label = 'YES'
	AND CAST(u.upc_number AS BIGINT) < 600000 
	UNION ALL
	SELECT sku.style_id
	FROM 	me_01.dbo.upc u 
	INNER JOIN me_01.dbo.sku sku on u.sku_id = sku.sku_id 
	INNER JOIN me_01.dbo.style_detail sd on sd.style_id = sku.style_id
	INNER JOIN me_01.dbo.style_group sg on sg.style_id = sku.style_id	
	INNER JOIN me_01.dbo.hierarchy_group hg on hg.hierarchy_group_id = sg.hierarchy_group_id
	WHERE (left(hg.hierarchy_group_code,11) in ('R-B-D-70-03') OR hg.hierarchy_group_code LIKE 'F%' OR hg.hierarchy_group_code LIKE 'W%')	--Test Test Chain Test Division	--temporarily added to do testing for the 960 warehouse - dave 6/9/2004
		and cast(u.upc_number as bigint) BETWEEN  234 AND 999999	
) 
GROUP BY u.upc_number,st.short_desc,st.long_desc,hierarchy_group_code,st.distribution_multiple,st.style_code,
	average_cost




dbo,vwItem_BABWSupplyItems_UK,CREATE VIEW vwItem_BABWSupplyItems_UK AS
SELECT u.upc_number
	,st.short_desc
	,st.long_desc
	,hierarchy_group_code
	,st.distribution_multiple
	,st.style_code
	,isnull(average_cost, 0.00) as cost
 	,max(case when ecp.custom_property_value is null then st.distribution_multiple else cast(cast(ecp.custom_property_value as float) as int) end) std_pack_qty
from 	me_01.dbo.upc u 
INNER JOIN me_01.dbo.sku sku on u.sku_id = sku.sku_id 
INNER JOIN me_01.dbo.style st on st.style_id = sku.style_id 
INNER JOIN me_01.dbo.style_detail sd on sd.style_id = st.style_id
INNER JOIN me_01.dbo.style_group sg on sg.style_id = st.style_id	
INNER JOIN me_01.dbo.hierarchy_group hg on hg.hierarchy_group_id = sg.hierarchy_group_id
LEFT JOIN me_01.dbo.entity_custom_property ecp on ecp.parent_id = st.style_id and custom_property_id = 2 --number of units in a pack
	and	parent_type = 1 and hg.hierarchy_group_code like 'R-%-%-60%'
LEFT JOIN me_01.dbo.keith_average_cost ac on (CAST(u.upc_number AS bigINT) = ac.style_code)--average_cost by style_code
WHERE st.style_id IN (
	SELECT s.style_id 
	FROM me_01.dbo.style s (nolock)
	INNER JOIN me_01.dbo.entity_attribute_set eas (nolock) on s.style_id = eas.parent_id
	INNER JOIN me_01.dbo.attribute_set att (nolock) on eas.attribute_set_id = att.attribute_set_id
	WHERE eas.attribute_id = 572 AND eas.attribute_set_id IN( 57200004,57200006)  --UK, UKWEB)
	AND CAST(u.upc_number AS BIGINT) < 600000 
	UNION ALL
	SELECT sku.style_id
	FROM 	me_01.dbo.upc u  (nolock)
	INNER JOIN me_01.dbo.sku sku (nolock) on u.sku_id = sku.sku_id 
	INNER JOIN me_01.dbo.style_detail sd (nolock) on sd.style_id = sku.style_id
	INNER JOIN me_01.dbo.style_group sg (nolock) on sg.style_id = sku.style_id	
	INNER JOIN me_01.dbo.hierarchy_group hg (nolock) on hg.hierarchy_group_id = sg.hierarchy_group_id
	WHERE hg.hierarchy_group_code LIKE 'R-B-Z-%' AND cast(u.upc_number as bigint) < 600000
) 
GROUP BY u.upc_number,st.short_desc,st.long_desc,hierarchy_group_code,st.distribution_multiple,st.style_code,
	average_cost
```

