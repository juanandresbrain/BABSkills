# dbo.wms_vwItemType

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.wms_vwItemType"]
    dbo_integrationstaging_wms_itemmaster(["dbo.integrationstaging_wms_itemmaster"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.integrationstaging_wms_itemmaster |

## View Code

```sql
create view dbo.wms_vwItemType
as
select
	entity,
	itemnumber,
	necessaryproductionworkingtimeschedulingpropertyid as ItemType
from LH_Mart.dbo.integrationstaging_wms_itemmaster
where isnumeric(itemnumber) = 1
and len(itemnumber) = 6
```

