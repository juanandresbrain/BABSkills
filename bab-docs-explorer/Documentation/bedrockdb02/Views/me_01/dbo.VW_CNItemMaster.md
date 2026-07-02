# dbo.VW_CNItemMaster

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.VW_CNItemMaster"]
    dbo_entity_custom_property(["dbo.entity_custom_property"]) --> VIEW
    dbo_hierarchy_group(["dbo.hierarchy_group"]) --> VIEW
    dbo_style(["dbo.style"]) --> VIEW
    dbo_style_group(["dbo.style_group"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.entity_custom_property |
| dbo.hierarchy_group |
| dbo.style |
| dbo.style_group |

## View Code

```sql
CREATE view [dbo].[VW_CNItemMaster]

as 

select  s.style_code,
		isnull(replace(s.short_desc, ',','' ), '') as short_desc,
		--case when substring(hg.hierarchy_group_code,7,2)='60'
		--	then	ecp.custom_property_value
		--	else	s.distribution_multiple
		--end as distribution_multiple
		case when substring(hg.hierarchy_group_code,7,2)='60'
			then	ecp.custom_property_value
			else	s.distribution_multiple
		end as distribution_multiple
from style s with (nolock)
join style_group sg with (nolock) on s.style_id = sg.style_id
join hierarchy_group hg with (nolock) on sg.hierarchy_group_id = hg.hierarchy_group_id
left join entity_custom_property ecp with (nolock) on s.style_id = ecp.parent_id
	and	ecp.custom_property_id = 2 -- FRCSTM
	and ecp.parent_type = 1
where left(s.style_code, 1) in ('8')
and s.active_flag = 1
and substring(hg.hierarchy_group_code,7,2)<>'60' --	EXCLUDES SUPPLIES, THESE ARE SENT FROM DYNAMICS NOW
```

