# dbo.NSB_SP_SUSP_CUST_TRN1

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.NSB_SP_SUSP_CUST_TRN1"]
    dbo_CUSTOMER(["dbo.CUSTOMER"]) --> SP
    dbo_CUSTOMER_ADDRESS(["dbo.CUSTOMER_ADDRESS"]) --> SP
    dbo_CUSTOMER_PERSON(["dbo.CUSTOMER_PERSON"]) --> SP
    dbo_DEPARTMENT(["dbo.DEPARTMENT"]) --> SP
    dbo_ITEM(["dbo.ITEM"]) --> SP
    dbo_RETAIL_TRANSACTION(["dbo.RETAIL_TRANSACTION"]) --> SP
    dbo_SALE_RTRN_LN_ITEM(["dbo.SALE_RTRN_LN_ITEM"]) --> SP
    dbo_SUSPENDED_TRN(["dbo.SUSPENDED_TRN"]) --> SP
    dbo_WORKSTATION(["dbo.WORKSTATION"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.CUSTOMER |
| dbo.CUSTOMER_ADDRESS |
| dbo.CUSTOMER_PERSON |
| dbo.DEPARTMENT |
| dbo.ITEM |
| dbo.RETAIL_TRANSACTION |
| dbo.SALE_RTRN_LN_ITEM |
| dbo.SUSPENDED_TRN |
| dbo.WORKSTATION |

## Stored Procedure Code

```sql
/*Report Id = 1130
```

