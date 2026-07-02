# dbo.DC_INS_ITM_QTY

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DC_INS_ITM_QTY"]
    dbo_DC_STOCK_ITEM(["dbo.DC_STOCK_ITEM"]) --> SP
    dbo_ITEM(["dbo.ITEM"]) --> SP
    dbo_ITEM_QUANTITY(["dbo.ITEM_QUANTITY"]) --> SP
    dbo_STK_LEDGER_ACCOUNT(["dbo.STK_LEDGER_ACCOUNT"]) --> SP
    dbo_STORE_ITEM(["dbo.STORE_ITEM"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.DC_STOCK_ITEM |
| dbo.ITEM |
| dbo.ITEM_QUANTITY |
| dbo.STK_LEDGER_ACCOUNT |
| dbo.STORE_ITEM |

## Stored Procedure Code

```sql

```

