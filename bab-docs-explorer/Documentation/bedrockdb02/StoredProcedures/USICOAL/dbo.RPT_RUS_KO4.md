# dbo.RPT_RUS_KO4

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.RPT_RUS_KO4"]
    dbo_SAFE_TENDER_STLMNT(["dbo.SAFE_TENDER_STLMNT"]) --> SP
    dbo_SETTLEMENT_TRN(["dbo.SETTLEMENT_TRN"]) --> SP
    dbo_SETTLEMENT_TRN_EXT(["dbo.SETTLEMENT_TRN_EXT"]) --> SP
    dbo_STORE_SAFE_TENDER(["dbo.STORE_SAFE_TENDER"]) --> SP
    dbo_TENDER_CONTROL_TRN(["dbo.TENDER_CONTROL_TRN"]) --> SP
    dbo_TENDER_CONTROL_TRN_EXT(["dbo.TENDER_CONTROL_TRN_EXT"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.SAFE_TENDER_STLMNT |
| dbo.SETTLEMENT_TRN |
| dbo.SETTLEMENT_TRN_EXT |
| dbo.STORE_SAFE_TENDER |
| dbo.TENDER_CONTROL_TRN |
| dbo.TENDER_CONTROL_TRN_EXT |

## Stored Procedure Code

```sql

```

