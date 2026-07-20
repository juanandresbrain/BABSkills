# dbo.webitemdiscounts

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.webitemdiscounts"]
    dbo_webitemdiscounts(["dbo.webitemdiscounts"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.webitemdiscounts |

## View Code

```sql
;

CREATE VIEW dbo.webitemdiscounts AS SELECT DiscountID, PromoCode COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS PromoCode, OrderID, OrderItemID, DiscountAmount, IsOrderDiscount, DiscountName COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS DiscountName, InsertDate, UpdateDate FROM LH_Mart.dbo.webitemdiscounts;;
```

