# dbo.DC_RPL_ITEM

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DC_RPL_ITEM"]
    dbo_CATEGORY(["dbo.CATEGORY"]) --> SP
    dbo_CLASS(["dbo.CLASS"]) --> SP
    dbo_COLOR(["dbo.COLOR"]) --> SP
    dbo_DC_ITEM(["dbo.DC_ITEM"]) --> SP
    dbo_DEPARTMENT(["dbo.DEPARTMENT"]) --> SP
    dbo_ITEM(["dbo.ITEM"]) --> SP
    dbo_LIFE_STYLE(["dbo.LIFE_STYLE"]) --> SP
    dbo_SEASON(["dbo.SEASON"]) --> SP
    dbo_SIZE(["dbo.SIZE"]) --> SP
    dbo_STYLE(["dbo.STYLE"]) --> SP
    dbo_SUB_CATEGORY(["dbo.SUB_CATEGORY"]) --> SP
    dbo_SUB_CLASS(["dbo.SUB_CLASS"]) --> SP
    dbo_SUB_DEPARTMENT(["dbo.SUB_DEPARTMENT"]) --> SP
    dbo_TMP_ITEM(["dbo.TMP_ITEM"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.CATEGORY |
| dbo.CLASS |
| dbo.COLOR |
| dbo.DC_ITEM |
| dbo.DEPARTMENT |
| dbo.ITEM |
| dbo.LIFE_STYLE |
| dbo.SEASON |
| dbo.SIZE |
| dbo.STYLE |
| dbo.SUB_CATEGORY |
| dbo.SUB_CLASS |
| dbo.SUB_DEPARTMENT |
| dbo.TMP_ITEM |

## Stored Procedure Code

```sql

```

