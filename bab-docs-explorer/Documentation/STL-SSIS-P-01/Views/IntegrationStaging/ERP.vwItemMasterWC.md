# ERP.vwItemMasterWC

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["ERP.vwItemMasterWC"]
    erp_ItemMasterToWM(["erp.ItemMasterToWM"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| erp.ItemMasterToWM |

## View Code

```sql
CREATE view [ERP].[vwItemMasterWC]

as

select 	left(convert(varchar, getdate(), 120), 10) as UpdateDate,
		'BABW' as UpdateUserID,
		'wcItemLoad' as UpdatePID,
		'A' as ActionCode,
		'IN' as Direction,
		'NEW' as InterfaceStatus,
		Style as SKU,
		'01' as Facility,
		'01' as Class,
		'' as InternalUse1,
		'' as InternalUse2,
		'' as InternalUse3,
		replace(Sku_Desc,'"','') as Description1,
		'' as Description2,
		'EA' as UnitDesc,
		'' as BulkDesc,
		'' as BulkQty,
		'' as InternalUse4,
		'' as InternalUse5,
		'' as InternalUse6,
		'0' as Length,
		'0' as Width,
		'0' as Height,
		'0' as Cube,
		'0' as Weight,
		'N' as SerialTrack,
		'N' as LotTrack,
		'N' as ExpDateTrack,
		'N' as MfgDateTrack,
		'' as HighQty,
		'' as TieQty,
		'N' as ShippableUnit,
		'Y' as AgeControl,
		'' as InternalUse7,
		'N' as InternalUse8,
		'0' as InternalUse9,
		'' as NMFCode,
		'' as InternalUse10,
		'' as InternalUse11,
		'' as InternalUse12,
		'1856' as InternalUse13, 
		'' as AltPartNbr
from erp.ItemMasterToWM with (nolock) 
where entity = 1100
and InWM is null
```

