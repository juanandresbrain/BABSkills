# dbo.spSelectEnterpriseSellingStoreInventory_BACKUP20200805

**Database:** esell  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spSelectEnterpriseSellingStoreInventory_BACKUP20200805"]
    dbo_attribute(["dbo.attribute"]) --> SP
    dbo_attribute_set(["dbo.attribute_set"]) --> SP
    dbo_entity_attribute_set(["dbo.entity_attribute_set"]) --> SP
    dbo_StoreInventoryStage(["dbo.StoreInventoryStage"]) --> SP
    dbo_Style(["dbo.Style"]) --> SP
    dbo_vwWebHierarchy(["dbo.vwWebHierarchy"]) --> SP
    dbo_vwWebIncludedStyles(["dbo.vwWebIncludedStyles"]) --> SP
    dbo_vwWebLocations(["dbo.vwWebLocations"]) --> SP
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
| dbo.StoreInventoryStage |
| dbo.Style |
| dbo.vwWebHierarchy |
| dbo.vwWebIncludedStyles |
| dbo.vwWebLocations |
| dbo.WebProductCatalogMasterAttributes |
| esell.outlet_sku_xref |
| esell.sku |

## Stored Procedure Code

```sql

```

