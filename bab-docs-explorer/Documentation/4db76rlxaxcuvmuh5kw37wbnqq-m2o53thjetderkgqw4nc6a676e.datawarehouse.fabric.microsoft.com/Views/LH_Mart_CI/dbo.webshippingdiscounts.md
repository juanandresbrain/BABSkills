# dbo.webshippingdiscounts

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.webshippingdiscounts"]
    dbo_webshippingdiscounts(["dbo.webshippingdiscounts"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.webshippingdiscounts |

## View Code

```sql
;

CREATE VIEW dbo.webshippingdiscounts AS SELECT ShippingDiscountID, OrderID, PromoCode COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS PromoCode, DiscountAmount, DiscountName COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS DiscountName, InsertDate, UpdateDate FROM LH_Mart.dbo.webshippingdiscounts;;
```

