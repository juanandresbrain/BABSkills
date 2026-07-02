# dbo.DC_UPD_ITM_PRC

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DC_UPD_ITM_PRC"]
    dbo_ITEM(["dbo.ITEM"]) --> SP
    dbo_ITEM_QUANTITY(["dbo.ITEM_QUANTITY"]) --> SP
    dbo_PRICE_CHANGE(["dbo.PRICE_CHANGE"]) --> SP
    dbo_PRICE_CHANGE_ITEM(["dbo.PRICE_CHANGE_ITEM"]) --> SP
    dbo_STK_LEDGER_ACCOUNT(["dbo.STK_LEDGER_ACCOUNT"]) --> SP
    dbo_STORE_ITEM(["dbo.STORE_ITEM"]) --> SP
    dbo_TMP_PRC_CHANGE(["dbo.TMP_PRC_CHANGE"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ITEM |
| dbo.ITEM_QUANTITY |
| dbo.PRICE_CHANGE |
| dbo.PRICE_CHANGE_ITEM |
| dbo.STK_LEDGER_ACCOUNT |
| dbo.STORE_ITEM |
| dbo.TMP_PRC_CHANGE |

## Stored Procedure Code

```sql

```

