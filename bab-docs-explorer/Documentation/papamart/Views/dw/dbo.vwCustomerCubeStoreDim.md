# dbo.vwCustomerCubeStoreDim

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwCustomerCubeStoreDim"]
    store_dim(["store_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| store_dim |

## View Code

```sql
CREATE view [dbo].[vwCustomerCubeStoreDim] 

as 

with 
StoreData as
	(
		SELECT
			sd.Store_Key as StoreKey,
			right(concat('0000', cast(sd.store_id as varchar(4))),4) as LocationCode,
			sd.store_name_abbrv AS StoreName,
			concat(right(concat('0000', cast(sd.store_id as varchar(4))),4), ' ', sd.store_name_abbrv) as StoreNumberName,
			CASE
				WHEN 
					sd.store_id IN (013, 136, 2013) 
					or
					sd.country IN ('US', 'UK', 'CA', 'IE', 'DK','CN')
						THEN 'Company' 
				WHEN 
					sd.store_id IN (480, 482, 473) 
					or
					sd.bearritory LIKE '%Corporate%'
					or
					sd.store_id > 9000
						THEN 'Other' 
			END AS CompanyLevel,
			CASE
				WHEN 
					sd.store_id IN (013, 136) 
					or
					sd.country IN ('US', 'CA')
						THEN 'North America' 						
				WHEN 
					sd.store_id IN (2013) 
					or
					sd.country IN ('UK', 'IE', 'DK','CN')
						THEN 'Europe'
				WHEN 
					sd.region LIKE ('%Corporate%') 
					or
					ISNULL(sd.region, 'Other') = 'Other' 
						THEN 'Other'
				ELSE 'Other'
			END AS BearRange,
			CASE
				WHEN sd.store_id IN (013, 136) THEN 'WebUS'
				WHEN sd.store_id IN (2013) THEN 'WebUS'
				ELSE ISNULL(sd.region, 'Other')
			END AS Zone,
			CASE
				WHEN sd.store_id IN (013) THEN 'WebUS'
				WHEN sd.store_id IN (2013) THEN 'WebUK'
				ELSE ISNULL(sd.bearritory, 'Other')
			END AS District,
			Case 
				when ISNULL(sd.bearea, 'N/A') = 'n/a' 
				then CASE
						WHEN sd.store_id IN (013) THEN 'WebUS'
						WHEN sd.store_id IN (2013) THEN 'WebUK'
						ELSE ISNULL(sd.bearritory, 'Other')
					END
				else bearea 
			end as Area,
			ISNULL(sd.country, 'n/a') AS Country,
			CASE
				WHEN sd.country_name IS NULL THEN 'n/a'
				WHEN LEN(sd.country_name) = 0 THEN 'n/a'
				ELSE sd.country_name
			END AS CountryName,
			CASE
				WHEN sd.state_province IS NULL OR LEN(sd.state_province) = 0 THEN 'n/a'
				ELSE sd.state_province
			END AS StateProvince,
			CASE
				WHEN sd.state_province_name IS NULL OR LEN(sd.state_province_name) = 0 THEN 'n/a'
				ELSE sd.state_province_name
			END AS StateProvinceName,
			CASE
				WHEN sd.city IS NULL OR city = '' THEN 'n/a'
				ELSE sd.city
			END AS City,
			isnull(sd.postal_code,0) as PostalCode,
			sd.Latitude,
			sd.Longitude
		FROM
			store_dim sd WITH (NOLOCK)
		WHERE
			sd.store_name IS NOT NULL
	),
StoreAddOn as
	(
		select 
			StoreKey,
			LocationCode,
			StoreName,
			StoreNumberName,
			CompanyLevel,
			BearRange,
			Zone,
			District,
			Area,
			Country,
			CountryName,
			StateProvince,
			StateProvinceName,
			City,
			PostalCode,
			Latitude,
			Longitude,
			dense_rank() over (order by  CompanyLevel, BearRange) as BearRangeID,
			dense_rank() over (order by  CompanyLevel, BearRange, Zone) as ZoneID,
			dense_rank() over (order by  CompanyLevel, BearRange, Zone, District) as DistrictID,
			dense_rank() over (order by  CompanyLevel, BearRange, Zone, District, Area) as AreaID,
			dense_rank() over (order by Country) as CountryID,
			dense_rank() over (order by CountryName) as CountryNameID,
			dense_rank() over (order by CountryName, StateProvince) as StateProvinceID,
			dense_rank() over (order by CountryName, StateProvinceName) as StateProvinceNameID,
			dense_rank() over (order by CountryName, StateProvinceName, City) as CityID
		from StoreData
		where PostalCode is not null
		and (
				(
					CompanyLevel = 'Company'
					and Zone not in ('Ridemakerz') --('Ridemakerz', 'Corporate UK', 'US Corporate', 'Corporate', 'Canada Corporate')
					and District not in ('Pool Point', 'Pool Points', 'Canada Pool Points', 'China', 'Denmark')
				)
			 OR
			 StoreKey = -4 --unknown
		   )
	)
select *
from StoreAddOn
```

