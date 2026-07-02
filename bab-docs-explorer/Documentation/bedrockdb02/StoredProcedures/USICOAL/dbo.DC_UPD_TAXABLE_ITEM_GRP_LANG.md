# dbo.DC_UPD_TAXABLE_ITEM_GRP_LANG

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DC_UPD_TAXABLE_ITEM_GRP_LANG"]
    dbo_DC_TAXABLE_ITEM_GRP_LANG(["dbo.DC_TAXABLE_ITEM_GRP_LANG"]) --> SP
    dbo_LANGUAGE(["dbo.LANGUAGE"]) --> SP
    dbo_TAXABLE_ITEM_GRP(["dbo.TAXABLE_ITEM_GRP"]) --> SP
    dbo_TAXABLE_ITEM_GRP_LANG(["dbo.TAXABLE_ITEM_GRP_LANG"]) --> SP
    dbo_TMP_TAXABLE_ITEM_GRP_LANG(["dbo.TMP_TAXABLE_ITEM_GRP_LANG"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.DC_TAXABLE_ITEM_GRP_LANG |
| dbo.LANGUAGE |
| dbo.TAXABLE_ITEM_GRP |
| dbo.TAXABLE_ITEM_GRP_LANG |
| dbo.TMP_TAXABLE_ITEM_GRP_LANG |

## Stored Procedure Code

```sql

```

