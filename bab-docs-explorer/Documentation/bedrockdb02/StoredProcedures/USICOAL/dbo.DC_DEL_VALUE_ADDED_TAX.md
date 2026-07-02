# dbo.DC_DEL_VALUE_ADDED_TAX

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DC_DEL_VALUE_ADDED_TAX"]
    dbo_DC_VALUE_ADDED_TAX(["dbo.DC_VALUE_ADDED_TAX"]) --> SP
    dbo_TMP_VALUE_ADDED_TAX(["dbo.TMP_VALUE_ADDED_TAX"]) --> SP
    dbo_VALUE_ADDED_TAX(["dbo.VALUE_ADDED_TAX"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.DC_VALUE_ADDED_TAX |
| dbo.TMP_VALUE_ADDED_TAX |
| dbo.VALUE_ADDED_TAX |

## Stored Procedure Code

```sql

```

