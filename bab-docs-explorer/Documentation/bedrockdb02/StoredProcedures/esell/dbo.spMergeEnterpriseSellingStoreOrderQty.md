# dbo.spMergeEnterpriseSellingStoreOrderQty

**Database:** esell  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMergeEnterpriseSellingStoreOrderQty"]
    dbo_StoreOrderQtyStage(["dbo.StoreOrderQtyStage"]) --> SP
    dbo_WebToESInventoryUpdateLog(["dbo.WebToESInventoryUpdateLog"]) --> SP
    esell_outlet_sku_xref(["esell.outlet_sku_xref"]) --> SP
    esell_sku(["esell.sku"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.StoreOrderQtyStage |
| dbo.WebToESInventoryUpdateLog |
| esell.outlet_sku_xref |
| esell.sku |

## Stored Procedure Code

```sql

```

