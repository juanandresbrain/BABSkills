# dbo.DC_BOOK_PRC_CHG

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DC_BOOK_PRC_CHG"]
    dbo_ITEM_QUANTITY(["dbo.ITEM_QUANTITY"]) --> SP
    dbo_PRICE_CHANGE(["dbo.PRICE_CHANGE"]) --> SP
    dbo_PRICE_CHANGE_ITEM(["dbo.PRICE_CHANGE_ITEM"]) --> SP
    dbo_TMP_PRC_CHANGE(["dbo.TMP_PRC_CHANGE"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ITEM_QUANTITY |
| dbo.PRICE_CHANGE |
| dbo.PRICE_CHANGE_ITEM |
| dbo.TMP_PRC_CHANGE |

## Stored Procedure Code

```sql

```

