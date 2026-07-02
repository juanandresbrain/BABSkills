# dbo.DC_UPD_STR_ITM

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DC_UPD_STR_ITM"]
    dbo_AGE_RESTRICT_GRP(["dbo.AGE_RESTRICT_GRP"]) --> SP
    dbo_DC_ITEM(["dbo.DC_ITEM"]) --> SP
    dbo_SPCL_RESTRICT_GRP(["dbo.SPCL_RESTRICT_GRP"]) --> SP
    dbo_STORE_ITEM(["dbo.STORE_ITEM"]) --> SP
    dbo_TMP_ITEM(["dbo.TMP_ITEM"]) --> SP
    dbo_TMP_STORE_ITEM(["dbo.TMP_STORE_ITEM"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.AGE_RESTRICT_GRP |
| dbo.DC_ITEM |
| dbo.SPCL_RESTRICT_GRP |
| dbo.STORE_ITEM |
| dbo.TMP_ITEM |
| dbo.TMP_STORE_ITEM |

## Stored Procedure Code

```sql

```

