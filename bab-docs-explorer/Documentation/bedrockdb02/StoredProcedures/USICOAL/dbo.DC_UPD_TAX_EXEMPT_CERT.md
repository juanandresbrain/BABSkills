# dbo.DC_UPD_TAX_EXEMPT_CERT

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DC_UPD_TAX_EXEMPT_CERT"]
    dbo_CUSTOMER(["dbo.CUSTOMER"]) --> SP
    dbo_DC_TAX_EXEMPT_CERT(["dbo.DC_TAX_EXEMPT_CERT"]) --> SP
    dbo_TAX_EXEMPT_CERT(["dbo.TAX_EXEMPT_CERT"]) --> SP
    dbo_TMP_TAX_EXEMPT_CERT(["dbo.TMP_TAX_EXEMPT_CERT"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.CUSTOMER |
| dbo.DC_TAX_EXEMPT_CERT |
| dbo.TAX_EXEMPT_CERT |
| dbo.TMP_TAX_EXEMPT_CERT |

## Stored Procedure Code

```sql

```

