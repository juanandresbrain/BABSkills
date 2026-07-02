# dbo.DC_DEL_ZIP_CODE_TAX_ZONE

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DC_DEL_ZIP_CODE_TAX_ZONE"]
    dbo_DC_ZIP_CODE_TAX_ZONE(["dbo.DC_ZIP_CODE_TAX_ZONE"]) --> SP
    dbo_TMP_ZIP_CODE_TAX_ZONE(["dbo.TMP_ZIP_CODE_TAX_ZONE"]) --> SP
    dbo_ZIP_CODE_TAX_ZONE(["dbo.ZIP_CODE_TAX_ZONE"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.DC_ZIP_CODE_TAX_ZONE |
| dbo.TMP_ZIP_CODE_TAX_ZONE |
| dbo.ZIP_CODE_TAX_ZONE |

## Stored Procedure Code

```sql

```

