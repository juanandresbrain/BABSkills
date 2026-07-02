# dbo.spDW_Inventory

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spDW_Inventory"]
    dbo_attribute(["dbo.attribute"]) --> SP
    dbo_attribute_set(["dbo.attribute_set"]) --> SP
    dbo_date_dim(["dbo.date_dim"]) --> SP
    dbo_entity_attribute_set(["dbo.entity_attribute_set"]) --> SP
    dbo_hierarchy_group(["dbo.hierarchy_group"]) --> SP
    dbo_hist_oh_style_loc_li(["dbo.hist_oh_style_loc_li"]) --> SP
    dbo_hist_oh_style_loc_wk(["dbo.hist_oh_style_loc_wk"]) --> SP
    dbo_jurisdiction(["dbo.jurisdiction"]) --> SP
    dbo_location(["dbo.location"]) --> SP
    dbo_style(["dbo.style"]) --> SP
    dbo_style_parent(["dbo.style_parent"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.attribute |
| dbo.attribute_set |
| dbo.date_dim |
| dbo.entity_attribute_set |
| dbo.hierarchy_group |
| dbo.hist_oh_style_loc_li |
| dbo.hist_oh_style_loc_wk |
| dbo.jurisdiction |
| dbo.location |
| dbo.style |
| dbo.style_parent |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spDW_Inventory]
```

