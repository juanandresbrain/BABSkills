# Azure.vwPOSOutbound_ReturnsTransDetail

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["Azure.vwPOSOutbound_ReturnsTransDetail"]
    dbo_DynamicsSalesDetailFacts(["dbo.DynamicsSalesDetailFacts"]) --> VIEW
    dbo_DynamicsTransactionHeaderFacts(["dbo.DynamicsTransactionHeaderFacts"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.DynamicsSalesDetailFacts |
| dbo.DynamicsTransactionHeaderFacts |

## View Code

```sql
CREATE VIEW [Azure].[vwPOSOutbound_ReturnsTransDetail] AS

with 
Header as 
	(
		select * 
		from [dbo].[DynamicsTransactionHeaderFacts] (nolock) 
		where datediff(dd, TransDate, getdate())<=45
		and isCurrent=1
	)
select * 
from [dbo].[DynamicsSalesDetailFacts] (nolock) 
where RetailTransactionId in (select RetailTransactionId from Header)
and isCurrent=1 
and RetailReceiptId not in (464806407,464806406)

;
```

