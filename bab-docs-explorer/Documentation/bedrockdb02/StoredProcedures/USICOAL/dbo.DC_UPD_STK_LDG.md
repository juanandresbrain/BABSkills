# dbo.DC_UPD_STK_LDG

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DC_UPD_STK_LDG"]
    dbo_STK_LEDGER_ACCOUNT(["dbo.STK_LEDGER_ACCOUNT"]) --> SP
    dbo_TMP_PRC_CHANGE(["dbo.TMP_PRC_CHANGE"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.STK_LEDGER_ACCOUNT |
| dbo.TMP_PRC_CHANGE |

## Stored Procedure Code

```sql

```

