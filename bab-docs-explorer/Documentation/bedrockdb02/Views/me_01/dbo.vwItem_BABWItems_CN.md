# dbo.vwItem_BABWItems_CN

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwItem_BABWItems_CN"]
    dbo_attribute_set(["dbo.attribute_set"]) --> VIEW
    dbo_entity_attribute_set(["dbo.entity_attribute_set"]) --> VIEW
    dbo_hierarchy_group(["dbo.hierarchy_group"]) --> VIEW
    dbo_size_master(["dbo.size_master"]) --> VIEW
    dbo_sku(["dbo.sku"]) --> VIEW
    dbo_style(["dbo.style"]) --> VIEW
    dbo_style_color(["dbo.style_color"]) --> VIEW
    dbo_style_group(["dbo.style_group"]) --> VIEW
    dbo_style_size(["dbo.style_size"]) --> VIEW
    dbo_upc(["dbo.upc"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.attribute_set |
| dbo.entity_attribute_set |
| dbo.hierarchy_group |
| dbo.size_master |
| dbo.sku |
| dbo.style |
| dbo.style_color |
| dbo.style_group |
| dbo.style_size |
| dbo.upc |

## View Code

```sql
CREATE VIEW [dbo].[vwItem_BABWItems_CN]
AS

SELECT u.upc_number
	,st.short_desc +' - '+ sc.short_desc +' - '+ sm.prim_size_label short_desc
	,hierarchy_group_code
	,st.distribution_multiple
FROM me_01.dbo.upc u (nolock)
	INNER JOIN me_01.dbo.sku sku (nolock)		ON u.sku_id = sku.sku_id 
	INNER JOIN me_01.dbo.style st (nolock)		ON st.style_id = sku.style_id 
	INNER JOIN me_01.dbo.style_color sc (nolock)	ON sc.style_color_id = sku.style_color_id 
	INNER JOIN me_01.dbo.style_size sz (nolock)	ON sz.style_size_id = sku.style_size_id 
	INNER JOIN me_01.dbo.size_master sm (nolock)	ON sm.size_master_id = sz.size_master_id
	INNER JOIN me_01.dbo.style_group sg (nolock)	ON sg.style_id = st.style_id	
	INNER JOIN me_01.dbo.hierarchy_group hg (nolock)	ON hg.hierarchy_group_id = sg.hierarchy_group_id
WHERE u.upc_type = 1 
AND CAST(u.upc_number as bigint) < 900000
AND st.style_id IN (
	SELECT s.style_id 
	FROM me_01.dbo.style s (nolock)
	INNER JOIN me_01.dbo.entity_attribute_set eas (nolock) on s.style_id = eas.parent_id
	INNER JOIN me_01.dbo.attribute_set att (nolock) on eas.attribute_set_id = att.attribute_set_id
	WHERE eas.attribute_id = 572 AND eas.attribute_set_id IN( 57200009)  --CN)
	
)
```

