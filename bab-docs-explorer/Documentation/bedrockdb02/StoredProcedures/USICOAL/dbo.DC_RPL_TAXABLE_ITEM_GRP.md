# dbo.DC_RPL_TAXABLE_ITEM_GRP

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DC_RPL_TAXABLE_ITEM_GRP"]
    dbo_DC_TAXABLE_ITEM_GRP(["dbo.DC_TAXABLE_ITEM_GRP"]) --> SP
    dbo_TMP_TAXABLE_ITEM_GRP(["dbo.TMP_TAXABLE_ITEM_GRP"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.DC_TAXABLE_ITEM_GRP |
| dbo.TMP_TAXABLE_ITEM_GRP |

## Stored Procedure Code

```sql

```

