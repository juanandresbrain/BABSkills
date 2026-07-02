# dbo.RPT_SP_STORE_FLASH_SALES

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.RPT_SP_STORE_FLASH_SALES"]
    dbo_CUST_ORD_LN_ITEM(["dbo.CUST_ORD_LN_ITEM"]) --> SP
    dbo_ITEM(["dbo.ITEM"]) --> SP
    dbo_ITEM_TAX_AUTH(["dbo.ITEM_TAX_AUTH"]) --> SP
    dbo_RETAIL_TRANSACTION(["dbo.RETAIL_TRANSACTION"]) --> SP
    dbo_SALE_RTRN_LN_ITEM(["dbo.SALE_RTRN_LN_ITEM"]) --> SP
    dbo_T_DATE_ONLY(["dbo.T_DATE_ONLY"]) --> SP
    dbo_T_FLG(["dbo.T_FLG"]) --> SP
    dbo_T_KEY_NUMBER(["dbo.T_KEY_NUMBER"]) --> SP
    dbo_T_LONG_CODE_W(["dbo.T_LONG_CODE_W"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.CUST_ORD_LN_ITEM |
| dbo.ITEM |
| dbo.ITEM_TAX_AUTH |
| dbo.RETAIL_TRANSACTION |
| dbo.SALE_RTRN_LN_ITEM |
| dbo.T_DATE_ONLY |
| dbo.T_FLG |
| dbo.T_KEY_NUMBER |
| dbo.T_LONG_CODE_W |

## Stored Procedure Code

```sql

```

