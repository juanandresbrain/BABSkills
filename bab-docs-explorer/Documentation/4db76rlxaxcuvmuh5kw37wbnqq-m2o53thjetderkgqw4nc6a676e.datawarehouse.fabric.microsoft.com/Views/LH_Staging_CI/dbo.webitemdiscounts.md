# dbo.webitemdiscounts

**Database:** LH_Staging_CI  
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
CREATE   VIEW [dbo].[webitemdiscounts]
AS
    SELECT [DiscountID], [PromoCode] COLLATE Latin1_General_CI_AS AS [PromoCode], [OrderID], [OrderItemID], [DiscountAmount], [IsOrderDiscount], [DiscountName] COLLATE Latin1_General_CI_AS AS [DiscountName]
    FROM LH_Staging.[dbo].[webitemdiscounts]
```

