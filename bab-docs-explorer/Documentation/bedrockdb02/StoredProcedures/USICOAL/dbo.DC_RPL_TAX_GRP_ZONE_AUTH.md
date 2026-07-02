# dbo.DC_RPL_TAX_GRP_ZONE_AUTH

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DC_RPL_TAX_GRP_ZONE_AUTH"]
    dbo_DC_TAX_GRP_ZONE_AUTH(["dbo.DC_TAX_GRP_ZONE_AUTH"]) --> SP
    dbo_EQUAL_TAX_ZONE(["dbo.EQUAL_TAX_ZONE"]) --> SP
    dbo_TAX_AUTHORITY(["dbo.TAX_AUTHORITY"]) --> SP
    dbo_TAX_EXEMPT_CERT(["dbo.TAX_EXEMPT_CERT"]) --> SP
    dbo_TAX_RULE(["dbo.TAX_RULE"]) --> SP
    dbo_TAXABLE_ITEM_GRP(["dbo.TAXABLE_ITEM_GRP"]) --> SP
    dbo_TMP_TAX_GRP_ZONE_AUTH(["dbo.TMP_TAX_GRP_ZONE_AUTH"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.DC_TAX_GRP_ZONE_AUTH |
| dbo.EQUAL_TAX_ZONE |
| dbo.TAX_AUTHORITY |
| dbo.TAX_EXEMPT_CERT |
| dbo.TAX_RULE |
| dbo.TAXABLE_ITEM_GRP |
| dbo.TMP_TAX_GRP_ZONE_AUTH |

## Stored Procedure Code

```sql

```

