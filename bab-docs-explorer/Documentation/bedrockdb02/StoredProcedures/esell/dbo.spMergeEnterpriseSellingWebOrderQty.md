# dbo.spMergeEnterpriseSellingWebOrderQty

**Database:** esell  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMergeEnterpriseSellingWebOrderQty"]
    dbo_WebOrderQtyStage(["dbo.WebOrderQtyStage"]) --> SP
    dbo_WebToESInventoryUpdateLog(["dbo.WebToESInventoryUpdateLog"]) --> SP
    esell_outlet_sku_xref(["esell.outlet_sku_xref"]) --> SP
    esell_sku(["esell.sku"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.WebOrderQtyStage |
| dbo.WebToESInventoryUpdateLog |
| esell.outlet_sku_xref |
| esell.sku |

## Stored Procedure Code

```sql

```

