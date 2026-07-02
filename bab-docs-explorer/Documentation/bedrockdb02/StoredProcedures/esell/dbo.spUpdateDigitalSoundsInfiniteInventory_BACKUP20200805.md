# dbo.spUpdateDigitalSoundsInfiniteInventory_BACKUP20200805

**Database:** esell  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spUpdateDigitalSoundsInfiniteInventory_BACKUP20200805"]
    dbo_attribute(["dbo.attribute"]) --> SP
    dbo_attribute_set(["dbo.attribute_set"]) --> SP
    dbo_entity_attribute_set(["dbo.entity_attribute_set"]) --> SP
    dbo_hierarchy_group(["dbo.hierarchy_group"]) --> SP
    dbo_style(["dbo.style"]) --> SP
    dbo_style_group(["dbo.style_group"]) --> SP
    esell_outlet_sku_xref(["esell.outlet_sku_xref"]) --> SP
    esell_sku(["esell.sku"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.attribute |
| dbo.attribute_set |
| dbo.entity_attribute_set |
| dbo.hierarchy_group |
| dbo.style |
| dbo.style_group |
| esell.outlet_sku_xref |
| esell.sku |

## Stored Procedure Code

```sql

```

