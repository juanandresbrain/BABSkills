# WMS.vwItemType

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["WMS.vwItemType"]
    WMS_ItemMaster(["WMS.ItemMaster"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| WMS.ItemMaster |

## View Code

```sql
CREATE view [WMS].[vwItemType]

as

select
	Entity,
	ItemNumber,
	NecessaryProductionWorkingTimeSchedulingPropertyId as ItemType
from WMS.ItemMaster with (nolock)
where isnumeric(ItemNumber) = 1
and len(ItemNumber) = 6
```

