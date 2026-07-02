# dbo.spSelectEnterpriseSellingInventory

**Database:** esell  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spSelectEnterpriseSellingInventory"]
    dbo_attribute(["dbo.attribute"]) --> SP
    dbo_attribute_set(["dbo.attribute_set"]) --> SP
    dbo_entity_attribute_set(["dbo.entity_attribute_set"]) --> SP
    dbo_Style(["dbo.Style"]) --> SP
    dbo_vwWebHierarchy(["dbo.vwWebHierarchy"]) --> SP
    dbo_vwWebIncludedStyles(["dbo.vwWebIncludedStyles"]) --> SP
    dbo_vwWebLocations(["dbo.vwWebLocations"]) --> SP
    dbo_WebInventoryStage(["dbo.WebInventoryStage"]) --> SP
    dbo_WebProductCatalogMasterAttributes(["dbo.WebProductCatalogMasterAttributes"]) --> SP
    esell_outlet_sku_xref(["esell.outlet_sku_xref"]) --> SP
    esell_sku(["esell.sku"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.attribute |
| dbo.attribute_set |
| dbo.entity_attribute_set |
| dbo.Style |
| dbo.vwWebHierarchy |
| dbo.vwWebIncludedStyles |
| dbo.vwWebLocations |
| dbo.WebInventoryStage |
| dbo.WebProductCatalogMasterAttributes |
| esell.outlet_sku_xref |
| esell.sku |

## Stored Procedure Code

```sql

```

