# dbo.IM_APPL_PRC_CHG

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.IM_APPL_PRC_CHG"]
    dbo_ITEM(["dbo.ITEM"]) --> SP
    dbo_ITEM_QUANTITY(["dbo.ITEM_QUANTITY"]) --> SP
    dbo_PLU(["dbo.PLU"]) --> SP
    dbo_PRICE_CHANGE(["dbo.PRICE_CHANGE"]) --> SP
    dbo_PRICE_CHANGE_ITEM(["dbo.PRICE_CHANGE_ITEM"]) --> SP
    dbo_STORE_ITEM(["dbo.STORE_ITEM"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ITEM |
| dbo.ITEM_QUANTITY |
| dbo.PLU |
| dbo.PRICE_CHANGE |
| dbo.PRICE_CHANGE_ITEM |
| dbo.STORE_ITEM |

## Stored Procedure Code

```sql

```

