# dbo.vwWebLocationsForDeck

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwWebLocationsForDeck"]
    azure_vwPOSOutbound_SellingContext(["azure.vwPOSOutbound_SellingContext"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| azure.vwPOSOutbound_SellingContext |

## View Code

```sql
CREATE view [dbo].[vwWebLocationsForDeck] 

as

select 
	StoreNumber,
	cast(concat(StoreNameFull,' (',StoreNumber,')') as varchar(100)) as Name,
	cast(Address1 as varchar(100)) as Address1,
	cast(Address2 as varchar(100)) as Address2,
	cast(City as varchar(100)) as City,
	cast(StateProvinceNameAbbr as varchar(100)) as State,
	cast(Zip as varchar(100)) as PostalCode,
	cast(StoreLongitude as varchar(100)) as GeoLongitude,
	cast(StoreLatitude as varchar(100)) as GeoLatitude,
	cast(StorePhoneNumber as varchar(100)) as Phone,
	cast(StoreEmail as varchar(100)) as Email,
	cast(case when StoreNumber<2000 then 'US' else 'UK' end as varchar(100)) as SiteID,
	cast(case when StoreNumber in (13,2013) then 'Warehouse' else 'Store' end as varchar(100)) as LocationType,
	CountryNameAbbr as Country
from azure.vwPOSOutbound_SellingContext
```

