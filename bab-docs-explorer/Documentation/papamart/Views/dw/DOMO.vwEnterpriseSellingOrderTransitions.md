# DOMO.vwEnterpriseSellingOrderTransitions

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["DOMO.vwEnterpriseSellingOrderTransitions"]
    dbo_vwDW_EnterpriseSellingOrderTransitions(["dbo.vwDW_EnterpriseSellingOrderTransitions"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.vwDW_EnterpriseSellingOrderTransitions |

## View Code

```sql
CREATE view DOMO.vwEnterpriseSellingOrderTransitions

as 

select 
	cast(OrderCreateDateTime as Date) as OrderCreateDate,
	OrderCreateDateTime,
	OrderNumber,
	OrderType,
	OrderStoreNumber,
	FulfillmentStoreNumber,
	CurrentState,
	OrderStatus,
	TransitionSequence,
	TransitionDateTime
from bedrockdb02.esell.dbo.vwDW_EnterpriseSellingOrderTransitions
where CAST(OrderCreateDateTime AS DATE)>=DATEADD(year, -2, DATEADD(yy, DATEDIFF(yy, 0, GETDATE()), 0))
```

