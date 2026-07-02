# dbo.NSB_SP_ORDER_DETAIL_ITEMS

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.NSB_SP_ORDER_DETAIL_ITEMS"]
    dbo_ACCOUNT(["dbo.ACCOUNT"]) --> SP
    dbo_CUST_ORD_DISCOUNT(["dbo.CUST_ORD_DISCOUNT"]) --> SP
    dbo_CUST_ORDER_ITEM(["dbo.CUST_ORDER_ITEM"]) --> SP
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
| dbo.CUST_ORD_DISCOUNT |
| dbo.CUST_ORDER_ITEM |
| dbo.CUST_ORDER_TYPE |
| dbo.CUSTOMER |
| dbo.CUSTOMER_ADDRESS |
| dbo.CUSTOMER_ORDER |
| dbo.CUSTOMER_PERSON |

## Stored Procedure Code

```sql
/*report ID = 1401
```

