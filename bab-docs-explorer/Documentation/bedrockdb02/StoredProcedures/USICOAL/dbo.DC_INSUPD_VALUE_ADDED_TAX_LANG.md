# dbo.DC_INSUPD_VALUE_ADDED_TAX_LANG

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DC_INSUPD_VALUE_ADDED_TAX_LANG"]
    dbo_DC_VALUE_ADDED_TAX_LANG(["dbo.DC_VALUE_ADDED_TAX_LANG"]) --> SP
    dbo_LANGUAGE(["dbo.LANGUAGE"]) --> SP
    dbo_TMP_VALUE_ADDED_TAX_LANG(["dbo.TMP_VALUE_ADDED_TAX_LANG"]) --> SP
    dbo_VALUE_ADDED_TAX(["dbo.VALUE_ADDED_TAX"]) --> SP
    dbo_VALUE_ADDED_TAX_LANG(["dbo.VALUE_ADDED_TAX_LANG"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.DC_VALUE_ADDED_TAX_LANG |
| dbo.LANGUAGE |
| dbo.TMP_VALUE_ADDED_TAX_LANG |
| dbo.VALUE_ADDED_TAX |
| dbo.VALUE_ADDED_TAX_LANG |

## Stored Procedure Code

```sql

```

