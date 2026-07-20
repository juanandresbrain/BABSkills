# dbo.weborderitems

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.weborderitems"]
    dbo_weborderitems(["dbo.weborderitems"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.weborderitems |

## View Code

```sql
; CREATE   VIEW [dbo].[weborderitems] AS     SELECT [TransactionID], [OrderID], [OrderItemID], [SKU] COLLATE Latin1_General_CI_AS AS [SKU], [Qty], [ItemDescription] COLLATE Latin1_General_CI_AS AS [ItemDescription], [Price], [DiscountedPrice], [InsertDate], [UpdateDate], [TrackingNumber] COLLATE Latin1_General_CI_AS AS [TrackingNumber], [product_key]     FROM [dbo].[weborderitems]
```

