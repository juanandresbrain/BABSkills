# dbo.DC_UPD_EQUAL_TAX_ZONE

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DC_UPD_EQUAL_TAX_ZONE"]
    dbo_DC_EQUAL_TAX_ZONE(["dbo.DC_EQUAL_TAX_ZONE"]) --> SP
    dbo_EQUAL_TAX_ZONE(["dbo.EQUAL_TAX_ZONE"]) --> SP
    dbo_TMP_EQUAL_TAX_ZONE(["dbo.TMP_EQUAL_TAX_ZONE"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.DC_EQUAL_TAX_ZONE |
| dbo.EQUAL_TAX_ZONE |
| dbo.TMP_EQUAL_TAX_ZONE |

## Stored Procedure Code

```sql

```

