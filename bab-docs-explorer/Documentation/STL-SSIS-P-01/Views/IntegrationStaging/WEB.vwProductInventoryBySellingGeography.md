# WEB.vwProductInventoryBySellingGeography

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["WEB.vwProductInventoryBySellingGeography"]
    WEB_InventoryFact(["WEB.InventoryFact"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| WEB.InventoryFact |

## View Code

```sql
CREATE view [WEB].[vwProductInventoryBySellingGeography]

as

select 
	case
		when LocationCode = '0013'
		then 'US'
		else 'UK'
	end as ProductSellingGeography,
	--SellingGeography as ProductSellingGeography,
	StyleCode as BABWProductID,
	case when sum(UnbufferedQTY) < 0 then 0 else sum(UnbufferedQTY) end  as Inventory
from WEB.InventoryFact
where LocationCode in ('0013', '2013')
--and StyleCode = '024196'
group by LocationCode, StyleCode
```

