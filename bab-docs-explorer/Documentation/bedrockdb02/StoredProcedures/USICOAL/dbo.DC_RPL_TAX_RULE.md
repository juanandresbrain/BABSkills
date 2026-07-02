# dbo.DC_RPL_TAX_RULE

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DC_RPL_TAX_RULE"]
    dbo_DC_TAX_RULE(["dbo.DC_TAX_RULE"]) --> SP
    dbo_TMP_TAX_RULE(["dbo.TMP_TAX_RULE"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.DC_TAX_RULE |
| dbo.TMP_TAX_RULE |

## Stored Procedure Code

```sql

```

