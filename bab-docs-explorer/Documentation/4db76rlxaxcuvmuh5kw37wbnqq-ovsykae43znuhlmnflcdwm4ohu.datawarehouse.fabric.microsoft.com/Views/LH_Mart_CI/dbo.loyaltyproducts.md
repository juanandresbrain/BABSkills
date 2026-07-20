# dbo.loyaltyproducts

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.loyaltyproducts"]
    dbo_loyaltyproducts(["dbo.loyaltyproducts"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.loyaltyproducts |

## View Code

```sql
; CREATE   VIEW loyaltyproducts AS SELECT * FROM LH_Mart.dbo.loyaltyproducts;
```

