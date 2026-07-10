# Azure.vwServiceDeskOpen

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["Azure.vwServiceDeskOpen"]
    dbo_ServiceDeskOpenStage(["dbo.ServiceDeskOpenStage"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ServiceDeskOpenStage |

## View Code

```sql
CREATE view Azure.vwServiceDeskOpen
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
	cast([Created On] as date) as CreateDate,
	[Source],	
	Team,	
	Area,	
	Category,	
	Subcategory,
	ResolvedDateTime,
	cast(ResolvedDateTime as date) as ResolvedDate,
	Description,	
	Country,	
	[Owner Email],	
	Problem,	
	OpenWK,	
	OpenMo,	
	OpenYr
from dwStaging.dbo.ServiceDeskOpenStage
```

