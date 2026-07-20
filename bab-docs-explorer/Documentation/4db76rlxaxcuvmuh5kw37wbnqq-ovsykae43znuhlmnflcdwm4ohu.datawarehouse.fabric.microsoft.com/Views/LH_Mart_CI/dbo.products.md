# dbo.products

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.products"]
    dbo_products(["dbo.products"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.products |

## View Code

```sql
; CREATE   VIEW [dbo].[products] AS     SELECT [ProductID], [ProductName] COLLATE Latin1_General_CI_AS AS [ProductName], [Rate]     FROM [dbo].[products]
```

