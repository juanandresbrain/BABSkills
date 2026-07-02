# dbo.DC_RPL_TAX_RULE_LANG

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DC_RPL_TAX_RULE_LANG"]
    dbo_DC_TAX_RULE_LANG(["dbo.DC_TAX_RULE_LANG"]) --> SP
    dbo_LANGUAGE(["dbo.LANGUAGE"]) --> SP
    dbo_TAX_RULE(["dbo.TAX_RULE"]) --> SP
    dbo_TMP_TAX_RULE_LANG(["dbo.TMP_TAX_RULE_LANG"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.DC_TAX_RULE_LANG |
| dbo.LANGUAGE |
| dbo.TAX_RULE |
| dbo.TMP_TAX_RULE_LANG |

## Stored Procedure Code

```sql

```

