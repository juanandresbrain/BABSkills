# dbo.DC_DEL_TAX_ZONE_TAX_AUTH

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DC_DEL_TAX_ZONE_TAX_AUTH"]
    dbo_DC_TAX_ZONE_TAX_AUTH(["dbo.DC_TAX_ZONE_TAX_AUTH"]) --> SP
    dbo_TAX_ZONE_TAX_AUTH(["dbo.TAX_ZONE_TAX_AUTH"]) --> SP
    dbo_TMP_TAX_ZONE_TAX_AUTH(["dbo.TMP_TAX_ZONE_TAX_AUTH"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.DC_TAX_ZONE_TAX_AUTH |
| dbo.TAX_ZONE_TAX_AUTH |
| dbo.TMP_TAX_ZONE_TAX_AUTH |

## Stored Procedure Code

```sql

```

