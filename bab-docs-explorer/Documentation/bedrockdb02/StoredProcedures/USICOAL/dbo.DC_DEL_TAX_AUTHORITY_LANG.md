# dbo.DC_DEL_TAX_AUTHORITY_LANG

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DC_DEL_TAX_AUTHORITY_LANG"]
    dbo_DC_TAX_AUTHORITY_LANG(["dbo.DC_TAX_AUTHORITY_LANG"]) --> SP
    dbo_TAX_AUTHORITY_LANG(["dbo.TAX_AUTHORITY_LANG"]) --> SP
    dbo_TMP_TAX_AUTHORITY_LANG(["dbo.TMP_TAX_AUTHORITY_LANG"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.DC_TAX_AUTHORITY_LANG |
| dbo.TAX_AUTHORITY_LANG |
| dbo.TMP_TAX_AUTHORITY_LANG |

## Stored Procedure Code

```sql

```

