# dbo.vwERPInventory

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwERPInventory"]
    dbo_NightlyWhseInventory(["dbo.NightlyWhseInventory"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.NightlyWhseInventory |

## View Code

```sql
CREATE view [dbo].[vwERPInventory]

--------------------------------------------------------------------------------------------------------------------------------------
--Dan Tweedie 2017-08-10 -- Created view to capture inventory to push to Dynamics365. 
--							View is dependent on data having already been staged from the Warehouses to me_01.dbo.tblNightlyInventory, 
--							which happens nightly via 'nightly sync' proc ->spMerchandisingSelectWhseInventoryShrink
--------------------------------------------------------------------------------------------------------------------------------------
as

select
	location_code as LocationCode,
	style_code as StyleCode,
	QTY
from NightlyWhseInventory with (nolock)
where location_code in ('0960','0980','2970','3970')
and datediff(dd, load_date, getdate()) = 0
```

