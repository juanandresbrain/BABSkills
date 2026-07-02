# dbo.DC_INSUPD_TAX_ZONE_TAX_AUTH

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DC_INSUPD_TAX_ZONE_TAX_AUTH"]
    dbo_DC_TAX_ZONE_TAX_AUTH(["dbo.DC_TAX_ZONE_TAX_AUTH"]) --> SP
    dbo_EQUAL_TAX_ZONE(["dbo.EQUAL_TAX_ZONE"]) --> SP
    dbo_TAX_AUTHORITY(["dbo.TAX_AUTHORITY"]) --> SP
    dbo_TAX_ZONE_TAX_AUTH(["dbo.TAX_ZONE_TAX_AUTH"]) --> SP
    dbo_TMP_TAX_ZONE_TAX_AUTH(["dbo.TMP_TAX_ZONE_TAX_AUTH"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.DC_TAX_ZONE_TAX_AUTH |
| dbo.EQUAL_TAX_ZONE |
| dbo.TAX_AUTHORITY |
| dbo.TAX_ZONE_TAX_AUTH |
| dbo.TMP_TAX_ZONE_TAX_AUTH |

## Stored Procedure Code

```sql

```

