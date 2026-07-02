# ERP.vwWarehouseIDToLocationCode

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["ERP.vwWarehouseIDToLocationCode"]
    ERP_WarehouseMaster(["ERP.WarehouseMaster"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| ERP.WarehouseMaster |

## View Code

```sql
CREATE view [ERP].[vwWarehouseIDToLocationCode]

as

---------------------------------------------------------------------------------
-- Dan Tweedie	-	2017-12-01	-	Maps D365 WarehouseID to Aptos Location Code
-- Dan Tweedie	-	2018-07-20	-	Updated view to allow locations from 1700, 2110 and 3001 to exist in 1100 entity
-- Dan Tweedie	-	2018-09-05	-	Updated view to allow for '92' locations to be included - These are hub locations in the UK and need to resolve to the WarehouseID 
---------------------------------------------------------------------------------

WITH
WhseMaster as
	(
		select 
			cast(WarehouseID as varchar(5)) as WarehouseID,
			cast(
					case 
						when left(WarehouseID,1) in ('1','9') or WarehouseID='8010'
							then 
								case 
									when WarehouseID = 9970
										then '2970'
									when WarehouseID = 9940
										then '3970'
									when WarehouseID = 9941
										then '3980'
									when WarehouseID = 9991
										then '9991' 
									when WarehouseID = 9451
										then '9451'
									when WarehouseID = 9473
										then '9473'										
									when WarehouseID='9942'
										then '9942'
									when left(WarehouseID,2) = '93'
										then WarehouseID 
									when left(WarehouseID,2) = '92'
										then WarehouseID 
									when WarehouseID='8010'
										then '2991'
									else concat(cast('0' as varchar), right(cast(WarehouseID as varchar),3))
								end 
							else WarehouseID
						end as varchar(4)
				)
				 as LocationCode,
			PrimaryAddressDescription,
			OperationalSiteID,
			cast(
					case 
						when left(OperationalSiteID,1) in ('1','9') or WarehouseID='8010'
							then 
								case 
									when (OperationalSiteID = 9970 and WarehouseID <> '9990')
									--when OperationalSiteID = 9970
										then '2970'
									when OperationalSiteID = 9940 and WarehouseID not in ('8502','8505')
										then '3970'
									when OperationalSiteID = 9941
										then '3980'
									when OperationalSiteID = 9991
										then '9991'
									when (OperationalSiteID = 9990 OR WarehouseID = '9990')
										then '2990' 
									when OperationalSiteID = 9451
										then '9451' 
									when WarehouseID='9942'
										then '9942'
									when OperationalSiteID in (9901,9902,9903,9473)
										then WarehouseID
									when WarehouseID in ('8502','8505')
										then WarehouseID 
									when WarehouseID='8010'
										then '2991'
									else concat(cast('0' as varchar), right(cast(OperationalSiteID as varchar),3))
								end 
							else cast(OperationalSiteID as varchar)
						end as varchar(4)
				)
				 as OperationalSiteCode,
				 Entity 
		from ERP.WarehouseMaster with (nolock)
		where 1=1
		and WarehouseID not like '%[^0-9]%'
--		and left(WarehouseID,2) not in ('92') --excludes various hubs, pool points, etc 
		--and WarehouseID <> '8010' --Keenpac - uk 
		--and WarehouseID = '9980'
		and WarehouseID not in  ('9404','9452')       --'9416', '9419'

	),
CAtoUS as
	(
		select DISTINCT
			WarehouseID, LocationCode, PrimaryAddressDescription, OperationalSiteID, OperationalSiteCode, '1100' as Entity
		from WhseMaster
		where entity = 1700
		and WarehouseID not in (select WarehouseID from WhseMaster where entity = 1100)
	),
UKtoUS as
	(
		select DISTINCT
			WarehouseID, LocationCode, PrimaryAddressDescription, OperationalSiteID, OperationalSiteCode, '1100' as Entity
		from WhseMaster
		where entity = 2110
		and WarehouseID not in (select WarehouseID from WhseMaster where entity = 1100)
	),
CNtoUS as
	(
		select DISTINCT
			WarehouseID, LocationCode, PrimaryAddressDescription, OperationalSiteID, OperationalSiteCode, '1100' as Entity
		from WhseMaster
		where entity = 3001
		and WarehouseID not in (select WarehouseID from WhseMaster where entity = 1100)
	),
CNtoUK as
	(
		select DISTINCT
			WarehouseID, LocationCode, PrimaryAddressDescription, OperationalSiteID, OperationalSiteCode, '2110' as Entity
		from WhseMaster
		where entity = 1700
		and WarehouseID not in (select WarehouseID from WhseMaster where entity = 2110)
	),
DKtoUK as
	(
		select DISTINCT
			WarehouseID, LocationCode, PrimaryAddressDescription, OperationalSiteID, OperationalSiteCode, '2110' as Entity
		from WhseMaster
		where entity = 2300
		and WarehouseID not in (select WarehouseID from WhseMaster where entity = 2110)
	),
AllInOne as
	(
		select WarehouseID, LocationCode, PrimaryAddressDescription, OperationalSiteID, OperationalSiteCode, Entity
		from WhseMaster 
		UNION
		select WarehouseID, LocationCode, PrimaryAddressDescription, OperationalSiteID, OperationalSiteCode, Entity
		from CAtoUS
		UNION
		select WarehouseID, LocationCode, PrimaryAddressDescription, OperationalSiteID, OperationalSiteCode, Entity
		from UKtoUS 
		UNION
		select WarehouseID, LocationCode, PrimaryAddressDescription, OperationalSiteID, OperationalSiteCode, Entity
		from CNtoUS 
		UNION
		select WarehouseID, LocationCode, PrimaryAddressDescription, OperationalSiteID, OperationalSiteCode, Entity
		from CNtoUK 
		UNION
		select WarehouseID, LocationCode, PrimaryAddressDescription, OperationalSiteID, OperationalSiteCode, Entity
		from DKtoUK  
	),
DupeCheck as
	(
		select Entity, WarehouseID, count(*) Rowz 
		from AllInOne 
		group by Entity, WarehouseID
		having count(*) > 1
	)
select 
	WarehouseID, 
	LocationCode, 
	PrimaryAddressDescription, 
	OperationalSiteID, 
	OperationalSiteCode, 
	Entity
from AllInOne 
where WarehouseID not in (select WarehouseID from DupeCheck) --if dupes found, there is a problem with the data, will be prevent distros from exporting
```

