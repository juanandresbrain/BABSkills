# Azure.vwWebInventoryRollups

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["Azure.vwWebInventoryRollups"]
    WebInventoryRollups(["WebInventoryRollups"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| WebInventoryRollups |

## View Code

```sql
CREATE view [Azure].[vwWebInventoryRollups]

as 

select 
	product_key,
	StyleCode,
	StoreInventoryUS,
	StoreInventoryUK,
	WebInventoryUS,
	WebInventoryUK,
	WarehouseInventoryUS,
	WarehouseInventoryUK,
	InsertDate 
from WebInventoryRollups with (nolock)
where product_key is not null
```

