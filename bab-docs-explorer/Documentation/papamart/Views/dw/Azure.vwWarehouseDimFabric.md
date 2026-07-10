# Azure.vwWarehouseDimFabric

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["Azure.vwWarehouseDimFabric"]
    dbo_store_dim(["dbo.store_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.store_dim |

## View Code

```sql
CREATE view [Azure].[vwWarehouseDimFabric] 

as

select 
	  CAST(sd.store_id as varchar) as WarehouseID
	, right(('0000' + CAST(sd.store_id as varchar)), 4) AS WarehouseNumber
	, CAST(sd.store_key as varchar) as WarehouseKey
	--, case when l.location_status_id = 5 then 1 else 0 end as PermCloseStatus
	,case when cast(isnull(sd.closing_date, '3030-12-31') as date) > cast(getdate() as date) then 0 else 1 end as PermCloseStatus
	, sd.store_name_abbrv as WarehouseNameAbbr
	, sd.store_name as WarehouseNameFull
	, sd.phone as WarehousePhoneNumber
	, sd.fax as WarehouseFaxNumber
	, sd.email as WarehouseEmail
	, 'Unknown' as TimeZoneDesc
	, sd.state_province as StateProvinceNameAbbr
	, state_province_name as StateProvinceNameFull
	, 'N/A' as WarehouseLocator
	, 'N/A' as WarehouseMallWebsiteURL
	, longitude as WarehouseLongitude
	, latitude as WarehouseLatitude
	, sd.legal_description as WarehouseLegalDescription
	, 'N/A' as Channel
	, CASE WHEN sd.country IN ('US','CA') THEN 'North America'
	          WHEN sd.country IN ('UK','DK','IE','CN') THEN 'Europe'
		 END AS TradingGroup
	, sd.country as CountryNameAbbr
	, sd.country_name as CountryNameFull
	, 'N/A' as SubChannel
	, 'N/A' AS Zone
    , 'N/A' AS Area
	, 'N/A' AS District
from dw.dbo.store_dim sd with (nolock)
where 
	(
		sd.closing_date >= DATEADD(day, -7, DATEADD(year, -2, DATEADD(yy, DATEDIFF(yy, 0, GETDATE()), 0)))
	OR 
		sd.closing_date IS NULL
	)
and 
	(
		store_name like '%Inventory%'
		or store_name like '%Costco%'
		or store_name like '%Warehouse%'
		or store_name like '%Keenpac%'
		or store_name like '%do not use%'
		or store_name like '%Whse%'
		or store_name like '%China%'
		or store_name like '%Distribution%'
		or store_name like '%Corporate%'
	)
```

