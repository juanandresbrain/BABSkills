# dbo.webshippingdiscounts

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

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
; CREATE   VIEW [dbo].[webshippingdiscounts] AS SELECT [ShippingDiscountID], [OrderID], [PromoCode] COLLATE Latin1_General_CI_AS AS [PromoCode], [DiscountAmount], [DiscountName] COLLATE Latin1_General_CI_AS AS [DiscountName] FROM [dbo].[webshippingdiscounts]
```

