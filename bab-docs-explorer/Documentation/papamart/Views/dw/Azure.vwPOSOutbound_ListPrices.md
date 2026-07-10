# Azure.vwPOSOutbound_ListPrices

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["Azure.vwPOSOutbound_ListPrices"]
    dbo_POSListPrices(["dbo.POSListPrices"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.POSListPrices |

## View Code

```sql
CREATE VIEW [Azure].[vwPOSOutbound_ListPrices] AS

	 
select * from Bedrockdb02.me_01.dbo.POSListPrices
```

