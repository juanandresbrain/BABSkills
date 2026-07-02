# dbo.DC_INS_UPC

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DC_INS_UPC"]
    dbo_ITEM(["dbo.ITEM"]) --> SP
    dbo_POS_IDENTITY(["dbo.POS_IDENTITY"]) --> SP
    dbo_TMP_POS_IDENTITY(["dbo.TMP_POS_IDENTITY"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ITEM |
| dbo.POS_IDENTITY |
| dbo.TMP_POS_IDENTITY |

## Stored Procedure Code

```sql

```

