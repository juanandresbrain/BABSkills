# dbo.RPT_SP_FLASH_SALES

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.RPT_SP_FLASH_SALES"]
    dbo_T_DATE_ONLY(["dbo.T_DATE_ONLY"]) --> SP
    dbo_T_FLG(["dbo.T_FLG"]) --> SP
    dbo_T_KEY_NUMBER(["dbo.T_KEY_NUMBER"]) --> SP
    dbo_WRKST_LOCAL_SALES(["dbo.WRKST_LOCAL_SALES"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.T_DATE_ONLY |
| dbo.T_FLG |
| dbo.T_KEY_NUMBER |
| dbo.WRKST_LOCAL_SALES |

## Stored Procedure Code

```sql

```

