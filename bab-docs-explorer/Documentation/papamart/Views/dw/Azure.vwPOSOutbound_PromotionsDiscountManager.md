# Azure.vwPOSOutbound_PromotionsDiscountManager

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["Azure.vwPOSOutbound_PromotionsDiscountManager"]
    dbo_vwPOSDiscountsExtract(["dbo.vwPOSDiscountsExtract"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.vwPOSDiscountsExtract |

## View Code

```sql
CREATE VIEW [Azure].[vwPOSOutbound_PromotionsDiscountManager] AS

select * from Kodiak.DiscountMstrData.dbo.vwPOSDiscountsExtract
```

