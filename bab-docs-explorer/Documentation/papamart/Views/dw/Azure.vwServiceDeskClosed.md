# Azure.vwServiceDeskClosed

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["Azure.vwServiceDeskClosed"]
    dbo_ServiceDeskClosedStage(["dbo.ServiceDeskClosedStage"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ServiceDeskClosedStage |

## View Code

```sql
CREATE view Azure.vwServiceDeskClosed
as

select
	Incident,	
	Summary,	
	Status,	
	Priority,	
	Customer,	
	CustomerLocation,	
	Owner,	
	[Created On],
	cast([Created On] as date) CreateDate,
	[Source],	
	Team,	
	Area,	
	Category,	
	Subcategory,	
	ResolvedDateTime,
	cast(ResolvedDateTime as date) as ResolvedDate,
	Address1Country,	
	[Problem ID],	
	[Avg Days Open],	
	OpenWk,	
	ClosedWk,	
	OpenMon,	
	CloseMo,	
	OpenYr,	
	CloseYr
from dwStaging.dbo.ServiceDeskClosedStage
```

