# dbo.NSB_SP_ORDER_SUMM

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.NSB_SP_ORDER_SUMM"]
    dbo_ACCOUNT(["dbo.ACCOUNT"]) --> SP
    dbo_ACCOUNT_TRANSACTION(["dbo.ACCOUNT_TRANSACTION"]) --> SP
    dbo_CUST_ORD_CHARGE(["dbo.CUST_ORD_CHARGE"]) --> SP
    dbo_CUST_ORDER_TYPE(["dbo.CUST_ORDER_TYPE"]) --> SP
    dbo_CUSTOMER(["dbo.CUSTOMER"]) --> SP
    dbo_CUSTOMER_ADDRESS(["dbo.CUSTOMER_ADDRESS"]) --> SP
    dbo_CUSTOMER_ORDER(["dbo.CUSTOMER_ORDER"]) --> SP
    dbo_CUSTOMER_PERSON(["dbo.CUSTOMER_PERSON"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ACCOUNT |
| dbo.ACCOUNT_TRANSACTION |
| dbo.CUST_ORD_CHARGE |
| dbo.CUST_ORDER_TYPE |
| dbo.CUSTOMER |
| dbo.CUSTOMER_ADDRESS |
| dbo.CUSTOMER_ORDER |
| dbo.CUSTOMER_PERSON |

## Stored Procedure Code

```sql
/*report ID = 1400
```

