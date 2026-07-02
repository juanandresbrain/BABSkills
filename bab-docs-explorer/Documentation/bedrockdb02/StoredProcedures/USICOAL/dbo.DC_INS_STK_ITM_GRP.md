# dbo.DC_INS_STK_ITM_GRP

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DC_INS_STK_ITM_GRP"]
    dbo_ITEM(["dbo.ITEM"]) --> SP
    dbo_ITEM_QUANTITY(["dbo.ITEM_QUANTITY"]) --> SP
    dbo_STK_LEDGER_ACCOUNT(["dbo.STK_LEDGER_ACCOUNT"]) --> SP
    dbo_STORE_GROUP(["dbo.STORE_GROUP"]) --> SP
    dbo_STORE_GROUP_STORE(["dbo.STORE_GROUP_STORE"]) --> SP
    dbo_STORE_ITEM(["dbo.STORE_ITEM"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ITEM |
| dbo.ITEM_QUANTITY |
| dbo.STK_LEDGER_ACCOUNT |
| dbo.STORE_GROUP |
| dbo.STORE_GROUP_STORE |
| dbo.STORE_ITEM |

## Stored Procedure Code

```sql

```

