# dbo.DC_DEL_ORPHAN_STK

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DC_DEL_ORPHAN_STK"]
    dbo_ITEM(["dbo.ITEM"]) --> SP
    dbo_ITEM_QUANTITY(["dbo.ITEM_QUANTITY"]) --> SP
    dbo_STK_LEDGER_ACCOUNT(["dbo.STK_LEDGER_ACCOUNT"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ITEM |
| dbo.ITEM_QUANTITY |
| dbo.STK_LEDGER_ACCOUNT |

## Stored Procedure Code

```sql

```

