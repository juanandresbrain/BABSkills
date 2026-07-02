# dbo.DC_UPD_EQUAL_TAX_ZONE_LANG

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DC_UPD_EQUAL_TAX_ZONE_LANG"]
    dbo_DC_EQUAL_TAX_ZONE_LANG(["dbo.DC_EQUAL_TAX_ZONE_LANG"]) --> SP
    dbo_EQUAL_TAX_ZONE(["dbo.EQUAL_TAX_ZONE"]) --> SP
    dbo_EQUAL_TAX_ZONE_LANG(["dbo.EQUAL_TAX_ZONE_LANG"]) --> SP
    dbo_LANGUAGE(["dbo.LANGUAGE"]) --> SP
    dbo_TMP_EQUAL_TAX_ZONE_LANG(["dbo.TMP_EQUAL_TAX_ZONE_LANG"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.DC_EQUAL_TAX_ZONE_LANG |
| dbo.EQUAL_TAX_ZONE |
| dbo.EQUAL_TAX_ZONE_LANG |
| dbo.LANGUAGE |
| dbo.TMP_EQUAL_TAX_ZONE_LANG |

## Stored Procedure Code

```sql

```

