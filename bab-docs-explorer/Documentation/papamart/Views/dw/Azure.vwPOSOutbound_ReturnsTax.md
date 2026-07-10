# Azure.vwPOSOutbound_ReturnsTax

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["Azure.vwPOSOutbound_ReturnsTax"]
    DynamicsTaxFacts(["DynamicsTaxFacts"]) --> VIEW
    dbo_DynamicsTransactionHeaderFacts(["dbo.DynamicsTransactionHeaderFacts"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| DynamicsTaxFacts |
| dbo.DynamicsTransactionHeaderFacts |

## View Code

```sql
CREATE VIEW [Azure].[vwPOSOutbound_ReturnsTax] AS

--POS_ReturnsTax
with 
Header as 
	(
		select * 
		from [dbo].[DynamicsTransactionHeaderFacts] (nolock) 
		where datediff(dd, TransDate, getdate())<=45
		and isCurrent=1
	)
select *
from  DynamicsTaxFacts (nolock) 
where RetailTransactionId in (select RetailTransactionId from Header)
and isCurrent=1 ;
```

