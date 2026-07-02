# dbo.DC_DEL_TAX_GRP_ZONE_AUTH

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DC_DEL_TAX_GRP_ZONE_AUTH"]
    dbo_DC_TAX_GRP_ZONE_AUTH(["dbo.DC_TAX_GRP_ZONE_AUTH"]) --> SP
    dbo_TAX_EXEMPT_CERT(["dbo.TAX_EXEMPT_CERT"]) --> SP
    dbo_TAX_GRP_ZONE_AUTH(["dbo.TAX_GRP_ZONE_AUTH"]) --> SP
    dbo_TMP_TAX_GRP_ZONE_AUTH(["dbo.TMP_TAX_GRP_ZONE_AUTH"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.DC_TAX_GRP_ZONE_AUTH |
| dbo.TAX_EXEMPT_CERT |
| dbo.TAX_GRP_ZONE_AUTH |
| dbo.TMP_TAX_GRP_ZONE_AUTH |

## Stored Procedure Code

```sql

```

