# Azure.vwPOSOutbound_SalePrices

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["Azure.vwPOSOutbound_SalePrices"]
    dbo_POSSalePrices(["dbo.POSSalePrices"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.POSSalePrices |

## View Code

```sql
CREATE VIEW [Azure].[vwPOSOutbound_SalePrices] AS

	 
select * from Bedrockdb02.me_01.dbo.POSSalePrices
```

