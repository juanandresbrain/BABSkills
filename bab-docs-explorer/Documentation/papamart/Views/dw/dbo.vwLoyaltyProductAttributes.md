# dbo.vwLoyaltyProductAttributes

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwLoyaltyProductAttributes"]
    dbo_productAttributes(["dbo.productAttributes"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.productAttributes |

## View Code

```sql
CREATE VIEW [dbo].[vwLoyaltyProductAttributes]  AS


select * from [DWStaging].[dbo].[productAttributes]
```

