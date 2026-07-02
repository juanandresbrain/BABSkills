# dbo.NSB_SP_TILL_DEC_SUMM

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.NSB_SP_TILL_DEC_SUMM"]
    dbo_SETTLEMENT_TRN(["dbo.SETTLEMENT_TRN"]) --> SP
    dbo_STLMNT_TRN_TNDR(["dbo.STLMNT_TRN_TNDR"]) --> SP
    dbo_TENDER(["dbo.TENDER"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.SETTLEMENT_TRN |
| dbo.STLMNT_TRN_TNDR |
| dbo.TENDER |

## Stored Procedure Code

```sql
/*Report Id = 1150*/
```

