# dbo.DC_UPD_STR_ITEM

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DC_UPD_STR_ITEM"]
    dbo_AGE_RESTRICT_GRP(["dbo.AGE_RESTRICT_GRP"]) --> SP
    dbo_DC_STORE_ITEM(["dbo.DC_STORE_ITEM"]) --> SP
    dbo_ITEM(["dbo.ITEM"]) --> SP
    dbo_SPCL_RESTRICT_GRP(["dbo.SPCL_RESTRICT_GRP"]) --> SP
    dbo_STORE_ITEM(["dbo.STORE_ITEM"]) --> SP
    dbo_TMP_STORE_ITEM(["dbo.TMP_STORE_ITEM"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.AGE_RESTRICT_GRP |
| dbo.DC_STORE_ITEM |
| dbo.ITEM |
| dbo.SPCL_RESTRICT_GRP |
| dbo.STORE_ITEM |
| dbo.TMP_STORE_ITEM |

## Stored Procedure Code

```sql

```

