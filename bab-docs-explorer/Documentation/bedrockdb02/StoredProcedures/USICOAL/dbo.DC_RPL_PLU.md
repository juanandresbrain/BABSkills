# dbo.DC_RPL_PLU

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DC_RPL_PLU"]
    dbo_CATEGORY(["dbo.CATEGORY"]) --> SP
    dbo_CLASS(["dbo.CLASS"]) --> SP
    dbo_COLOR(["dbo.COLOR"]) --> SP
    dbo_ITEM(["dbo.ITEM"]) --> SP
    dbo_ITEM_ADDL_INFO(["dbo.ITEM_ADDL_INFO"]) --> SP
    dbo_ITEM_POS_SELL_RULE(["dbo.ITEM_POS_SELL_RULE"]) --> SP
    dbo_SEASON(["dbo.SEASON"]) --> SP
    dbo_SIZE(["dbo.SIZE"]) --> SP
    dbo_SPIFF_DEFINITION(["dbo.SPIFF_DEFINITION"]) --> SP
    dbo_STORE_ITEM(["dbo.STORE_ITEM"]) --> SP
    dbo_STYLE(["dbo.STYLE"]) --> SP
    dbo_SUB_CATEGORY(["dbo.SUB_CATEGORY"]) --> SP
    dbo_SUB_CLASS(["dbo.SUB_CLASS"]) --> SP
    dbo_SUB_DEPARTMENT(["dbo.SUB_DEPARTMENT"]) --> SP
    dbo_TMP_PLU(["dbo.TMP_PLU"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.CATEGORY |
| dbo.CLASS |
| dbo.COLOR |
| dbo.ITEM |
| dbo.ITEM_ADDL_INFO |
| dbo.ITEM_POS_SELL_RULE |
| dbo.SEASON |
| dbo.SIZE |
| dbo.SPIFF_DEFINITION |
| dbo.STORE_ITEM |
| dbo.STYLE |
| dbo.SUB_CATEGORY |
| dbo.SUB_CLASS |
| dbo.SUB_DEPARTMENT |
| dbo.TMP_PLU |

## Stored Procedure Code

```sql

```

