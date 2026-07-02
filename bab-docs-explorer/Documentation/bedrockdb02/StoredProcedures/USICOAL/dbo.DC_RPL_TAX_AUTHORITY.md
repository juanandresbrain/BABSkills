# dbo.DC_RPL_TAX_AUTHORITY

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DC_RPL_TAX_AUTHORITY"]
    dbo_DC_TAX_AUTHORITY(["dbo.DC_TAX_AUTHORITY"]) --> SP
    dbo_TMP_TAX_AUTHORITY(["dbo.TMP_TAX_AUTHORITY"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.DC_TAX_AUTHORITY |
| dbo.TMP_TAX_AUTHORITY |

## Stored Procedure Code

```sql

```

